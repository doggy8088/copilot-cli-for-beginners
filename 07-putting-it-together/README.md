![Chapter 07: Putting It All Together](images/chapter-header.png)

> **您所學的一切在此匯聚。在單一工作階段中，從想法到合併 PR。**

在本章中，您將把所學的一切整合成完整的工作流程。您將使用多代理程式協作來建構功能、設定能在提交前攔截安全問題的 pre-commit 鉤子、將 Copilot 整合進 CI/CD 流水線，並在單一終端工作階段中從功能想法到合併 PR。這正是 GitHub Copilot CLI 成為真正效率倍增器的地方。

> 💡 **注意**：本章示範如何組合您所學的一切。**您不需要代理程式、技能或 MCP 才能保持高效（儘管它們非常有幫助）。** 核心工作流程——描述、規劃、實作、測試、審查、交付——只需使用第 00-03 章的內建功能即可運作。

## 🎯 學習目標

完成本章後，您將能夠：

- 在統一的工作流程中組合代理程式、技能和 MCP（模型情境協定）
- 使用多工具方法建構完整功能
- 利用鉤子設定基本自動化
- 應用專業開發的最佳實踐

> ⏱️ **預計時間**：約 75 分鐘（15 分鐘閱讀 + 60 分鐘實作）

---

## 🧩 現實類比：管弦樂團

<img src="images/orchestra-analogy.png" alt="Orchestra Analogy - Unified Workflow" width="800"/>

交響樂團由多個聲部組成：
- **弦樂**提供基礎（如您的核心工作流程）
- **銅管**增添力度（如具備專業知識的代理程式）
- **木管**增添色彩（如擴展能力的技能）
- **打擊樂**維持節奏（如連接外部系統的 MCP）

單獨來看，每個聲部都有其局限。但在出色的指揮下，它們共同創造出宏偉的樂章。

**這正是本章所要教授的！**<br>
*就像指揮家與管弦樂團，您統籌代理程式、技能和 MCP，形成統一的工作流程*

讓我們從一個情境開始，演示如何在單一工作階段中修改程式碼、產生測試、審查並建立 PR。

---

## 從想法到合併 PR，一氣呵成

