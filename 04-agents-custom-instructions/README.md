![Chapter 04: Agents and Custom Instructions](assets/chapter-header.png)

> **如果你能在一個工具裡同時聘請 Python 程式碼審查員、測試專家和安全審查員會怎樣？**

在第三章中，你已經精通了基本工作流程：程式碼審查、重構、除錯、測試產生，以及 git 整合。這些讓你能高效使用 GitHub Copilot CLI。現在，讓我們更進一步。

到目前為止，你一直把 Copilot CLI 當作通用型助手來使用。Agent 讓你能賦予它特定角色與內建標準，例如強制使用型別提示與 PEP 8 的程式碼審查員，或是能撰寫 pytest 測試案例的測試助手。你將看到，同樣的提示詞，交給有明確指示的 agent 處理時，結果會明顯更好。

## 🎯 學習目標

完成本章後，你將能夠：

- 使用內建 agent：Plan（`/plan`）、Code-review（`/review`），並了解自動 agent（Explore、Task）
- 使用 agent 檔案（`.agent.md`）建立專業化 agent
- 讓 agent 處理領域專屬任務
- 透過 `/agent` 與 `--agent` 在 agent 間切換
- 撰寫專案專屬標準的自訂指示檔

> ⏱️ **預估時間**：約 55 分鐘（閱讀 20 分鐘 + 實作 35 分鐘）

---

## 🧩 真實世界類比：聘請專家

當你需要修繕房子時，你不會只找一個「通才助手」。你會找專家：

| 問題 | 專家 | 為什麼 |
|---------|------------|-----|
| 水管漏水 | 水電工 | 熟悉水管法規，有專業工具 |
| 電線重拉 | 電工 | 了解安全規範，符合法規 |
| 換新屋頂 | 屋頂師傅 | 熟悉材料，考慮當地氣候 |

Agent 的運作方式也是如此。與其用通用型 AI，不如用專注於特定任務、了解正確流程的 agent。只需設定一次指示，之後每次需要該專業時都能重複使用：程式碼審查、測試、安全、文件撰寫。

<img src="assets/hiring-specialists-analogy.png" alt="聘請專家類比——就像你為房屋修繕找專業技師，AI agent 也專精於特定任務，如程式碼審查、測試、安全與文件撰寫" width="800" />

---

# 使用 Agent

立即開始使用內建與自訂 agent。

---

## *第一次用 Agent？* 從這裡開始！
從未用過或建立過 agent？這裡有你入門本課程所需的一切。

1. **立刻試用一個*內建* agent：**
   ```bash
   copilot
   > /plan Add input validation for book year in the book app
   ```
   這會呼叫 Plan agent，產生逐步實作計畫。

2. **看看我們的自訂 agent 範例：** 定義 agent 指示很簡單，參考我們提供的 [python-reviewer.agent.md](../.github/agents/python-reviewer.agent.md) 檔案即可了解格式。

3. **理解核心概念：** Agent 就像諮詢專家而非通才。「前端 agent」會自動專注於無障礙與元件模式，你不必每次都提醒它，因為這些已經寫在 agent 的指示裡。


## 內建 Agent

**你在第三章開發流程已經用過部分內建 agent！**
<br>`/plan` 和 `/review` 其實就是內建 agent。現在你知道背後發生了什麼。完整清單如下：

| Agent | 如何呼叫 | 功能說明 |
|-------|---------------|--------------|
| **Plan** | `/plan` 或 `Shift+Tab`（切換模式） | 在寫程式前產生逐步實作計畫 |
| **Code-review** | `/review` | 針對暫存/未暫存變更給予聚焦且可執行的回饋 |
| **Init** | `/init` | 產生專案設定檔（指示、agent） |
| **Explore** | *自動* | 當你請 Copilot 探索或分析程式碼庫時內部使用 |
| **Task** | *自動* | 執行測試、建置、lint、安裝相依套件等指令 |

<br>

**內建 agent 實例** - 呼叫 Plan、Code-review、Explore 與 Task 的範例

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

那 Task Agent 呢？它在幕後協助管理與追蹤執行狀態，並以清楚明瞭的格式回報：

| 結果 | 你會看到什麼 |
|---------|--------------|
| ✅ **成功** | 簡要摘要（如「全部 247 個測試通過」、「建置成功」） |
| ❌ **失敗** | 完整輸出（含堆疊追蹤、編譯錯誤、詳細日誌） |


> 📚 **官方文件**：[GitHub Copilot CLI Agents](https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents)

---

# 將 Agent 加入 Copilot CLI

