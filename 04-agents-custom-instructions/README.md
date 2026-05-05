![Chapter 04: Agents and Custom Instructions](images/chapter-header.png)

> **如果你能在一個工具裡同時聘請 Python 程式碼審查員、測試專家和安全審查員，會怎樣？**

在第三章，你已經掌握了基本的工作流程：程式碼審查、重構、除錯、測試產生，以及 git 整合。這些讓你能高效使用 GitHub Copilot CLI。現在，讓我們再進一步。

到目前為止，你都是把 Copilot CLI 當作通用型助手來用。Agent 讓你能賦予它特定角色與內建標準，例如：強制使用型別註記與 PEP 8 的程式碼審查員，或是會撰寫 pytest 測試案例的測試助手。你將看到，同樣的提示詞，交給有針對性指令的 agent 處理，結果會明顯更好。

## 🎯 學習目標

完成本章後，你將能夠：

- 使用內建 agent：Plan（`/plan`）、Code-review（`/review`），並理解自動 agent（Explore、Task）
- 使用 agent 檔案（`.agent.md`）建立專業化 agent
- 讓 agent 處理領域專屬任務
- 透過 `/agent` 與 `--agent` 在 agent 之間切換
- 為專案撰寫自訂指令檔，制定專案標準

> ⏱️ **預估時間**：約 55 分鐘（20 分鐘閱讀 + 35 分鐘實作）

---

## 🧩 真實世界比喻：聘請專家

當你需要修理房子時，你不會只叫一個「萬事通」。你會找專家：

| 問題 | 專家 | 為什麼 |
|------|------|--------|
| 水管漏水 | 水電工 | 熟悉水管規範，擁有專業工具 |
| 重新配線 | 電工 | 了解安全規定，符合法規 |
| 換新屋頂 | 屋頂師傅 | 熟悉材料、在地氣候考量 |

Agent 的運作方式也是如此。與其用一個通用型 AI，不如用專注於特定任務、懂得正確流程的 agent。只要設定一次指令，之後每次需要該專業時就能重複使用：程式碼審查、測試、安全、文件。

<img src="images/hiring-specialists-analogy.png" alt="Hiring Specialists Analogy - Just as you call specialized tradespeople for house repairs, AI agents are specialized for specific tasks like code review, testing, security, and documentation" width="800" />

---

# 使用 Agent

立刻開始使用內建與自訂 agent。

---

## *第一次接觸 Agent？* 從這裡開始！
從沒用過或建立過 agent？這裡有你需要知道的入門重點。

1. **馬上試用一個*內建* agent：**
   ```bash
   copilot
   > /plan Add input validation for book year in the book app
   ```
   這會呼叫 Plan agent，產生逐步實作計畫。

2. **看看我們的自訂 agent 範例：** 定義 agent 指令很簡單，參考我們提供的 [python-reviewer.agent.md](../.github/agents/python-reviewer.agent.md) 檔案即可了解模式。

3. **理解核心概念：** Agent 就像諮詢專家而非通才。「前端 agent」會自動關注無障礙與元件模式，你不用每次都提醒，因為 agent 指令裡已經規定好了。

## 內建 Agent

**你在第三章開發流程已經用過一些內建 agent！**
<br>`/plan` 和 `/review` 其實就是內建 agent。現在你知道底層發生什麼事了。完整清單如下：

| Agent | 如何呼叫 | 功能說明 |
|-------|----------|----------|
| **Plan** | `/plan` 或 `Shift+Tab`（切換模式） | 在撰寫程式前產生逐步實作計畫 |
| **Code-review** | `/review` | 針對已 staged/未 staged 變更給予聚焦且可執行的回饋 |
| **Init** | `/init` | 產生專案設定檔（指令、agent） |
| **Explore** | *自動* | 當你請 Copilot 探索或分析程式碼庫時自動使用 |
| **Task** | *自動* | 執行測試、建置、檢查、安裝相依等指令 |

<br>

