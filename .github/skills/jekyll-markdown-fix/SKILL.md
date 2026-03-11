---
name: jekyll-markdown-fix
description: 診斷並修復 Jekyll/GitHub Pages Markdown 渲染問題 - 適用於 details 區塊內容未渲染、HTML 標籤外洩為純文字等問題
---

# Jekyll Markdown 渲染問題修復技能

當 GitHub Pages (Jekyll + Kramdown) 的 Markdown 未正確渲染時，使用此技能進行診斷與修復。

## 已知問題類型

### 問題一：`<details>` 區塊內的 Markdown 未渲染

**症狀**：`<details>` 折疊區塊展開後，表格、標題、程式碼區塊、引用等 Markdown 語法以純文字顯示，未轉換為 HTML。

**根本原因**：Jekyll 使用 Kramdown 作為 Markdown 處理器。預設情況下，Kramdown 不處理 HTML 區塊內部的 Markdown 語法，直接將其原樣輸出。

**修復方式**：在含有 Markdown 內容的 `<details>` 標籤加上 `markdown="1"` 屬性：

```diff
-<details>
+<details markdown="1">
 <summary>展開查看詳情</summary>

 | 欄位 | 說明 |
 |------|------|
 | 範例 | 表格內容 |

 </details>
```

**受影響的 Markdown 語法**（需加 `markdown="1"` 才能正確渲染）：
- 表格 `| ... |`
- 標題 `### ...`
- 程式碼區塊（以 ` ``` ` 開頭的行）
- 引用區塊 `> ...`
- 無序清單 `- ...`
- 有序清單 `1. ...`

> 💡 **僅含純 HTML 的 `<details>` 不需要加此屬性**（例如只含 `<img>` 或 `<em>` 的區塊）。

---

### 問題二：HTML 標籤外洩為純文字（例如 `</a>`）

**症狀**：頁面上出現裸露的 HTML 標籤，如 `</a>`、`</picture>` 等，被視為純文字顯示。

**根本原因**：Kramdown 的 HTML 區塊解析規則在偵測到某些巢狀 HTML 標籤（如 `<picture>` 在 `<a>` 內）時，提前結束 HTML 區塊，導致後續閉合標籤（如 `</a>`）脫離 HTML 環境，被輸出為文字。

**常見情境**：`<a>` 包裹 `<picture>` 且 `<picture>` 沒有 `<source>` 子元素時，`<picture>` 本身毫無作用，卻會破壞解析。

**修復方式**：移除無用的 `<picture>` 包裝，直接使用 `<img>`：

```diff
 <a href="https://example.com" target="_blank">
-  <picture>
-    <img src="./image.png" alt="說明" width="100%" />
-  </picture>
+  <img src="./image.png" alt="說明" width="100%" />
 </a>
```

> 💡 **`<picture>` 的正確用法**：只在需要提供多種格式或依視口切換圖片時使用，且必須搭配 `<source>` 子元素。

---

## 診斷流程

當頁面出現渲染異常時，依序執行：

### 步驟一：搜尋所有 `<details>` 區塊

```bash
grep -rn "^<details>" --include="*.md" .
```

### 步驟二：確認哪些區塊含有 Markdown 內容

```bash
# 找出沒有 markdown="1" 但含有 Markdown 語法的 <details>
python3 << 'EOF'
import re, glob

for filepath in glob.glob('**/*.md', recursive=True):
    with open(filepath) as f:
        lines = f.readlines()
    in_details, has_md1, start = False, False, 0
    content = []
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if re.match(r'^<details[\s>]', stripped):
            in_details, start, has_md1 = True, i, 'markdown="1"' in line
            content = []
        elif stripped == '</details>' and in_details:
            md_patterns = [r'^#{1,6} ', r'^\|', r'^```', r'^- ', r'^\* ', r'^> ', r'^\d+\. ']
            has_md_content = any(
                re.match(p, c.strip()) for c in content for p in md_patterns
            )
            if not has_md1 and has_md_content:
                print(f"{filepath}:{start}: 缺少 markdown=\"1\"")
            in_details = False
        elif in_details:
            content.append(line)
EOF
```

### 步驟三：搜尋 `<picture>` 標籤

```bash
grep -rn "<picture>" --include="*.md" .
# 確認每個 <picture> 是否有 <source> 子元素；若無，移除 <picture> 包裝
```

---

## 批次修復指令

### 自動為含 Markdown 的 `<details>` 加上 `markdown="1"`

```bash
# 先備份，再執行 in-place 替換
# 注意：此指令僅適用於獨立成行的 <details> 標籤
# Linux (GNU sed):
grep -rl "^<details>$" --include="*.md" . | xargs -r sed -i 's/^<details>$/<details markdown="1">/'
# macOS (BSD sed，需要備份副檔名，用空字串表示不備份):
grep -rl "^<details>$" --include="*.md" . | xargs sed -i '' 's/^<details>$/<details markdown="1">/'
```

> ⚠️ **請務必人工確認**：部分 `<details>` 只含純 HTML（如 GIF 圖片展示），不需要 `markdown="1"`。批次替換後請逐一檢視。

---

## 驗證方式

修復後，在本機啟動 Jekyll 預覽確認：

```bash
bundle exec jekyll serve
# 開啟 http://localhost:4000 確認頁面渲染正常
```

或直接檢視原始 HTML 輸出中是否仍有 Markdown 語法殘留（如 `|---`、` ``` ` 等字串）。
