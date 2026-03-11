![Chapter 01: First Steps](images/chapter-header.png)

> **看著 AI 瞬間找出 bug、解釋令人困惑的程式碼、生成可執行的腳本，然後學習使用 GitHub Copilot CLI 的三種不同方式。**

魔法從這章開始！你將親身體驗為何開發者形容 GitHub Copilot CLI 是「隨時待命的資深工程師」。你將看著 AI 在幾秒內找出安全漏洞、用白話文解釋複雜程式碼、即時生成可執行腳本。接著你將掌握三種互動模式（互動模式、計畫模式和程式化模式），確切知道每種情境該用哪種模式。

> ⚠️ **前置需求**：請先完成 **[第 00 章：快速開始](../00-quick-start/README.md)**。執行以下示範前，你需要已安裝並完成驗證的 GitHub Copilot CLI。

## 🎯 學習目標

完成本章後，你將能夠：

- 透過實作示範，親身體驗 GitHub Copilot CLI 帶來的生產力提升
- 針對任何任務選擇正確的模式（互動模式、計畫模式或程式化模式）
- 使用斜線指令控制你的工作階段

> ⏱️ **預估時間**：約 45 分鐘（閱讀 15 分鐘 + 實作 30 分鐘）

---

# 你的第一次 Copilot CLI 體驗

<img src="images/first-copilot-experience.png" alt="Developer sitting at a desk with code on the monitor and glowing particles representing AI assistance" width="800"/>

直接上手，看看 Copilot CLI 能做什麼。

---

## 暖身：你的第一批提示

在進入精彩示範之前，先試試幾個可以立刻上手的簡單提示。**完全不需要程式碼儲存庫**！只需開啟終端機並啟動 Copilot CLI：

```bash
copilot
```

試試這些適合初學者的提示：

```
> Explain what a dataclass is in Python in simple terms

> Write a function that sorts a list of dictionaries by a specific key

> What's the difference between a list and a tuple in Python?

> Give me 5 best practices for writing clean Python code
```

不用 Python？沒關係！換成你熟悉的程式語言來提問。

感受一下這有多自然——就像和同事說話一樣提問即可。探索完畢後，輸入 `/exit` 離開工作階段。

**核心洞察**：GitHub Copilot CLI 是對話式的，不需要特殊語法就能上手，用白話文提問即可。

## 看看實際效果

現在讓我們看看為何開發者稱這是「隨時待命的資深工程師」。

> 📖 **閱讀範例說明**：以 `>` 開頭的行是你在互動式 Copilot CLI 工作階段內輸入的提示；不帶 `>` 前綴的行則是你在終端機執行的 shell 指令。

> 💡 **關於範例輸出**：本課程中展示的範例輸出僅供參考。由於 Copilot CLI 的每次回應都會有所不同，你的結果在措辭、格式和細節上都可能不同。請專注於回傳的*資訊類型*，而非精確的文字內容。

### 示範一：幾秒內完成程式碼審查

本課程包含含有刻意設計之程式碼品質問題的範例檔案，讓我們來審查其中一個：

```bash
# 若在本機工作且尚未複製，請先 clone 課程儲存庫
git clone https://github.com/github/copilot-cli-for-beginners
cd copilot-cli-for-beginners

# 啟動 Copilot
copilot
```

進入互動式工作階段後：

```
> Review @samples/book-app-project/book_app.py for code quality issues and suggest improvements
```

> 💡 **`@` 是什麼？** `@` 符號告訴 Copilot CLI 讀取某個檔案。你將在第 02 章學到所有相關細節。現在只需照著指令複製貼上即可。

---

<details>
<summary>🎬 看看實際效果！</summary>

<img src="images/code-review-demo.gif" alt="Code Review Demo">

<em>示範輸出僅供參考，你的模型、工具與回應內容可能與此不同。</em>

</details>

---

**重點整理**：幾秒鐘完成一次專業程式碼審查。手動審查要花……嗯，比這久多了！

---

### 示範二：解釋令人困惑的程式碼