與其在編輯器、終端、測試執行器和 GitHub UI 之間反覆切換並不斷失去情境，您可以在單一終端工作階段中組合所有工具。我們將在下方的[整合模式](#the-integration-pattern-for-power-users)一節中詳細說明此模式。

```bash
# Start Copilot in interactive mode
copilot

> I need to add a "list unread" command to the book app that shows only
> books where read is False. What files need to change?

# Copilot creates high-level plan...

# SWITCH TO PYTHON-REVIEWER AGENT
> /agent
# Select "python-reviewer"

> @samples/book-app-project/books.py Design a get_unread_books method.
> What is the best approach?

# Python-reviewer agent produces:
# - Method signature and return type
# - Filter implementation using list comprehension
# - Edge case handling for empty collections

# SWITCH TO PYTEST-HELPER AGENT
> /agent
# Select "pytest-helper"

> @samples/book-app-project/tests/test_books.py Design test cases for
> filtering unread books.

# Pytest-helper agent produces:
# - Test cases for empty collections
# - Test cases with mixed read/unread books
# - Test cases with all books read

# IMPLEMENT
> Add a get_unread_books method to BookCollection in books.py
> Add a "list unread" command option in book_app.py
> Update the help text in the show_help function

# TEST
> Generate comprehensive tests for the new feature

# Multiple tests are generated similar to the following:
# - Happy path (3 tests) — filters correctly, excludes read, includes unread
# - Edge cases (4 tests) — empty collection, all read, none read, single book
# - Parametrized (5 cases) — varying read/unread ratios via @pytest.mark.parametrize
# - Integration (4 tests) — interplay with mark_as_read, remove_book, add_book, and data integrity

# Review the changes
> /review

# If review passes, generate a PR (uses GitHub MCP covered earlier in the course)
> Create a pull request titled "Feature: Add list unread books command"
```

**傳統做法**：在編輯器、終端、測試執行器、文件和 GitHub UI 之間切換，每次切換都造成情境流失和摩擦。

**核心洞察**：您像架構師一樣指揮專家。他們負責細節，您負責願景。

> 💡 **進一步深入**：對於像這樣的大型多步驟計劃，可嘗試 `/fleet`，讓 Copilot 平行執行獨立的子任務。詳情請參閱[官方文件](https://docs.github.com/copilot/concepts/agents/copilot-cli/fleet)。

---

<details>
<summary>🎬 觀看實際演示！</summary>

<img src="images/full-review-demo.gif" alt="Full Review Demo">

<em>示範輸出僅供參考。您的模型、工具和回應可能與此處顯示的有所不同。</em>

</details>

---

# 更多工作流程

<img src="images/combined-workflows.png" alt="People assembling a colorful giant jigsaw puzzle with gears, representing how agents, skills, and MCP combine into unified workflows" width="800"/>

對於已完成第 04-06 章的進階使用者，這些工作流程展示了代理程式、技能和 MCP 如何倍增您的效率。

## 整合模式

以下是組合所有工具的心智模型：

<img src="images/integration-pattern.png" alt="The Integration Pattern - A 4-phase workflow: Gather Context (MCP), Analyze and Plan (Agents), Execute (Skills + Manual), Complete (MCP)" width="800"/>

---

## 工作流程 1：Bug 調查與修復

搭配完整工具整合的真實 bug 修復流程：

```bash
copilot

# PHASE 1: Understand the bug from GitHub (MCP provides this)
> Get the details of issue #1

# Learn: "find_by_author doesn't work with partial names"

# PHASE 2: Research best practice (deep research with web + GitHub sources)
> /research Best practices for Python case-insensitive string matching

# PHASE 3: Find related code
> @samples/book-app-project/books.py Show me the find_by_author method

# PHASE 4: Get expert analysis
> /agent
# Select "python-reviewer"

> Analyze this method for issues with partial name matching

# Agent identifies: Method uses exact equality instead of substring matching

# PHASE 5: Fix with agent guidance
> Implement the fix using lowercase comparison and 'in' operator

# PHASE 6: Generate tests
> /agent
# Select "pytest-helper"

> Generate pytest tests for find_by_author with partial matches
> Include test cases: partial name, case variations, no matches

# PHASE 7: Commit and PR
> Generate a commit message for this fix

> Create a pull request linking to issue #1
```

---

## 工作流程 2：自動化程式碼審查（選讀）

> 💡 **本節為選讀內容。** Pre-commit 鉤子對團隊很有用，但並非提升效率的必要條件。如果您才剛開始，可以跳過此節。
>
> ⚠️ **效能注意事項**：此鉤子會對每個已暫存的檔案呼叫 `copilot -p`，每個檔案需要數秒。對於大型提交，建議僅限於關鍵檔案，或改為手動使用 `/review` 進行審查。

**git 鉤子**是 Git 在特定時間點自動執行的腳本，例如在提交之前。您可以使用此功能對程式碼執行自動化檢查。以下是如何為您的提交設定自動化 Copilot 審查：

```bash
# Create a pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash

# Get staged files (Python files only)
STAGED=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.py$')

if [ -n "$STAGED" ]; then
  echo "Running Copilot review on staged files..."

  for file in $STAGED; do
    echo "Reviewing $file..."

    # Use timeout to prevent hanging (60 seconds per file)
    # --allow-all auto-approves file reads/writes so the hook can run unattended.
    # Only use this in automated scripts. In interactive sessions, let Copilot ask for permission.
    REVIEW=$(timeout 60 copilot --allow-all -p "Quick security review of @$file - critical issues only" 2>/dev/null)

    # Check if timeout occurred
    if [ $? -eq 124 ]; then
      echo "Warning: Review timed out for $file (skipping)"
      continue
    fi

    if echo "$REVIEW" | grep -qi "CRITICAL"; then
      echo "Critical issues found in $file:"
      echo "$REVIEW"
      exit 1
    fi
  done

  echo "Review passed"
fi
EOF

chmod +x .git/hooks/pre-commit
```

> ⚠️ **macOS 使用者**：macOS 預設不包含 `timeout` 指令。請以 `brew install coreutils` 安裝，或直接移除 `timeout 60` 以省略超時保護。

> 📚 **官方文件**：[使用鉤子](https://docs.github.com/copilot/how-tos/copilot-cli/use-hooks)與[鉤子設定參考](https://docs.github.com/copilot/reference/hooks-configuration)，提供完整的 hooks API。
>
> 💡 **內建替代方案**：Copilot CLI 也有內建的鉤子系統（`copilot hooks`），可在 pre-commit 等事件時自動執行。上方的手動 git 鉤子提供完整控制，而內建系統設定更簡便。請參閱上方文件，決定哪種方式更適合您的工作流程。

如此一來，每次提交都會進行快速的安全審查：

```bash
git add samples/book-app-project/books.py
git commit -m "Update book collection methods"

# Output:
# Running Copilot review on staged files...
# Reviewing samples/book-app-project/books.py...
# Critical issues found in samples/book-app-project/books.py:
# - Line 15: File path injection vulnerability in load_from_file
#
# Fix the issue and try again.
```

---

## 工作流程 3：加入新程式碼庫的新手上路

加入新專案時，結合情境、代理程式和 MCP 快速上手：

```bash
# Start Copilot in interactive mode
copilot

# PHASE 1: Get the big picture with context
> @samples/book-app-project/ Explain the high-level architecture of this codebase

# PHASE 2: Understand a specific flow
> @samples/book-app-project/book_app.py Walk me through what happens
> when a user runs "python book_app.py add"

# PHASE 3: Get expert analysis with an agent
> /agent
# Select "python-reviewer"

> @samples/book-app-project/books.py Are there any design issues,
> missing error handling, or improvements you would recommend?

# PHASE 4: Find something to work on (MCP provides GitHub access)
> List open issues labeled "good first issue"

# PHASE 5: Start contributing
> Pick the simplest open issue and outline a plan to fix it
```

此工作流程將 `@` 情境、代理程式和 MCP 整合進單一的新手上路工作階段，正是本章前面介紹的整合模式。

---

# 最佳實踐與自動化

讓您的工作流程更有效率的模式與習慣。

---

## 最佳實踐

### 1. 分析前先收集情境

在請求分析前，務必先收集情境：

```bash
# Good
> Get the details of issue #42
> /agent
# Select python-reviewer
> Analyze this issue

# Less effective
> /agent
# Select python-reviewer
> Fix login bug
# Agent doesn't have issue context
```

### 2. 了解差異：代理程式、技能與自訂指令

每種工具都有其最適合的使用情境：

```bash
# Agents: Specialized personas you explicitly activate
> /agent
# Select python-reviewer
> Review this authentication code for security issues

# Skills: Modular capabilities that auto-activate when your prompt
# matches the skill's description (you must create them first — see Ch 05)
> Generate comprehensive tests for this code
# If you have a testing skill configured, it activates automatically

# Custom instructions (.github/copilot-instructions.md): Always-on
# guidance that applies to every session without switching or triggering
```

> 💡 **重點**：代理程式和技能都能分析並產生程式碼。真正的差異在於**啟動方式**——代理程式是明確啟動（`/agent`），技能是自動觸發（依提示詞比對），而自訂指令則永遠保持啟用。

### 3. 保持工作階段聚焦

使用 `/rename` 為您的工作階段命名（方便在歷史記錄中查找），並以 `/exit` 乾淨地結束：

```bash
# Good: One feature per session
> /rename list-unread-feature
# Work on list unread
> /exit

copilot
> /rename export-csv-feature
# Work on CSV export
> /exit

# Less effective: Everything in one long session
```

### 4. 借助 Copilot 讓工作流程可重複使用

與其只是在 wiki 上記錄工作流程，不如直接在程式庫中編碼，讓 Copilot 也能利用：

- **自訂指令**（`.github/copilot-instructions.md`）：針對程式碼標準、架構規則及建構/測試/部署步驟的永遠啟用指引，每個工作階段都自動遵循。
- **提示詞檔案**（`.github/prompts/`）：可重複使用且可參數化的提示詞，供團隊共享——例如程式碼審查、元件產生或 PR 描述的範本。
- **自訂代理程式**（`.github/agents/`）：編碼專屬角色（例如安全審查員或文件撰寫員），讓團隊任何人都可以用 `/agent` 啟用。
- **自訂技能**（`.github/skills/`）：打包逐步工作流程指令，於相關時自動啟用。

> 💡 **回報**：新團隊成員免費獲得您的工作流程——它們內建於程式庫，而不是鎖在某人腦中。

---

## 進階：生產環境模式

這些模式是選讀內容，但對專業環境很有價值。

### PR 描述產生器

```bash
# Generate comprehensive PR descriptions
BRANCH=$(git branch --show-current)
COMMITS=$(git log main..$BRANCH --oneline)

copilot -p "Generate a PR description for:
Branch: $BRANCH
Commits:
$COMMITS

Include: Summary, Changes Made, Testing Done, Screenshots Needed"
```

### CI/CD 整合

對於已有 CI/CD 流水線的團隊，您可以使用 GitHub Actions 在每個 PR 上自動執行 Copilot 審查，包括自動發布審查意見並篩選關鍵問題。

> 📖 **深入了解**：請參閱 [CI/CD 整合](../appendices/ci-cd-integration.md)，獲取完整的 GitHub Actions 工作流程、設定選項和疑難排解提示。

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

將完整的工作流程付諸實踐。

---

## ▶️ 親自試試看

完成示範後，嘗試以下變化：

1. **端對端挑戰**：選擇一個小功能（例如「列出未讀書籍」或「匯出為 CSV」）。使用完整工作流程：
   - 以 `/plan` 規劃
   - 以代理程式設計（python-reviewer、pytest-helper）
   - 實作
   - 產生測試
   - 建立 PR

2. **自動化挑戰**：設定「程式碼審查自動化工作流程」中的 pre-commit 鉤子。提交一個帶有刻意設計的檔案路徑漏洞的提交。它會被攔截嗎？

3. **您的生產工作流程**：為您常做的某個任務設計自己的工作流程。以清單形式記錄下來。哪些部分可以用技能、代理程式或鉤子自動化？

**自我檢核**：當您能向同事說明代理程式、技能和 MCP 如何協同運作，以及各自的使用時機時，您就完成了本課程。

---

## 📝 作業

### 主要挑戰：端對端功能

實作範例帶您完成了「列出未讀書籍」功能的建構。現在，請在另一個功能上練習完整工作流程：**依年份範圍搜尋書籍**：

1. 啟動 Copilot 並收集情境：`@samples/book-app-project/books.py`
2. 以 `/plan Add a "search by year" command that lets users find books published between two years` 進行規劃
3. 在 `BookCollection` 中實作 `find_by_year_range(start_year, end_year)` 方法
4. 在 `book_app.py` 中新增 `handle_search_year()` 函式，提示使用者輸入起始和結束年份
5. 產生測試：`@samples/book-app-project/books.py @samples/book-app-project/tests/test_books.py Generate tests for find_by_year_range() including edge cases like invalid years, reversed range, and no results.`
6. 以 `/review` 審查
7. 更新 README：`@samples/book-app-project/README.md Add documentation for the new "search by year" command.`
8. 產生提交訊息

過程中記錄您的工作流程。

**成功標準**：您使用 Copilot CLI 從想法到提交完成了整個功能，包括規劃、實作、測試、文件和審查。

> 💡 **進階**：如果您已在第 04 章設定了代理程式，嘗試建立並使用自訂代理程式。例如，一個用於實作審查的 error-handler 代理程式，和一個用於 README 更新的 doc-writer 代理程式。

<details>
<summary>💡 提示（點擊展開）</summary>

**遵循本章開頭[「從想法到合併 PR」](#從想法到合併-pr一氣呵成)範例的模式**。關鍵步驟如下：

1. 以 `@samples/book-app-project/books.py` 收集情境
2. 以 `/plan Add a "search by year" command` 規劃
3. 實作方法和指令處理器
4. 產生包含邊界情況的測試（無效輸入、無結果、反向範圍）
5. 以 `/review` 審查
6. 以 `@samples/book-app-project/README.md` 更新 README
7. 以 `-p` 產生提交訊息

**需要考慮的邊界情況：**
- 如果使用者輸入「2000」和「1990」（反向範圍）怎麼辦？
- 如果沒有書籍符合範圍怎麼辦？
- 如果使用者輸入非數字怎麼辦？

**關鍵在於練習完整工作流程**：想法 → 情境 → 規劃 → 實作 → 測試 → 文件 → 提交。

</details>

---

<details>
<summary>🔧 <strong>常見錯誤</strong>（點擊展開）</summary>

| 錯誤 | 後果 | 解決方法 |
|------|------|----------|
| 直接跳到實作 | 遺漏設計問題，事後修復代價高昂 | 先用 `/plan` 思考方法 |
| 只用一種工具，其實可以用多種 | 結果較慢、較不全面 | 組合使用：代理程式分析 → 技能執行 → MCP 整合 |
| 提交前未審查 | 安全問題或 bug 溜過 | 始終執行 `/review` 或使用 [pre-commit 鉤子](#工作流程-2自動化程式碼審查選讀) |
| 忘記與團隊共享工作流程 | 每個人各自重複造輪子 | 在共享的代理程式、技能和指令中記錄模式 |

</details>

---

# 總結

## 🔑 重點摘要

1. **整合 > 孤立**：組合工具以發揮最大效益
2. **情境優先**：分析前務必先收集所需情境
3. **代理程式分析，技能執行**：選對適合任務的工具
4. **自動化重複工作**：鉤子和腳本讓您的效率倍增
5. **記錄工作流程**：可共享的模式讓整個團隊受益

> 📋 **快速參考**：請參閱 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)，獲取完整的指令和快捷鍵清單。

---

## 🎓 課程完成！

恭喜！您已學習：

| 章節 | 您學到的內容 |
|------|-------------|
| 00 | Copilot CLI 安裝與快速入門 |
| 01 | 三種互動模式 |
| 02 | 使用 @ 語法管理情境 |
| 03 | 開發工作流程 |
| 04 | 專業代理程式 |
| 05 | 可擴展的技能 |
| 06 | 透過 MCP 連接外部資源 |
| 07 | 統一的生產環境工作流程 |

您現在已具備將 GitHub Copilot CLI 作為真正效率倍增器的能力。

## ➡️ 接下來

您的學習不止於此：

1. **每日練習**：將 Copilot CLI 用於實際工作
2. **建立自訂工具**：為您的特定需求建立代理程式和技能
3. **分享知識**：協助團隊採用這些工作流程
4. **保持更新**：關注 GitHub Copilot 的最新功能

### 資源

- [GitHub Copilot CLI 文件](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)
- [MCP 伺服器登錄檔](https://github.com/modelcontextprotocol/servers)
- [社群技能](https://github.com/topics/copilot-skill)

---

**做得好！現在去建構令人驚嘆的作品吧。**

**[← 返回第 06 章](../06-mcp-servers/README.md)** | **[返回課程首頁 →](../README.md)**
