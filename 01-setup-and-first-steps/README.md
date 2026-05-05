![Chapter 01: First Steps](images/chapter-header.png)

> **觀看 AI 如何即時找出錯誤、解釋難懂的程式碼，並產生可執行的腳本。接著學習三種使用 GitHub Copilot CLI 的方式。**

這一章就是魔法的起點！你將親身體驗為什麼開發者形容 GitHub Copilot CLI 就像有一位資深工程師隨傳隨到。你會看到 AI 在幾秒內找出安全性漏洞、用簡單易懂的語言解釋複雜程式碼，並立即產生可執行的腳本。然後你會學會三種互動模式（互動模式、規劃模式、程式化模式），讓你能針對不同任務選擇最適合的方式。

> ⚠️ **先備條件**：請先完成 **[Chapter 00: Quick Start](../00-quick-start/README.md)**。你必須已安裝並驗證 GitHub Copilot CLI，才能執行下方的示範。

## 🎯 學習目標

完成本章後，你將能夠：

- 透過實作示範，體驗 GitHub Copilot CLI 帶來的生產力提升
- 依任務選擇正確的模式（互動、規劃或程式化）
- 使用斜線指令控制你的對話

> ⏱️ **預估時間**：約 45 分鐘（閱讀 15 分鐘 + 實作 30 分鐘）

---

# 你的第一次 Copilot CLI 體驗

<img src="images/first-copilot-experience.png" alt="Developer sitting at a desk with code on the monitor and glowing particles representing AI assistance" width="800"/>

立刻動手，看看 Copilot CLI 能做些什麼。

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

不用 Python？沒問題！直接問你想要的程式語言相關問題即可。

你會發現這種互動很自然。就像問同事一樣提問。探索完畢後，輸入 `/exit` 離開對話。

**關鍵重點**：GitHub Copilot CLI 是對話式的。你不需要特殊語法，只要用自然語言提問即可。

## 實際看看 Copilot CLI 的威力

現在來看看為什麼開發者說這就像「有資深工程師隨傳隨到」。

> 📖 **閱讀範例說明**：以 `>` 開頭的行是你在互動式 Copilot CLI 對話中輸入的提示詞。沒有 `>` 前綴的行則是你在終端機執行的 shell 指令。

> 💡 **關於範例輸出**：本課程中的範例輸出僅供參考。由於 Copilot CLI 每次回應都可能不同，你看到的文字、格式和細節都會有所差異。請著重於回傳「資訊的類型」，而非完全一樣的內容。

### 示範 1：幾秒內完成程式碼審查

本課程包含有意設計程式碼品質問題的範例檔案。如果你在本機操作且尚未 clone 程式庫，請執行下方 `git clone` 指令，進入 `copilot-cli-for-beginners` 資料夾，然後啟動 copilot。

```bash
# 如果你在本機操作且尚未 clone，請先下載課程程式庫
git clone https://github.com/github/copilot-cli-for-beginners
cd copilot-cli-for-beginners

# 啟動 Copilot
copilot
```

進入互動式 Copilot CLI 對話後，執行以下指令：

```
> Review @samples/book-app-project/book_app.py for code quality issues and suggest improvements
```

> 💡 **`@` 符號是做什麼用的？** `@` 代表讓 Copilot CLI 讀取一個檔案。你會在第 02 章詳細學到這個用法。現在只要照抄指令即可。

---

<details>
<summary>🎬 實際操作畫面</summary>

