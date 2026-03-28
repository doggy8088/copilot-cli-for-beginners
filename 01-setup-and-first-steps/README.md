![Chapter 01: First Steps](images/chapter-header.png)

> **觀看 AI 如何即時找出錯誤、解釋難懂的程式碼，並產生可運作的腳本。接著學習三種不同的 GitHub Copilot CLI 使用方式。**

這一章就是魔法的開始！你將親身體驗為什麼開發者會形容 GitHub Copilot CLI 就像隨時能請教的資深工程師。你會看到 AI 在幾秒內找出安全性漏洞、用簡單易懂的英文解釋複雜程式碼，並即時產生可運作的腳本。然後你會學會三種互動模式（互動模式、規劃模式、程式化模式），讓你知道在任何任務下該用哪一種。

> ⚠️ **前置準備**：請先完成 **[第 00 章：快速開始](../00-quick-start/README.md)**。你需要安裝並驗證 GitHub Copilot CLI，才能執行下方的示範。

## 🎯 學習目標

完成本章後，你將能夠：

- 透過實作示範，體驗 GitHub Copilot CLI 帶來的生產力提升
- 根據任務選擇正確的模式（互動、規劃或程式化）
- 使用斜線指令控制你的對話

> ⏱️ **預估時間**：約 45 分鐘（閱讀 15 分鐘 + 實作 30 分鐘）

---

# 你的第一個 Copilot CLI 體驗

<img src="images/first-copilot-experience.png" alt="Developer sitting at a desk with code on the monitor and glowing particles representing AI assistance" width="800"/>

直接開始，看看 Copilot CLI 能做些什麼。

---

## 先暖身：你的第一個提示詞

在進入精彩的示範之前，先從一些簡單的提示詞開始，這些你現在就能嘗試。**不需要任何程式碼庫**！只要打開終端機並啟動 Copilot CLI：

```bash
copilot
```

試試這些新手友善的提示詞：

```
> Explain what a dataclass is in Python in simple terms

> Write a function that sorts a list of dictionaries by a specific key

> What's the difference between a list and a tuple in Python?

> Give me 5 best practices for writing clean Python code
```

不用 Python 也沒關係！只要問你想用的語言相關問題即可。

你會發現這種互動很自然。就像和同事對話一樣提問。探索完畢後，輸入 `/exit` 離開對話。

**關鍵重點**：GitHub Copilot CLI 是對話式的。你不需要特殊語法，只要用簡單英文提問即可。

## 實際看看

現在來看看為什麼開發者會說這就像「隨時請教資深工程師」。

> 📖 **閱讀範例說明**：以 `>` 開頭的行是你在互動式 Copilot CLI 對話中輸入的提示詞。沒有 `>` 前綴的行則是你在終端機執行的指令。

> 💡 **關於範例輸出**：本課程中的範例輸出僅供參考。由於 Copilot CLI 每次回應都可能不同，你看到的內容在措辭、格式和細節上會有所差異。請專注於回傳資訊的「類型」，而非完全一樣的文字。

### 示範 1：幾秒內完成程式碼審查

本課程提供了帶有刻意程式碼品質問題的範例檔案。如果你在本機操作且尚未複製課程專案，請執行下方 `git clone` 指令，進入 `copilot-cli-for-beginners` 資料夾，然後啟動 `copilot`。

```bash
# 如果你在本機操作且尚未複製課程專案
git clone https://github.com/github/copilot-cli-for-beginners
cd copilot-cli-for-beginners

# 啟動 Copilot
copilot
```

進入互動式 Copilot CLI 對話後，執行下列指令：

```
> Review @samples/book-app-project/book_app.py for code quality issues and suggest improvements
```

> 💡 **`@` 符號是做什麼的？** `@` 符號告訴 Copilot CLI 讀取某個檔案。你會在第 02 章學到詳細內容。現在只要照著輸入即可。

---

<details>
<summary>🎬 實際操作畫面</summary>

