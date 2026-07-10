![Chapter 04: Agents and Custom Instructions](assets/chapter-header.png)

> **如果你能在一個工具裡同時聘請 Python 程式碼審查員、測試專家和安全審查員，會怎樣？**

在第三章中，你已經精通了基本的工作流程：程式碼審查、重構、除錯、測試產生，以及 git 整合。這些讓你能高效運用 GitHub Copilot CLI。現在，讓我們更進一步。

到目前為止，你一直把 Copilot CLI 當作通用型助手來使用。Agent 讓你能賦予它特定角色與內建標準，例如強制使用型別提示與 PEP 8 的程式碼審查員，或是會撰寫 pytest 測試案例的測試助手。你將會看到，同樣的提示詞，交給有明確指示的 agent 處理，結果會明顯更好。

## 🎯 學習目標

完成本章後，你將能夠：

- 使用內建 agent：Plan（`/plan`）、Code-review（`/review`），並了解自動 agent（Explore、Task）
- 透過 agent 檔案（`.agent.md`）建立專業化 agent
- 使用 agent 處理領域專屬任務
- 透過 `/agent` 與 `--agent` 在 agent 之間切換
- 撰寫專案專屬標準的自訂指示檔案

> ⏱️ **預估時間**：約 55 分鐘（閱讀 20 分鐘 + 實作 35 分鐘）

---

## 🧩 真實世界類比：聘請專家

當你需要修繕房子時，你不會只找一位「通才幫手」。你會找專家：

| 問題 | 專家 | 為什麼 |
|---------|------------|-----|
| 水管漏水 | 水電工 | 熟悉水管法規，擁有專業工具 |
| 電線重拉 | 電工 | 了解安全規範，符合法規 |
| 換新屋頂 | 屋頂工 | 熟悉材料，考量當地氣候 |

Agent 的運作方式也是如此。與其使用通用型 AI，不如使用專注於特定任務並了解正確流程的 agent。只需設定一次指示，之後每次需要該專業時都能重複使用：程式碼審查、測試、安全、文件撰寫。

<img src="assets/hiring-specialists-analogy.png" alt="聘請專家類比 - 就像你會為房屋修繕找專業工匠，AI agent 也專精於特定任務，例如程式碼審查、測試、安全與文件撰寫" width="800" />

---

# 使用 Agent

立即開始使用內建與自訂 agent。

---

## *第一次用 Agent？* 請從這裡開始！
從未用過或建立過 agent 嗎？這裡有你開始本課程所需的一切。

1. **立刻嘗試一個*內建* agent：**
   ```bash
   copilot
   > /plan Add input validation for book year in the book app
   ```
   這會呼叫 Plan agent，產生逐步實作計畫。

2. **看看我們的自訂 agent 範例之一：** 定義 agent 指示很簡單，參考我們提供的 [python-reviewer.agent.md](../.github/agents/python-reviewer.agent.md) 檔案即可了解格式。

3. **理解核心概念：** Agent 就像諮詢專家而非通才。「前端 agent」會自動專注於無障礙與元件設計模式，你不必每次都提醒它，因為這些已在 agent 指示中明確規定。

## 內建 Agent

**你在第三章開發工作流程中已經用過一些內建 agent！**
<br>`/plan` 和 `/review` 其實就是內建 agent。現在你知道背後發生了什麼。完整清單如下：

| Agent | 如何呼叫 | 功能說明 |
|-------|---------------|--------------|
| **Plan** | `/plan` 或 `Shift+Tab`（循環切換模式） | 在寫程式前產生逐步實作計畫 |
| **Code-review** | `/review` | 針對已 staged/未 staged 變更給予聚焦且可執行的回饋 |
| **Init** | `/init` | 產生專案設定檔（指示、agent） |
| **Explore** | *自動* | 當你要求 Copilot 探索或分析程式碼庫時內部使用 |
| **Task** | *自動* | 執行測試、建置、靜態檢查與安裝相依套件等指令 |

<br>

**內建 agent 實際運作範例** - 呼叫 Plan、Code-review、Explore 與 Task

```bash
copilot

# 呼叫 Plan agent 產生實作計畫
> /plan Add input validation for book year in the book app

# 呼叫 Code-review agent 審查你的變更
> /review

# Explore 與 Task agent 會在相關時自動呼叫：
> Run the test suite        # 使用 Task agent

> Explore how book data is loaded    # 使用 Explore agent
```

