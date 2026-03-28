![Chapter 07: Putting It All Together](images/chapter-header.png)

> **你學到的一切都將在這裡結合。從想法到合併 PR，一次完成。**

在本章中，你將把所學的內容整合成完整的工作流程。你會利用多 Agent 協作來開發功能，設定 pre-commit hook 在提交前攔截安全性問題，將 Copilot 整合進 CI/CD 流程，並從功能構想到合併 PR，一次在終端機 session 內完成。這正是 GitHub Copilot CLI 成為真正倍增器的時刻。

> 💡 **注意**：本章展示如何結合你所學的一切。**你不需要 Agent、Skill 或 MCP 才能高效工作（雖然它們很有幫助）。** 核心工作流程——描述、規劃、實作、測試、審查、發佈——只靠第 00-03 章的內建功能就能完成。

## 🎯 學習目標

完成本章後，你將能夠：

- 在統一的工作流程中結合 Agent、Skill 與 MCP（模型情境協定）
- 以多工具方法建構完整功能
- 以 hook 建立基本自動化
- 應用專業開發的最佳實踐

> ⏱️ **預估時間**：約 75 分鐘（閱讀 15 分鐘 + 實作 60 分鐘）

---

## 🧩 真實世界比喻：管弦樂團

<img src="images/orchestra-analogy.png" alt="Orchestra Analogy - Unified Workflow" width="800"/>

一個交響樂團有許多聲部：
- **弦樂** 提供基礎（就像你的核心工作流程）
- **銅管** 增添力量（就像具專業知識的 Agent）
- **木管** 增添色彩（就像擴充能力的 Skill）
- **打擊樂** 維持節奏（就像 MCP 連接外部系統）

單獨來看，每個聲部都有限。但若能妥善指揮，合奏就能創造壯麗的樂章。

**這正是本章要教你的！**<br>
*就像指揮家帶領樂團，你要協調 Agent、Skill 與 MCP，組成統一的工作流程*

讓我們從一個情境開始，這個情境會修改程式碼、產生測試、審查並建立 PR——全部在同一個 session 內完成。

---

## 一次 Session 從想法到合併 PR

