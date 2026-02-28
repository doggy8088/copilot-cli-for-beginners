# Skills 範例

適用於 GitHub Copilot CLI 的現成 skill 範本。複製任一 skill 資料夾即可立即使用。

## 快速開始

```bash
# Copy a skill to your personal skills folder
cp -r hello-world ~/.copilot/skills/

# Or copy to your project for team sharing
cp -r code-checklist .github/skills/
```

## 可用的 Skills

| Skill | 說明 | 適用情境 |
|-------|------|----------|
| `hello-world` | 最簡範例（學習格式用） | 初次建立 skill 的人 |
| `code-checklist` | Python 程式碼品質檢查清單（PEP 8、型別提示、驗證） | 維持一致的品質標準 |
| `pytest-gen` | 生成完整的 pytest 測試 | 結構化測試生成 |
| `commit-message` | 慣例式提交訊息 | 標準化的 git 歷史紀錄 |

## Skills 的運作方式

當你的提示符合 skill 的 `description` 欄位時，Skills 會**自動觸發**，無需手動呼叫。

```bash
copilot

> Check this code for quality issues
# Copilot detects this matches "code-checklist" skill and loads it automatically

> Generate a commit message
# Copilot loads the "commit-message" skill
```

你也可以直接呼叫 skills：
```bash
> /code-checklist Check books.py
> /pytest-gen Generate tests for BookCollection
> /commit-message
```

## Skill 結構

每個 skill 是一個包含 `SKILL.md` 檔案的資料夾：

```
skill-name/
└── SKILL.md    # Required: Contains frontmatter + instructions
```

`SKILL.md` 檔案包含 YAML 前置區塊，`name` 和 `description` 均為必填欄位：

```markdown
---
name: my-skill
description: What this skill does and when to use it
---

# Skill Instructions

Your instructions here...
```

## 探索更多 Skills

- **[github/awesome-copilot](https://github.com/github/awesome-copilot)** - GitHub 官方資源，收錄社群 skills
- **`/plugin marketplace`** - 在 Copilot CLI 內瀏覽並安裝 skills

## 建立你自己的 Skill

1. 建立資料夾：`mkdir ~/.copilot/skills/my-skill`
2. 建立包含前置區塊的 `SKILL.md`
3. 加入你的指令說明
4. 向 Copilot 提問符合你描述的問題，進行測試

詳細說明請參閱 [第 05 章：Skills](../../05-skills/README.md)。