曾盯著程式碼卻不知道它在做什麼嗎？在你的 Copilot CLI 工作階段中試試：

```
> Explain what @samples/book-app-project/books.py does in simple terms
```

---

<details>
<summary>🎬 看看實際效果！</summary>

<img src="images/explain-code-demo.gif" alt="Explain Code Demo">

<em>示範輸出僅供參考，你的模型、工具與回應內容可能與此不同。</em>

</details>

---

**實際發生的事**：（你的輸出會有所不同）Copilot CLI 讀取檔案、理解程式碼，並以白話文說明。

```
This is a book collection management module using Python dataclasses.

Think of it like a digital bookshelf:
- Book is a dataclass - a simple way to store book information (title, author, year, read status)
- BookCollection manages the entire collection and handles saving/loading

Key components:

1. @dataclass decorator (line 8)
   - Automatically creates __init__, __repr__, etc.
   - Clean way to define data structures in Python

2. BookCollection class (line 16)
   - Maintains a list of Book objects
   - Handles persistence with JSON file I/O
   - load_books() reads from data.json
   - save_books() writes to data.json using asdict()

3. Book operations:
   - add_book() - creates and saves new books
   - find_book_by_title() - searches collection
   - mark_as_read() - updates read status
   - find_by_author() - filters by author name

Common pattern: Read from JSON → Work with Python objects → Write back to JSON
```

**重點整理**：複雜的程式碼被解釋得就像一位有耐心的導師在說明。

---

### 示範三：生成可執行的程式碼

需要一個否則要花 15 分鐘 Google 的函式？繼續在工作階段中操作：

```
> Write a Python function that takes a list of books and returns statistics: 
  total count, number read, number unread, oldest and newest book
```

---

<details>
<summary>🎬 看看實際效果！</summary>

<img src="images/generate-code-demo.gif" alt="Generate Code Demo">

<em>示範輸出僅供參考，你的模型、工具與回應內容可能與此不同。</em>

</details>

---

**實際發生的事**：幾秒鐘內生成完整可執行的函式，複製貼上即可使用。

探索完畢後，離開工作階段：

```
> /exit
```

**重點整理**：即時獲得成果，而且整個過程都在同一個連續工作階段中完成。

---

# 模式與指令

<img src="images/modes-and-commands.png" alt="Futuristic control panel with glowing screens, dials, and equalizers representing Copilot CLI modes and commands" width="800"/>

你已經看到 Copilot CLI 能做什麼了。現在讓我們理解*如何*有效運用這些能力。關鍵在於知道三種互動模式各自適用於哪些情境。

> 💡 **備註**：Copilot CLI 還有一種 **Autopilot** 模式，可以不等待你的輸入自行完成任務。它非常強大，但需要授予完整權限，且會自主消耗高級請求配額。本課程聚焦於以下三種模式。等你熟悉基礎後，我們會引導你了解 Autopilot。

---

## 🧩 現實生活類比：外出用餐

把使用 GitHub Copilot CLI 想像成外出用餐。從規劃行程到點餐，不同情境需要不同的方式：

| 模式 | 用餐類比 | 適用時機 |
|------|---------|---------|
| **計畫模式** | 前往餐廳的 GPS 導航 | 複雜任務——規劃路線、確認停靠點、同意計畫，然後出發 |
| **互動模式** | 與服務員交談 | 探索與迭代——提問、客製化、即時獲得回饋 |
| **程式化模式** | 得來速點餐 | 快速、明確的任務——留在自己的環境中，快速取得結果 |

就像外出用餐一樣，你會自然地學會各種方式的適用時機。

<img src="images/ordering-food-analogy.png" alt="Three Ways to Use GitHub Copilot CLI - Plan Mode (GPS route to restaurant), Interactive Mode (talking to waiter), Programmatic Mode (drive-through)" width="800"/>

*依任務選擇模式：計畫模式用於先規劃再行動，互動模式用於來回協作，程式化模式用於快速一次性取得結果*

### 我該從哪個模式開始？

