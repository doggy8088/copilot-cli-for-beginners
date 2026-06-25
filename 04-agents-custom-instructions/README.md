![Chapter 04: Agents and Custom Instructions](assets/chapter-header.png)

> **如果你能在一個工具裡同時聘請 Python 程式碼審查員、測試專家和安全性審查員，會怎麼樣？**

在第三章中，你已經掌握了基本工作流程：程式碼審查、重構、除錯、測試產生，以及 git 整合。這些讓你能高效運用 GitHub Copilot CLI。現在，讓我們再更進一步。

到目前為止，你一直把 Copilot CLI 當作通用型助手來使用。Agent 讓你能賦予它特定角色與內建標準，例如：強制使用型別註記和 PEP 8 的程式碼審查員，或是會撰寫 pytest 測試案例的測試助手。你將看到，同樣的提示詞，交給有明確指示的 agent 處理，結果會明顯更好。

## 🎯 學習目標

完成本章後，你將能夠：

- 使用內建 agent：Plan（`/plan`）、Code-review（`/review`），並了解自動 agent（Explore、Task）
- 使用 agent 檔案（`.agent.md`）建立專業化 agent
- 讓 agent 處理領域專屬任務
- 透過 `/agent` 與 `--agent` 在 agent 之間切換
- 撰寫專案專屬標準的自訂指示檔案

> ⏱️ **預估時間**：約 55 分鐘（20 分鐘閱讀 + 35 分鐘實作）

---

## 🧩 真實世界類比：聘請專家

當你需要修理房子時，你不會只叫一個「通用幫手」。你會找專家：

| 問題 | 專家 | 原因 |
|---------|------------|-----|
| 水管漏水 | 水電工 | 熟悉水管規範，有專業工具 |
| 電線重拉 | 電工 | 了解安全規定，符合規範 |
| 換新屋頂 | 屋頂師傅 | 了解材料、在地氣候考量 |

Agent 的運作方式也是如此。與其用一個通用 AI，不如用專注於特定任務、知道正確流程的 agent。只要設定一次指示，之後需要那個專業時就能重複使用：程式碼審查、測試、安全、文件。

<img src="assets/hiring-specialists-analogy.png" alt="Hiring Specialists Analogy - Just as you call specialized tradespeople for house repairs, AI agents are specialized for specific tasks like code review, testing, security, and documentation" width="800" />

---

# 使用 Agent

立即開始使用內建與自訂 agent。

---

## *第一次接觸 Agent？* 從這裡開始！
從沒用過或建立過 agent？這裡有你入門本課程所需的一切。

1. **立刻試用一個*內建* agent：**
   ```bash
   copilot
   > /plan Add input validation for book year in the book app
   ```
   這會呼叫 Plan agent，產生逐步實作計畫。

2. **看看我們的自訂 agent 範例：** 定義 agent 指示很簡單，參考我們提供的 [python-reviewer.agent.md](../.github/agents/python-reviewer.agent.md) 檔案即可了解模式。

3. **理解核心概念：** Agent 就像是找專家諮詢，而不是問通才。「前端 agent」會自動專注於無障礙與元件設計，你不用每次都提醒它，因為這些已經寫在 agent 的指示裡了。

## 內建 Agent

**你在第三章開發流程已經用過部分內建 agent！**
<br>`/plan` 和 `/review` 其實就是內建 agent。現在你知道背後發生了什麼。完整清單如下：

| Agent | 如何呼叫 | 功能說明 |
|-------|---------------|--------------|
| **Plan** | `/plan` 或 `Shift+Tab`（切換模式） | 在撰寫程式前產生逐步實作計畫 |
| **Code-review** | `/review` | 審查已暫存/未暫存變更，給予具體可執行的回饋 |
| **Init** | `/init` | 產生專案設定檔（指示、agent） |
| **Explore** | *自動* | 當你請 Copilot 探索或分析程式碼庫時自動使用 |
| **Task** | *自動* | 執行測試、建置、檢查、安裝相依套件等指令 |

<br>

**內建 agent 實際應用** - 呼叫 Plan、Code-review、Explore 與 Task 的範例