![Code Review Demo](images/code-review-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容可能與此不同。*

</details>

---

**重點**：專業的程式碼審查只需幾秒。人工審查……肯定花更久！

---

### 示範 2：解釋難懂的程式碼

是否曾經盯著程式碼發呆，不知道它在做什麼？在 Copilot CLI 對話中試試這個：

```
> Explain what @samples/book-app-project/books.py does in simple terms
```

---

<details>
<summary>🎬 實際操作畫面</summary>

![Explain Code Demo](images/explain-code-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容可能與此不同。*

</details>

---

**會發生什麼事**：（你的輸出會不同）Copilot CLI 會讀取檔案、理解程式碼，並用簡單英文解釋。

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

**重點**：複雜的程式碼也能像有耐心的導師一樣解釋給你聽。

---

### 示範 3：產生可運作的程式碼

需要一個你本來要花 15 分鐘 Google 的函式？繼續在對話中輸入：

```
> Write a Python function that takes a list of books and returns statistics: 
  total count, number read, number unread, oldest and newest book
```

---

<details>
<summary>🎬 實際操作畫面</summary>

![Generate Code Demo](images/generate-code-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容可能與此不同。*

</details>

---

**會發生什麼事**：幾秒內產生一個完整、可用的函式，你可以直接複製、貼上、執行。

探索完畢後，離開對話：

```
> /exit
```

**重點**：即時滿足，而且全程都在同一個連貫的對話中。

---

# 模式與指令

<img src="images/modes-and-commands.png" alt="Futuristic control panel with glowing screens, dials, and equalizers representing Copilot CLI modes and commands" width="800"/>

你剛剛已經看到 Copilot CLI 能做什麼。現在來了解*如何*有效運用這些能力。關鍵在於知道三種互動模式該在什麼情境下使用。

> 💡 **注意**：Copilot CLI 也有一種 **自動駕駛（Autopilot）** 模式，可以自動執行任務而不等待你的輸入。這很強大，但需要授予完整權限，並會自動使用高級請求。本課程聚焦於下方三種模式。等你熟悉基本操作後，我們會再介紹自動駕駛模式。

---

## 🧩 真實世界比喻：外出用餐

把使用 GitHub Copilot CLI 想像成外出用餐。從規劃行程到點餐，不同情境適合不同方式：

| 模式 | 用餐比喻 | 何時使用 |
|------|----------|----------|
| **規劃（Plan）** | 用 GPS 規劃去餐廳的路線 | 複雜任務——先規劃路線、檢查停靠點、同意計畫再出發 |
| **互動（Interactive）** | 和服務生對話 | 探索與反覆調整——提問、客製化、即時回饋 |
| **程式化（Programmatic）** | 得來速點餐 | 快速、明確的任務——留在原本環境，迅速取得結果 |

就像外出用餐一樣，你會自然學會什麼情境該用哪種方式。

<img src="images/ordering-food-analogy.png" alt="Three Ways to Use GitHub Copilot CLI - Plan Mode (GPS route to restaurant), Interactive Mode (talking to waiter), Programmatic Mode (drive-through)" width="800"/>

*根據任務選擇模式：規劃模式適合先規劃，互動模式適合來回討論，程式化模式適合快速一次性結果*

### 我應該從哪個模式開始？

**建議從互動模式開始。** 
- 你可以自由嘗試、追問
- 情境會隨對話自然累積
- 出錯時用 `/clear` 很容易重來

熟悉後可以嘗試：
- **程式化模式**（`copilot -p "<你的提示詞>"`）適合快速、單次提問
- **規劃模式**（`/plan`）適合需要先詳細規劃再寫程式的情境

---

## 三種模式介紹

### 模式一：互動模式（建議起手式）

<img src="images/interactive-mode.png" alt="Interactive Mode - Like talking to a waiter who can answer questions and adjust the order" width="250"/>

**最適合**：探索、反覆調整、多輪對話。就像和服務生對話，可以即時提問、回饋、調整。

啟動互動式對話：

```bash
copilot
```

如同前面所見，會出現一個提示符讓你自然輸入。想查詢可用指令，只要輸入：

```
> /help
```

**關鍵重點**：互動模式會保留情境。每則訊息都會建立在前一則之上，就像真實對話。

#### 互動模式範例

```bash
copilot

> Review @samples/book-app-project/utils.py and suggest improvements

> Add type hints to all functions

> Make the error handling more robust

> /exit
```

注意每個提示詞都建立在前一個回答之上。你是在進行一場對話，而不是每次都從頭開始。

---

### 模式二：規劃模式

<img src="images/plan-mode.png" alt="Plan Mode - Like planning a route before a trip using GPS" width="250"/>

**最適合**：需要在執行前先檢查流程的複雜任務。就像出發前用 GPS 規劃路線。

規劃模式會協助你在寫程式前，先產生逐步計畫。使用 `/plan` 指令或按 **Shift+Tab** 切換到規劃模式：

> 💡 **小技巧**：**Shift+Tab** 可在模式間切換：互動 → 規劃 → 自動駕駛。任何時候都可在互動對話中按下切換，不用輸入指令。

```bash
copilot

> /plan Add a "mark as read" command to the book app
```

**規劃模式輸出範例**：（你的結果可能不同）

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

**關鍵重點**：規劃模式讓你在寫程式前先檢查、調整流程。規劃完成後，還能請 Copilot CLI 把計畫存成檔案，例如「Save this plan to `mark_as_read_plan.md`」就會建立一份詳細計畫的 markdown 檔。

> 💡 **想挑戰更複雜的嗎？** 試試：`/plan Add search and filter capabilities to the book app`。規劃模式可從簡單功能一路擴展到完整應用程式。

> 📚 **自動駕駛模式**：你可能注意到 Shift+Tab 會切到第三種模式「自動駕駛」。在自動駕駛模式下，Copilot 會自動執行整個計畫，不會在每個步驟等你回應——就像把任務交給同事並說「做完再告訴我」。典型流程是規劃 → 接受 → 自動駕駛，所以你得先會寫計畫。建議先熟悉互動與規劃模式，再參考 [官方文件](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot)。

---

### 模式三：程式化模式

<img src="images/programmatic-mode.png" alt="Programmatic Mode - Like using a drive-through for a quick order" width="250"/>

**最適合**：自動化、腳本、CI/CD、單次指令。就像得來速點餐，不用和服務生互動。

用 `-p` 旗標執行一次性、不需互動的指令：

```bash
# 產生程式碼
copilot -p "Write a function that checks if a number is even or odd"

# 快速查詢
copilot -p "How do I read a JSON file in Python?"
```

**關鍵重點**：程式化模式給你快速答案並結束。不會有對話，只有輸入 → 輸出。

<details>
<summary>📚 <strong>進階：在腳本中使用程式化模式</strong>（點擊展開）</summary>

熟悉後，你可以在 shell 腳本中用 `-p`：

```bash
#!/bin/bash

# 自動產生提交訊息
COMMIT_MSG=$(copilot -p "Generate a commit message for: $(git diff --staged)")
git commit -m "$COMMIT_MSG"

# 審查檔案
copilot --allow-all -p "Review @myfile.py for issues"
```
> ⚠️ **關於 `--allow-all`**：這個旗標會略過所有權限提示，讓 Copilot CLI 可直接讀取檔案、執行指令、存取網址。這對程式化模式（`-p`）很重要，因為沒有互動對話可確認。只在你自己寫的提示詞、信任的目錄下使用 `--allow-all`。不要用在不信任的輸入或敏感目錄。

</details>

---

## 必備斜線指令

這些指令適用於互動模式。**先記住這六個**——就能涵蓋 90% 的日常需求：

| 指令 | 功能說明 | 何時使用 |
|------|----------|----------|
| `/help` | 顯示所有可用指令 | 忘記指令時 |
| `/clear` | 清除對話，重新開始 | 換主題時 |
| `/plan` | 寫程式前先規劃 | 複雜功能時 |
| `/research` | 用 GitHub 與網路資源做深入研究 | 需要先調查主題時 |
| `/model` | 顯示或切換 AI 模型 | 想換 AI 模型時 |
| `/exit` | 結束對話 | 完成時 |

這樣就能順利開始！熟悉後可再探索更多指令。

> 📚 **官方文件**：[CLI 指令參考](https://docs.github.com/copilot/reference/cli-command-reference) 可查詢完整指令與旗標列表。

<details>
<summary>📚 <strong>進階指令</strong>（點擊展開）</summary>

> 💡 上述必備指令已涵蓋大部分日常需求。這份參考表方便你進一步探索。

### Agent 環境

| 指令 | 功能說明 |
|------|----------|
| `/init` | 初始化 Copilot 指令給你的程式庫 |
| `/agent` | 瀏覽並選擇可用的 Agent |
| `/skills` | 管理技能以增強能力 |
| `/mcp` | 管理 MCP 伺服器設定 |

> 💡 技能會在 [第 05 章](../05-skills/README.md) 詳細介紹。MCP 伺服器則在 [第 06 章](../06-mcp-servers/README.md) 說明。

### 模型與子代理

| 指令 | 功能說明 |
|------|----------|
| `/model` | 顯示或切換 AI 模型 |
| `/delegate` | 任務交給 GitHub 上的 Copilot 程式代理（雲端 agent） |
| `/fleet` | 將複雜任務拆分為平行子任務，加速完成 |
| `/tasks` | 檢視背景子代理與分離的 shell 對話 |

### 程式碼

| 指令 | 功能說明 |
|------|----------|
| `/diff` | 檢查目前目錄的變更 |
| `/pr` | 操作目前分支的 pull request |
| `/review` | 執行程式碼審查 agent 分析變更 |
| `/research` | 用 GitHub 與網路資源做深入研究 |
| `/terminal-setup` | 啟用多行輸入（shift+enter、ctrl+enter） |

### 權限

| 指令 | 功能說明 |
|------|----------|
| `/allow-all` | 本次對話自動同意所有權限提示 |
| `/add-dir <directory>` | 將目錄加入允許清單 |
| `/list-dirs` | 顯示所有允許的目錄 |
| `/cwd`, `/cd [directory]` | 檢視或切換工作目錄 |

> ⚠️ **請小心使用**：`/allow-all` 會略過確認提示。適合信任的專案，但遇到不信任的程式碼要特別小心。

### 對話

| 指令 | 功能說明 |
|------|----------|
| `/resume` | 切換到其他對話（可選 session ID） |
| `/rename` | 重新命名目前對話 |
| `/context` | 顯示情境視窗的 token 使用量與視覺化 |
| `/usage` | 顯示對話使用統計 |
| `/session` | 顯示對話資訊與工作區摘要 |
| `/compact` | 摘要對話內容以減少情境用量 |
| `/share` | 匯出對話為 markdown 檔或 GitHub gist |

### 說明與回饋

| 指令 | 功能說明 |
|------|----------|
| `/help` | 顯示所有可用指令 |
| `/changelog` | 顯示 CLI 版本更新紀錄 |
| `/feedback` | 提交回饋給 GitHub |
| `/theme` | 檢視或設定終端機主題 |

### 快速 Shell 指令

在提示詞前加上 `!` 可直接執行 shell 指令，不經 AI 處理：

```bash
copilot

> !git status
# 直接執行 git status，不經 AI

> !python -m pytest tests/
# 直接執行 pytest
```

### 切換模型

Copilot CLI 支援多種 AI 模型（OpenAI、Anthropic、Google 等）。你可用的模型取決於訂閱等級與地區。用 `/model` 查看選項並切換：

```bash
copilot
> /model

# 顯示可用模型並讓你選擇。選擇 Sonnet 4.5。
```

> 💡 **小技巧**：有些模型會消耗更多「高級請求」。標註 **1x**（如 Claude Sonnet 4.5）的模型很適合當預設，效能佳又省額度。倍率較高的模型會更快用完高級配額，建議留給真正需要時再用。

</details>

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

是時候實際動手練習了！

---

## ▶️ 自己試試看

### 互動式探索

啟動 Copilot，並用追問方式反覆優化書籍應用程式：

```bash
copilot

> Review @samples/book-app-project/book_app.py - what could be improved?

> Refactor the if/elif chain into a more maintainable structure

> Add type hints to all the handler functions

> /exit
```

### 規劃一個功能

用 `/plan` 讓 Copilot CLI 在寫程式前先規劃實作方式：

```bash
copilot

> /plan Add a search feature to the book app that can find books by title or author

# 檢查規劃
# 同意或修改
# 觀察它一步步實作
```

### 用程式化模式自動化

`-p` 旗標讓你直接在終端機執行 Copilot CLI，不需進入互動模式。從專案根目錄複製下方腳本到終端機（不是 Copilot 內），即可批次審查書籍應用程式的所有 Python 檔案。

```bash
# 審查書籍應用程式所有 Python 檔案
for file in samples/book-app-project/*.py; do
  echo "Reviewing $file..."
  copilot --allow-all -p "Quick code quality review of @$file - critical issues only"
done
```

**PowerShell（Windows）：**

```powershell
# 審查書籍應用程式所有 Python 檔案
Get-ChildItem samples/book-app-project/*.py | ForEach-Object {
  $relativePath = "samples/book-app-project/$($_.Name)";
  Write-Host "Reviewing $relativePath...";
  copilot --allow-all -p "Quick code quality review of @$relativePath - critical issues only" 
}
```

---

完成示範後，試試這些變化：

1. **互動挑戰**：啟動 `copilot` 並探索書籍應用程式。詢問 `@samples/book-app-project/books.py`，連續請求三次改進建議。
2. **規劃模式挑戰**：執行 `/plan Add rating and review features to the book app`。仔細閱讀規劃，是否合理？
3. **程式化挑戰**：執行 `copilot --allow-all -p "List all functions in @samples/book-app-project/book_app.py and describe what each does"`。第一次就成功嗎？

---

## 📝 作業

### 主要挑戰：優化書籍應用程式工具函式

前面實作聚焦在 `book_app.py` 的審查與重構。現在請用同樣技巧練習另一個檔案 `utils.py`：

1. 啟動互動式對話：`copilot`
2. 請 Copilot CLI 摘要檔案內容：`@samples/book-app-project/utils.py What does each function in this file do?`
3. 請它加上輸入驗證：「Add validation to `get_user_choice()` so it handles empty input and non-numeric entries」
4. 請它改善錯誤處理：「What happens if `get_book_details()` receives an empty string for the title? Add guards for that.」
5. 請它加上 docstring：「Add a comprehensive docstring to `get_book_details()` with parameter descriptions and return values」
6. 觀察情境如何在提示詞間傳遞。每次改進都建立在前一次之上
7. 用 `/exit` 離開

**成功標準**：你應該會得到一份經過輸入驗證、錯誤處理與 docstring 強化的 `utils.py`，而且全程透過多輪對話完成。

<details>
<summary>💡 提示（點擊展開）</summary>

**可嘗試的範例提示詞：**
```bash
> @samples/book-app-project/utils.py What does each function in this file do?
> Add validation to get_user_choice() so it handles empty input and non-numeric entries
> What happens if get_book_details() receives an empty string for the title? Add guards for that.
> Add a comprehensive docstring to get_book_details() with parameter descriptions and return values
```

**常見問題：**
- 如果 Copilot CLI 反問你細節，只要自然回答即可
- 情境會自動累積，每個提示詞都會延續前面的內容
- 想重來就用 `/clear`

</details>

### 進階挑戰：比較三種模式

範例中用 `/plan` 實作搜尋功能、用 `-p` 批次審查。現在請針對新增 `list_by_year()` 方法到 `BookCollection` 類別這個新任務，三種模式都試一次：

1. **互動**：`copilot` → 請它一步步設計並實作該方法
2. **規劃**：`/plan Add a list_by_year(start, end) method to BookCollection that filters books by publication year range`
3. **程式化**：`copilot --allow-all -p "@samples/book-app-project/books.py Add a list_by_year(start, end) method that returns books published between start and end year inclusive"`

**反思**：哪種模式最順手？什麼情境會用哪一種？

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 會發生什麼事 | 解法 |
|------|--------------|------|
| 輸入 `exit` 而非 `/exit` | Copilot CLI 會把 "exit" 當成提示詞，不是指令 | 斜線指令都要 `/` 開頭 |
| 用 `-p` 進行多輪對話 | 每次 `-p` 都是獨立的，不會記憶前一次內容 | 需要多輪對話請用互動模式（`copilot`） |
| 忘記用引號包住含 `$` 或 `!` 的提示詞 | Shell 會先解析特殊字元，Copilot CLI 收不到 | 用引號包住提示詞：`copilot -p "What does $HOME mean?"` |

### 疑難排解

**"Model not available"** - 你的訂閱可能不含所有模型。用 `/model` 查看可用選項。

**"Context too long"** - 對話已用滿情境視窗。用 `/clear` 重設，或開新對話。

**"Rate limit exceeded"** - 請稍候幾分鐘再試。批次作業可考慮用程式化模式並加延遲。

</details>

---

# 小結

## 🔑 重要重點
1. **互動模式** 適合用來探索與反覆嘗試——情境會持續保留。這就像和一個會記得你之前說過什麼的人對話。
2. **規劃模式** 通常用於較複雜的任務。實作前先檢查規劃內容。
3. **程式化模式** 適合自動化流程。不需要互動。
4. **四個基本指令**（`/help`、`/clear`、`/plan`、`/exit`）涵蓋了大多數日常需求。

> 📋 **快速參考**：完整指令與快捷鍵清單請參見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 接下來

現在你已經了解三種模式，接下來讓我們學習如何讓 Copilot CLI 取得你的程式碼情境。

在 **[第 02 章：情境與對話](../02-context-conversations/README.md)**，你將會學到：

- 使用 `@` 語法參照檔案與目錄
- 使用 `--resume` 和 `--continue` 進行工作階段管理
- 為什麼情境管理讓 Copilot CLI 如此強大

---

**[← 回到課程首頁](../README.md)** | **[繼續前往第 02 章 →](../02-context-conversations/README.md)**