**從互動模式開始。**
- 你可以實驗並追問後續問題
- 透過對話自然累積上下文
- 用 `/clear` 輕鬆修正錯誤

熟悉後，再嘗試：
- **程式化模式**（`copilot -p "<你的提示>"`）用於快速一次性問題
- **計畫模式**（`/plan`）用於在寫程式前需要更詳細規劃的情境

---

## 三種模式

### 模式一：互動模式（從這裡開始）

<img src="images/interactive-mode.png" alt="Interactive Mode - Like talking to a waiter who can answer questions and adjust the order" width="250"/>

**最適合**：探索、迭代、多輪對話。就像與服務員交談——他能回答問題、接受意見、隨時調整訂單。

啟動互動式工作階段：

```bash
copilot
```

如你目前所見，會出現一個提示符讓你自然輸入。若想查看可用指令，只需輸入：

```
> /help
```

**核心洞察**：互動模式會保持上下文，每條訊息都建立在前一條之上，就像真實的對話。

#### 互動模式範例

```bash
copilot

> Review @samples/book-app-project/utils.py and suggest improvements

> Add type hints to all functions

> Make the error handling more robust

> /exit
```

注意每個提示如何建立在前一個答案上。你在進行對話，而不是每次都重新開始。

---

### 模式二：計畫模式

<img src="images/plan-mode.png" alt="Plan Mode - Like planning a route before a trip using GPS" width="250"/>

**最適合**：你想在執行前先審視方法的複雜任務。類似於旅行前用 GPS 規劃路線。

計畫模式幫助你在撰寫任何程式碼前建立逐步計畫。使用 `/plan` 指令或按 **Shift+Tab** 切換至計畫模式：

> 💡 **提示**：**Shift+Tab** 循環切換模式：互動模式 → 計畫模式 → Autopilot。在互動式工作階段中隨時按下，即可無需輸入指令直接切換模式。

```bash
copilot

> /plan Add a "mark as read" command to the book app
```

**計畫模式輸出：**（你的輸出可能不同）

```
📋 Implementation Plan

Step 1: Update the command handler in book_app.py
  - Add new elif branch for "mark" command
  - Create handle_mark_as_read() function

Step 2: Implement the handler function
  - Prompt user for book title
  - Call collection.mark_as_read(title)
  - Display success/failure message

Step 3: Update help text
  - Add "mark" to available commands list
  - Document the command usage

Step 4: Test the flow
  - Add a book
  - Mark it as read
  - Verify status changes in list output

Proceed with implementation? [Y/n]
```

**核心洞察**：計畫模式讓你在寫任何程式碼之前先審視並修改方法。計畫完成後，你甚至可以告訴 Copilot CLI 將其儲存為檔案以供後續參考。例如，「Save this plan to `mark_as_read_plan.md`」會建立一個包含計畫詳情的 Markdown 檔案。

> 💡 **想試試更複雜的？** 試試：`/plan Add search and filter capabilities to the book app`。計畫模式從簡單功能到完整應用程式都能勝任。

> 📚 **Autopilot 模式**：你可能注意到 Shift+Tab 會循環到第三種叫做 **Autopilot** 的模式。在 Autopilot 模式中，Copilot 會執行整個計畫，每個步驟完成後無需等待你的輸入——就像把任務交給同事並說「完成後告訴我」。典型工作流程是計畫 → 接受 → Autopilot，這意味著你需要先擅長撰寫計畫。先熟悉互動模式和計畫模式，準備好後再查看[官方文件](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot)。

---

### 模式三：程式化模式

<img src="images/programmatic-mode.png" alt="Programmatic Mode - Like using a drive-through for a quick order" width="250"/>

**最適合**：自動化、腳本、CI/CD、一次性指令。就像使用得來速快速點餐，無需與服務員交談。

使用 `-p` 旗標執行不需要互動的一次性指令：

```bash
# 生成程式碼
copilot -p "Write a function that checks if a number is even or odd"

# 快速取得說明
copilot -p "How do I read a JSON file in Python?"
```

**核心洞察**：程式化模式給你一個快速答案然後退出。沒有對話，只有輸入 → 輸出。