你不必再在編輯器、終端機、測試工具與 GitHub 介面間來回切換、每次都失去情境。你可以把所有工具整合在同一個終端機 session 內。我們會在下方的 [整合模式](#the-integration-pattern-for-power-users) 章節詳細拆解這個模式。

```bash
# 啟動 Copilot 互動模式
copilot

> 我需要在書籍應用程式中新增一個 "list unread" 指令，只顯示
> read 為 False 的書。哪些檔案需要修改？

# Copilot 產生高階規劃...

# 切換到 PYTHON-REVIEWER AGENT
> /agent
# 選擇 "python-reviewer"

> @samples/book-app-project/books.py 設計一個 get_unread_books 方法。
> 最佳做法是什麼？

# Python-reviewer agent 產生：
# - 方法簽名與回傳型別
# - 使用 list comprehension 的篩選實作
# - 處理空集合等邊界情境

# 切換到 PYTEST-HELPER AGENT
> /agent
# 選擇 "pytest-helper"

> @samples/book-app-project/tests/test_books.py 設計
> 篩選未讀書籍的測試案例。

# Pytest-helper agent 產生：
# - 空集合的測試案例
# - 混合已讀/未讀書籍的測試案例
# - 全部已讀書籍的測試案例

# 實作
> 在 books.py 的 BookCollection 中新增 get_unread_books 方法
> 在 book_app.py 新增 "list unread" 指令選項
> 更新 show_help 函式的說明文字

# 測試
> 產生新功能的完整測試

# 產生多個測試，類似以下內容：
# - 標準情境（3 個測試）— 正確篩選，排除已讀，包含未讀
# - 邊界情境（4 個測試）— 空集合、全部已讀、全部未讀、單一本書
# - 參數化（5 種情境）— 以 @pytest.mark.parametrize 測試不同已讀/未讀比例
# - 整合測試（4 個）— 與 mark_as_read、remove_book、add_book 及資料完整性的互動

# 審查變更
> /review

# 若審查通過，使用 /pr 操作目前分支的 pull request
> /pr [view|create|fix|auto]

# 或自然詢問 Copilot 直接從終端機草擬 PR
> 建立一個標題為 "Feature: Add list unread books command" 的 pull request
```

**傳統做法**：在編輯器、終端機、測試工具、文件與 GitHub 介面間不斷切換。每次切換都會失去情境並增加摩擦。

**關鍵洞見**：你像建築師一樣指揮專家。他們處理細節，你掌控全局。

> 💡 **進階應用**：對於這種大型多步驟規劃，可以試試 `/fleet`，讓 Copilot 並行執行獨立子任務。詳情請見 [官方文件](https://docs.github.com/copilot/concepts/agents/copilot-cli/fleet)。

---

# 進階工作流程

<img src="images/combined-workflows.png" alt="People assembling a colorful giant jigsaw puzzle with gears, representing how agents, skills, and MCP combine into unified workflows" width="800"/>

對已完成第 04-06 章的進階使用者，這些工作流程展示了 Agent、Skill 與 MCP 如何倍增你的效率。

## 整合模式

這是結合一切的心智模型：

<img src="images/integration-pattern.png" alt="The Integration Pattern - A 4-phase workflow: Gather Context (MCP), Analyze and Plan (Agents), Execute (Skills + Manual), Complete (MCP)" width="800"/>

---

## 工作流程 1：錯誤調查與修正

真實世界的錯誤修正，完整整合所有工具：

```bash
copilot

# 階段 1：從 GitHub 了解錯誤（由 MCP 提供）
> 取得 issue #1 的詳細資訊

# 得知：「find_by_author 無法處理部分名稱」

# 階段 2：研究最佳實踐（結合網路與 GitHub 資源深入研究）
> /research Python 不區分大小寫字串比對的最佳實踐

# 階段 3：找出相關程式碼
> @samples/book-app-project/books.py 顯示 find_by_author 方法

# 階段 4：取得專家分析
> /agent
# 選擇 "python-reviewer"

> 分析此方法在部分名稱比對上的問題

# Agent 指出：方法使用完全相等而非子字串比對

# 階段 5：依 Agent 指引修正
> 用小寫比對與 'in' 運算子實作修正

# 階段 6：產生測試
> /agent
# 選擇 "pytest-helper"

> 產生 find_by_author 支援部分比對的 pytest 測試
> 包含測試案例：部分名稱、大小寫變化、無符合

# 階段 7：提交並建立 PR
> 產生本次修正的 commit 訊息

> 建立一個關聯 issue #1 的 pull request
```

---

## 工作流程 2：程式碼審查自動化（選用）

> 💡 **本節為選用內容。** Pre-commit hook 對團隊很有用，但不是高效工作的必要條件。若你剛開始，可先略過。
>
> ⚠️ **效能注意**：此 hook 會對每個已暫存檔案執行 `copilot -p`，每個檔案需數秒。若提交大量檔案，建議僅針對關鍵檔案，或改用 `/review` 手動審查。

**git hook** 是 Git 在特定時機自動執行的腳本，例如在 commit 前。你可以用它自動檢查程式碼。以下是設定 Copilot 自動審查 commit 的方法：

```bash
# 建立 pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash

# 取得已暫存的 Python 檔案
STAGED=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.py$')

if [ -n "$STAGED" ]; then
  echo "Running Copilot review on staged files..."

  for file in $STAGED; do
    echo "Reviewing $file..."

    # 用 timeout 防止卡住（每檔案 60 秒）
    # --allow-all 自動允許讀寫檔案，讓 hook 可無人值守執行。
    # 僅建議用於自動化腳本。互動時請讓 Copilot 詢問權限。
    REVIEW=$(timeout 60 copilot --allow-all -p "Quick security review of @$file - critical issues only" 2>/dev/null)

    # 檢查是否 timeout
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

> ⚠️ **macOS 使用者**：`timeout` 指令 macOS 預設未安裝。請用 `brew install coreutils` 安裝，或將 `timeout 60` 改為單純執行（無 timeout 保護）。

> 📚 **官方文件**：[使用 hook](https://docs.github.com/copilot/how-tos/copilot-cli/use-hooks) 及 [Hooks 設定參考](https://docs.github.com/copilot/reference/hooks-configuration) 提供完整 hooks API。
>
> 💡 **內建替代方案**：Copilot CLI 也有內建 hooks 系統（`copilot hooks`），可自動於 pre-commit 等事件執行。上述 git hook 給你完全控制權，內建系統則較易設定。請參考上述文件選擇適合你的方式。

現在每次 commit 都會自動進行安全審查：

```bash
git add samples/book-app-project/books.py
git commit -m "Update book collection methods"

# 輸出：
# Running Copilot review on staged files...
# Reviewing samples/book-app-project/books.py...
# Critical issues found in samples/book-app-project/books.py:
# - Line 15: File path injection vulnerability in load_from_file
#
# 修正問題後再試一次。
```

---

## 工作流程 3：新專案快速上手

加入新專案時，結合情境、Agent 與 MCP 快速熟悉：

```bash
# 啟動 Copilot 互動模式
copilot

# 階段 1：用情境取得全貌
> @samples/book-app-project/ 說明此程式碼庫的高階架構

# 階段 2：理解特定流程
> @samples/book-app-project/book_app.py 帶我走過
> 使用者執行 "python book_app.py add" 時發生的事

# 階段 3：用 Agent 取得專家分析
> /agent
# 選擇 "python-reviewer"

> @samples/book-app-project/books.py 有哪些設計問題、
> 缺漏的錯誤處理或建議改進？

# 階段 4：找待辦事項（MCP 提供 GitHub 存取）
> 列出標記為 "good first issue" 的開放議題

# 階段 5：開始貢獻
> 選最簡單的 open issue，規劃修正步驟
```

這個流程將 `@` 情境、Agent 與 MCP 結合成單一上手 session，正是本章前面介紹的整合模式。

---

# 最佳實踐與自動化

讓你的工作流程更有效率的模式與習慣。

---

## 最佳實踐

### 1. 分析前先蒐集情境

分析前務必先蒐集情境：

```bash
# 好的做法
> 取得 issue #42 的詳細資訊
> /agent
# 選擇 python-reviewer
> 分析此 issue

# 效果較差
> /agent
# 選擇 python-reviewer
> 修正登入錯誤
# Agent 沒有 issue 情境
```

### 2. 分清楚：Agent、Skill 與自訂指令

每種工具都有其最佳應用情境：

```bash
# Agent：你明確啟用的專業角色
> /agent
# 選擇 python-reviewer
> 審查這段驗證程式碼的安全性問題

# Skill：模組化能力，當你的提示詞
# 符合 skill 描述時自動啟用（需先建立，見第 05 章）
> 產生這段程式碼的完整測試
# 若已設定測試 skill，會自動啟用

# 自訂指令（.github/copilot-instructions.md）：全時啟用
# 的指引，適用於每個 session，無需切換或觸發
```

> 💡 **重點**：Agent 與 Skill 都能分析與產生程式碼。真正差異在於**啟用方式**——Agent 需明確呼叫（`/agent`），Skill 則自動（提示詞比對），自訂指令則全時啟用。

### 3. 保持 Session 專注

用 `/rename` 標記 session（方便日後查詢），用 `/exit` 結束 session：

```bash
# 好的：每個 session 處理一個功能
> /rename list-unread-feature
# 處理 list unread
> /exit

copilot
> /rename export-csv-feature
# 處理 CSV 匯出
> /exit

# 效果較差：所有事都塞在一個長 session
```

### 4. 讓工作流程可重用

不要只把工作流程寫在 wiki，直接編碼在 repo 讓 Copilot 可用：

- **自訂指令**（`.github/copilot-instructions.md`）：全時啟用的指引，涵蓋程式規範、架構規則、建置/測試/部署步驟。每個 session 都自動遵循。
- **提示檔**（`.github/prompts/`）：可重用、可參數化的提示詞，團隊可共用——如程式碼審查、元件產生、PR 描述等範本。
- **自訂 Agent**（`.github/agents/`）：編碼專業角色（如安全審查員、文件撰寫者），團隊成員可用 `/agent` 啟用。
- **自訂 Skill**（`.github/skills/`）：包裝逐步工作流程指令，相關時自動啟用。

> 💡 **好處**：新成員自動取得你的工作流程——它們寫在 repo 裡，不會只存在某人腦中。

---

## 加分題：正式環境模式

這些模式非必須，但對專業環境很有價值。

### PR 描述產生器

```bash
# 產生完整的 PR 描述
BRANCH=$(git branch --show-current)
COMMITS=$(git log main..$BRANCH --oneline)

copilot -p "Generate a PR description for:
Branch: $BRANCH
Commits:
$COMMITS

Include: Summary, Changes Made, Testing Done, Screenshots Needed"
```

### CI/CD 整合

若團隊已有 CI/CD 流程，可用 GitHub Actions 自動在每個 pull request 執行 Copilot 審查。這包含自動張貼審查意見，並篩選關鍵問題。

> 📖 **深入了解**：參見 [CI/CD 整合](../appendices/ci-cd-integration.md) 取得完整 GitHub Actions 工作流程、設定選項與疑難排解。

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

實際操作完整工作流程。

---

## ▶️ 自己動手試試

完成示範後，試試這些變化：

1. **端到端挑戰**：選一個小功能（如「列出未讀書籍」或「匯出 CSV」）。用完整工作流程：
   - 用 `/plan` 規劃
   - 用 Agent（python-reviewer、pytest-helper）設計
   - 實作
   - 產生測試
   - 建立 PR

2. **自動化挑戰**：設定程式碼審查自動化工作流程中的 pre-commit hook。提交一個有意的檔案路徑漏洞。會被擋下來嗎？

3. **你的正式環境工作流程**：設計你常做任務的專屬工作流程。寫成檢查清單。哪些部分可用 Skill、Agent 或 hook 自動化？

**自我檢查**：當你能向同事解釋 Agent、Skill 與 MCP 如何協作，以及何時該用哪一種時，就代表你已完成本課程。

---

## 📝 作業

### 主要挑戰：端到端功能

實作範例帶你做了「列出未讀書籍」功能。現在請用完整工作流程練習另一個功能：**依年份區間搜尋書籍**：

1. 啟動 Copilot 並蒐集情境：`@samples/book-app-project/books.py`
2. 用 `/plan Add a "search by year" command that lets users find books published between two years` 規劃
3. 在 `BookCollection` 中實作 `find_by_year_range(start_year, end_year)` 方法
4. 在 `book_app.py` 新增 `handle_search_year()` 函式，提示使用者輸入起訖年份
5. 產生測試：`@samples/book-app-project/books.py @samples/book-app-project/tests/test_books.py 產生 find_by_year_range() 的測試，包含無效年份、區間反轉、無結果等邊界情境`
6. 用 `/review` 審查
7. 更新 README：`@samples/book-app-project/README.md 新增 "search by year" 指令的說明`
8. 產生 commit 訊息

邊做邊記錄你的工作流程。

**成功標準**：你已用 Copilot CLI 完成從想法到 commit 的功能開發，包括規劃、實作、測試、文件與審查。

> 💡 **加分**：若你已設定第 04 章的 Agent，試著建立並使用自訂 Agent。例如，實作審查用 error-handler agent，更新 README 用 doc-writer agent。

<details>
<summary>💡 提示（點擊展開）</summary>

**請參考本章開頭 ["一次 Session 從想法到合併 PR"](#idea-to-merged-pr-in-one-session) 的範例**。關鍵步驟如下：

1. 用 `@samples/book-app-project/books.py` 蒐集情境
2. 用 `/plan Add a "search by year" command` 規劃
3. 實作方法與指令處理器
4. 產生含邊界情境（無效輸入、無結果、區間反轉）的測試
5. 用 `/review` 審查
6. 用 `@samples/book-app-project/README.md` 更新 README
7. 用 `-p` 產生 commit 訊息

**可思考的邊界情境：**
- 使用者輸入 "2000" 和 "1990"（區間反轉）怎麼辦？
- 若無書籍符合區間怎麼辦？
- 使用者輸入非數字怎麼辦？

**重點是練習完整工作流程**：從想法 → 情境 → 規劃 → 實作 → 測試 → 文件 → commit。

</details>

---

<details>
<summary>🔧 <strong>常見錯誤</strong>（點擊展開）</summary>

| 錯誤 | 結果 | 修正方式 |
|---------|--------------|-----|
| 直接實作 | 錯過設計問題，後續修正成本高 | 先用 `/plan` 思考做法 |
| 只用單一工具 | 速度慢、結果不完整 | 結合：Agent 分析 → Skill 執行 → MCP 整合 |
| 未審查就提交 | 安全性問題或 bug 混入 | 一定要執行 `/review` 或用 [pre-commit hook](#workflow-2-code-review-automation-optional) |
| 忘記與團隊分享流程 | 每人都要重頭摸索 | 用共用 Agent、Skill、指令文件記錄模式 |

</details>

---

# 小結

## 🔑 重點整理

1. **整合 > 各自為政**：結合工具發揮最大效益
2. **先情境再分析**：分析前務必蒐集所需情境
3. **Agent 負責分析，Skill 負責執行**：用對工具做對事
4. **重複自動化**：hook 與腳本讓你事半功倍
5. **文件化工作流程**：可共用的模式造福全團隊

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## 🎓 恭喜完成課程！

你已學會：

| 章節 | 你學到的內容 |
|---------|-------------------|
| 00 | Copilot CLI 安裝與快速上手 |
| 01 | 三種互動模式 |
| 02 | 用 @ 語法管理情境 |
| 03 | 開發工作流程 |
| 04 | 專業 Agent |
| 05 | 可擴充 Skill |
| 06 | 透過 MCP 連接外部資源 |
| 07 | 統一的正式環境工作流程 |

你現在已能將 GitHub Copilot CLI 作為開發流程的真正倍增器。

## ➡️ 接下來

你的學習不會在這裡結束：

1. **每天練習**：在實際工作中使用 Copilot CLI
2. **打造自訂工具**：為你的需求建立 Agent 與 Skill
3. **分享知識**：協助團隊導入這些工作流程
4. **持續關注**：追蹤 GitHub Copilot 新功能

### 資源

- [GitHub Copilot CLI 文件](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)
- [MCP Server Registry](https://github.com/modelcontextprotocol/servers)
- [Community Skills](https://github.com/topics/copilot-skill)

---

**做得好！現在去打造一些令人驚豔的東西吧。**

**[← 回到第 06 章](../06-mcp-servers/README.md)** | **[返回課程首頁 →](../README.md)**