那 Task Agent 呢？它在幕後負責管理與追蹤執行狀況，並以清楚明瞭的格式回報：

| 結果 | 你會看到什麼 |
|---------|--------------|
| ✅ **成功** | 簡短摘要（例如：「全部 247 項測試通過」、「建置成功」） |
| ❌ **失敗** | 完整輸出（包含堆疊追蹤、編譯錯誤與詳細日誌） |


> 📚 **官方文件**：[GitHub Copilot CLI Agents](https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents)

---

# 將 Agent 加入 Copilot CLI

你可以輕鬆定義自己的 agent，納入你的工作流程！定義一次，隨時指揮！

<img src="assets/using-agents.png" alt="四個色彩繽紛的 AI 機器人站在一起，各自持有不同工具，象徵專業 agent 能力" width="800"/>

## 🗂️ 新增你的 agent

Agent 檔案是副檔名為 `.agent.md` 的 Markdown 檔案。分為兩部分：YAML frontmatter（中繼資料）與 Markdown 指示內容。

> 💡 **不熟 YAML frontmatter？** 它是檔案頂部一小段被 `---` 包圍的設定區塊。YAML 就是 `key: value` 配對。其餘內容則是一般 Markdown。

以下是一個最小範例：

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
|----------|-------|----------|
| `.github/agents/` | 專案專屬 | 團隊共用、符合專案慣例的 agent |
| `~/.copilot/agents/` | 全域（所有專案） | 你個人隨處可用的 agent |

**本專案已在 [.github/agents/](../.github/agents/) 資料夾內附上範例 agent 檔案**。你可以自行撰寫，或直接修改現有範例。

<details>
<summary>📂 查看本課程的範例 agent</summary>

| 檔案 | 說明 |
|------|-------------|
| `hello-world.agent.md` | 最小範例－從這裡開始 |
| `python-reviewer.agent.md` | Python 程式碼品質審查員 |
| `pytest-helper.agent.md` | Pytest 測試專家 |

```bash
# 或複製一份到你的個人 agent 資料夾（所有專案都能用）
cp .github/agents/python-reviewer.agent.md ~/.copilot/agents/
```