![Code Review Demo](images/code-review-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容可能與這裡顯示的不同。*

</details>

---

**重點**：專業的程式碼審查只需幾秒。人工審查……肯定要花更多時間！

---

### 示範 2：解釋難懂的程式碼

是否曾經盯著一段程式碼發呆，不知道它在做什麼？在 Copilot CLI 對話中試試這個：

```
> Explain what @samples/book-app-project/books.py does in simple terms
```

---

<details>
<summary>🎬 實際操作畫面</summary>

![Explain Code Demo](images/explain-code-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容可能與這裡顯示的不同。*

</details>

---

**發生了什麼事**：（你的輸出會不同）Copilot CLI 讀取檔案、理解程式碼，並用簡單易懂的語言解釋。

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

**重點**：複雜的程式碼也能像有耐心的導師一樣，為你詳細解釋。

---

### 示範 3：產生可執行的程式碼

需要一個你本來要花 15 分鐘 Google 的函式？在同一個對話中繼續：

```
> Write a Python function that takes a list of books and returns statistics: 
  total count, number read, number unread, oldest and newest book
```

---

<details>
<summary>🎬 實際操作畫面</summary>

![Generate Code Demo](images/generate-code-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容可能與這裡顯示的不同。*

</details>

---

**發生了什麼事**：幾秒內產生完整可用的函式，直接複製貼上即可執行。

探索完畢後，離開對話：

```
> /exit
```

**重點**：即時滿足需求，而且全程都在同一個對話中完成。

---

# 模式與指令

<img src="images/modes-and-commands.png" alt="Futuristic control panel with glowing screens, dials, and equalizers representing Copilot CLI modes and commands" width="800"/>

你已經見識到 Copilot CLI 的強大功能。現在來了解該如何有效運用這些能力。關鍵在於知道三種互動模式該在什麼情境下使用。

> 💡 **注意**：Copilot CLI 也有一個 **自動駕駛（Autopilot）** 模式，可以自動執行任務而不需你逐步確認。這很強大，但需要授權完整權限，並會自動使用 premium 請求。本課程聚焦於下方三種模式。等你熟悉基本操作後，我們會再介紹 Autopilot。

---

## 🧩 真實世界比喻：外出用餐

把使用 GitHub Copilot CLI 想成外出用餐。從規劃行程到點餐，不同情境適合不同方式：

| 模式 | 用餐比喻 | 適用時機 |
|------|----------|----------|
| **Plan** | 用 GPS 規劃去餐廳的路線 | 複雜任務——先規劃路線、檢查停靠點、同意計畫，再出發 |
| **Interactive** | 和服務生對話 | 探索與反覆調整——隨時提問、客製化、即時回饋 |
| **Programmatic** | 得來速點餐 | 快速、明確的任務——留在原本環境，迅速取得結果 |

就像用餐一樣，你會自然學會什麼情境該用哪種方式。

<img src="images/ordering-food-analogy.png" alt="Three Ways to Use GitHub Copilot CLI - Plan Mode (GPS route to restaurant), Interactive Mode (talking to waiter), Programmatic Mode (drive-through)" width="800"/>

*依任務選擇模式：Plan 用於先規劃路線，Interactive 適合來回討論，Programmatic 適合快速一次到位的結果*

### 我該從哪個模式開始？

**建議從互動模式開始。** 
- 可以自由嘗試、追問
- 情境會隨對話自然累積
- 出錯時用 `/clear` 很容易重來

熟悉後可以嘗試：
- **程式化模式**（`copilot -p "<your prompt>"`）適合快速單次提問
- **規劃模式**（`/plan`）適合需要先詳細規劃再動手的情境

---

## 三種模式介紹

### 模式 1：互動模式（建議起手）

<img src="images/interactive-mode.png" alt="Interactive Mode - Like talking to a waiter who can answer questions and adjust the order" width="250"/>

**最適合**：探索、反覆調整、多輪對話。就像和服務生對話，可以隨時提問、給回饋、即時調整。

啟動互動式對話：

```bash
copilot
```

如同前面示範，你會看到一個提示符號，可以自然輸入內容。想查詢所有可用指令，只要輸入：

```
> /help
```

**關鍵重點**：互動模式會保留情境。每一則訊息都會建立在前一則之上，就像真實對話一樣。

#### 互動模式範例

```bash
copilot

> Review @samples/book-app-project/utils.py and suggest improvements

> Add type hints to all functions

> Make the error handling more robust

> /exit
```

注意每個提示詞都延續前一個回覆。你是在進行一場對話，而不是每次都從頭開始。

---

### 模式 2：規劃模式

<img src="images/plan-mode.png" alt="Plan Mode - Like planning a route before a trip using GPS" width="250"/>

**最適合**：複雜任務，需要在動手前先檢查整體做法。就像出發前用 GPS 規劃路線。

規劃模式會協助你在寫程式前，先產生逐步執行計畫。使用 `/plan` 指令，按下 **Shift+Tab** 可切換到規劃模式：

```bash
copilot

> /plan Add a "mark as read" command to the book app
```

> 💡 **小技巧**：**Shift+Tab** 可在模式間循環切換：互動 → 規劃 → 自動駕駛。任何時候都能在互動對話中切換，不用輸入指令。

你也可以用 `--plan` 旗標直接啟動規劃模式：

```bash
copilot --plan
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

**關鍵重點**：規劃模式讓你能在寫程式前先檢查、調整做法。計畫完成後，還能請 Copilot CLI 幫你存成檔案，例如「Save this plan to `mark_as_read_plan.md`」就會建立一份包含計畫內容的 markdown 檔案。

> 💡 **想挑戰更複雜的嗎？** 試試：`/plan Add search and filter capabilities to the book app`。規劃模式可從單一功能擴展到完整應用程式。

> 📚 **自動駕駛模式**：你可能注意到 Shift+Tab 會切到第三種模式「自動駕駛」。在自動駕駛模式下，Copilot 會自動執行整個計畫，不需你每步確認——就像把任務交給同事說「做完再告訴我」。典型流程是規劃 → 同意 → 自動駕駛，所以你得先會寫計畫。也可用 `copilot --autopilot` 直接啟動。建議先熟悉互動與規劃模式，再參考 [官方文件](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot)。

---

### 模式 3：程式化模式

<img src="images/programmatic-mode.png" alt="Programmatic Mode - Like using a drive-through for a quick order" width="250"/>

**最適合**：自動化、腳本、CI/CD、單次指令。就像得來速，快速下單不需和服務生對話。

用 `-p` 旗標執行一次性指令，不需互動：

```bash
# 產生程式碼
copilot -p "Write a function that checks if a number is even or odd"

# 快速查詢
copilot -p "How do I read a JSON file in Python?"
```

**關鍵重點**：程式化模式給你快速答案後就結束。沒有對話，只有輸入 → 輸出。

<details>
<summary>📚 <strong>進階：在腳本中使用程式化模式</strong>（點擊展開）</summary>

熟悉後，你可以在 shell 腳本中用 `-p`：

```bash
#!/bin/bash

# 自動產生 commit 訊息
COMMIT_MSG=$(copilot -p "Generate a commit message for: $(git diff --staged)")
git commit -m "$COMMIT_MSG"

# 審查檔案
copilot --allow-all -p "Review @myfile.py for issues"
```
> ⚠️ **關於 `--allow-all`**：這個旗標會略過所有權限提示，讓 Copilot CLI 可直接讀取檔案、執行指令、存取網址。這對程式化模式（`-p`）很重要，因為沒有互動對話可確認。只在你信任的目錄、自己寫的提示詞下使用 `--allow-all`。不要用在不信任的輸入或敏感目錄。

</details>

---

## 必備斜線指令

剛開始使用 Copilot CLI 時，建議先熟悉這些指令：

| 指令 | 功能說明 | 使用時機 |
|------|----------|----------|
| `/ask` | 提問不影響對話歷史 | 想快速問問題又不想影響目前任務時 |
| `/clear` | 清除對話，重新開始 | 換主題時 |
| `/help` | 顯示所有可用指令 | 忘記指令時 |
| `/model` | 顯示或切換 AI 模型 | 想換模型時 |
| `/plan` | 寫程式前先規劃 | 複雜功能時 |
| `/research` | 深入研究 GitHub 與網路資源 | 寫程式前需先調查主題時 |
| `/exit` | 結束對話 | 完成時 |

> 💡 **`/ask` 與一般對話的差異**：一般訊息都會成為後續對話的情境，影響未來回應。`/ask` 是「不留紀錄」的捷徑——很適合像 `/ask What does YAML mean?` 這種單次提問，不會污染你的對話情境。

> 💡 **Tab 自動補齊**：輸入斜線指令時，按 **Tab** 可自動補齊指令名稱，或在子指令與參數間循環。忘記指令時特別好用。

這些就是入門必備！熟悉後可以探索更多指令。

> 📚 **官方文件**：[CLI 指令參考](https://docs.github.com/copilot/reference/cli-command-reference) 可查詢完整指令與旗標列表。

<details>
<summary>📚 <strong>進階指令</strong>（點擊展開）</summary>

> 💡 上述必備指令已涵蓋日常大部分需求。這份參考適合你想進一步探索時查閱。

### Agent 環境

| 指令 | 功能說明 |
|------|----------|
| `/agent` | 瀏覽並選擇可用的 Agent |
| `/env` | 顯示已載入的環境細節——包含指令、MCP 伺服器、Skill、Agent、外掛等 |
| `/init` | 初始化 Copilot 指令至你的程式庫 |
| `/mcp` | 管理 MCP 伺服器設定 |
| `/skills` | 管理 Skill 以增強功能 |

> 💡 Agent 介紹請見 [第 04 章](../04-agents-custom-instructions/README.md)，Skill 介紹見 [第 05 章](../05-skills/README.md)，MCP 伺服器見 [第 06 章](../06-mcp-servers/README.md)。

### 模型與子 Agent

| 指令 | 功能說明 |
|------|----------|
| `/delegate` | 交辦任務給 GitHub Copilot 雲端 Agent |
| `/fleet` | 將複雜任務拆分為平行子任務，加速完成 |
| `/model` | 顯示或切換 AI 模型 |
| `/tasks` | 查看背景子 Agent 與分離的 shell 對話 |

### 程式碼

| 指令 | 功能說明 |
|------|----------|
| `/diff` | 檢查目前目錄的變更內容 |
| `/pr` | 操作目前分支的 Pull Request |
| `/research` | 使用 GitHub 與網路資源進行深度研究 |
| `/review` | 啟動程式碼審查 Agent 分析變更 |
| `/terminal-setup` | 啟用多行輸入支援（shift+enter 與 ctrl+enter） |

### 權限

| 指令 | 功能說明 |
|------|----------|
| `/add-dir <directory>` | 將目錄加入允許清單 |
| `/allow-all [on\|off\|show]` | 自動同意所有權限提示；用 `on` 啟用、`off` 關閉、`show` 查看狀態 |
| `/yolo` | `/allow-all on` 的快速別名——自動同意所有權限提示 |
| `/cwd`, `/cd [directory]` | 查看或切換工作目錄 |
| `/list-dirs` | 顯示所有允許的目錄 |

> ⚠️ **請小心使用**：`/allow-all` 與 `/yolo` 會略過確認提示。適合信任的專案，但對不信任的程式碼要特別小心。

### 對話

| 指令 | 功能說明 |
|------|----------|
| `/clear` | 放棄目前對話（不儲存歷史），重新開始 |
| `/compact` | 摘要對話內容，減少情境用量 |
| `/context` | 顯示情境視窗 Token 用量與視覺化 |
| `/keep-alive` | 防止 Copilot CLI 執行時系統進入睡眠——適合筆電長時間任務 |
| `/new` | 結束目前對話（儲存至歷史以便搜尋/繼續），並開始新對話 |
| `/resume` | 切換到其他對話（可指定對話 ID 或名稱） |
| `/rename` | 重新命名目前對話（不輸入名稱則自動產生） |
| `/rewind` | 開啟時間軸選擇器，回到對話任意早期狀態 |
| `/usage` | 顯示對話用量統計 |
| `/session` | 顯示對話資訊與工作區摘要；可用 `/session delete`、`/session delete <id>` 或 `/session delete-all` 刪除對話 |
| `/share` | 匯出對話為 markdown 檔、GitHub gist 或自含式 HTML 檔案 |

### 顯示

| 指令 | 功能說明 |
|------|----------|
| `/statusline`（或 `/footer`） | 自訂底部狀態列顯示項目（目錄、分支、努力值、情境視窗、配額） |
| `/theme` | 查看或設定終端機主題 |

### 說明與回饋

| 指令 | 功能說明 |
|------|----------|
| `/changelog` | 顯示 CLI 版本更新紀錄 |
| `/feedback` | 提交回饋給 GitHub |
| `/help` | 顯示所有可用指令 |

### 快速 Shell 指令

在 Copilot CLI 內直接執行 shell 指令（不經 AI），指令前加 `!`：

```bash
copilot

> !git status
# 直接執行 git status，不經 AI

> !python -m pytest tests/
# 直接執行 pytest
```

### 切換模型

Copilot CLI 支援多種 AI 模型（OpenAI、Anthropic、Google 等）。你可用 `/model` 查看可用模型並切換：

```bash
copilot
> /model

# 顯示可用模型並讓你選擇。選擇 Sonnet 4.5。
```

> 💡 **小技巧**：有些模型會消耗更多「premium 請求」。標記 **1x**（如 Claude Sonnet 4.5）的模型很適合預設使用，效能好又經濟。倍率較高的模型會更快用完配額，建議留給真正需要時再用。

> 💡 **不知道選哪個模型？** 選擇 **`Auto`** 讓 Copilot 自動為每次對話挑選最佳模型。剛開始用時這是很好的預設選項，無需煩惱模型選擇。

</details>

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

是時候把學到的內容實際操作一遍了。

---

## ▶️ 自己動手試試

### 互動式探索

啟動 Copilot，並用追問提示詞反覆改善書籍應用程式：

```bash
copilot

> Review @samples/book-app-project/book_app.py - what could be improved?

> Refactor the if/elif chain into a more maintainable structure

> Add type hints to all the handler functions

> /exit
```

### 規劃一個功能

用 `/plan` 讓 Copilot CLI 在寫程式前先幫你規劃實作步驟：

```bash
copilot

> /plan Add a search feature to the book app that can find books by title or author

# 檢查規劃內容
# 同意或修改
# 觀察逐步實作
```

### 用程式化模式自動化

`-p` 旗標讓你直接在終端機執行 Copilot CLI，不需進入互動模式。從程式庫根目錄複製下方腳本到終端機（不是 Copilot 內），即可審查書籍應用程式所有 Python 檔案。

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

1. **互動挑戰**：啟動 `copilot` 並探索書籍應用程式。詢問 `@samples/book-app-project/books.py`，並連續請求三次改善建議。
2. **規劃模式挑戰**：執行 `/plan Add rating and review features to the book app`。仔細閱讀規劃內容。合理嗎？
3. **程式化挑戰**：執行 `copilot --allow-all -p "List all functions in @samples/book-app-project/book_app.py and describe what each does"`。第一次就成功了嗎？

---

## 💡 小技巧：用網頁或手機遠端控制 CLI 對話

GitHub Copilot CLI 支援**遠端對話**，讓你能從網頁瀏覽器（桌機或手機）或 GitHub Mobile app 監控、互動進行中的 CLI 對話，而不必坐在終端機前。

用 `--remote` 旗標啟動遠端對話：

```bash
copilot --remote
```

Copilot CLI 會顯示一個連結並提供 QR code。用手機或桌機瀏覽器開啟連結，即可即時觀看對話、發送追問、檢查規劃、遠端操控 Agent。每個使用者只能存取自己的 Copilot CLI 對話。

你也可以在任何進行中的對話隨時啟用遠端存取：

```
> /remote
```

更多遠端對話細節請見 [Copilot CLI 文件](https://docs.github.com/copilot/how-tos/copilot-cli/steer-remotely)。

---

## 📝 作業

### 主要挑戰：改善書籍應用程式的工具程式（utils）

前面的實作範例聚焦在審查與重構 `book_app.py`。現在請你用同樣的技巧，練習處理另一個檔案 `utils.py`：1. 啟動互動式工作階段：`copilot`
2. 請 Copilot CLI 摘要這個檔案：「Summarize @samples/book-app-project/utils.py 並解釋這個檔案中每個函式的作用」
3. 請它加入輸入驗證：「Add validation to `get_user_choice()` so it handles empty input and non-numeric entries」
4. 請它改善錯誤處理：「What happens if `get_book_details()` receives an empty string for the title? Add guards for that.」
5. 請它補上說明文件：「Add a comprehensive docstring to `get_book_details()` with parameter descriptions and return values」
6. 觀察情境如何在多次提示間保留。每次改進都會建立在前一次的基礎上
7. 使用 `/exit` 離開

**成功標準**：你應該會得到一個改進過的 `utils.py`，具備輸入驗證、錯誤處理，以及說明文件，這些都是透過多輪對話逐步完成的。

<details>
<summary>💡 提示（點擊展開）</summary>

**可嘗試的範例提示：**
```bash
> @samples/book-app-project/utils.py What does each function in this file do?
> Add validation to get_user_choice() so it handles empty input and non-numeric entries
> What happens if get_book_details() receives an empty string for the title? Add guards for that.
> Add a comprehensive docstring to get_book_details() with parameter descriptions and return values
```

**常見問題：**
- 如果 Copilot CLI 需要你補充說明，只要自然回答即可
- 情境會持續累積，所以每個提示都會建立在前一次的基礎上
- 如果想重新開始，請使用 `/clear`

</details>

### 加分挑戰：比較三種模式

範例中使用 `/plan` 來設計搜尋功能，並用 `-p` 進行批次審查。現在請用三種模式完成一個新任務：為 `BookCollection` 類別新增 `list_by_year()` 方法：

1. **互動模式**：`copilot` → 請它一步步設計並實作這個方法
2. **計畫模式**：`/plan Add a list_by_year(start, end) method to BookCollection that filters books by publication year range`
3. **程式化模式**：`copilot --allow-all -p "@samples/book-app-project/books.py Add a list_by_year(start, end) method that returns books published between start and end year inclusive"`

**反思**：哪一種模式最自然？你會在什麼情境下使用哪一種？

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 結果 | 修正方式 |
|------|------|----------|
| 輸入 `exit` 而非 `/exit` | Copilot CLI 會把 "exit" 當成提示詞，而不是指令 | 斜線指令一律以 `/` 開頭 |
| 在多輪對話中使用 `-p` | 每次 `-p` 執行都是獨立的，無法記憶前文 | 需要情境累積時請用互動模式（`copilot`） |
| 忘記用引號包住含 `$` 或 `!` 的提示 | Shell 會先處理特殊字元，Copilot CLI 收不到完整內容 | 用引號包住提示：`copilot -p "What does $HOME mean?"` |
| 按一次 Esc 取消執行中的任務 | 現在按一次 Esc 不會中斷進行中的工作（避免誤觸） | 處理中時請按 **Esc 兩次** 取消 |

### 疑難排解

**"Model not available"** - 你的訂閱可能不包含所有模型。用 `/model` 查看可用清單。

**"Context too long"** - 你的對話已用滿情境窗口。請用 `/clear` 重設，或開啟新工作階段。

**"Rate limit exceeded"** - 請稍等幾分鐘再試。若需大量批次操作，可用程式化模式並加上延遲。

</details>

---

# 摘要

## 🔑 重要重點

1. **互動模式** 適合探索與反覆嘗試——情境會持續累積。就像和一個記得你說過什麼的夥伴對話。
2. **計畫模式** 通常用於較複雜的任務。會先檢查再執行。
3. **程式化模式** 適合自動化。無需互動。
4. **常用指令**（`/ask`、`/help`、`/clear`、`/plan`、`/research`、`/model`、`/exit`）涵蓋日常大多數需求。

> 📋 **快速參考**：完整指令與快捷鍵請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

現在你已經了解三種模式，接下來要學習如何讓 Copilot CLI 理解你的程式碼情境。

在 **[第 02 章：情境與對話](../02-context-conversations/README.md)**，你將學到：

- 用 `@` 語法引用檔案與目錄
- 用 `--resume` 和 `--continue` 管理工作階段
- 為什麼情境管理讓 Copilot CLI 如虎添翼

---

**[← 回課程首頁](../README.md)** | **[繼續前往第 02 章 →](../02-context-conversations/README.md)**
