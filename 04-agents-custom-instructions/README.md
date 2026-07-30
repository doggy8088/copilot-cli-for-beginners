![第 04 章：Agent 與自訂指令](assets/chapter-header.png)

> **如果你能在一個工具裡同時聘請 Python 程式碼審查員、測試專家與安全審查員，會怎樣？**

在第 03 章，你已經學會了最重要的工作流程：程式碼審查、重構、除錯、測試產生，以及 git 整合。這些讓你能高效使用 GitHub Copilot CLI。現在，讓我們更進一步。

到目前為止，你一直把 Copilot CLI 當作通用助手來用。Agent 讓你能賦予它特定角色與內建標準，例如：強制使用型別提示與 PEP 8 的程式碼審查員，或是會撰寫 pytest 測試案例的測試助手。你將看到，同樣的提示詞，交給有明確指令的 agent 處理時，結果會明顯更好。

## 🎯 學習目標

完成本章後，你將能夠：

- 使用內建 agent：Plan（`/plan`）、Code-review（`/review`），並了解自動 agent（Explore、Task）
- 使用 agent 檔案（`.agent.md`）建立專業化 agent
- 讓 agent 處理領域專屬任務
- 透過 `/agent` 與 `--agent` 在 agent 間切換
- 撰寫專案專屬標準的自訂指令檔

> ⏱️ **預估時間**：約 55 分鐘（閱讀 20 分鐘 + 實作 35 分鐘）

---

## 🧩 真實世界類比：聘請專家

當你需要修繕房子時，你不會只找一位「萬事通」。你會找專業人士：

| 問題 | 專家 | 為什麼 |
|------|------|--------|
| 水管漏水 | 水電工 | 熟悉水管法規，擁有專業工具 |
| 重新配線 | 電工 | 了解安全規範，符合標準 |
| 換新屋頂 | 屋頂工 | 熟悉材料，考量當地氣候 |

Agent 的運作方式也是如此。與其用一個通用 AI，不如用專注於特定任務、懂得正確流程的 agent。只要設定一次指令，之後每次需要該專業時都能重複使用：程式碼審查、測試、安全、文件。

<img src="assets/hiring-specialists-analogy.png" alt="聘請專家類比——就像你會找專業工匠修繕房屋，AI agent 也專精於特定任務，如程式碼審查、測試、安全與文件" width="800" />

---

# 使用 Agent

立即開始使用內建與自訂 agent。

---

## *第一次用 Agent？* 從這裡開始！
從沒用過或建立過 agent？這裡有本課程入門所需的所有重點。

1. **馬上試試 *內建* agent：**
   ```bash
   copilot
   > /plan Add input validation for book year in the book app
   ```
   這會呼叫 Plan agent，產生逐步實作計畫。

2. **看看我們的自訂 agent 範例：** 定義 agent 指令很簡單，參考我們提供的 [python-reviewer.agent.md](../.github/agents/python-reviewer.agent.md) 檔案即可了解格式。

3. **理解核心概念：** Agent 就像諮詢專家而不是通才。「前端 agent」會自動聚焦於無障礙與元件設計模式，你不必每次都提醒它，因為這些已經寫在 agent 指令裡了。


## 內建 Agent

**你在第 03 章開發流程已經用過部分內建 agent！**
<br>`/plan` 和 `/review` 其實就是內建 agent。現在你知道背後發生了什麼。完整清單如下：

| Agent | 呼叫方式 | 功能說明 |
|-------|----------|----------|
| **Plan** | `/plan` 或 `Shift+Tab`（切換模式） | 在寫程式前產生逐步實作計畫 |
| **Code-review** | `/review` | 針對已暫存／未暫存變更給出聚焦且可行的回饋 |
| **Init** | `/init` | 產生專案設定檔（指令、agent） |
| **Explore** | *自動* | 當你請 Copilot 探索或分析程式碼庫時自動啟用 |
| **Task** | *自動* | 執行測試、建置、靜態檢查、安裝相依套件等指令 |

<br>

**內建 agent 實際操作範例** - 呼叫 Plan、Code-review、Explore 與 Task

