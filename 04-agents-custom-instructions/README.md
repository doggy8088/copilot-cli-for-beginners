![第 04 章：Agent 與自訂指令](assets/chapter-header.png)

> **如果你能在一個工具裡聘請 Python 程式碼審查員、測試專家和安全性審查員，會怎麼樣？**

在第 03 章，你已經掌握了核心工作流程：程式碼審查、重構、除錯、測試產生，以及 git 整合。這些讓你在 GitHub Copilot CLI 上極具生產力。現在，讓我們更進一步。

到目前為止，你都是把 Copilot CLI 當作通用助手來使用。Agent 讓你能賦予它特定角色與內建標準，例如：強制型別提示與 PEP 8 的程式碼審查員，或是會撰寫 pytest 測試案例的測試助手。你將看到同一個提示詞，經由具備專業指令的 agent 處理後，結果明顯更好。

## 🎯 學習目標

完成本章後，你將能夠：

- 使用內建 agent：Plan（`/plan`）、Code-review（`/review`），並了解自動 agent（Explore、Task）
- 利用 agent 檔案（`.agent.md`）建立專業 agent
- 使用 agent 執行領域專屬任務
- 透過 `/agent` 與 `--agent` 在 agent 間切換
- 撰寫專案專屬標準的自訂指令檔案

> ⏱️ **預估時間**：約 55 分鐘（20 分鐘閱讀 + 35 分鐘實作）

---

## 🧩 真實世界比喻：聘請專家

當你需要房屋維修時，不會只找一個「萬事通」；你會找專業人士：

| 問題 | 專家 | 原因 |
|------|------|------|
| 水管漏水 | 水電工 | 熟悉水管法規，有專業工具 |
| 電線重拉 | 電工 | 了解安全規範，符合法規 |
| 新屋頂 | 屋頂工 | 熟悉材料，考量當地氣候 |

Agent 的運作方式也一樣。不要用通用 AI，而是用專注於特定任務、懂得正確流程的 agent。只需設定一次指令，之後每次需要該專業時都能重複使用：程式碼審查、測試、安全性、文件撰寫。

<img src="assets/hiring-specialists-analogy.png" alt="聘請專家比喻——就像你為房屋維修找專業工匠，AI agent 也專精於程式碼審查、測試、安全性、文件等特定任務" width="800" />

---

# 使用 Agent

立即開始使用內建與自訂 agent。

---

## *第一次接觸 Agent？* 從這裡開始！
從未用過或建立過 agent？這裡有你入門本課程所需的一切。

1. **馬上試用一個*內建* agent：**
   ```bash
   copilot
   > /plan Add input validation for book year in the book app
   ```
   這會呼叫 Plan agent，產生逐步實作計畫。

2. **看看我們的自訂 agent 範例之一：** 定義 agent 指令很簡單，參考我們提供的 [python-reviewer.agent.md](../.github/agents/python-reviewer.agent.md) 檔案即可了解模式。

3. **理解核心概念：** Agent 就像諮詢專家而非通才。「前端 agent」會自動專注於無障礙與元件模式，你不必每次提醒，因為 agent 指令裡已經規定好了。


## 內建 Agent

**你已經在第 03 章開發流程用過部分內建 agent！**
<br>`/plan` 和 `/review` 其實就是內建 agent。現在你知道背後發生了什麼。完整列表如下：

| Agent | 呼叫方式 | 功能說明 |
|-------|----------|----------|
| **Plan** | `/plan` 或 `Shift+Tab`（切換模式） | 在撰寫程式前產生逐步實作計畫 |
| **Code-review** | `/review` | 針對暫存／未暫存變更進行專注且可執行的回饋審查 |
| **Init** | `/init` | 產生專案設定檔（指令、agent） |
| **Explore** | *自動* | 當你要求 Copilot 探索或分析程式碼庫時內部使用 |
| **Task** | *自動* | 執行測試、建置、lint、安裝依賴等指令 |

<br>

