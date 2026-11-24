# 範例 Skill

GitHub Copilot CLI 的現成 skill 範本。複製任一 skill 資料夾即可立即使用。

## 快速開始

```bash
# 複製 skill 到你的個人 skills 資料夾
cp -r hello-world ~/.copilot/skills/

# 或複製到你的專案中以便團隊共享
cp -r code-checklist .github/skills/
```

## 可用的 Skill

| Skill | 說明 | 最適用於 |
|-------|-------------|----------|
| `hello-world` | 最簡範例（學習格式用） | 首次建立 skill 的使用者 |
| `code-checklist` | Python 程式碼品質檢查清單（PEP 8、型別提示、驗證） | 一致的品質檢查 |
| `pytest-gen` | 產生完整的 pytest 測試 | 結構化測試產生 |
| `commit-message` | Conventional Commit 訊息 | 標準化 git 歷史 |

## Skill 如何運作

當你的提示詞符合 skill 的 `description` 欄位時，Skill 會**自動觸發**。你不需要手動呼叫它們。

```bash
copilot

> Check this code for quality issues
# Copilot 偵測到這符合 "code-checklist" skill 並自動載入

> Generate a commit message
# Copilot 載入 "commit-message" skill
```

你也可以直接呼叫 skill：
```
> /code-checklist Check books.py
> /pytest-gen Generate tests for BookCollection
> /commit-message
```

## Skill 結構

每個 skill 是一個包含 `SKILL.md` 檔案的資料夾：

```
skill-name/
└── SKILL.md    # 必要：包含 frontmatter 與指令說明
```

`SKILL.md` 檔案需有 YAML frontmatter，包含 `name` 和 `description`（兩者皆必填）：

```markdown
---
name: my-skill
description: 這個 skill 的用途與適用時機
---

# Skill 指令說明

在這裡撰寫你的指令說明...
```

## 尋找更多 Skill

- **[github/awesome-copilot](https://github.com/github/awesome-copilot)** - 官方 GitHub 資源與社群 skill
- **`/plugin marketplace`** - 直接在 Copilot CLI 內瀏覽並安裝 skill

## 自行建立 Skill

1. 建立資料夾：`mkdir ~/.copilot/skills/my-skill`
2. 建立帶有 frontmatter 的 `SKILL.md`
3. 加入你的指令說明
4. 測試：請 Copilot 執行符合你描述的內容

詳細教學請參見 [第 05 章：Skill](../../05-skills/README.md)。