<details markdown="1">
<summary>📚 <strong>進階應用：在腳本中使用程式化模式</strong>（點擊展開）</summary>

熟悉後，你可以在 shell 腳本中使用 `-p`：

```bash
#!/bin/bash

# 自動生成提交訊息
COMMIT_MSG=$(copilot -p "Generate a commit message for: $(git diff --staged)")
git commit -m "$COMMIT_MSG"

# 審查檔案
copilot --allow-all -p "Review @myfile.py for issues"
```
> ⚠️ **關於 `--allow-all`**：此旗標會跳過所有權限提示，讓 Copilot CLI 無需確認即可讀取檔案、執行指令和存取 URL。這在程式化模式（`-p`）中是必要的，因為沒有互動式工作階段可供核准操作。只在你自己撰寫的提示且在你信任的目錄中使用 `--allow-all`，切勿在不受信任的輸入或敏感目錄中使用。

</details>

---

## 基本斜線指令

這些指令在互動模式中使用。**先從以下四個開始**——它們涵蓋了 90% 的日常需求：

| 指令 | 功能 | 適用時機 |
|------|------|---------|
| `/help` | 顯示所有可用指令 | 忘記某個指令時 |
| `/clear` | 清除對話並重新開始 | 切換話題時 |
| `/plan` | 在寫程式前先規劃工作 | 處理較複雜的功能時 |
| `/research` | 使用 GitHub 和網路來源深度調查 | 需要在寫程式前先研究某個主題時 |
| `/model` | 顯示或切換 AI 模型 | 想更換 AI 模型時 |
| `/exit` | 結束工作階段 | 完成工作時 |

入門部分到此為止！隨著你越來越熟練，可以繼續探索更多指令。