**內建 agent 實際運作範例** - 呼叫 Plan、Code-review、Explore、Task

```bash
copilot

# 呼叫 Plan agent 產生實作計畫
> /plan Add input validation for book year in the book app

# 呼叫 Code-review agent 審查你的變更
> /review

# Explore 與 Task agent 會在相關情境自動呼叫：
> Run the test suite        # 使用 Task agent

> Explore how book data is loaded    # 使用 Explore agent
```

Task Agent 呢？它在幕後管理並追蹤進度，並以清晰格式回報：

| 結果 | 你看到的內容 |
|------|--------------|
| ✅ **成功** | 簡短摘要（如「全部 247 個測試通過」、「建置成功」） |
| ❌ **失敗** | 完整輸出（包含堆疊追蹤、編譯器錯誤、詳細日誌） |


> 📚 **官方文件**：[GitHub Copilot CLI Agents](https://docs.github.com/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-custom-agents)

---

# 將 Agent 加入 Copilot CLI

你可以輕鬆定義自己的 agent，納入工作流程！只需定義一次，隨時指派！

<img src="assets/using-agents.png" alt="四個彩色 AI 機器人並肩站立，各自持有不同工具，代表專業 agent 能力" width="800"/>

## 🗂️ 新增你的 agent 

Agent 檔案是副檔名為 `.agent.md` 的 Markdown 檔案。分為兩部分：YAML frontmatter（元資料）與 Markdown 指令。

> 💡 **第一次接觸 YAML frontmatter？** 它是檔案頂部一小段設定，用 `---` 包圍。YAML 就是 `key: value` 配對。其餘部分是一般 Markdown。

這是一個最簡的 agent 範例：

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

> 💡 **必填與選填**：`description` 欄位必填。其他如 `name`、`tools`、`model` 為選填。

## Agent 檔案放哪裡

| 位置 | 範圍 | 適用情境 |
|------|------|----------|
| `.github/agents/` | 專案專屬 | 團隊共享 agent，符合專案慣例 |
| `~/.copilot/agents/` | 全域（所有專案） | 個人常用 agent，隨處可用 |

**本專案已在 [.github/agents/](../.github/agents/) 資料夾提供範例 agent 檔案**。你可以自行撰寫或客製現有範例。

<details>
<summary>📂 查看本課程的範例 agent</summary>

| 檔案 | 說明 |
|------|------|
| `hello-world.agent.md` | 最簡範例——從這裡開始 |
| `python-reviewer.agent.md` | Python 程式碼品質審查員 |
| `pytest-helper.agent.md` | Pytest 測試專家 |

```bash
# 或複製到你的個人 agent 資料夾（所有專案皆可用）
cp .github/agents/python-reviewer.agent.md ~/.copilot/agents/
```

更多社群 agent，請參考 [github/awesome-copilot](https://github.com/github/awesome-copilot)

</details>


## 🚀 使用自訂 agent 的兩種方式

### 互動模式
在互動模式中，使用 `/agent` 列出 agent 並選擇要開始工作的 agent。
選擇 agent 後即可繼續對話。

```bash
copilot
> /agent
```

要切換到不同 agent，或回到預設模式，再次使用 `/agent` 指令即可。

### 程式化模式

直接以 agent 啟動新會話。

```bash
copilot --agent python-reviewer
> Review @samples/book-app-project/books.py
```

> 💡 **切換 agent**：隨時可用 `/agent` 或 `--agent` 切換到其他 agent。若要回到標準 Copilot CLI 體驗，使用 `/agent` 並選擇**無 agent**。

---

# 深入 Agent 的運作

<img src="assets/creating-custom-agents.png" alt="機器人在工作台上組裝，周圍有零件與工具，象徵自訂 agent 建立" width="800"/>

> 💡 **本節為選讀。** 內建 agent（`/plan`、`/review`）已足夠應付大多數工作流程。當你需要專業且一致應用的專家時，再建立自訂 agent。

以下每個主題都可獨立閱讀。**挑你有興趣的，不需一次讀完全部。**

| 我想要... | 跳到 |
|---|---|
| 看看 agent 為何優於通用提示詞 | [專家 vs 通用](#specialist-vs-generic-see-the-difference) |
| 在一個功能上結合多個 agent | [多 agent 協作](#working-with-multiple-agents) |
| 整理、命名、分享 agent | [Agent 組織與分享](#organizing--sharing-agents) |
| 設定專案永遠啟用的情境 | [Copilot 專案設定](#configuring-your-project-for-copilot) |
| 查詢 YAML 屬性與工具 | [Agent 檔案參考](#agent-file-reference) |

選擇下方情境展開閱讀。

---

<a id="specialist-vs-generic-see-the-difference"></a>
<details>
<summary><strong>專家 vs 通用：看見差異</strong> - 為何 agent 產生的結果比通用提示詞更好</summary>

## 專家 vs 通用：看見差異

這正是 agent 展現價值的地方。看看差異：

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

基本可用，但缺少很多細節。

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
- ✅ 詳細 docstring，含 Args/Returns/Raises
- ✅ 輸入驗證與正確錯誤處理
- ✅ 使用 list comprehension 提升效能
- ✅ 邊界情境處理（缺少／無效年份）
- ✅ PEP 8 格式化
- ✅ 防禦式程式設計

**差異**：同一個提示詞，輸出品質大幅提升。agent 帶來你可能忘記要求的專業。

</details>

---

<a id="working-with-multiple-agents"></a>
<details>
<summary><strong>多 agent 協作</strong> - 結合專家、會話中切換、agent 作為工具</summary>

## 多 agent 協作

真正的威力在於專家協同合作完成功能。

### 範例：建立一個簡單功能

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

# 綜合設計
> Create an implementation plan that includes the method implementation and comprehensive tests.
```

**關鍵洞見**：你是總設計師，指揮專家處理細節，你把握整體方向。

<details>
<summary>🎬 實際操作展示！</summary>

![Python Reviewer Demo](assets/python-reviewer-demo.gif)

*示範輸出會依模型、工具、回應而異，與此處展示不同。*

</details>

### Agent 作為工具

當 agent 設定完成後，Copilot 也能在複雜任務中自動呼叫 agent 作為工具。如果你要求全端功能，Copilot 可能會自動分派部分任務給適合的專業 agent。

</details>

---

<a id="organizing--sharing-agents"></a>
<details>
<summary><strong>Agent 組織與分享</strong> - 命名、檔案放置、指令檔、團隊共享</summary>

## Agent 組織與分享

### 命名你的 agent

建立 agent 檔案時，名稱很重要。這是你在 `/agent` 或 `--agent` 後輸入的名稱，也是團隊成員在 agent 清單中看到的。

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
- 需要時具體：`react-typescript` 而非單純 `frontend`

---

### 團隊共享

將 agent 檔案放在 `.github/agents/`，即可納入版本控制。推到 repo，所有團隊成員自動取得。但 agent 只是 Copilot 讀取的其中一種檔案。Copilot 也支援**指令檔**，自動套用於每次會話，無需任何人執行 `/agent`。

換個角度：agent 是你隨時召喚的專家，指令檔則是團隊永遠啟用的規則。

### 檔案放置位置

你已經知道兩個主要位置（見上方 [Agent 檔案放哪裡](#where-to-put-agent-files)）。用這個決策樹選擇：

<img src="assets/agent-file-placement-decision-tree.png" alt="Agent 檔案放置決策樹：實驗 → 當前資料夾，團隊使用 → .github/agents/，全域 → ~/.copilot/agents/" width="800"/>

**簡單開始：** 在專案資料夾建立一個 `*.agent.md` 檔案。滿意後再移到正式位置。

除了 agent 檔案，Copilot 也會自動讀取**專案層級指令檔**，無需 `/agent`。詳見下方 [Copilot 專案設定](#configuring-your-project-for-copilot) 的 `AGENTS.md`、`.instructions.md`、`/init`。

</details>

---

<a id="configuring-your-project-for-copilot"></a>
<details>
<summary><strong>Copilot 專案設定</strong> - AGENTS.md、指令檔、/init 設定</summary>

## Copilot 專案設定

Agent 是你隨時召喚的專家。**專案設定檔**則不同：Copilot 會在每次會話自動讀取，了解你的專案慣例、技術棧、規則。無需任何人執行 `/agent`，所有 repo 成員都能自動啟用情境。

### 用 /init 快速設定

最快的方式是讓 Copilot 自動產生設定檔：

```bash
copilot
> /init
```

Copilot 會掃描你的專案並產生專屬指令檔。你可以後續編輯。

### 指令檔格式

| 檔案 | 範圍 | 備註 |
|------|------|------|
| `AGENTS.md` | 專案根目錄或子資料夾 | **跨平台標準**——適用 Copilot 與其他 AI 助手 |
| `.github/copilot-instructions.md` | 專案 | GitHub Copilot 專用 |
| `.github/instructions/*.instructions.md` | 專案 | 細分主題的指令檔 |
| `~/.copilot/instructions/**/*.instructions.md` | 使用者（所有專案） | 個人指令，所有 repo 都適用 |
| `CLAUDE.md`, `GEMINI.md` | 專案根目錄 | 相容性支援 |

> 🎯 **剛開始？** 用 `AGENTS.md` 撰寫專案指令。其他格式可視需求再探索。

### AGENTS.md

`AGENTS.md` 是推薦格式。它是[開放標準](https://agents.md/)，可跨 Copilot 與其他 AI 程式工具使用。放在 repo 根目錄，Copilot 會自動讀取。本專案的 [AGENTS.md](../AGENTS.md) 就是實際範例。

典型的 `AGENTS.md` 會描述專案情境、程式碼風格、安全需求、測試標準。依照我們範例檔案模式撰寫即可。

### 自訂指令檔（.instructions.md）

團隊若需更細緻控制，可將指令拆分為主題檔案。每個檔案涵蓋一項規範，自動套用：

```
.github/
└── instructions/
    ├── python-standards.instructions.md
    ├── security-checklist.instructions.md
    └── api-design.instructions.md
```

> 💡 **注意**：指令檔適用任何語言。此例用 Python 配合課程專案，你也可為 TypeScript、Go、Rust 等技術建立類似檔案。

#### 用 `applyTo` 限定指令適用範圍

預設指令檔適用所有會話。若要限定特定檔案型態，可在 YAML frontmatter（檔案頂部 `---` 之間）加上 `applyTo` 欄位：

```markdown
---
applyTo: "**/*.py"
---
# Python Standards
Always follow PEP 8 style conventions.
Use type hints in all function signatures.
```

有了 `applyTo: "**/*.py"`，Copilot 只會在你處理 Python 檔案時載入該指令檔。Python 風格指令不會干擾 Dockerfile 或 SQL 查詢等會話。

常見模式如下：

| `applyTo` 值 | 套用時機 |
|---|---|
| `"**/*.py"` | 任一 Python 檔案 |
| `"**/*.{ts,tsx}"` | TypeScript 與 TSX 檔案 |
| `"tests/**"` | `tests/` 資料夾內所有檔案 |
|（無 frontmatter）| 所有會話——預設 |

> 💡 **提示**：將萬用字元模式用引號包住（如 `"**/*.py"`），確保在所有作業系統與 shell 都能正確解析。

**尋找社群指令檔**：瀏覽 [github/awesome-copilot](https://github.com/github/awesome-copilot) 可取得 .NET、Angular、Azure、Python、Docker 等多種技術的現成指令檔。

### 停用自訂指令

若需 Copilot 忽略所有專案專屬設定（適合除錯或比較行為）：

```bash
copilot --no-custom-instructions
```

</details>

---

<a id="agent-file-reference"></a>
<details>
<summary><strong>Agent 檔案參考</strong> - YAML 屬性、工具別名、完整範例</summary>

## Agent 檔案參考

### 更完整的範例

你已看過[最簡 agent 格式](#-add-your-agents)。這裡是更完整、使用 `tools` 屬性的 agent。建立 `~/.copilot/agents/python-reviewer.agent.md`：

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
| `tools` | 否 | 可用工具清單（省略＝全部工具可用）。見下方工具別名。 |
| `target` | 否 | 限定只用於 `vscode` 或 `github-copilot` |

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

> 💡 **新手注意**：以下範例為範本。**請依專案需求替換技術內容。**重點在 agent 結構，不在技術細節。

本專案在 [.github/agents/](../.github/agents/) 資料夾提供實際範例：
- [hello-world.agent.md](../.github/agents/hello-world.agent.md) - 最簡範例，適合入門
- [python-reviewer.agent.md](../.github/agents/python-reviewer.agent.md) - Python 程式碼品質審查員
- [pytest-helper.agent.md](../.github/agents/pytest-helper.agent.md) - Pytest 測試專家

社群 agent 請參考 [github/awesome-copilot](https://github.com/github/awesome-copilot)。

</details>

---

# 練習

<img src="../assets/practice.png" alt="溫暖的桌面擺設，螢幕顯示程式碼、檯燈、咖啡杯與耳機，準備實作練習" width="800"/>

建立自己的 agent，並實際操作看看。

---

## ▶️ 自己動手試試看

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

# 現在開始使用
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

### 主要挑戰：建立專業 agent 團隊

實作範例已建立 `reviewer` 與 `documentor` agent。現在請練習建立並使用 agent 執行另一項任務——提升書籍應用程式的資料驗證：1. 建立 3 個專為書籍應用程式設計的 agent 檔案（`.agent.md`），每個 agent 一個檔案，放置於 `.github/agents/`
2. 你的 agents：
   - **data-validator**：檢查 `data.json` 是否有缺漏或格式錯誤的資料（作者為空、year=0、缺少欄位）
   - **error-handler**：檢查 Python 程式碼的錯誤處理是否一致，並提出統一的處理方式建議
   - **doc-writer**：產生或更新 docstring 與 README 內容
3. 在書籍應用程式中使用每個 agent：
   - `data-validator` → 審查 `@samples/book-app-project/data.json`
   - `error-handler` → 檢查 `@samples/book-app-project/books.py` 和 `@samples/book-app-project/utils.py`
   - `doc-writer` → 為 `@samples/book-app-project/books.py` 增加 docstring
4. 協作：先用 `error-handler` 找出錯誤處理的缺口，再用 `doc-writer` 記錄改進後的處理方式

**成功標準**：你擁有 3 個可用的 agent，能產出一致且高品質的結果，並可透過 `/agent` 切換使用。

<details>
<summary>💡 提示（點擊展開）</summary>

**起始範本**：在 `.github/agents/` 中為每個 agent 建立一個檔案：

`data-validator.agent.md`:
```markdown
---
description: 分析 JSON 資料檔案，找出缺漏或格式錯誤的項目
---

你會分析 JSON 資料檔案，找出缺漏或格式錯誤的項目。

**重點檢查：**
- 作者欄位為空或缺漏
- 年份無效（year=0、未來年份、負數年份）
- 必要欄位缺漏（title、author、year、read）
- 重複項目
```

`error-handler.agent.md`:
```markdown
---
description: 審查 Python 程式碼的錯誤處理一致性
---

你會審查 Python 程式碼的錯誤處理一致性。

**標準：**
- 不使用裸 except 子句
- 適當時使用自訂例外
- 所有檔案操作皆使用 context manager
- 成功／失敗回傳型別一致
```

`doc-writer.agent.md`:
```markdown
---
description: 為 Python 撰寫清晰技術文件的技術寫手
---

你是一位技術寫手，負責撰寫清晰的 Python 技術文件。

**標準：**
- Google 風格 docstring
- 包含參數型別與回傳值
- 為公開方法加入使用範例
- 註明會拋出的例外狀況
```

**測試你的 agents：**

> 💡 **注意：** 你應該已在本地複製的 repo 中有 `samples/book-app-project/data.json`。如果缺少，請從原始 repo 下載：
> [data.json](https://github.com/github/copilot-cli-for-beginners/blob/main/samples/book-app-project/data.json)

```bash
copilot
> /agent
# 從清單中選擇 "data-validator"
> @samples/book-app-project/data.json 檢查書籍是否有作者欄位為空或年份無效
```

**提示：** YAML frontmatter 的 `description` 欄位是 agent 必須的。

</details>

### 加分挑戰：指令庫

你已建立可隨選啟用的 agent。現在嘗試另一種方式：**指令檔案**，讓 Copilot 在每次會話自動讀取，不需 `/agent`。

建立 `.github/instructions/` 資料夾，至少包含 3 個指令檔案：
- `python-style.instructions.md`：強制 PEP 8 與 type hint 規範
- `test-standards.instructions.md`：強制 pytest 測試檔案規範
- `data-quality.instructions.md`：驗證 JSON 資料項目品質

在書籍應用程式程式碼上測試每個指令檔案。

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生狀況 | 修正方式 |
|------|----------|----------|
| agent frontmatter 缺少 `description` | agent 無法載入或無法被發現 | YAML frontmatter 一定要包含 `description:` |
| agent 檔案位置錯誤 | agent 找不到，無法使用 | 放在 `~/.copilot/agents/`（個人）或 `.github/agents/`（專案） |
| 用 `.md` 而非 `.agent.md` | 檔案可能無法被識別為 agent | 檔名要像 `python-reviewer.agent.md` |
| agent 提示過長 | 可能超過 30,000 字元限制 | agent 定義要精簡，詳細指令用 skill 檔案 |

### 疑難排解

**agent 找不到** - 請確認 agent 檔案存在於以下位置之一：
- `~/.copilot/agents/`
- `.github/agents/`

列出所有可用 agent：

```bash
copilot
> /agent
# 顯示所有可用 agent
```

**agent 未遵循指令** - 請在提示中明確說明，並在 agent 定義中加入更多細節：
- 指定框架／函式庫與版本
- 團隊慣例
- 範例程式碼模式

**自訂指令未載入** - 在專案中執行 `/init` 設定專案指令：

```bash
copilot
> /init
```

或檢查是否被停用：
```bash
# 若要載入自訂指令，不要使用 --no-custom-instructions
copilot  # 預設會載入自訂指令
```

</details>

---

# 摘要

## 🔑 重點整理

1. **內建 agent**：`/plan` 和 `/review` 可直接呼叫；Explore 與 Task 會自動運作
2. **自訂 agent** 是專家角色，定義於 `.agent.md` 檔案中
3. **好的 agent** 有明確專業、標準與輸出格式
4. **多 agent 協作** 可結合專業解決複雜問題
5. **指令檔案**（`.instructions.md`）將團隊標準自動化應用
6. **一致輸出** 來自明確的 agent 指令定義

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

agent 改變了 *Copilot 如何針對你的程式碼採取精準行動*。接下來你將學習 **skills** ——它們改變 Copilot *執行哪些步驟*。想知道 agent 與 skill 有何不同？第 05 章會詳細說明。

在 **[第 05 章：Skills 系統](../05-skills/README.md)**，你將學到：

- 如何讓 skill 根據提示自動觸發（不需斜線指令）
- 安裝社群 skill
- 用 SKILL.md 檔案建立自訂 skill
- agent、skill 與 MCP 的差異
- 何時該用哪一種

---

**[← 回到第 03 章](../03-development-workflows/README.md)** | **[繼續前往第 05 章 →](../05-skills/README.md)**