更多社群 agent，請參考 [github/awesome-copilot](https://github.com/github/awesome-copilot)

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

直接以指定 agent 啟動新會話。

```bash
copilot --agent python-reviewer
> Review @samples/book-app-project/books.py
```

> 💡 **切換 agent**：你可以隨時用 `/agent` 或 `--agent` 切換到其他 agent。若要回到標準 Copilot CLI 模式，使用 `/agent` 並選擇**無 agent**。

> 💡 **Agent 模式僅限本次會話**：你選擇的 agent 只會套用在目前這個會話。當你用 `/new`、`/clear` 或開啟新終端機時，Copilot 會回到預設模式——agent 選擇不會自動延續。這代表每次會話都從乾淨狀態開始，有助於保持專注。

---

# 更深入運用 Agent

<img src="assets/creating-custom-agents.png" alt="機器人在工作台上被組裝，周圍有各種零件與工具，象徵自訂 agent 的創建" width="800"/>

> 💡 **本節為選讀。** 內建 agent（`/plan`、`/review`）已足以應付大多數工作流程。當你需要跨專案一致套用的專業知識時，再建立自訂 agent。

以下每個主題都是獨立的。**挑你有興趣的看，不必一次讀完全部。**

| 我想要... | 跳到 |
|---|---|
| 看看 agent 為何優於通用提示詞 | [專家 vs 通用](#specialist-vs-generic-see-the-difference) |
| 在一個功能上結合多個 agent | [多 agent 協作](#working-with-multiple-agents) |
| 組織、命名與分享 agent | [組織與分享 agent](#organizing--sharing-agents) |
| 設定專案全時情境 | [專案 Copilot 設定](#configuring-your-project-for-copilot) |
| 查詢 YAML 屬性與工具 | [Agent 檔案參考](#agent-file-reference) |

選擇下方情境展開細節。

---

<a id="specialist-vs-generic-see-the-difference"></a>
<details>
<summary><strong>專家 vs 通用：看見差異</strong>－為什麼 agent 產生的結果比通用提示詞更好</summary>

## 專家 vs 通用：看見差異

這正是 agent 展現價值的地方。來看看差別：

### 沒有 Agent（通用 Copilot）

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

很基本，能用，但缺漏很多。

---

### 使用 Python Reviewer Agent

```bash
copilot

> /agent
# 選擇 "python-reviewer"

> Add a function to search books by year range in the book app
```

**專家級輸出**：
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
- ✅ 完整 docstring，包含 Args/Returns/Raises
- ✅ 輸入驗證與正確的錯誤處理
- ✅ 使用 list comprehension 提升效能
- ✅ 邊界情境處理（缺漏/無效 year 值）
- ✅ PEP 8 合規格式
- ✅ 防禦式程式設計

**差異**：同樣的提示詞，產出卻大不相同。agent 帶來你可能會忘記要求的專業細節。

</details>

---

<a id="working-with-multiple-agents"></a>
<details>
<summary><strong>多 agent 協作</strong>－結合專家、會話中切換、agent 當工具</summary>

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

**關鍵觀念**：你是總設計師，指揮專家。他們處理細節，你掌握全局。

<details>
<summary>🎬 實際操作影片！</summary>

![Python Reviewer Demo](assets/python-reviewer-demo.gif)

*Demo 輸出會有所不同——你的模型、工具與回應可能與此不同。*

</details>

### Agent 當工具

當 agent 已設定好，Copilot 也能在複雜任務中把它們當工具呼叫。如果你要求一個全端功能，Copilot 可能會自動將部分任務分派給合適的專家 agent。

</details>

---

<a id="organizing--sharing-agents"></a>
<details>
<summary><strong>組織與分享 agent</strong>－命名、檔案放置、指示檔案與團隊共用</summary>

## 組織與分享 agent

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
- 使用小寫加連字號：`my-agent-name.agent.md`
- 包含領域：`frontend`、`backend`、`devops`、`security`
- 需要時更具體：`react-typescript` 比單純 `frontend` 更明確

---

### 與團隊分享

將 agent 檔案放在 `.github/agents/`，即可納入版本控制。推送到你的 repo，團隊每個人都會自動取得。但 agent 只是 Copilot 會讀取的其中一種檔案。它也支援**指示檔案**，這類檔案會自動套用到每次會話，無需任何人執行 `/agent`。

換個角度想：agent 是你隨時可召喚的專家，指示檔案則是團隊永遠啟用的規則。

### 檔案該放哪裡

你已知道兩個主要位置（見上方 [Agent 檔案放哪裡](#where-to-put-agent-files)）。用這個決策樹來選擇：

<img src="assets/agent-file-placement-decision-tree.png" alt="Agent 檔案放置決策樹：實驗 → 當前資料夾，團隊共用 → .github/agents/，全域 → ~/.copilot/agents/" width="800"/>

**從簡單開始：** 先在專案資料夾建立一個 `*.agent.md` 檔案。滿意後再移到正式位置。

除了 agent 檔案，Copilot 也會自動讀取**專案層級指示檔案**，無需 `/agent`。詳見下方 [專案 Copilot 設定](#configuring-your-project-for-copilot) 介紹 `AGENTS.md`、`.instructions.md` 與 `/init`。

</details>

---

<a id="configuring-your-project-for-copilot"></a>
<details>
<summary><strong>專案 Copilot 設定</strong>－AGENTS.md、指示檔案與 /init 設定</summary>

## 專案 Copilot 設定

Agent 是你隨選的專家。**專案設定檔**則不同：Copilot 會在每次會話自動讀取，了解你的專案慣例、技術棧與規則。無需任何人執行 `/agent`，情境對所有協作者都自動啟用。

### 用 /init 快速設定

最快的方式是讓 Copilot 幫你產生設定檔：

```bash
copilot
> /init
```

Copilot 會掃描你的專案並建立專屬指示檔。你可以事後編輯。

### 指示檔案格式

| 檔案 | 作用範圍 | 備註 |
|------|-------|-------|
| `AGENTS.md` | 專案根目錄或子資料夾 | **跨平台標準**－Copilot 與其他 AI 助手皆支援 |
| `.github/copilot-instructions.md` | 專案 | GitHub Copilot 專用 |
| `.github/instructions/*.instructions.md` | 專案 | 更細緻、主題專屬指示 |
| `~/.copilot/instructions/**/*.instructions.md` | 使用者（所有專案） | 你的個人指示，適用於所有 repo |
| `CLAUDE.md`, `GEMINI.md` | 專案根目錄 | 為相容性而支援 |

> 🎯 **剛開始用？** 請用 `AGENTS.md` 來寫專案指示。其他格式可視需求日後再探索。

### AGENTS.md

`AGENTS.md` 是推薦格式。它是[開放標準](https://agents.md/)，可跨 Copilot 與其他 AI 程式工具使用。放在 repo 根目錄，Copilot 會自動讀取。本專案的 [AGENTS.md](../AGENTS.md) 就是實際範例。

典型的 `AGENTS.md` 會描述你的專案情境、程式風格、安全需求與測試標準。請依我們範例檔案格式撰寫。

### 自訂指示檔（.instructions.md）

若團隊想更細緻控管，可將指示拆分為主題專屬檔案。每個檔案聚焦一個主題，會自動套用：

```
.github/
└── instructions/
    ├── python-standards.instructions.md
    ├── security-checklist.instructions.md
    └── api-design.instructions.md
```

> 💡 **注意**：指示檔案支援任何語言。本例用 Python 配合課程專案，你也可為 TypeScript、Go、Rust 等技術建立類似檔案。

#### 用 `applyTo` 限定指示範圍

預設情況下，指示檔會套用到每次對話。若只想限定特定檔案型別，可在 YAML frontmatter（檔案最上方 `---` 之間的區塊）加上 `applyTo` 欄位：

```markdown
---
applyTo: "**/*.py"
---
# Python Standards
Always follow PEP 8 style conventions.
Use type hints in all function signatures.
```

有了 `applyTo: "**/*.py"`，Copilot 只會在你處理 Python 檔案時載入這份指示。Python 風格指示不會干擾 Dockerfile 或 SQL 查詢的對話。

常見模式如下：

| `applyTo` 值 | 何時套用 |
|---|---|
| `"**/*.py"` | 任何 Python 檔案 |
| `"**/*.{ts,tsx}"` | TypeScript 與 TSX 檔案 |
| `"tests/**"` | 任何 `tests/` 資料夾內檔案 |
| （無 frontmatter） | 每次對話－預設 |

> 💡 **提示**：請用引號包住萬用字元（如 `"**/*.py"`），以確保在所有作業系統與 shell 下都能正確解析。

#### 用 `@` 匯入其他檔案

你可以在 `AGENTS.md` 或任何指示檔內用 `@filepath` 語法引用其他檔案。Copilot 會自動展開並引入該檔案內容，讓主檔案保持精簡，細節則分散存放：

```markdown
<!-- AGENTS.md -->
# Project Instructions

@.github/instructions/python-standards.instructions.md
@.github/instructions/test-standards.instructions.md
```

當指示內容變多時，這很方便。把它們拆成專注檔案，再用單一 `AGENTS.md` 用 `@` 匯入即可。這個語法同樣適用於 `.github/copilot-instructions.md` 與其他指示檔。

> 💡 **提示**：用 `@` 匯入可讓多個指示檔共用同一份基礎規則。例如，你可以有一份 `@.github/instructions/shared-rules.md`，讓其他指示檔都能引用。

**尋找社群指示檔**：瀏覽 [github/awesome-copilot](https://github.com/github/awesome-copilot) 可找到 .NET、Angular、Azure、Python、Docker 等多種技術的現成指示檔。

### 關閉自訂指示

若你需要 Copilot 忽略所有專案專屬設定（例如除錯或比較行為時）：

```bash
copilot --no-custom-instructions
```

</details>

---

<a id="agent-file-reference"></a>
<details>
<summary><strong>Agent 檔案參考</strong>－YAML 屬性、工具別名與完整範例</summary>

## Agent 檔案參考

### 更完整的範例

你已看過[最小 agent 格式](#-add-your-agents)。這裡是一個更完整、使用 `tools` 屬性的範例。建立 `~/.copilot/agents/python-reviewer.agent.md`：

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
| `description` | **是** | agent 功能說明－協助 Copilot 理解何時建議使用 |
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
> ⚠️ **僅限 VS Code**：`model` 屬性（選擇 AI 模型）僅支援於 VS Code，不適用於 GitHub Copilot CLI。為跨平台 agent 檔案可安全包含，Copilot CLI 會自動忽略。

### 更多 agent 範本

> 💡 **新手注意**：下方範例為模板。**請依你的專案替換具體技術。** 重要的是 agent 的*結構*，不是範例裡的技術名稱。

本專案在 [.github/agents/](../.github/agents/) 資料夾內有完整範例：
- [hello-world.agent.md](../.github/agents/hello-world.agent.md)－最小範例，從這裡開始
- [python-reviewer.agent.md](../.github/agents/python-reviewer.agent.md)－Python 程式碼品質審查員
- [pytest-helper.agent.md](../.github/agents/pytest-helper.agent.md)－Pytest 測試專家

社群 agent 請見 [github/awesome-copilot](https://github.com/github/awesome-copilot)。

</details>

---

# 練習

<img src="../assets/practice.png" alt="溫馨桌面擺設，螢幕顯示程式碼、檯燈、咖啡杯與耳機，準備動手實作" width="800"/>

建立你自己的 agent，並實際體驗它們的運作。

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

**審查優先順序：**
1. 安全性漏洞
2. 效能問題
3. 維護性疑慮
4. 違反最佳實踐

**輸出格式：**
請以編號清單列出問題，並加上嚴重性標籤：
[CRITICAL]、[HIGH]、[MEDIUM]、[LOW]
EOF

# 建立文件撰寫 Agent
cat > .github/agents/documentor.agent.md << 'EOF'
---
name: documentor
description: 負責撰寫清晰且完整技術文件的技術寫手
---

# 文件撰寫 Agent

你是一位技術寫手，負責撰寫清晰的文件。

**文件標準：**
- 以一句話摘要開頭
- 包含使用範例
- 文件化參數與回傳值
- 註明任何注意事項或限制
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

### 主要挑戰：建立專業分工的 Agent 團隊

動手範例已建立 `reviewer` 與 `documentor` 兩個 Agent。現在請練習為另一個任務建立並使用 Agent —— 改善書籍應用程式的資料驗證：

1. 建立 3 個專為書籍應用程式設計的 Agent 檔案（`.agent.md`），每個 Agent 一個，放在 `.github/agents/` 目錄下
2. 你的 Agent：
   - **data-validator**：檢查 `data.json` 是否有遺漏或格式錯誤的資料（如作者為空、年份=0、缺少欄位）
   - **error-handler**：檢查 Python 程式碼的錯誤處理是否一致，並建議統一做法
   - **doc-writer**：產生或更新 docstring 與 README 內容
3. 對書籍應用程式分別使用每個 Agent：
   - `data-validator` → 稽核 `@samples/book-app-project/data.json`
   - `error-handler` → 審查 `@samples/book-app-project/books.py` 及 `@samples/book-app-project/utils.py`
   - `doc-writer` → 為 `@samples/book-app-project/books.py` 新增 docstring
4. 協作流程：先用 `error-handler` 找出錯誤處理缺口，再用 `doc-writer` 文件化改進後的做法

**成功標準**：你有 3 個可運作的 Agent，能產生一致且高品質的輸出，並可用 `/agent` 在它們之間切換。

<details>
<summary>💡 提示（點擊展開）</summary>

**起始範本**：每個 Agent 建立一個檔案，放在 `.github/agents/`：

`data-validator.agent.md`:
```markdown
---
description: 分析 JSON 資料檔案，找出遺漏或格式錯誤的項目
---

你負責分析 JSON 資料檔案，找出遺漏或格式錯誤的項目。

**重點檢查：**
- 作者欄位為空或缺少
- 無效年份（year=0、未來年份、負數年份）
- 缺少必要欄位（title、author、year、read）
- 重複項目
```

`error-handler.agent.md`:
```markdown
---
description: 檢查 Python 程式碼的錯誤處理一致性
---

你負責檢查 Python 程式碼的錯誤處理一致性。

**標準：**
- 不允許裸 except 子句
- 適當時使用自訂例外
- 所有檔案操作皆使用 context manager
- 成功／失敗的回傳型態一致
```

`doc-writer.agent.md`:
```markdown
---
description: 負責撰寫清晰 Python 文件的技術寫手
---

你是一位技術寫手，負責撰寫清晰的 Python 文件。

**標準：**
- 採用 Google 風格 docstring
- 包含參數型態與回傳值
- 為公開方法新增使用範例
- 註明會拋出的例外
```

**測試你的 Agent：**

> 💡 **注意：** 你應該已在本地複本的 repo 中有 `samples/book-app-project/data.json`。若缺少，請從原始 repo 下載：
> [data.json](https://github.com/github/copilot-cli-for-beginners/blob/main/samples/book-app-project/data.json)

```bash
copilot
> /agent
# 從清單中選擇 "data-validator"
> @samples/book-app-project/data.json 檢查書籍資料是否有作者為空或年份無效的項目
```

**提示：** YAML frontmatter 的 `description` 欄位是 Agent 能正常運作的必要條件。

</details>

### 加分挑戰：指令庫

你已建立可隨選啟用的 Agent。現在試試另一種方式：**指令檔案**，讓 Copilot 在每次會話自動讀取，無需 `/agent`。

請在 `.github/instructions/` 資料夾中建立至少 3 個指令檔案：
- `python-style.instructions.md`：強制執行 PEP 8 與型態提示慣例
- `test-standards.instructions.md`：強制測試檔案遵循 pytest 慣例
- `data-quality.instructions.md`：驗證 JSON 資料項目的品質

請在書籍應用程式程式碼上測試每個指令檔案。

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 會發生什麼事 | 修正方式 |
|------|--------------|----------|
| Agent frontmatter 缺少 `description` | Agent 無法載入或無法被發現 | 一定要在 YAML frontmatter 中加上 `description:` |
| Agent 檔案放錯位置 | 嘗試使用時找不到 Agent | 請放在 `~/.copilot/agents/`（個人）或 `.github/agents/`（專案） |
| 用 `.md` 而非 `.agent.md` | 可能無法被辨識為 Agent | 檔名請用 `python-reviewer.agent.md` 這種格式 |
| Agent 提示過長 | 可能超過 30,000 字元限制 | 保持 Agent 定義精簡，詳細指令請用 skill 實現 |

### 疑難排解

**找不到 Agent** —— 請確認 Agent 檔案存在於以下其中一個位置：
- `~/.copilot/agents/`
- `.github/agents/`

列出可用的 Agent：

```bash
copilot
> /agent
# 顯示所有可用 Agent
```

**Agent 未遵循指令** —— 請在提示中明確說明，並在 Agent 定義中加入更多細節：
- 指定框架／函式庫與版本
- 團隊慣例
- 範例程式碼模式

**自訂指令未載入** —— 在專案中執行 `/init` 以初始化專案指令：

```bash
copilot
> /init
```

或檢查是否被停用：
```bash
# 若要載入自訂指令，請勿加 --no-custom-instructions
copilot  # 預設會載入自訂指令
```

</details>

---

# 摘要

## 🔑 重點整理

1. **內建 Agent**：`/plan` 與 `/review` 可直接呼叫；Explore 與 Task 會自動運作
2. **自訂 Agent**：以 `.agent.md` 檔案定義專家角色
3. **優秀的 Agent**：具備明確專業、標準與輸出格式
4. **多 Agent 協作**：結合多種專業解決複雜問題
5. **指令檔案**（`.instructions.md`）：將團隊標準自動化應用
6. **一致輸出**：來自明確定義的 Agent 指令

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

Agent 會改變 *Copilot 處理與執行目標任務* 的方式。接下來你將學習 **skills** —— 它們決定 Copilot *採取哪些步驟*。想知道 Agent 與 Skill 有何不同？第五章會詳細說明。

在 **[第五章：Skills 系統](../05-skills/README.md)**，你將學到：

- 如何讓 skill 依據提示自動觸發（無需斜線指令）
- 安裝社群 skills
- 用 SKILL.md 檔案自訂 skill
- Agent、skill 與 MCP 的差異
- 何時該用哪一種

---

**[← 回到第三章](../03-development-workflows/README.md)** | **[繼續前往第五章 →](../05-skills/README.md)**