```bash
copilot

# 呼叫 Plan agent 產生實作計畫
> /plan Add input validation for book year in the book app

# 呼叫 Code-review agent 審查你的變更
> /review

# Explore 與 Task agent 會在需要時自動啟用：
> Run the test suite        # 使用 Task agent

> Explore how book data is loaded    # 使用 Explore agent
```

那 Task Agent 呢？它在幕後管理與追蹤執行情況，並以清楚明瞭的格式回報：

| 結果 | 你會看到什麼 |
|------|--------------|
| ✅ **成功** | 簡短摘要（例如：「全部 247 項測試通過」、「建置成功」） |
| ❌ **失敗** | 完整輸出（包含堆疊追蹤、編譯錯誤、詳細日誌） |

> 💡 **多輪子 agent（subagent）**：子 agent（由 agent 啟動的背景任務）支援後續訊息。當 agent 在背景執行時，你可以開啟 `/tasks` 查看並傳送後續指令。你不必等它跑完才能再下指示。就像你能在助手工作途中拍拍他肩膀補充說明一樣。

### 為 Plan 模式選擇模型

預設情況下，`/plan` 會使用你目前會話選擇的 AI 模型。你也可以只在 plan 模式下選用*不同*模型——這很適合規劃時用較快或較便宜的模型，實作時再切回更強大的模型：

```bash
copilot

# 只針對 plan 模式開啟模型選擇器
> /model plan

# 或直接指定模型 ID（用 'off' 清除 plan 模式模型）
> /model plan gpt-5.6-sol

# 離開 plan 模式後，模型會自動回復為你的會話模型
```

> 💡 **為什麼要設定 plan 模式模型？** 由先進模型產生的高品質計畫，實際上能節省 token 與時間。精確、範圍明確的計畫，能減少實作過程中的來回修正。

> 📚 **官方文件**：[GitHub Copilot CLI Agents](https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/invoke-custom-agents)

---

# 將 Agent 加入 Copilot CLI

你可以輕鬆定義自己的 agent，納入工作流程！定義一次，隨時調度！

<img src="assets/using-agents.png" alt="四個色彩繽紛的 AI 機器人站在一起，各自拿著不同工具，象徵專業 agent 能力" width="800"/>

## 🗂️ 新增你的 agent

Agent 檔案是副檔名為 `.agent.md` 的 Markdown 檔案。分為兩部分：YAML frontmatter（中繼資料）與 Markdown 指令內容。

> 💡 **沒用過 YAML frontmatter？** 它是檔案頂部一小塊被 `---` 包住的設定區塊。YAML 就是 `key: value` 配對。其餘部分就是一般 Markdown。

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

> 💡 **必填與選填**：`description` 欄位是必填。其他如 `name`、`tools`、`model` 則為選填。

## Agent 檔案放哪裡

| 位置 | 範圍 | 適用情境 |
|------|------|----------|
| `.github/agents/` | 專案專屬 | 適合團隊共用、符合專案慣例的 agent |
| `~/.copilot/agents/` | 全域（所有專案） | 你個人常用、每個專案都能用的 agent |

**本專案已在 [.github/agents/](../.github/agents/) 資料夾內附上範例 agent 檔案**。你可以自行撰寫，也能直接修改現有範例。

<details>
<summary>📂 查看本課程的範例 agent</summary>

| 檔案 | 說明 |
|------|------|
| `hello-world.agent.md` | 最簡範例——從這裡開始 |
| `python-reviewer.agent.md` | Python 程式碼品質審查員 |
| `pytest-helper.agent.md` | Pytest 測試專家 |

```bash
# 或複製一份到你的個人 agent 資料夾（每個專案都能用）
cp .github/agents/python-reviewer.agent.md ~/.copilot/agents/
```