```bash
copilot

# 呼叫 Plan agent 產生實作計畫
> /plan Add input validation for book year in the book app

# 呼叫 Code-review agent 審查你的變更
> /review

# Explore 與 Task agent 會在需要時自動呼叫：
> Run the test suite        # 使用 Task agent

> Explore how book data is loaded    # 使用 Explore agent
```

那 Task Agent 呢？它在幕後負責管理、追蹤執行狀況，並以清楚簡潔的格式回報：

| 結果 | 你會看到什麼 |
|---------|--------------|
| ✅ **成功** | 簡短摘要（如「全部 247 項測試通過」、「建置成功」） |
| ❌ **失敗** | 完整輸出（包含堆疊追蹤、編譯錯誤、詳細日誌） |

> 📚 **官方文件**：[GitHub Copilot CLI Agents](https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents)

---

# 將 Agent 加入 Copilot CLI

你可以輕鬆定義自己的 agent，納入你的工作流程！定義一次，隨時指揮！

<img src="assets/using-agents.png" alt="Four colorful AI robots standing together, each with different tools representing specialized agent capabilities" width="800"/>

## 🗂️ 新增你的 agent

Agent 檔案是副檔名為 `.agent.md` 的 markdown 檔案。分為兩部分：YAML frontmatter（中繼資料）與 markdown 指示內容。

> 💡 **第一次接觸 YAML frontmatter？** 它是檔案最上方、被 `---` 包圍的一小段設定。YAML 就是 `key: value` 配對。其餘內容就是一般 markdown。

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

> 💡 **必填與選填**：`description` 欄位為必填。其他如 `name`、`tools`、`model` 則為選填。

## Agent 檔案放哪裡

| 位置 | 作用範圍 | 適用情境 |
|----------|-------|----------|
| `.github/agents/` | 專案專屬 | 適合團隊共用、專案慣例的 agent |
| `~/.copilot/agents/` | 全域（所有專案） | 你個人常用、每個專案都想用的 agent |

**本專案已在 [.github/agents/](../.github/agents/) 資料夾內附上範例 agent 檔案**。你可以自行撰寫，也能直接改用現有的。

<details>
<summary>📂 查看本課程的範例 agent</summary>

| 檔案 | 說明 |
|------|-------------|
| `hello-world.agent.md` | 最簡範例，從這裡開始 |
| `python-reviewer.agent.md` | Python 程式碼品質審查員 |
| `pytest-helper.agent.md` | Pytest 測試專家 |

```bash
# 或複製一份到你的個人 agent 資料夾（所有專案都能用）
cp .github/agents/python-reviewer.agent.md ~/.copilot/agents/
```