你可以輕鬆定義自己的 agent，納入你的工作流程！只需定義一次，隨時指揮調用！

<img src="assets/using-agents.png" alt="四個色彩繽紛的 AI 機器人並肩站立，各自持有不同工具，象徵專業 agent 能力" width="800"/>

## 🗂️ 新增你的 agent

Agent 檔案是副檔名為 `.agent.md` 的 Markdown 檔案。分為兩部分：YAML frontmatter（中繼資料）與 Markdown 指示內容。

> 💡 **第一次接觸 YAML frontmatter？** 它是檔案頂部用 `---` 包圍的一小段設定。YAML 就是 `key: value` 配對。其餘部分是一般 Markdown。

這是一個最簡單的 agent 範例：

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

| 位置 | 範圍 | 適用情境 |
|----------|-------|----------|
| `.github/agents/` | 專案專屬 | 適合團隊共用、符合專案慣例的 agent |
| `~/.copilot/agents/` | 全域（所有專案） | 你個人常用的 agent |

**本專案已在 [.github/agents/](../.github/agents/) 資料夾內附上範例 agent 檔案**。你可以自行撰寫，也可直接修改現有範例。

<details>
<summary>📂 查看本課程的範例 agent</summary>

| 檔案 | 說明 |
|------|-------------|
| `hello-world.agent.md` | 最簡範例——從這裡開始 |
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
在互動模式下，使用 `/agent` 列出 agent 並選擇要開始工作的 agent。
選擇一個 agent 後即可繼續對話。

```bash
copilot
> /agent
```

若要切換到其他 agent，或回到預設模式，再次使用 `/agent` 指令即可。

### 程式化模式

直接用 agent 啟動新會話。

```bash
copilot --agent python-reviewer
> Review @samples/book-app-project/books.py
```

> 💡 **切換 agent**：你隨時可以用 `/agent` 或 `--agent` 切換到其他 agent。若要回到標準 Copilot CLI 體驗，請用 `/agent` 並選擇**無 agent**。

---

# 更深入運用 Agent

<img src="assets/creating-custom-agents.png" alt="機器人在工作台上組裝，周圍有各種零件與工具，象徵自訂 agent 的打造" width="800"/>

> 💡 **本節為進階選讀。** 內建 agent（`/plan`、`/review`）已足夠應付多數工作流程。只有當你需要某種專業知識能在工作中持續被應用時，才需建立自訂 agent。

下列主題各自獨立。**挑你有興趣的看，不必一次全讀完。**