> 📚 **官方文件**：[CLI 指令參考](https://docs.github.com/copilot/reference/cli-command-reference) — 取得完整指令與旗標列表。

<details markdown="1">
<summary>📚 <strong>更多指令</strong>（點擊展開）</summary>

> 💡 以上五個指令涵蓋了大部分的日常使用。這份參考資料在你準備好深入探索時隨時可用。

### Agent 環境

| 指令 | 功能 |
|------|------|
| `/init` | 為你的儲存庫初始化 Copilot 指示 |
| `/agent` | 瀏覽並選擇可用的 agent |
| `/skills` | 管理用於強化能力的 skill |
| `/mcp` | 管理 MCP server 設定 |

> 💡 Skill 在[第 05 章](../05-skills/README.md)詳細介紹。MCP server 在[第 06 章](../06-mcp-servers/README.md)介紹。

### 模型與子 Agent

| 指令 | 功能 |
|------|------|
| `/model` | 顯示或切換 AI 模型 |
| `/delegate` | 將任務移交給 GitHub 上的 Copilot 編程 agent（雲端 agent） |
| `/fleet` | 將複雜任務拆分為平行子任務以加快完成速度 |
| `/tasks` | 檢視背景子 agent 和已分離的 shell 工作階段 |

### 程式碼

| 指令 | 功能 |
|------|------|
| `/diff` | 審查目前目錄中的變更 |
| `/review` | 執行程式碼審查 agent 分析變更 |
| `/research` | 使用 GitHub 和網路來源執行深度調查 |
| `/terminal-setup` | 啟用多行輸入支援（shift+enter 和 ctrl+enter） |

### 權限

| 指令 | 功能 |
|------|------|
| `/allow-all` | 本工作階段自動核准所有權限提示 |
| `/add-dir <directory>` | 將目錄加入允許清單 |
| `/list-dirs` | 顯示所有允許的目錄 |
| `/cwd`、`/cd [directory]` | 檢視或變更工作目錄 |

> ⚠️ **謹慎使用**：`/allow-all` 會跳過確認提示。對於可信任的專案很方便，但面對不信任的程式碼時請小心。

### 工作階段

| 指令 | 功能 |
|------|------|
| `/resume` | 切換到其他工作階段（可選擇指定工作階段 ID） |
| `/rename` | 重新命名目前的工作階段 |
| `/context` | 顯示上下文視窗的 token 使用量與視覺化 |
| `/usage` | 顯示工作階段使用量指標與統計 |
| `/session` | 顯示工作階段資訊與工作區摘要 |
| `/compact` | 摘要對話以減少上下文使用量 |
| `/share` | 將工作階段匯出為 Markdown 檔案或 GitHub gist |

### 說明與回饋

| 指令 | 功能 |
|------|------|
| `/help` | 顯示所有可用指令 |
| `/changelog` | 顯示 CLI 各版本的更新日誌 |
| `/feedback` | 向 GitHub 提交回饋 |
| `/theme` | 檢視或設定終端機主題 |

### 快速 Shell 指令

在提示前加上 `!` 可直接執行 shell 指令，跳過 AI：

```bash
copilot

> !git status
# 直接執行 git status，不經過 AI

> !python -m pytest tests/
# 直接執行 pytest
```

### 切換模型

Copilot CLI 支援來自 OpenAI、Anthropic、Google 等多家廠商的 AI 模型。可用模型依你的訂閱等級和地區而異。使用 `/model` 查看選項並在模型間切換：

```bash
copilot
> /model

# 顯示可用模型並讓你選擇。選擇 Sonnet 4.5。
```

> 💡 **提示**：部分模型消耗的「高級請求」比其他模型多。標示 **1x** 的模型（如 Claude Sonnet 4.5）是絕佳的預設選擇——能力強且效率高。倍數較高的模型會更快消耗你的高級請求配額，請留待真正需要時再使用。

</details>

---

# 實作練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

是時候將所學付諸實踐了。

---

## ▶️ 自行嘗試

### 互動式探索

啟動 Copilot 並使用後續提示逐步改善書籍應用程式：

```bash
copilot

> Review @samples/book-app-project/book_app.py - what could be improved?

> Refactor the if/elif chain into a more maintainable structure

> Add type hints to all the handler functions

> /exit
```

### 規劃一個功能

使用 `/plan` 讓 Copilot CLI 在撰寫任何程式碼前先規劃實作方案：

```bash
copilot

> /plan Add a search feature to the book app that can find books by title or author

# 審查計畫
# 核准或修改
# 看著它一步步實作
```

### 使用程式化模式自動化

`-p` 旗標讓你直接從終端機執行 Copilot CLI，無需進入互動模式。從儲存庫根目錄將以下腳本複製貼上到終端機（不是在 Copilot 內部），以審查書籍應用程式中所有 Python 檔案。

```bash
# 審查書籍應用程式中所有 Python 檔案
for file in samples/book-app-project/*.py; do
  echo "Reviewing $file..."
  copilot --allow-all -p "Quick code quality review of @$file - critical issues only"
done
```

**PowerShell（Windows）：**

```powershell
# 審查書籍應用程式中所有 Python 檔案
Get-ChildItem samples/book-app-project/*.py | ForEach-Object {
  $relativePath = "samples/book-app-project/$($_.Name)";
  Write-Host "Reviewing $relativePath...";
  copilot --allow-all -p "Quick code quality review of @$relativePath - critical issues only" 
}
```

---

完成示範後，試試這些變化：

1. **互動挑戰**：啟動 `copilot` 並探索書籍應用程式。詢問 `@samples/book-app-project/books.py` 並連續請求改善 3 次。

2. **計畫模式挑戰**：執行 `/plan Add rating and review features to the book app`。仔細閱讀計畫，它合理嗎？

3. **程式化挑戰**：執行 `copilot --allow-all -p "List all functions in @samples/book-app-project/book_app.py and describe what each does"`。第一次就成功了嗎？

---

## 📝 作業

### 主要挑戰：改善書籍應用程式工具函式

實作範例專注於審查和重構 `book_app.py`。現在對另一個檔案 `utils.py` 練習相同的技能：

1. 啟動互動式工作階段：`copilot`
2. 請 Copilot CLI 摘要這個檔案：`@samples/book-app-project/utils.py What does each function in this file do?`
3. 請它加入輸入驗證：「Add validation to `get_user_choice()` so it handles empty input and non-numeric entries」
4. 請它改善錯誤處理：「What happens if `get_book_details()` receives an empty string for the title? Add guards for that.」
5. 請它加入 docstring：「Add a comprehensive docstring to `get_book_details()` with parameter descriptions and return values」
6. 觀察上下文如何在提示之間延續。每次改善都建立在上一次的基礎上
7. 以 `/exit` 離開

**成功標準**：你應該得到一個改善後的 `utils.py`，包含輸入驗證、錯誤處理和 docstring，全部透過多輪對話完成。

<details markdown="1">
<summary>💡 提示（點擊展開）</summary>

**可嘗試的範例提示：**
```bash
> @samples/book-app-project/utils.py What does each function in this file do?
> Add validation to get_user_choice() so it handles empty input and non-numeric entries
> What happens if get_book_details() receives an empty string for the title? Add guards for that.
> Add a comprehensive docstring to get_book_details() with parameter descriptions and return values
```

**常見問題：**
- 若 Copilot CLI 提出澄清問題，直接自然地回答即可
- 上下文會延續，所以每個提示都建立在上一個的基礎上
- 若想重新開始，使用 `/clear`

</details>

### 加分挑戰：比較三種模式

範例中用 `/plan` 處理搜尋功能，用 `-p` 批次審查。現在對一個全新任務嘗試全部三種模式：為 `BookCollection` 類別新增 `list_by_year()` 方法：

1. **互動模式**：`copilot` → 請它一步步設計並建立該方法
2. **計畫模式**：`/plan Add a list_by_year(start, end) method to BookCollection that filters books by publication year range`
3. **程式化模式**：`copilot --allow-all -p "@samples/book-app-project/books.py Add a list_by_year(start, end) method that returns books published between start and end year inclusive"`

**省思**：哪種模式感覺最自然？你會在什麼時候選用各種模式？

---

<details markdown="1">
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生的事 | 解決方式 |
|------|---------|---------|
| 輸入 `exit` 而非 `/exit` | Copilot CLI 將「exit」視為提示，而非指令 | 斜線指令必須以 `/` 開頭 |
| 用 `-p` 進行多輪對話 | 每次 `-p` 呼叫都是獨立的，沒有先前呼叫的記憶 | 需要建立上下文的對話請使用互動模式（`copilot`） |
| 提示中含有 `$` 或 `!` 時忘記加引號 | Shell 在 Copilot CLI 看到之前就解譯了特殊字元 | 將提示用引號包圍：`copilot -p "What does $HOME mean?"` |

### 疑難排解

**「Model not available」** - 你的訂閱可能未包含所有模型。使用 `/model` 查看可用項目。

**「Context too long」** - 你的對話已使用完整的上下文視窗。使用 `/clear` 重置，或開始新工作階段。

**「Rate limit exceeded」** - 等幾分鐘後再試。考慮在批次操作中使用程式化模式並加入延遲。

</details>

---

# 摘要

## 🔑 重點整理

1. **互動模式**適合探索和迭代——上下文持續延續，就像與記住你說過的話的人對話。
2. **計畫模式**通常用於較複雜的任務，實作前先審查。
3. **程式化模式**用於自動化，無需互動。
4. **四個基本指令**（`/help`、`/clear`、`/plan`、`/exit`）涵蓋大部分的日常使用。

> 📋 **快速參考**：查看 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference) 以取得完整指令與快捷鍵列表。

---

## ➡️ 接下來

現在你已了解三種模式，讓我們學習如何為 Copilot CLI 提供程式碼的上下文。

在**[第 02 章：上下文與對話](../02-context-conversations/README.md)**中，你將學習：

- 用於參照檔案和目錄的 `@` 語法
- 以 `--resume` 和 `--continue` 管理工作階段
- 上下文管理如何讓 Copilot CLI 真正發揮威力

---

**[← 回到課程首頁](../README.md)** | **[繼續前往第 02 章 →](../02-context-conversations/README.md)**