更多社群 agent，請參考 [github/awesome-copilot](https://github.com/github/awesome-copilot)

</details>


## 🚀 使用自訂 agent 的兩種方式

### 互動模式
在互動模式下，使用 `/agent` 列出 agent 並選擇要開始工作的 agent。
選擇 agent 後即可繼續對話。

```bash
copilot
> /agent
```

要切換到其他 agent，或回到預設模式，再次使用 `/agent` 指令即可。

### 程式化模式

直接用 agent 啟動新會話。

```bash
copilot --agent python-reviewer
> Review @samples/book-app-project/books.py
```

> 💡 **切換 agent**：你隨時可以用 `/agent` 或 `--agent` 切換到其他 agent。若要回到標準 Copilot CLI 體驗，使用 `/agent` 並選擇**無 agent**。

> 💡 **Agent 模式只作用於當前會話**：你選的 agent 只會套用在目前這個會話。每次用 `/new`、`/clear` 或開新終端機時，Copilot 都會回到預設模式——agent 選擇不會自動延續。這讓每次會話都能從乾淨狀態開始，有助於專注工作。

---

# 更深入運用 Agent

<img src="assets/creating-custom-agents.png" alt="一個機器人在工作台上被組裝，周圍有各種零件與工具，象徵自訂 agent 的打造過程" width="800"/>

> 💡 **本節為進階選讀。** 內建 agent（`/plan`、`/review`）已足夠應付多數工作流程。只有當你需要跨專案一致套用的專業知識時，才需建立自訂 agent。

下列主題各自獨立。**挑你有興趣的看，不必一次全讀完。**

| 我想要... | 跳到 |
|---|---|
| 看看 agent 為什麼比通用提示好 | [專家 vs 通用](#specialist-vs-generic-see-the-difference) |
| 多個 agent 合作處理一個功能 | [多 agent 協作](#working-with-multiple-agents) |
| 管理、命名與分享 agent | [Agent 組織與分享](#organizing--sharing-agents) |
| 設定專案全時啟用的情境 | [Copilot 專案設定](#configuring-your-project-for-copilot) |
| 查詢 YAML 屬性與工具 | [Agent 檔案參考](#agent-file-reference) |

請選擇下方情境展開詳情。

---

<a id="specialist-vs-generic-see-the-difference"></a>
<details>
<summary><strong>專家 vs 通用：看看差異</strong> - 為什麼 agent 產生的結果比通用提示更好</summary>

## 專家 vs 通用：看看差異

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

很基本，能用，但缺少很多細節。

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
- ✅ 所有參數與回傳值皆有型別提示
- ✅ 完整 docstring，含 Args/Returns/Raises
- ✅ 輸入驗證與正確錯誤處理
- ✅ 使用 list comprehension 提升效能
- ✅ 處理邊界情境（缺少／無效年份）
- ✅ PEP 8 合規格式
- ✅ 防禦式程式設計

**差別在於**：同一個提示，產出品質天差地遠。agent 自帶你可能會忘記要求的專業細節。

</details>

---

<a id="working-with-multiple-agents"></a>
<details>
<summary><strong>多 agent 協作</strong> - 專家組合、會話中切換、agent 當工具</summary>

## 多 agent 協作

真正的威力在於多位專家協作處理同一功能。

### 範例：打造一個簡單功能

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

**關鍵觀念**：你是總設計師，指揮專家處理細節。他們負責專業，你負責全局。

<details>
<summary>🎬 實際操作影片！</summary>

![Python Reviewer Demo](assets/python-reviewer-demo.gif)

*Demo 輸出會因模型、工具、回應而異，與此處展示內容可能不同。*

</details>

### Agent 當工具

當 agent 設定妥當時，Copilot 也能在複雜任務中自動呼叫它們作為工具。若你要求全端功能，Copilot 可能會自動分派部分工作給適合的專家 agent。

</details>

---

<a id="organizing--sharing-agents"></a>
<details>
<summary><strong>Agent 組織與分享</strong> - 命名、檔案放置、指令檔與團隊共用</summary>

## Agent 組織與分享

### 命名你的 agent

建立 agent 檔案時，名稱很重要。這是你在 `/agent` 或 `--agent` 後要輸入的，也是團隊成員在 agent 清單裡看到的。

| ✅ 好名稱 | ❌ 避免 |
|----------|---------|
| `frontend` | `my-agent` |
| `backend-api` | `agent1` |
| `security-reviewer` | `helper` |
| `react-specialist` | `code` |
| `python-backend` | `assistant` |

**命名慣例：**
- 使用小寫加連字號：`my-agent-name.agent.md`
- 包含領域：`frontend`、`backend`、`devops`、`security`
- 需要時更具體：`react-typescript` 比單純 `frontend` 更明確

---

### 與團隊分享

把 agent 檔案放在 `.github/agents/`，就會納入版本控制。推送到你的 repo，團隊每個人都會自動取得。但 agent 只是 Copilot 會讀取的其中一種檔案。它也支援**指令檔**，這類檔案會自動套用到每次會話，無需手動執行 `/agent`。

可以這樣想：agent 是你隨時能召喚的專家，指令檔則是團隊永遠啟用的規則。

### 檔案該放哪裡

你已經知道兩個主要位置（見上方 [Agent 檔案放哪裡](#where-to-put-agent-files)）。用這張決策樹來選擇：

<img src="assets/agent-file-placement-decision-tree.png" alt="Agent 檔案放置決策樹：實驗 → 當前資料夾，團隊用 → .github/agents/，全域用 → ~/.copilot/agents/" width="800"/>

**從簡單開始：** 先在專案資料夾建立一個 `*.agent.md` 檔。滿意後再移到正式位置。

除了 agent 檔案，Copilot 也會自動讀取**專案層級指令檔**，無需 `/agent`。詳見下方 [Copilot 專案設定](#configuring-your-project-for-copilot) 介紹 `AGENTS.md`、`.instructions.md` 與 `/init`。

</details>

---

<a id="configuring-your-project-for-copilot"></a>
<details>
<summary><strong>Copilot 專案設定</strong> - AGENTS.md、指令檔與 /init 快速設定</summary>

## Copilot 專案設定

Agent 是你隨選的專家。**專案設定檔**則不同：Copilot 會在每次會話自動讀取，了解你的專案慣例、技術棧與規範。沒有人需要執行 `/agent`，情境對所有協作者都自動啟用。

### 用 /init 快速設定

最快的方式是讓 Copilot 幫你產生設定檔：

```bash
copilot
> /init
```

Copilot 會掃描你的專案並建立量身打造的指令檔。你可以事後編輯。

### 指令檔格式

| 檔案 | 範圍 | 備註 |
|------|------|------|
| `AGENTS.md` | 專案根目錄或子資料夾 | **跨平台標準**——Copilot 與其他 AI 助手皆支援 |
| `.github/copilot-instructions.md` | 專案 | GitHub Copilot 專用 |
| `.github/instructions/*.instructions.md` | 專案 | 更細緻、主題式指令 |
| `~/.copilot/instructions/**/*.instructions.md` | 使用者（所有專案） | 你個人適用於所有 repo 的指令 |
| `CLAUDE.md`、`GEMINI.md` | 專案根目錄 | 為相容性而支援 |

> 🎯 **剛開始用？** 請用 `AGENTS.md` 撰寫專案指令。其他格式可視需求再探索。

### AGENTS.md

`AGENTS.md` 是推薦格式。它是[開放標準](https://agents.md/)，可在 Copilot 與其他 AI 程式工具通用。放在 repo 根目錄，Copilot 會自動讀取。本專案的 [AGENTS.md](../AGENTS.md) 就是實際範例。

典型的 `AGENTS.md` 會描述你的專案情境、程式風格、安全需求與測試標準。請依我們範例檔案格式撰寫。

### 自訂指令檔（.instructions.md）

若團隊需要更細緻的控制，可將指令拆分為主題式檔案。每個檔案聚焦一個面向，且會自動套用：

```
.github/
└── instructions/
    ├── python-standards.instructions.md
    ├── security-checklist.instructions.md
    └── api-design.instructions.md
```

> 💡 **注意**：指令檔支援任何語言。這裡用 Python 只是配合課程專案，你也能為 TypeScript、Go、Rust 或任何技術建立類似檔案。

#### 用 `applyTo` 限定指令作用範圍

預設情況下，指令檔會套用到每次對話。若只想限定特定檔案型別，可在 YAML frontmatter（檔案最上方 `---` 區塊）加上 `applyTo` 欄位：

```markdown
---
applyTo: "**/*.py"
---
# Python Standards
Always follow PEP 8 style conventions.
Use type hints in all function signatures.
```

加上 `applyTo: "**/*.py"` 後，Copilot 只會在你處理 Python 檔案時載入這份指令。Python 風格指令不會干擾你討論 Dockerfile 或 SQL 查詢。

常見範例：

| `applyTo` 值 | 何時套用 |
|---|---|
| `"**/*.py"` | 任何 Python 檔案 |
| `"**/*.{ts,tsx}"` | TypeScript 與 TSX 檔案 |
| `"tests/**"` | 任何 `tests/` 資料夾內檔案 |
| （無 frontmatter） | 每次對話——預設 |

> 💡 **小技巧**：請用引號包住萬用字元（如 `"**/*.py"`），確保在所有作業系統與 shell 下都能正確解析。

#### 用 `@` 匯入其他檔案

你可以在 `AGENTS.md` 或任何指令檔內用 `@filepath` 語法參照其他檔案。Copilot 會自動展開並引入該檔案內容，讓主檔案保持簡潔，細節集中在其他檔：

```markdown
<!-- AGENTS.md -->
# Project Instructions

@.github/instructions/python-standards.instructions.md
@.github/instructions/test-standards.instructions.md
```

當指令內容變多時，這很方便。可將指令拆分成聚焦檔案，再用 `@` 匯入到單一 `AGENTS.md`。同樣語法也適用於 `.github/copilot-instructions.md` 與其他指令檔。

> 💡 **小技巧**：用 `@` 匯入可讓多個指令檔共用同一基礎檔案。例如，你可以有一份 `@.github/instructions/shared-rules.md`，讓每個指令檔都能引入。

**尋找社群指令檔**：瀏覽 [github/awesome-copilot](https://github.com/github/awesome-copilot) 取得 .NET、Angular、Azure、Python、Docker 等多種技術的現成指令檔。

### 關閉自訂指令

若你需要 Copilot 忽略所有專案設定（適合除錯或比較行為）：

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

你已經看過[最小 agent 格式](#-add-your-agents)。這裡是一個使用 `tools` 屬性的進階範例。建立 `~/.copilot/agents/python-reviewer.agent.md`：

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
| `description` | **是** | agent 功能說明——協助 Copilot 理解何時建議使用 |
| `tools` | 否 | 可用工具清單（省略＝全部可用）。見下方工具別名。 |
| `target` | 否 | 限定只在 `vscode` 或 `github-copilot` 使用 |

### 工具別名

在 `tools` 清單中可用這些名稱：
- `read` - 讀取檔案內容
- `edit` - 編輯檔案
- `search` - 搜尋檔案（grep/glob）
- `execute` - 執行 shell 指令（也可用：`shell`、`Bash`）
- `agent` - 呼叫其他自訂 agent

> 📖 **官方文件**：[自訂 agent 設定](https://docs.github.com/copilot/reference/custom-agents-configuration)
>
> ⚠️ **僅限 VS Code**：`model` 屬性（選擇 AI 模型）僅支援於 VS Code，不支援 GitHub Copilot CLI。為跨平台 agent 檔案可安全保留，Copilot CLI 會自動忽略。

### 更多 agent 範本

> 💡 **新手注意**：下方範例為模板。**請將特定技術換成你專案實際用的。** 重要的是 agent 的*結構*，不是範例中的技術名稱。
本專案在 [.github/agents/](../.github/agents/) 資料夾中包含可運作的範例：
- [hello-world.agent.md](../.github/agents/hello-world.agent.md) - 最簡範例，建議從這裡開始
- [python-reviewer.agent.md](../.github/agents/python-reviewer.agent.md) - Python 程式碼品質審查員
- [pytest-helper.agent.md](../.github/agents/pytest-helper.agent.md) - Pytest 測試專家

社群貢獻的 Agent，請參見 [github/awesome-copilot](https://github.com/github/awesome-copilot)。

</details>

---

# 練習

<img src="../assets/practice.png" alt="溫暖的書桌擺設，螢幕顯示程式碼，檯燈、咖啡杯與耳機，準備動手練習" width="800"/>

建立你自己的 Agent，並實際運作看看。

---

## ▶️ 自己動手試試看

```bash

# 建立 agents 目錄（如果尚未存在）
mkdir -p .github/agents

# 建立一個程式碼審查 Agent
cat > .github/agents/reviewer.agent.md << 'EOF'
---
name: reviewer
description: 專注於安全性與最佳實踐的資深程式碼審查員
---

# Code Reviewer Agent

你是一位專注於程式碼品質的資深程式碼審查員。

**審查重點：**
1. 安全性漏洞
2. 效能問題
3. 可維護性疑慮
4. 違反最佳實踐

**輸出格式：**
請以編號清單列出問題，並加上嚴重程度標籤：
[CRITICAL]、[HIGH]、[MEDIUM]、[LOW]
EOF

# 建立一個文件撰寫 Agent
cat > .github/agents/documentor.agent.md << 'EOF'
---
name: documentor
description: 撰寫清楚且完整文件的技術寫手
---

# Documentation Agent

你是一位能撰寫清楚文件的技術寫手。

**文件標準：**
- 以一句話摘要開頭
- 包含使用範例
- 記錄參數與回傳值
- 註明注意事項或限制
EOF

# 現在開始使用它們
copilot --agent reviewer
> Review @samples/book-app-project/books.py

# 或切換 Agent
copilot
> /agent
# 選擇 "documentor"
> Document @samples/book-app-project/books.py
```

---

## 📝 作業

### 主要挑戰：打造專業分工的 Agent 團隊

動手範例建立了 `reviewer` 與 `documentor` 兩個 Agent。現在請練習為另一個任務——提升書籍應用程式的資料驗證——建立並使用 Agent：

1. 建立 3 個專為書籍應用程式設計的 Agent 檔案（`.agent.md`），每個 Agent 一個，放在 `.github/agents/` 目錄下
2. 你的 Agent：
   - **data-validator**：檢查 `data.json` 是否有遺漏或格式錯誤的資料（如作者為空、year=0、缺少欄位）
   - **error-handler**：審查 Python 程式碼的錯誤處理是否一致，並建議統一做法
   - **doc-writer**：產生或更新 docstring 與 README 內容
3. 對書籍應用程式分別使用這些 Agent：
   - `data-validator` → 稽核 `@samples/book-app-project/data.json`
   - `error-handler` → 審查 `@samples/book-app-project/books.py` 與 `@samples/book-app-project/utils.py`
   - `doc-writer` → 為 `@samples/book-app-project/books.py` 加上 docstring
4. 協作流程：先用 `error-handler` 找出錯誤處理缺口，再用 `doc-writer` 記錄改進後的做法

**成功標準**：你有 3 個可運作的 Agent，能產生一致且高品質的輸出，並可用 `/agent` 在它們之間切換。

<details>
<summary>💡 提示（點擊展開）</summary>

**起手範本**：每個 Agent 建立一個檔案，放在 `.github/agents/`：

`data-validator.agent.md`:
```markdown
---
description: 分析 JSON 資料檔案是否有遺漏或格式錯誤的項目
---

你會分析 JSON 資料檔案，找出遺漏或格式錯誤的項目。

**重點檢查：**
- 作者欄位為空或遺漏
- 無效年份（year=0、未來年份、負數年份）
- 必要欄位缺失（title、author、year、read）
- 重複項目
```

`error-handler.agent.md`:
```markdown
---
description: 審查 Python 程式碼的錯誤處理一致性
---

你會審查 Python 程式碼的錯誤處理一致性。

**標準：**
- 不可有裸 except 子句
- 適當時使用自訂例外
- 所有檔案操作皆使用 context manager
- 成功／失敗的回傳型別一致
```

`doc-writer.agent.md`:
```markdown
---
description: 撰寫清楚 Python 文件的技術寫手
---

你是一位撰寫清楚 Python 文件的技術寫手。

**標準：**
- 採用 Google 風格 docstring
- 包含參數型別與回傳值
- 為公開方法加上使用範例
- 註明可能拋出的例外
```

**測試你的 Agent：**

> 💡 **注意：** 你本地的 repo 應已包含 `samples/book-app-project/data.json`。若缺少，請從原始 repo 下載：
> [data.json](https://github.com/github/copilot-cli-for-beginners/blob/main/samples/book-app-project/data.json)

```bash
copilot
> /agent
# 從清單中選擇 "data-validator"
> @samples/book-app-project/data.json 檢查書籍是否有作者為空或年份無效
```

**小提醒：** YAML frontmatter 的 `description` 欄位是 Agent 能運作的必要條件。

</details>

### 加分挑戰：指令庫

你已經建立了可隨選啟用的 Agent。現在試試另一種方式：**指令檔**，讓 Copilot 在每次會話都自動讀取，無需 `/agent`。

建立 `.github/instructions/` 資料夾，並新增至少 3 個指令檔：
- `python-style.instructions.md`：強制執行 PEP 8 與型別提示慣例
- `test-standards.instructions.md`：強制測試檔案遵循 pytest 慣例
- `data-quality.instructions.md`：驗證 JSON 資料項目的品質

在書籍應用程式程式碼上測試每個指令檔。

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 結果 | 修正方式 |
|------|------|----------|
| Agent frontmatter 缺少 `description` | Agent 無法載入或無法被發現 | YAML frontmatter 一定要有 `description:` |
| Agent 檔案放錯位置 | 使用時找不到 Agent | 請放在 `~/.copilot/agents/`（個人）或 `.github/agents/`（專案） |
| 用 `.md` 而非 `.agent.md` | 檔案可能不會被辨識為 Agent | 檔名請用 `python-reviewer.agent.md` 這種格式 |
| Agent 提示太長 | 可能超過 30,000 字元限制 | Agent 定義保持精簡，細節可用 skill 補充 |

### 疑難排解

**找不到 Agent** - 請確認 Agent 檔案存在於下列其中一個位置：
- `~/.copilot/agents/`
- `.github/agents/`

列出可用的 Agent：

```bash
copilot
> /agent
# 顯示所有可用的 Agent
```

**Agent 未遵循指示** - 請在提示中明確說明，並在 Agent 定義中補充細節：
- 指定框架／函式庫與版本
- 團隊慣例
- 範例程式碼模式

**自訂指令未載入** - 在專案中執行 `/init` 以設定專案專屬指令：

```bash
copilot
> /init
```

或檢查是否被停用：
```bash
# 若要載入自訂指令，請勿加上 --no-custom-instructions
copilot  # 預設會載入自訂指令
```

</details>

---

# 小結

## 🔑 重點整理

1. **內建 Agent**：`/plan` 與 `/review` 可直接呼叫；Explore 與 Task 會自動運作
2. **自訂 Agent**：以 `.agent.md` 檔案定義專家角色
3. **好的 Agent**：具備明確專業、標準與輸出格式
4. **多 Agent 協作**：結合多位專家解決複雜問題
5. **指令檔**（`.instructions.md`）：將團隊標準自動化
6. **一致輸出**：來自明確定義的 Agent 指示

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

Agent 會改變 *Copilot 處理與執行目標任務* 的方式。接下來你將學到 **skills**——它們則改變 *Copilot 採取哪些步驟*。想知道 Agent 與 Skill 有何不同？第五章會直接說明。

在 **[第五章：Skills 系統](../05-skills/README.md)**，你將學到：

- 如何讓 Skill 根據你的提示自動觸發（無需斜線指令）
- 安裝社群技能
- 用 SKILL.md 檔案自訂技能
- Agent、Skill 與 MCP 的差異
- 何時該用哪一種

---

**[← 回到第三章](../03-development-workflows/README.md)** | **[繼續前往第五章 →](../05-skills/README.md)**
