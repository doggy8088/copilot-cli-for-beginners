#!/usr/bin/env python3
"""
translate.py — 使用 Azure OpenAI v1 API 將 Markdown 文件翻譯成 zh-tw

用法：
    python translate.py \
        --changed-files /tmp/changed_md_files.txt \
        --upstream-ref upstream/main \
        --glossary GLOSSARY.md

環境變數：
    AZURE_OPENAI_ENDPOINT: Azure OpenAI 資源端點或完整 `/openai/v1` 基底 URL
    AZURE_OPENAI_API_KEY: Azure OpenAI API 金鑰
    AZURE_OPENAI_MODEL: Azure OpenAI deployment name（請部署 GPT-4.1，常見值為 `gpt-4.1`）
"""

import argparse
import os
import subprocess
import sys
import time

import requests

# ── 設定 ──────────────────────────────────────────────────────────────────────

# 單次請求最大字元數（保守值，避免超出 context window）
CHUNK_SIZE = 24_000
# 每次 API 呼叫後的等待秒數（避免速率限制）
REQUEST_DELAY = 2

# ── 系統提示 ──────────────────────────────────────────────────────────────────

SYSTEM_PROMPT_TEMPLATE = """你是一位專業的技術文件翻譯員，專精於將軟體開發教學材料從英文翻譯成繁體中文（zh-tw）。

## 翻譯規則

1. **保留不翻譯的內容**（完全原封不動）：
   - 程式碼區塊（``` ... ``` 或縮排程式碼）
   - 行內程式碼（`code`）
   - 指令與 CLI 語法（如 `gh copilot suggest`、`git commit`）
   - 檔案路徑與目錄名稱（如 `.github/agents/`）
   - URL 與超連結的網址部分
   - HTML 標籤與屬性（如 `<details>`、`<summary>`、`<a id="...">` 等）
   - YAML frontmatter（--- ... ---）
   - Markdown 圖片與連結語法中的 URL 部分
   - 變數名稱、函數名稱、類別名稱

2. **翻譯的內容**：
   - 一般說明文字與段落
   - 標題（保留 # 等標記符號）
   - 表格中的說明文字
   - 列表中的說明文字
   - 引言（blockquote > 內的文字）
   - HTML 標籤內的純文字內容（如 `<summary>` 的文字）

3. **術語一致性**：嚴格遵守以下術語表。術語表中已有繁體中文對應的，直接使用，不另外翻譯。

## 術語表（Glossary）

{glossary}

## 輸出格式

- 直接輸出翻譯後的 Markdown 原始文字，不加任何額外說明或包裝
- 保持原始檔案的所有縮排、空行、格式
- 不改變任何 Markdown 語法結構
"""

# ── 工具函式 ──────────────────────────────────────────────────────────────────