**內建 agent 實際運作範例** - 呼叫 Plan、Code-review、Explore 與 Task

```bash
copilot

# 呼叫 Plan agent 產生實作計畫
> /plan Add input validation for book year in the book app

# 呼叫 Code-review agent 審查你的變更
> /review

# Explore 與 Task agent 會在相關情境自動啟用：
> Run the test suite        # 使用 Task agent

> Explore how book data is loaded    # 使用 Explore agent
```

那 Task Agent 呢？它在幕後負責管理、追蹤執行狀態，並以清楚明瞭的格式回報：

| 結果 | 你會看到什麼 |
|------|--------------|
| ✅ **成功** | 簡短摘要（例如：「247 項測試全部通過」、「建置成功」） |
| ❌ **失敗** | 完整輸出（含堆疊追蹤、編譯錯誤、詳細日誌） |

> 📚 **官方文件**：[GitHub Copilot CLI Agents](https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents)

---

# 將 Agent 加入 Copilot CLI

你可以輕鬆定義自己的 agent，納入工作流程！定義一次，隨時指派！

<img src="images/using-agents.png" alt="Four colorful AI robots standing together, each with different tools representing specialized agent capabilities" width="800"/>

## 🗂️ 新增你的 agent

Agent 檔案是副檔名為 `.agent.md` 的 Markdown 檔案。分為兩部分：YAML frontmatter（中繼資料）與 Markdown 指令內容。

> 💡 **不熟 YAML frontmatter？** 它是檔案頂部、被 `---` 包圍的一小段設定。YAML 就是 `key: value` 配對。檔案其餘部分是一般的 markdown。

以下是一個最簡單的 agent 範例：

```markdown
---
name: my-reviewer
description: Code reviewer focused on bugs and security issues
---

# Code Reviewer

You are a code reviewer focused on finding bugs and security issues.

When reviewing code, always check for:
- SQL injection vulnerabilities
- Missing error handling
- Hardcoded secrets
```

> 💡 **必填與選填**：`description` 欄位為必填。其他如 `name`、`tools`、`model` 為選填。

## Agent 檔案放哪裡

| 位置 | 作用範圍 | 適用情境 |
|------|----------|----------|
| `.github/agents/` | 專案專屬 | 團隊共用、符合專案慣例的 agent |
| `~/.copilot/agents/` | 全域（所有專案） | 你個人常用的 agent |

**本專案已在 [.github/agents/](../.github/agents/) 資料夾內附上範例 agent 檔案**。你可以自行撰寫，也能直接修改現有範例。

<details>
<summary>📂 查看本課程的範例 agent</summary>

| 檔案 | 說明 |
|------|------|
| `hello-world.agent.md` | 最簡範例 - 從這裡開始 |
| `python-reviewer.agent.md` | Python 程式碼品質審查員 |
| `pytest-helper.agent.md` | Pytest 測試專家 |

```bash
# 或複製到你的個人 agent 資料夾（所有專案都能用）
cp .github/agents/python-reviewer.agent.md ~/.copilot/agents/
```