| 我想要... | 跳到 |
|---|---|
| 看看 agent 為何比通用提示更強 | [專家 vs 通用](#specialist-vs-generic-see-the-difference) |
| 在一個功能上結合多個 agent | [多 agent 協作](#working-with-multiple-agents) |
| 組織、命名與分享 agent | [agent 組織與分享](#organizing--sharing-agents) |
| 設定專案全時啟用情境 | [Copilot 專案設定](#configuring-your-project-for-copilot) |
| 查詢 YAML 屬性與工具 | [Agent 檔案參考](#agent-file-reference) |

選擇下方情境展開細節。

---

<a id="specialist-vs-generic-see-the-difference"></a>
<details>
<summary><strong>專家 vs 通用：看見差異</strong>——為什麼 agent 輸出比通用提示更好</summary>

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

很基本。能用，但缺少很多細節。

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
- ✅ 所有參數與回傳值都有型別提示
- ✅ 完整 docstring，含 Args/Returns/Raises
- ✅ 輸入驗證與正確錯誤處理
- ✅ 使用 list comprehension 提升效能
- ✅ 邊界情境處理（缺漏/無效年份）
- ✅ PEP 8 格式規範
- ✅ 防禦式程式設計

**差異**：同樣的提示，輸出品質天差地遠。agent 自帶你可能忘記要求的專業。

</details>

---

<a id="working-with-multiple-agents"></a>
<details>
<summary><strong>多 agent 協作</strong>——結合專家、會話中切換、agent 作為工具</summary>

## 多 agent 協作

真正的威力在於多位專家共同打造一個功能。

### 範例：開發一個簡單功能

```bash
copilot

> I want to add a "search by year range" feature to the book app

# 用 python-reviewer 設計
> /agent
# 選擇 "python-reviewer"

> @samples/book-app-project/books.py Design a find_by_year_range method. What's the best approach?

# 切換到 pytest-helper 設計測試
> /agent
# 選擇 "pytest-helper"

> @samples/book-app-project/tests/test_books.py Design test cases for a find_by_year_range method.
> What edge cases should we cover?

# 綜合兩者設計
> Create an implementation plan that includes the method implementation and comprehensive tests.
```

**關鍵觀念**：你是總設計師，指揮專家處理細節。你掌握全局，他們負責專業。

<details>
<summary>🎬 實際操作影片！</summary>

![Python Reviewer Demo](assets/python-reviewer-demo.gif)

*Demo 輸出會有所不同——你的模型、工具和回應可能與此不同。*

</details>

### Agent 作為工具

當 agent 已設定好，Copilot 也能在複雜任務中自動把部分工作交給合適的專家 agent。例如你要求全端功能時，Copilot 可能自動分派給對應領域的 agent。

</details>

---

<a id="organizing--sharing-agents"></a>
<details>
<summary><strong>agent 組織與分享</strong>——命名、檔案放置、指示檔與團隊共用</summary>

## agent 組織與分享

### 命名你的 agent

建立 agent 檔案時，名稱很重要。這是你在 `/agent` 或 `--agent` 後要輸入的，也是團隊成員在 agent 清單中會看到的。

| ✅ 好名稱 | ❌ 避免 |
|--------------|----------|
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

將 agent 檔案放在 `.github/agents/`，即可納入版本控制。推送到你的 repo，每位團隊成員都能自動取得。但 agent 只是 Copilot 會讀取的其中一種檔案。它也支援**指示檔**，這類檔案會自動套用到每個會話，無需任何人執行 `/agent`。

換個角度想：agent 是你隨時可召喚的專家，指示檔則是團隊永遠生效的規則。

### 檔案該放哪裡

你已知道兩個主要位置（見上方 [Agent 檔案放哪裡](#where-to-put-agent-files)）。用這張決策樹來選擇：

<img src="assets/agent-file-placement-decision-tree.png" alt="Agent 檔案放置決策樹：實驗 → 當前資料夾，團隊共用 → .github/agents/，全域 → ~/.copilot/agents/" width="800"/>

**從簡單開始：** 先在專案資料夾建立一個 `*.agent.md` 檔案。滿意後再移到正式位置。

除了 agent 檔案，Copilot 也會自動讀取**專案層級指示檔**，無需 `/agent`。詳見下方 [Copilot 專案設定](#configuring-your-project-for-copilot) 介紹 `AGENTS.md`、`.instructions.md` 與 `/init`。

</details>

---

<a id="configuring-your-project-for-copilot"></a>
<details>
<summary><strong>Copilot 專案設定</strong>——AGENTS.md、指示檔與 /init 設定</summary>

## Copilot 專案設定

Agent 是你隨選召喚的專家。**專案設定檔**則不同：Copilot 會在每次會話自動讀取，了解你的專案慣例、技術棧與規則。無需任何人執行 `/agent`，情境對所有協作者都自動生效。

### 用 /init 快速設定

最快的方式是讓 Copilot 自動產生設定檔：

```bash
copilot
> /init
```

Copilot 會掃描你的專案並建立專屬指示檔。你可以事後編輯。

### 指示檔格式

| 檔案 | 範圍 | 備註 |
|------|-------|-------|
| `AGENTS.md` | 專案根目錄或子資料夾 | **跨平台標準**——Copilot 與其他 AI 助手皆支援 |
| `.github/copilot-instructions.md` | 專案 | GitHub Copilot 專用 |
| `.github/instructions/*.instructions.md` | 專案 | 更細緻、主題專屬指示 |
| `CLAUDE.md`, `GEMINI.md` | 專案根目錄 | 為相容性而支援 |

> 🎯 **剛開始？** 用 `AGENTS.md` 寫專案指示。其他格式可視需求再探索。

### AGENTS.md

`AGENTS.md` 是推薦格式。它是[開放標準](https://agents.md/)，可跨 Copilot 與其他 AI 程式工具使用。放在 repo 根目錄，Copilot 會自動讀取。本專案的 [AGENTS.md](../AGENTS.md) 就是實際範例。

典型的 `AGENTS.md` 會描述你的專案情境、程式風格、安全需求與測試標準。可依我們的範例檔案撰寫。

### 自訂指示檔（.instructions.md）

若團隊需要更細緻的控制，可將指示拆成主題專屬檔案。每個檔案只針對一個議題，且會自動套用：

```
.github/
└── instructions/
    ├── python-standards.instructions.md
    ├── security-checklist.instructions.md
    └── api-design.instructions.md
```

> 💡 **注意**：指示檔支援任何語言。此例用 Python 配合課程專案，但你也能為 TypeScript、Go、Rust 或任何技術建立類似檔案。

#### 用 `applyTo` 限定指示範圍

預設情況下，指示檔會套用到每個會話。若只想限定特定檔案型別，可在 YAML frontmatter（檔案最上方 `---` 區塊）加上 `applyTo` 欄位：

```markdown
---
applyTo: "**/*.py"
---
# Python Standards
Always follow PEP 8 style conventions.
Use type hints in all function signatures.
```

有了 `applyTo: "**/*.py"`，Copilot 只會在你處理 Python 檔案時載入這份指示檔。Python 風格指示不會干擾 Dockerfile 或 SQL 查詢的對話。

以下是常見模式：

| `applyTo` 值 | 套用時機 |
|---|---|
| `"**/*.py"` | 任何 Python 檔案 |
| `"**/*.{ts,tsx}"` | TypeScript 與 TSX 檔案 |
| `"tests/**"` | `tests/` 資料夾下所有檔案 |
| （無 frontmatter） | 每個會話——預設 |

> 💡 **小技巧**：請用引號包住萬用字元（如 `"**/*.py"`），確保在所有作業系統與 shell 下都能正確解析。

**尋找社群指示檔**：瀏覽 [github/awesome-copilot](https://github.com/github/awesome-copilot) 可找到 .NET、Angular、Azure、Python、Docker 等多種現成指示檔。

### 關閉自訂指示

若你需要 Copilot 忽略所有專案設定（例如除錯或比較行為時）：

```bash
copilot --no-custom-instructions
```

</details>

---

<a id="agent-file-reference"></a>
<details>
<summary><strong>Agent 檔案參考</strong>——YAML 屬性、工具別名與完整範例</summary>

## Agent 檔案參考

### 更完整的範例

你已看過[最小 agent 格式](#-add-your-agents)。這裡是一個使用 `tools` 屬性的進階範例。建立 `~/.copilot/agents/python-reviewer.agent.md`：

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
| `description` | **是** | agent 功能說明——協助 Copilot 理解何時建議使用 |
| `tools` | 否 | 可用工具清單（省略＝全部可用）。見下方工具別名。 |
| `target` | 否 | 限定僅在 `vscode` 或 `github-copilot` 使用 |

### 工具別名

在 `tools` 清單中可用這些名稱：
- `read` - 讀取檔案內容
- `edit` - 編輯檔案
- `search` - 搜尋檔案（grep/glob）
- `execute` - 執行 shell 指令（也可用：`shell`、`Bash`）
- `agent` - 呼叫其他自訂 agent

> 📖 **官方文件**：[自訂 agent 設定](https://docs.github.com/copilot/reference/custom-agents-configuration)
>
> ⚠️ **僅限 VS Code**：`model` 屬性（選擇 AI 模型）僅支援於 VS Code，不支援 GitHub Copilot CLI。為跨平台 agent 檔案可安全包含，Copilot CLI 會自動忽略。

### 更多 agent 範本

> 💡 **新手注意**：下方範例為模板。**請將特定技術替換成你專案實際用的。** 重要的是 agent 的*結構*，不是範例中的技術名稱。

本專案在 [.github/agents/](../.github/agents/) 資料夾內有實作範例：
- [hello-world.agent.md](../.github/agents/hello-world.agent.md) - 最小範例，從這裡開始
- [python-reviewer.agent.md](../.github/agents/python-reviewer.agent.md) - Python 程式碼品質審查員
- [pytest-helper.agent.md](../.github/agents/pytest-helper.agent.md) - Pytest 測試專家

更多社群 agent，請見 [github/awesome-copilot](https://github.com/github/awesome-copilot)。

</details>

---

# 練習

<img src="../assets/practice.png" alt="溫馨桌面擺設，螢幕顯示程式碼、檯燈、咖啡杯與耳機，準備動手實作" width="800"/>

建立你自己的 agent，實際體驗它們的威力。

---

## ▶️ 自己動手試試

```bash

# 建立 agents 資料夾（若尚未存在）
mkdir -p .github/agents

# 建立程式碼審查 agent
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

# 建立文件撰寫 agent
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

# 現在開始使用它們
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

實作範例已建立 `reviewer` 與 `documentor` agent。現在請練習建立並使用 agent，針對另一個任務——改進書籍應用程式的資料驗證：1. 建立 3 個專為書籍應用程式設計的 agent 檔案（`.agent.md`），每個 agent 各一個，放在 `.github/agents/` 目錄下
2. 你的 agents：
   - **data-validator**：檢查 `data.json` 是否有遺漏或格式錯誤的資料（作者為空、年份為 0、缺少欄位）
   - **error-handler**：檢閱 Python 程式碼的錯誤處理是否一致，並建議統一的做法
   - **doc-writer**：產生或更新 docstring 及 README 內容
3. 在書籍應用程式上使用每個 agent：
   - `data-validator` → 稽核 `@samples/book-app-project/data.json`
   - `error-handler` → 檢閱 `@samples/book-app-project/books.py` 和 `@samples/book-app-project/utils.py`
   - `doc-writer` → 為 `@samples/book-app-project/books.py` 新增 docstring
4. 協作：先用 `error-handler` 找出錯誤處理的缺口，再用 `doc-writer` 記錄改進後的方法

**成功標準**：你擁有 3 個可運作的 agent，能產生一致且高品質的輸出，並可透過 `/agent` 在它們之間切換。

<details>
<summary>💡 提示（點擊展開）</summary>

**起始範本**：在 `.github/agents/` 為每個 agent 建立一個檔案：

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

**測試你的 agents：**

> 💡 **注意：** 你應該已經在本地複本的這個 repo 中有 `samples/book-app-project/data.json`。如果缺少，請從原始 repo 下載原版：
> [data.json](https://github.com/github/copilot-cli-for-beginners/blob/main/samples/book-app-project/data.json)

```bash
copilot
> /agent
# 從清單中選擇 "data-validator"
> @samples/book-app-project/data.json 檢查書籍是否有作者欄位為空或年份無效
```

**提示：** YAML frontmatter 中的 `description` 欄位是 agent 能正常運作的必要條件。

</details>

### 加分挑戰：指令庫

你已經建立了可隨選呼叫的 agents。現在試試另一種方式：**指令檔**，讓 Copilot 在每次會話中自動讀取，無需 `/agent`。

建立 `.github/instructions/` 資料夾，並新增至少 3 個指令檔：
- `python-style.instructions.md`：強制執行 PEP 8 及型別提示慣例
- `test-standards.instructions.md`：強制測試檔案遵循 pytest 慣例
- `data-quality.instructions.md`：驗證 JSON 資料項目的品質

在書籍應用程式程式碼上測試每個指令檔。

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 結果 | 修正方式 |
|------|------|----------|
| agent frontmatter 缺少 `description` | agent 無法載入或無法被發現 | 一定要在 YAML frontmatter 中加入 `description:` |
| agent 檔案位置錯誤 | 使用時找不到 agent | 放在 `~/.copilot/agents/`（個人）或 `.github/agents/`（專案） |
| 用 `.md` 而非 `.agent.md` | 檔案可能不被辨識為 agent | 檔名應為 `python-reviewer.agent.md` 這類格式 |
| agent 提示過長 | 可能超過 30,000 字元限制 | 保持 agent 定義精簡；詳細指令可用 skill 實現 |

### 疑難排解

**找不到 agent** - 請確認 agent 檔案存在於下列其中一個位置：
- `~/.copilot/agents/`
- `.github/agents/`

列出可用的 agents：

```bash
copilot
> /agent
# 顯示所有可用的 agents
```

**agent 未遵循指令** - 請在提示中明確說明，並在 agent 定義中加入更多細節：
- 指定框架／函式庫及其版本
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

1. **內建 agents**：`/plan` 和 `/review` 可直接呼叫；Explore 和 Task 會自動運作
2. **自訂 agents** 是以 `.agent.md` 檔案定義的專家角色
3. **優秀的 agent** 具備明確的專業領域、標準與輸出格式
4. **多 agent 協作** 能結合專業解決複雜問題
5. **指令檔**（`.instructions.md`）可自動套用團隊標準
6. **一致的輸出** 來自明確定義的 agent 指令

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

Agents 會改變 *Copilot 在你的程式碼中採取目標行動的方式*。接下來你將學到 **skills** —— 它們則改變 *Copilot 執行的步驟*。想知道 agents 和 skills 有何不同？第 05 章會直接說明。

在 **[第 05 章：Skills 系統](../05-skills/README.md)**，你將學到：

- skills 如何根據你的提示自動觸發（不需斜線指令）
- 安裝社群 skills
- 用 SKILL.md 檔案建立自訂 skills
- agents、skills 與 MCP 的差異
- 何時該用哪一種

---

**[← 回到第 03 章](../03-development-workflows/README.md)** | **[繼續前往第 05 章 →](../05-skills/README.md)**