更多社群 agent，請見 [github/awesome-copilot](https://github.com/github/awesome-copilot)

</details>

## 🚀 使用自訂 agent 的兩種方式

### 互動模式
在互動模式下，使用 `/agent` 列出 agent 並選擇要開始合作的 agent。
選擇一個 agent 後即可繼續對話。

```bash
copilot
> /agent
```

若要切換其他 agent，或回到預設模式，再次使用 `/agent` 指令即可。

### 程式化模式

直接用 agent 啟動新會話。

```bash
copilot --agent python-reviewer
> Review @samples/book-app-project/books.py
```

> 💡 **切換 agent**：你隨時都能用 `/agent` 或 `--agent` 切換到其他 agent。若要回到標準 Copilot CLI 體驗，使用 `/agent` 並選擇**無 agent**。

> 💡 **Agent 模式僅限當前會話**：你選擇的 agent 只會套用在目前這個會話。當你用 `/new`、`/clear` 或開新終端機時，Copilot 會回到預設模式——agent 選擇不會自動延續。這代表每次會話都是全新開始，有助於保持專注。

---

# 更深入運用 Agent

<img src="assets/creating-custom-agents.png" alt="Robot being assembled on a workbench surrounded by components and tools representing custom agent creation" width="800"/>

> 💡 **本節為進階選讀。** 內建 agent（`/plan`、`/review`）已足夠應付多數工作流程。當你需要跨專案一致應用的專業知識時，再來建立自訂 agent。

以下主題各自獨立。**挑你有興趣的看，不必一次讀完。**

| 我想要... | 跳到 |
|---|---|
| 看看 agent 為何比通用提示更強 | [專家 vs 通用](#specialist-vs-generic-see-the-difference) |
| 多 agent 協作 | [多 agent 協作](#working-with-multiple-agents) |
| 組織、命名與分享 agent | [組織與分享 agent](#organizing--sharing-agents) |
| 設定專案全時情境 | [設定 Copilot 專案環境](#configuring-your-project-for-copilot) |
| 查詢 YAML 屬性與工具 | [Agent 檔案參考](#agent-file-reference) |

選擇下方情境展開細節。

---

<a id="specialist-vs-generic-see-the-difference"></a>
<details>
<summary><strong>專家 vs 通用：看見差異</strong> - 為什麼 agent 產生的結果比通用提示更好</summary>

## 專家 vs 通用：看見差異

這正是 agent 價值所在。來看看差別：

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

**python-reviewer agent 自動包含的內容**：
- ✅ 所有參數與回傳值皆有型別註記
- ✅ 詳盡 docstring，包含 Args/Returns/Raises
- ✅ 輸入驗證與正確的錯誤處理
- ✅ 使用串列生成式提升效能
- ✅ 處理邊界情境（缺少/無效年份）
- ✅ PEP 8 格式
- ✅ 防禦式程式設計

**差異**：同一個提示，結果卻大不相同。agent 自帶你可能忘記要求的專業。

</details>

---

<a id="working-with-multiple-agents"></a>
<details>
<summary><strong>多 agent 協作</strong> - 專家組合、會話中切換、agent 當工具</summary>

## 多 agent 協作

真正的威力來自多位專家協作同一功能。

### 範例：打造一個簡單功能

```bash
copilot

> I want to add a "search by year range" feature to the book app

# 用 python-reviewer 設計
> /agent
# 選擇 "python-reviewer"

> @samples/book-app-project/books.py Design a find_by_year_range method. What's the best approach?

# 換 pytest-helper 設計測試
> /agent
# 選擇 "pytest-helper"

> @samples/book-app-project/tests/test_books.py Design test cases for a find_by_year_range method.
> What edge cases should we cover?

# 綜合兩者設計
> Create an implementation plan that includes the method implementation and comprehensive tests.
```

**關鍵觀念**：你是總設計師，指揮專家。他們處理細節，你掌握全局。

<details>
<summary>🎬 實際操作影片！</summary>

![Python Reviewer Demo](assets/python-reviewer-demo.gif)

*實際輸出會依模型、工具、回應而異，與此處展示內容不同屬正常現象。*

</details>

### Agent 當工具

當 agent 設定妥當，Copilot 也能在複雜任務中自動呼叫它們作為工具。如果你要求一個全端功能，Copilot 可能會自動分派部分工作給合適的專家 agent。

</details>

---

<a id="organizing--sharing-agents"></a>
<details>
<summary><strong>組織與分享 agent</strong> - 命名、檔案放置、指示檔案與團隊共用</summary>

## 組織與分享 agent

### 命名你的 agent

建立 agent 檔案時，命名很重要。這會是你在 `/agent` 或 `--agent` 後輸入的名稱，也是團隊成員在 agent 清單中看到的。

| ✅ 好名稱 | ❌ 避免 |
|--------------|----------|
| `frontend` | `my-agent` |
| `backend-api` | `agent1` |
| `security-reviewer` | `helper` |
| `react-specialist` | `code` |
| `python-backend` | `assistant` |

**命名慣例：**
- 使用小寫加連字號：`my-agent-name.agent.md`
- 包含領域：`frontend`、`backend`、`devops`、`security`
- 需要時具體：`react-typescript` 比單純 `frontend` 更明確

---

### 與團隊分享

將 agent 檔案放在 `.github/agents/`，就會納入版本控制。推送到你的 repo，所有團隊成員都能自動取得。但 agent 只是 Copilot 會讀取的其中一種檔案。它也支援**指示檔案**，這類檔案會自動套用到每個會話，無需手動執行 `/agent`。

換個角度想：agent 是你隨選的專家，指示檔案則是團隊規則，永遠生效。

### 檔案放哪裡

你已經知道兩個主要位置（見上方 [Agent 檔案放哪裡](#where-to-put-agent-files)）。用這個決策樹判斷：

<img src="assets/agent-file-placement-decision-tree.png" alt="Decision tree for where to put agent files: experimenting → current folder, team use → .github/agents/, everywhere → ~/.copilot/agents/" width="800"/>

**從簡單開始：** 先在專案資料夾建立一個 `*.agent.md` 檔案。滿意後再移到正式位置。

除了 agent 檔案，Copilot 也會自動讀取**專案層級指示檔案**，無需 `/agent`。詳見下方 [設定 Copilot 專案環境](#configuring-your-project-for-copilot) 章節，介紹 `AGENTS.md`、`.instructions.md` 與 `/init`。

</details>

---

<a id="configuring-your-project-for-copilot"></a>
<details>
<summary><strong>設定 Copilot 專案環境</strong> - AGENTS.md、指示檔案與 /init 設定</summary>

## 設定 Copilot 專案環境

Agent 是你隨選的專家。**專案設定檔**則不同：Copilot 每次會話都會自動讀取，了解你的專案慣例、技術棧與規則。沒有人需要執行 `/agent`，情境對所有協作者都自動生效。

### 用 /init 快速設定

最快的方式是讓 Copilot 幫你產生設定檔：

```bash
copilot
> /init
```

Copilot 會掃描你的專案，自動建立合適的指示檔。你可以事後編輯。

### 指示檔案格式

| 檔案 | 作用範圍 | 備註 |
|------|-------|-------|
| `AGENTS.md` | 專案根目錄或子資料夾 | **跨平台標準**——Copilot 與其他 AI 助手皆支援 |
| `.github/copilot-instructions.md` | 專案 | GitHub Copilot 專用 |
| `.github/instructions/*.instructions.md` | 專案 | 更細分、主題專屬指示 |
| `~/.copilot/instructions/**/*.instructions.md` | 使用者（所有專案） | 你的個人指示，所有 repo 都適用 |
| `CLAUDE.md`, `GEMINI.md` | 專案根目錄 | 為相容性而支援 |

> 🎯 **剛開始？** 用 `AGENTS.md` 寫專案指示即可。其他格式可視需求再探索。

### AGENTS.md

`AGENTS.md` 是推薦格式。它是[開放標準](https://agents.md/)，Copilot 與其他 AI 程式工具都支援。放在 repo 根目錄，Copilot 會自動讀取。本專案的 [AGENTS.md](../AGENTS.md) 就是範例。

一般的 `AGENTS.md` 會描述你的專案情境、程式風格、安全需求與測試標準。可依我們的範例檔案自行撰寫。

### 自訂指示檔案（.instructions.md）

想更細緻控管時，可將指示拆成主題專屬檔案。每個檔案只涵蓋一個重點，且自動生效：

```
.github/
└── instructions/
    ├── python-standards.instructions.md
    ├── security-checklist.instructions.md
    └── api-design.instructions.md
```

> 💡 **注意**：指示檔案支援任何語言。此例用 Python 配合課程專案，你也能為 TypeScript、Go、Rust 或任何技術建立類似檔案。

#### 用 `applyTo` 限定指示範圍

預設情況下，指示檔案會套用到每個會話。若只想限定特定檔案型別，可在 YAML frontmatter（最上方 `---` 區塊）加上 `applyTo` 欄位：

```markdown
---
applyTo: "**/*.py"
---
# Python Standards
Always follow PEP 8 style conventions.
Use type hints in all function signatures.
```

有了 `applyTo: "**/*.py"`，Copilot 只會在你處理 Python 檔案時載入這份指示。Python 風格指示不會干擾 Dockerfile 或 SQL 查詢的討論。

常見模式如下：

| `applyTo` 值 | 何時生效 |
|---|---|
| `"**/*.py"` | 任何 Python 檔案 |
| `"**/*.{ts,tsx}"` | TypeScript 與 TSX 檔案 |
| `"tests/**"` | `tests/` 資料夾內所有檔案 |
| （無 frontmatter） | 每個會話——預設 |

> 💡 **小技巧**：用引號包住萬用字元模式（如 `"**/*.py"`），可確保在所有作業系統與 shell 下正確解析。

**尋找社群指示檔案**：瀏覽 [github/awesome-copilot](https://github.com/github/awesome-copilot) 可找到 .NET、Angular、Azure、Python、Docker 等多種技術的現成指示檔。

### 關閉自訂指示

若需讓 Copilot 忽略所有專案設定（例如除錯或比較行為時）：

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

你已看過[最小 agent 格式](#-add-your-agents)。以下是一個更完整、使用 `tools` 屬性的 agent。建立 `~/.copilot/agents/python-reviewer.agent.md`：

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
|----------|----------|-------------|
| `name` | 否 | 顯示名稱（預設為檔名） |
| `description` | **是** | agent 功能說明——協助 Copilot 判斷何時建議使用 |
| `tools` | 否 | 可用工具清單（省略＝全部可用）。見下方工具別名。 |
| `target` | 否 | 僅限 `vscode` 或 `github-copilot` |

### 工具別名

在 `tools` 清單中可用這些名稱：
- `read` - 讀取檔案內容
- `edit` - 編輯檔案
- `search` - 搜尋檔案（grep/glob）
- `execute` - 執行 shell 指令（亦可用：`shell`、`Bash`）
- `agent` - 呼叫其他自訂 agent

> 📖 **官方文件**：[自訂 agent 設定](https://docs.github.com/copilot/reference/custom-agents-configuration)
>
> ⚠️ **僅 VS Code 支援**：`model` 屬性（選擇 AI 模型）僅於 VS Code 有效，GitHub Copilot CLI 不支援。為跨平台 agent 檔案可放心加上，Copilot CLI 會自動忽略。

### 更多 agent 範本

> 💡 **新手注意**：下方範例為模板。**請依你專案實際技術調整內容。** 重要的是 agent 的*結構*，不是範例中的技術。

本專案於 [.github/agents/](../.github/agents/) 目錄內有實用範例：
- [hello-world.agent.md](../.github/agents/hello-world.agent.md) - 最簡範例，建議先看
- [python-reviewer.agent.md](../.github/agents/python-reviewer.agent.md) - Python 程式碼品質審查員
- [pytest-helper.agent.md](../.github/agents/pytest-helper.agent.md) - Pytest 測試專家

更多社群 agent，請見 [github/awesome-copilot](https://github.com/github/awesome-copilot)。

</details>

---

# 練習

<img src="../assets/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

建立你自己的 agent，實際體驗它們的威力。

---

## ▶️ 自己動手試試

```bash

# 建立 agents 目錄（若尚未存在）
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

實作範例中建立了 `reviewer` 和 `documentor` 代理人。現在請練習為不同任務建立並使用代理人——提升書籍應用程式的資料驗證：

1. 建立 3 個專為書籍應用程式設計的代理人檔案（`.agent.md`），每個代理人一個檔案，放在 `.github/agents/` 目錄下
2. 你的代理人：
   - **data-validator**：檢查 `data.json` 是否有遺漏或格式錯誤的資料（作者為空、年份=0、欄位遺漏）
   - **error-handler**：檢查 Python 程式碼的錯誤處理是否一致，並建議統一的做法
   - **doc-writer**：產生或更新 docstring 與 README 內容
3. 在書籍應用程式中使用每個代理人：
   - `data-validator` → 稽核 `@samples/book-app-project/data.json`
   - `error-handler` → 檢查 `@samples/book-app-project/books.py` 和 `@samples/book-app-project/utils.py`
   - `doc-writer` → 為 `@samples/book-app-project/books.py` 新增 docstring
4. 協作：先用 `error-handler` 找出錯誤處理的缺口，再用 `doc-writer` 記錄改進後的做法

**成功標準**：你擁有 3 個可運作的代理人，能產生一致且高品質的輸出，並能透過 `/agent` 在它們之間切換。

<details>
<summary>💡 提示（點擊展開）</summary>

**起始範本**：在 `.github/agents/` 目錄下，每個代理人建立一個檔案：

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

**Standards:**
- No bare except clauses
- Use custom exceptions where appropriate
- All file operations use context managers
- Consistent return types for success/failure
```

`doc-writer.agent.md`:
```markdown
---
description: Technical writer for clear Python documentation
---

You are a technical writer who creates clear Python documentation.

**Standards:**
- Google-style docstrings
- Include parameter types and return values
- Add usage examples for public methods
- Note any exceptions raised
```

**測試你的代理人：**

> 💡 **注意：** 你應該已經在本地複本的這個儲存庫中有 `samples/book-app-project/data.json`。如果缺少，請從原始儲存庫下載原始版本：
> [data.json](https://github.com/github/copilot-cli-for-beginners/blob/main/samples/book-app-project/data.json)

```bash
copilot
> /agent
# 從清單中選擇 "data-validator"
> @samples/book-app-project/data.json 檢查作者欄位為空或年份無效的書籍
```

**提示：** YAML frontmatter 中的 `description` 欄位是代理人運作所必需的。

</details>

### 加分挑戰：指令庫

你已經建立了可隨選啟用的代理人。現在來試試另一種方式：**指令檔案**，讓 Copilot 在每次會話中自動讀取，無需 `/agent`。

建立 `.github/instructions/` 資料夾，並新增至少 3 個指令檔案：
- `python-style.instructions.md`：強制執行 PEP 8 與型別提示慣例
- `test-standards.instructions.md`：強制測試檔案遵循 pytest 慣例
- `data-quality.instructions.md`：驗證 JSON 資料項目的品質

在書籍應用程式程式碼上測試每個指令檔案。

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生情況 | 修正方式 |
|------|----------|----------|
| 代理人 frontmatter 缺少 `description` | 代理人無法載入或無法被發現 | 一定要在 YAML frontmatter 中加入 `description:` |
| 代理人檔案位置錯誤 | 嘗試使用時找不到代理人 | 放在 `~/.copilot/agents/`（個人）或 `.github/agents/`（專案） |
| 使用 `.md` 而非 `.agent.md` | 檔案可能不會被辨識為代理人 | 檔名應為 `python-reviewer.agent.md` 這類格式 |
| 代理人提示過長 | 可能超過 30,000 字元限制 | 讓代理人定義聚焦，詳細指令可用 skill 實現 |

### 疑難排解

**找不到代理人** - 請確認代理人檔案存在於下列其中一個位置：
- `~/.copilot/agents/`
- `.github/agents/`

列出所有可用代理人：

```bash
copilot
> /agent
# 顯示所有可用代理人
```

**代理人未遵循指令** - 在提示中明確說明需求，並在代理人定義中加入更多細節：
- 指定框架／函式庫及版本
- 團隊慣例
- 範例程式碼模式

**自訂指令未載入** - 在專案中執行 `/init` 以設定專案專屬指令：

```bash
copilot
> /init
```

或檢查是否被停用：
```bash
# 若要載入自訂指令，請勿使用 --no-custom-instructions
copilot  # 預設會載入自訂指令
```

</details>

---

# 摘要

## 🔑 重點整理

1. **內建代理人**：`/plan` 和 `/review` 可直接呼叫；Explore 與 Task 會自動運作
2. **自訂代理人**：以 `.agent.md` 檔案定義專家角色
3. **優秀代理人**：具備明確專業、標準與輸出格式
4. **多代理人協作**：結合專業解決複雜問題
5. **指令檔案**（`.instructions.md`）：將團隊標準自動化
6. **一致輸出**：來自明確定義的代理人指令

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

代理人會改變 *Copilot 處理與執行目標動作* 的方式。接下來你將學習 **技能**——它們則改變 *Copilot 採取哪些步驟*。想知道代理人與技能有何不同？第五章會直接說明。

在 **[第五章：技能系統](../05-skills/README.md)**，你將學到：

- 技能如何根據你的提示自動觸發（不需斜線指令）
- 安裝社群技能
- 用 SKILL.md 檔案建立自訂技能
- 代理人、技能與 MCP 的差異
- 何時該用哪一種

---

**[← 回到第三章](../03-development-workflows/README.md)** | **[繼續前往第五章 →](../05-skills/README.md)**