更多社群 agent，參見 [github/awesome-copilot](https://github.com/github/awesome-copilot)

</details>

## 🚀 使用自訂 agent 的兩種方式

### 互動模式
在互動模式下，使用 `/agent` 列出 agent 並選擇要開始工作的 agent。
選擇一個 agent 繼續你的對話。

```bash
copilot
> /agent
```

要切換到其他 agent，或回到預設模式，再次使用 `/agent` 指令。

### 程式化模式

直接用 agent 啟動新對話。

```bash
copilot --agent python-reviewer
> Review @samples/book-app-project/books.py
```

> 💡 **切換 agent**：隨時可用 `/agent` 或 `--agent` 切換其他 agent。要回到標準 Copilot CLI 體驗，執行 `/agent` 並選擇**無 agent**。

---

# 更深入運用 Agent

<img src="images/creating-custom-agents.png" alt="Robot being assembled on a workbench surrounded by components and tools representing custom agent creation" width="800"/>

> 💡 **本節為選讀。** 內建 agent（`/plan`、`/review`）已足以應付大多數工作流程。當你需要跨專案一致套用專業知識時，再建立自訂 agent。

下列主題各自獨立。**挑你有興趣的看，不必一次讀完。**

| 我想要... | 跳到 |
|---|---|
| 看看 agent 為何比通用提示詞強 | [專家 vs 通用](#specialist-vs-generic-see-the-difference) |
| 多 agent 協作 | [多 agent 協作](#working-with-multiple-agents) |
| 組織、命名與分享 agent | [組織與分享 agent](#organizing--sharing-agents) |
| 設定專案全時啟用情境 | [專案設定](#configuring-your-project-for-copilot) |
| 查詢 YAML 屬性與工具 | [Agent 檔案參考](#agent-file-reference) |

選擇下方情境展開細節。

---

<a id="specialist-vs-generic-see-the-difference"></a>
<details>
<summary><strong>專家 vs 通用：看見差異</strong> - 為什麼 agent 產生的結果比通用提示詞更好</summary>

## 專家 vs 通用：看見差異

這正是 agent 展現價值的地方。來看看差別：

### 沒有 agent（通用 Copilot）

```bash
copilot

> Add a function to search books by year range in the book app
```

**通用輸出**：
```python
def search_by_year_range(books, start_year, end_year):
    results = []
    for book in books:
        if book['year'] >= start_year and book['year'] <= end_year:
            results.append(book)
    return results
```

很基本，可以用，但缺少很多細節。

---

### 使用 Python Reviewer Agent

```bash
copilot

> /agent
# 選擇 "python-reviewer"

> Add a function to search books by year range in the book app
```

**專家輸出**：
```python
from typing import List, Dict, Any

def search_by_year_range(
    books: List[Dict[str, Any]],
    start_year: int,
    end_year: int
) -> List[Dict[str, Any]]:
    """
    Search for books within a specified year range.

    Args:
        books: List of book dictionaries
        start_year: Starting year (inclusive)
        end_year: Ending year (inclusive)

    Returns:
        List of books published within the year range

    Raises:
        ValueError: If start_year is greater than end_year
        TypeError: If year values are not integers
    """
    if not isinstance(start_year, int) or not isinstance(end_year, int):
        raise TypeError("Year values must be integers")

    if start_year > end_year:
        raise ValueError(f"Start year ({start_year}) cannot be greater than end year ({end_year})")

    return [
        book for book in books
        if isinstance(book.get('year'), int)
        and start_year <= book['year'] <= end_year
    ]
```

**python-reviewer agent 自動包含：**
- ✅ 所有參數與回傳值的型別註記
- ✅ 詳盡 docstring（含 Args/Returns/Raises）
- ✅ 輸入驗證與正確錯誤處理
- ✅ 使用串列生成式提升效能
- ✅ 邊界情境處理（缺漏/無效年份）
- ✅ PEP 8 格式規範
- ✅ 防禦式程式設計

**差異**：同樣的提示，結果卻大不同。agent 自帶你可能忘記要求的專業細節。

</details>

---

<a id="working-with-multiple-agents"></a>
<details>
<summary><strong>多 agent 協作</strong> - 專家協同、對話中切換、agent 作為工具</summary>

## 多 agent 協作

真正的威力在於多位專家協同處理一個功能。

### 範例：打造一個簡單功能

```bash
copilot

> I want to add a "search by year range" feature to the book app

# 用 python-reviewer 做設計
> /agent
# 選擇 "python-reviewer"

> @samples/book-app-project/books.py Design a find_by_year_range method. What's the best approach?

# 換 pytest-helper 設計測試
> /agent
# 選擇 "pytest-helper"

> @samples/book-app-project/tests/test_books.py Design test cases for a find_by_year_range method.
> What edge cases should we cover?

# 綜合設計
> Create an implementation plan that includes the method implementation and comprehensive tests.
```

**重點**：你是總設計師，指揮專家處理細節，你專注於全局。

<details>
<summary>🎬 實際操作影片！</summary>

![Python Reviewer Demo](images/python-reviewer-demo.gif)

*實際輸出會因模型、工具、回應而異。*

</details>

### Agent 作為工具

當 agent 已設定好，Copilot 也能在複雜任務中自動呼叫它們。例如你要求全端功能時，Copilot 可能自動把部分任務分派給合適的專家 agent。

</details>

---

<a id="organizing--sharing-agents"></a>
<details>
<summary><strong>組織與分享 agent</strong> - 命名、檔案放置、指令檔與團隊共用</summary>

## 組織與分享 agent

### 命名你的 agent

建立 agent 檔案時，名稱很重要。這是你在 `/agent` 或 `--agent` 後要輸入的，也是團隊成員在 agent 清單中會看到的。

| ✅ 好名稱 | ❌ 避免 |
|----------|--------|
| `frontend` | `my-agent` |
| `backend-api` | `agent1` |
| `security-reviewer` | `helper` |
| `react-specialist` | `code` |
| `python-backend` | `assistant` |

**命名慣例：**
- 用小寫加連字號：`my-agent-name.agent.md`
- 包含領域：`frontend`、`backend`、`devops`、`security`
- 需要時更具體：`react-typescript` 比單純 `frontend` 更明確

---

### 與團隊分享

將 agent 檔案放在 `.github/agents/`，即可納入版本控制。推送到 repo，所有團隊成員自動取得。但 agent 只是 Copilot 會讀取的其中一種檔案。它也支援**指令檔**，這類檔案會自動套用到每次對話，無需手動 `/agent`。

換個角度想：agent 是你隨選的專家，指令檔則是團隊規則，永遠生效。

### 檔案放哪裡

你已知道兩個主要位置（見上方 [Agent 檔案放哪裡](#where-to-put-agent-files)）。用這張決策樹選擇：

<img src="images/agent-file-placement-decision-tree.png" alt="Decision tree for where to put agent files: experimenting → current folder, team use → .github/agents/, everywhere → ~/.copilot/agents/" width="800"/>

**從簡單開始：** 先在專案資料夾建立一個 `*.agent.md`。滿意後再移到正式位置。

除了 agent 檔案，Copilot 也會自動讀取**專案層級指令檔**，無需 `/agent`。詳見下方 [專案設定](#configuring-your-project-for-copilot) 介紹 `AGENTS.md`、`.instructions.md` 與 `/init`。

</details>

---

<a id="configuring-your-project-for-copilot"></a>
<details>
<summary><strong>專案設定</strong> - AGENTS.md、指令檔與 /init 設定</summary>

## 專案設定

Agent 是你隨選的專家。**專案設定檔**則不同：Copilot 會在每次對話自動讀取，了解你的專案慣例、技術棧與規則。無需手動 `/agent`，所有協作者都會自動套用情境。

### 用 /init 快速設定

最快的方式是讓 Copilot 幫你產生設定檔：

```bash
copilot
> /init
```

Copilot 會掃描專案，自動建立專屬指令檔。你可以再自行編輯。

### 指令檔格式

| 檔案 | 作用範圍 | 備註 |
|------|----------|------|
| `AGENTS.md` | 專案根目錄或子目錄 | **跨平台標準** - Copilot 與其他 AI 助手皆支援 |
| `.github/copilot-instructions.md` | 專案 | GitHub Copilot 專用 |
| `.github/instructions/*.instructions.md` | 專案 | 更細分、主題式指令 |
| `CLAUDE.md`, `GEMINI.md` | 專案根目錄 | 為相容性而設 |

> 🎯 **剛開始？** 用 `AGENTS.md` 撰寫專案指令。其他格式可視需求再探索。

### AGENTS.md

`AGENTS.md` 是推薦格式。它是[開放標準](https://agents.md/)，可跨 Copilot 與其他 AI 工具通用。放在 repo 根目錄，Copilot 會自動讀取。本專案的 [AGENTS.md](../AGENTS.md) 就是範例。

一般的 `AGENTS.md` 會描述專案情境、程式風格、安全需求、測試標準。可依我們的範例檔案撰寫。

### 自訂指令檔（.instructions.md）

想要更細緻控管，可將指令拆成主題式檔案。每個檔案聚焦一個面向，自動生效：

```
.github/
└── instructions/
    ├── python-standards.instructions.md
    ├── security-checklist.instructions.md
    └── api-design.instructions.md
```

> 💡 **注意**：指令檔支援所有語言。這裡用 Python 配合課程專案，你也能為 TypeScript、Go、Rust 等技術建立類似檔案。

**尋找社群指令檔**：可在 [github/awesome-copilot](https://github.com/github/awesome-copilot) 找到 .NET、Angular、Azure、Python、Docker 等多種現成指令檔。

### 關閉自訂指令

若需讓 Copilot 忽略所有專案設定（例如除錯或比較行為）：

```bash
copilot --no-custom-instructions
```

</details>

---

<a id="agent-file-reference"></a>
<details>
<summary><strong>Agent 檔案參考</strong> - YAML 屬性、工具別名與完整範例</summary>

## Agent 檔案參考

### 更完整的範例

你已看過[最簡 agent 格式](#-add-your-agents)。這裡是一個用到 `tools` 屬性的完整 agent。建立 `~/.copilot/agents/python-reviewer.agent.md`：

```markdown
---
name: python-reviewer
description: Python code quality specialist for reviewing Python projects
tools: ["read", "edit", "search", "execute"]
---

# Python Code Reviewer

You are a Python specialist focused on code quality and best practices.

**Your focus areas:**
- Code quality (PEP 8, type hints, docstrings)
- Performance optimization (list comprehensions, generators)
- Error handling (proper exception handling)
- Maintainability (DRY principles, clear naming)

**Code style requirements:**
- Use Python 3.10+ features (dataclasses, type hints, pattern matching)
- Follow PEP 8 naming conventions
- Use context managers for file I/O
- All functions must have type hints and docstrings

**When reviewing code, always check:**
- Missing type hints on function signatures
- Mutable default arguments
- Proper error handling (no bare except)
- Input validation completeness
```

### YAML 屬性

| 屬性 | 必填 | 說明 |
|------|------|------|
| `name` | 否 | 顯示名稱（預設為檔名） |
| `description` | **是** | agent 功能說明 - 幫助 Copilot 判斷何時建議使用 |
| `tools` | 否 | 允許使用的工具清單（省略 = 全部可用）。見下方工具別名。 |
| `target` | 否 | 限定僅於 `vscode` 或 `github-copilot` 使用 |

### 工具別名

在 `tools` 清單中可用這些名稱：
- `read` - 讀取檔案內容
- `edit` - 編輯檔案
- `search` - 搜尋檔案（grep/glob）
- `execute` - 執行 shell 指令（也可用：`shell`、`Bash`）
- `agent` - 呼叫其他自訂 agent

> 📖 **官方文件**：[自訂 agent 設定](https://docs.github.com/copilot/reference/custom-agents-configuration)
>
> ⚠️ **僅 VS Code 支援**：`model` 屬性（選擇 AI 模型）僅於 VS Code 有效，GitHub Copilot CLI 不支援。你可放心加入以便跨平台，Copilot CLI 會自動忽略。

### 更多 agent 範本

> 💡 **新手注意**：以下僅為範本。**請依專案實際技術替換內容。** 重要的是 agent 的*結構*，不是技術細節。

本專案在 [.github/agents/](../.github/agents/) 夾內有實作範例：
- [hello-world.agent.md](../.github/agents/hello-world.agent.md) - 最簡範例，建議先看
- [python-reviewer.agent.md](../.github/agents/python-reviewer.agent.md) - Python 程式碼品質審查員
- [pytest-helper.agent.md](../.github/agents/pytest-helper.agent.md) - Pytest 測試專家

更多社群 agent，參見 [github/awesome-copilot](https://github.com/github/awesome-copilot)。

</details>

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

自己建立 agent 並實際操作看看。

---

## ▶️ 自己動手試試

```bash

# 建立 agents 資料夾（若尚未存在）
mkdir -p .github/agents

# 建立一個程式碼審查 agent
cat > .github/agents/reviewer.agent.md << 'EOF'
---
name: reviewer
description: Senior code reviewer focused on security and best practices
---

# Code Reviewer Agent

You are a senior code reviewer focused on code quality.

**Review priorities:**
1. Security vulnerabilities
2. Performance issues
3. Maintainability concerns
4. Best practice violations

**Output format:**
Provide issues as a numbered list with severity tags:
[CRITICAL], [HIGH], [MEDIUM], [LOW]
EOF

# 建立一個文件撰寫 agent
cat > .github/agents/documentor.agent.md << 'EOF'
---
name: documentor
description: Technical writer for clear and complete documentation
---

# Documentation Agent

You are a technical writer who creates clear documentation.

**Documentation standards:**
- Start with a one-sentence summary
- Include usage examples
- Document parameters and return values
- Note any gotchas or limitations
EOF

# 現在來使用它們
copilot --agent reviewer
> Review @samples/book-app-project/books.py

# 或切換 agent
copilot
> /agent
# 選擇 "documentor"
> Document @samples/book-app-project/books.py
```

---

## 📝 作業

### 主要挑戰：打造專業 agent 團隊

上方實作範例建立了 `reviewer` 與 `documentor` agent。現在請練習建立並使用不同任務的 agent，提升書籍應用程式的資料驗證：

1. 建立 3 個針對書籍應用程式的 agent 檔案（`.agent.md`），每個 agent 一個檔案，放在 `.github/agents/`
2. 你的 agent：
   - **data-validator**：檢查 `data.json` 是否有缺漏或格式錯誤（作者為空、year=0、缺欄位）
   - **error-handler**：審查 Python 程式碼的錯誤處理一致性，並建議統一做法
   - **doc-writer**：產生或更新 docstring 與 README 內容
3. 對書籍應用程式使用每個 agent：
   - `data-validator` → 稽核 `@samples/book-app-project/data.json`
   - `error-handler` → 審查 `@samples/book-app-project/books.py` 與 `@samples/book-app-project/utils.py`
   - `doc-writer` → 為 `@samples/book-app-project/books.py` 補上 docstring
4. 協作流程：先用 `error-handler` 找出錯誤處理缺口，再用 `doc-writer` 記錄改進後的做法

**成功標準**：你有 3 個可用 agent，能產生一致且高品質的結果，並可用 `/agent` 在它們之間切換。

<details>
<summary>💡 提示（點擊展開）</summary>

**起手範本**：每個 agent 建一個檔案於 `.github/agents/`：

`data-validator.agent.md`:
```markdown
---
description: Analyzes JSON data files for missing or malformed entries
---

You analyze JSON data files for missing or malformed entries.

**Focus areas:**
- Empty or missing author fields
- Invalid years (year=0, future years, negative years)
- Missing required fields (title, author, year, read)
- Duplicate entries
```

`error-handler.agent.md`:
```markdown
---
description: Reviews Python code for error handling consistency
---

You review Python code for error handling consistency.

**標準：**
- 不可使用裸露的 except 子句
- 適當時請使用自訂例外
- 所有檔案操作皆使用 context manager
- 成功／失敗時回傳型別需一致
```

`doc-writer.agent.md`:
```markdown
---
description: 技術寫手，撰寫清晰的 Python 文件
---

你是一位技術寫手，負責撰寫清晰的 Python 文件。

**標準：**
- 採用 Google 風格的 docstring
- 包含參數型別與回傳值
- 為公開方法新增使用範例
- 註明會拋出的例外狀況
```

**測試你的 Agent：**

> 💡 **注意：** 你的本機專案應已包含 `samples/book-app-project/data.json`。若缺少此檔案，請從原始儲存庫下載：
> [data.json](https://github.com/github/copilot-cli-for-beginners/blob/main/samples/book-app-project/data.json)

```bash
copilot
> /agent
# 從清單中選擇 "data-validator"
> @samples/book-app-project/data.json 檢查書籍資料中作者欄位為空或年份無效的項目
```

**提示：** YAML frontmatter 中的 `description` 欄位是 Agent 能正常運作的必要條件。

</details>

### 額外挑戰：指令庫

你已經建立了可隨選呼叫的 Agent。現在來試試另一種方式：**指令檔案**，Copilot 會在每次對話自動讀取，無需 `/agent`。

建立 `.github/instructions/` 資料夾，並新增至少 3 個指令檔案：
- `python-style.instructions.md`：強制遵循 PEP 8 及型別標註慣例
- `test-standards.instructions.md`：強制測試檔案遵循 pytest 慣例
- `data-quality.instructions.md`：驗證 JSON 資料內容品質

在書籍應用程式程式碼上測試每個指令檔案。

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 結果 | 修正方式 |
|------|------|----------|
| Agent frontmatter 缺少 `description` | Agent 無法載入或無法被發現 | 一定要在 YAML frontmatter 加入 `description:` |
| Agent 檔案位置錯誤 | 使用時找不到 Agent | 請放在 `~/.copilot/agents/`（個人）或 `.github/agents/`（專案） |
| 使用 `.md` 而非 `.agent.md` | 檔案可能不會被辨識為 Agent | 檔名需為 `python-reviewer.agent.md` 這種格式 |
| Agent 提示內容過長 | 可能超過 30,000 字元限制 | 保持 Agent 定義精簡，詳細指令請用 Skill 實現 |

### 疑難排解

**找不到 Agent** — 請確認 Agent 檔案存在於下列任一位置：
- `~/.copilot/agents/`
- `.github/agents/`

列出所有可用 Agent：

```bash
copilot
> /agent
# 顯示所有可用的 Agent
```

**Agent 未依指示執行** — 請在提示中明確說明，並於 Agent 定義中加入更多細節：
- 指定框架／函式庫及版本
- 團隊慣例
- 範例程式碼模式

**自訂指令未載入** — 在專案中執行 `/init` 以設定專案專屬指令：

```bash
copilot
> /init
```

或檢查是否有關閉自訂指令：
```bash
# 若希望載入自訂指令，請勿使用 --no-custom-instructions
copilot  # 預設會載入自訂指令
```

</details>

---

# 摘要

## 🔑 重點整理

1. **內建 Agent**：`/plan` 和 `/review` 可直接呼叫；Explore 與 Task 會自動運作
2. **自訂 Agent**：以 `.agent.md` 檔案定義的專家角色
3. **優秀的 Agent** 具備明確專業、標準與輸出格式
4. **多 Agent 協作**：結合多位專家解決複雜問題
5. **指令檔案**（`.instructions.md`）可將團隊標準自動化套用
6. **一致的輸出** 來自明確定義的 Agent 指令

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

Agent 會改變 *Copilot 處理與執行目標行動* 的方式。接下來你將學到 **Skill** —— 它們則改變 Copilot *執行哪些步驟*。想知道 Agent 與 Skill 有何不同？第五章會直接說明。

在 **[第五章：Skills 系統](../05-skills/README.md)**，你將學到：

- Skill 如何根據你的提示自動觸發（不需斜線指令）
- 安裝社群 Skill
- 使用 SKILL.md 檔案建立自訂 Skill
- Agent、Skill 與 MCP 的差異
- 何時該用哪一種

---

**[← 回到第三章](../03-development-workflows/README.md)** | **[繼續前往第五章 →](../05-skills/README.md)**