def get_file_from_upstream(filepath: str, upstream_ref: str) -> str | None:
    """從 upstream ref 取得檔案內容。若檔案不存在則回傳 None。"""
    result = subprocess.run(
        ["git", "show", f"{upstream_ref}:{filepath}"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        return None
    return result.stdout


def load_glossary(glossary_path: str) -> str:
    """載入術語表，擷取其中的術語對應部分（簡化版）。"""
    if not os.path.isfile(glossary_path):
        return "（術語表不存在，請使用通用技術翻譯慣例）"
    with open(glossary_path, encoding="utf-8") as f:
        return f.read()


def build_azure_openai_chat_url(endpoint: str) -> str:
    """將 Azure OpenAI endpoint 正規化為 v1 chat completions URL。"""
    normalized = endpoint.strip().rstrip("/")
    if not normalized:
        raise ValueError("AZURE_OPENAI_ENDPOINT 不可為空。")

    if normalized.endswith("/chat/completions"):
        return normalized
    if normalized.endswith("/openai/v1"):
        return f"{normalized}/chat/completions"
    if "/openai/v1/" in normalized:
        raise ValueError(
            "AZURE_OPENAI_ENDPOINT 格式不正確，請提供資源端點、`.../openai/v1`，"
            "或完整的 `.../chat/completions` URL。"
        )
    return f"{normalized}/openai/v1/chat/completions"


def chunk_markdown(content: str, max_chars: int = CHUNK_SIZE) -> list[str]:
    """
    將大型 Markdown 文件拆成多個區塊，盡量在空行處切割以保持語意完整。
    每個區塊（最後一個除外）會保留末尾的空行，使區塊直接串接即可還原原文。
    """
    if len(content) <= max_chars:
        return [content]

    chunks = []
    current_start = 0
    while current_start < len(content):
        end = current_start + max_chars
        if end >= len(content):
            chunks.append(content[current_start:])
            break
        # 找到最近的 \n\n 作為切割點，並將 \n\n 包含在當前區塊末尾
        cut = content.rfind("\n\n", current_start, end)
        if cut == -1 or cut <= current_start:
            # 找不到空行：強制切割，不跳過任何字元
            chunks.append(content[current_start:end])
            current_start = end
        else:
            # 切割點包含 \n\n（cut 指向第一個 \n 的位置）
            chunks.append(content[current_start : cut + 2])
            current_start = cut + 2
    return chunks


def translate_chunk(
    chunk: str,
    api_url: str,
    model: str,
    system_prompt: str,
    api_key: str,
    retries: int = 3,
) -> str:
    """呼叫 Azure OpenAI v1 API 翻譯單一區塊，失敗時自動重試。"""
    headers = {
        "api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": (
                    "請將以下 Markdown 內容翻譯成繁體中文（zh-tw）。"
                    "直接輸出翻譯結果，不要加任何前言或說明：\n\n"
                    + chunk
                ),
            },
        ],
        "temperature": 0.2,  # 低溫度讓翻譯更穩定一致
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.post(
                api_url,
                headers=headers,
                json=payload,
                timeout=120,
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except requests.HTTPError as e:
            status = e.response.status_code if e.response else "unknown"
            print(
                f"  ⚠️  HTTP {status} 錯誤（第 {attempt}/{retries} 次）：{e}",
                file=sys.stderr,
            )
            if status == 429:
                # 速率限制：等待更久
                wait = 30 * attempt
                print(f"  ⏳ 速率限制，等待 {wait}s ...", file=sys.stderr)
                time.sleep(wait)
            elif attempt < retries:
                time.sleep(REQUEST_DELAY * attempt)
            else:
                raise
        except requests.RequestException as e:
            print(f"  ⚠️  請求失敗（第 {attempt}/{retries} 次）：{e}", file=sys.stderr)
            if attempt < retries:
                time.sleep(REQUEST_DELAY * attempt)
            else:
                raise

    raise RuntimeError("翻譯失敗：已超過最大重試次數")


def translate_file(
    filepath: str,
    upstream_ref: str,
    api_url: str,
    model: str,
    system_prompt: str,
    api_key: str,
) -> bool:
    """
    翻譯單一 Markdown 檔案並寫入本地端。
    回傳 True 表示成功，False 表示略過（例如檔案不存在）。
    """
    print(f"\n📄 翻譯：{filepath}")

    content = get_file_from_upstream(filepath, upstream_ref)
    if content is None:
        print(f"  ⚠️  無法從 {upstream_ref} 取得 {filepath}，略過。", file=sys.stderr)
        return False

    chunks = chunk_markdown(content)
    print(f"  分成 {len(chunks)} 個區塊進行翻譯...")

    translated_parts = []
    for i, chunk in enumerate(chunks, 1):
        print(f"  🔄 區塊 {i}/{len(chunks)}（{len(chunk)} 字元）...")
        translated = translate_chunk(chunk, api_url, model, system_prompt, api_key)
        translated_parts.append(translated)
        if i < len(chunks):
            time.sleep(REQUEST_DELAY)

    translated_content = "".join(translated_parts) if len(chunks) > 1 else translated_parts[0]

    # 確保目錄存在
    dirpath = os.path.dirname(filepath)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(translated_content)
        # 確保檔案以換行結尾
        if not translated_content.endswith("\n"):
            f.write("\n")

    print(f"  ✅ 完成（{len(translated_content)} 字元）")
    return True


# ── 主程式 ────────────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="使用 Azure OpenAI v1 API 將 Markdown 文件翻譯成 zh-tw"
    )
    parser.add_argument(
        "--changed-files",
        required=True,
        help="含有需翻譯的 Markdown 檔案路徑清單的文字檔（每行一個路徑）",
    )
    parser.add_argument(
        "--upstream-ref",
        default="upstream/main",
        help="upstream git ref（預設：upstream/main）",
    )
    parser.add_argument(
        "--glossary",
        default="GLOSSARY.md",
        help="術語表 Markdown 檔案路徑（預設：GLOSSARY.md）",
    )
    args = parser.parse_args()

    endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT", "")
    api_key = os.environ.get("AZURE_OPENAI_API_KEY", "")
    model = os.environ.get("AZURE_OPENAI_MODEL", "")

    missing = [
        name
        for name, value in (
            ("AZURE_OPENAI_ENDPOINT", endpoint),
            ("AZURE_OPENAI_API_KEY", api_key),
            ("AZURE_OPENAI_MODEL", model),
        )
        if not value
    ]
    if missing:
        print(
            f"❌ 錯誤：缺少必要環境變數：{', '.join(missing)}。",
            file=sys.stderr,
        )
        print(
            "   請在 Repository Secrets 中新增對應的 Azure OpenAI 參數。",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        api_url = build_azure_openai_chat_url(endpoint)
    except ValueError as exc:
        print(f"❌ 錯誤：{exc}", file=sys.stderr)
        sys.exit(1)

    # 讀取術語表
    glossary_content = load_glossary(args.glossary)
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(glossary=glossary_content)

    # 讀取需翻譯的檔案清單
    with open(args.changed_files, encoding="utf-8") as f:
        filepaths = [line.strip() for line in f if line.strip()]

    if not filepaths:
        print("ℹ️  沒有需要翻譯的 Markdown 檔案。")
        return

    print(f"🌏 開始翻譯 {len(filepaths)} 個檔案（使用 {model}）...\n")

    succeeded = []
    failed = []

    for filepath in filepaths:
        try:
            ok = translate_file(
                filepath,
                args.upstream_ref,
                api_url,
                model,
                system_prompt,
                api_key,
            )
            if ok:
                succeeded.append(filepath)
            time.sleep(REQUEST_DELAY)
        except Exception as e:
            print(f"  ❌ {filepath} 翻譯失敗：{e}", file=sys.stderr)
            failed.append(filepath)

    # 輸出摘要
    print(f"\n{'='*60}")
    print(f"✅ 成功翻譯：{len(succeeded)} 個檔案")
    if succeeded:
        for p in succeeded:
            print(f"   - {p}")
    if failed:
        print(f"❌ 翻譯失敗：{len(failed)} 個檔案")
        for p in failed:
            print(f"   - {p}")
        sys.exit(1)  # 以非零狀態結束，讓 workflow 標記為失敗


if __name__ == "__main__":
    main()
