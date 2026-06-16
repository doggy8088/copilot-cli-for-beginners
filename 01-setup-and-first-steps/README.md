![Chapter 01: First Steps](assets/chapter-header.png)

> **觀看 AI 如何即時找出錯誤、解釋令人困惑的程式碼，並產生可運作的腳本。接著學習三種使用 GitHub Copilot CLI 的方式。**

這一章就是魔法的起點！你將親身體驗為什麼開發者會形容 GitHub Copilot CLI 就像隨時能聯絡的資深工程師。你會看到 AI 在幾秒內找出安全性錯誤、用簡單英文解釋複雜程式碼，並立即產生可運作的腳本。然後你會學會三種互動模式（互動、規劃、程式化），讓你清楚知道每個任務該用哪一種。

> ⚠️ **先決條件**：請先完成 **[第 00 章：快速開始](../00-quick-start/README.md)**。你需要先安裝並驗證 GitHub Copilot CLI，才能執行下方的示範。

## 🎯 學習目標

完成本章後，你將能夠：

- 透過實作體驗 GitHub Copilot CLI 帶來的生產力提升
- 根據任務選擇正確的模式（互動、規劃或程式化）
- 使用斜線指令來控制你的會話

> ⏱️ **預估時間**：約 45 分鐘（閱讀 15 分鐘 + 實作 30 分鐘）

---

# 你的第一個 Copilot CLI 體驗

<img src="assets/first-copilot-experience.png" alt="Developer sitting at a desk with code on the monitor and glowing particles representing AI assistance" width="800"/>

立即開始，看看 Copilot CLI 能做些什麼。

---

## 先暖身：你的第一個提示詞

在進入精彩的示範之前，讓我們先從一些簡單的提示詞開始，這些你現在就能嘗試。**不需要任何程式碼儲存庫**！只要打開終端機並啟動 Copilot CLI：

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

不用 Python？沒關係！直接問你所用語言的問題即可。

你會發現這種互動非常自然。就像問同事一樣提問。探索完畢後，輸入 `/exit` 離開會話。

**關鍵洞見**：GitHub Copilot CLI 是對話式的。你不需要特殊語法，只要用簡單英文提問即可。

## 實際看看

現在來看看為什麼開發者會說這就像「隨時有資深工程師待命」。

> 📖 **閱讀範例說明**：以 `>` 開頭的行是你在互動式 Copilot CLI 會話中輸入的提示詞。沒有 `>` 前綴的行則是你在終端機執行的 shell 指令。

> 💡 **關於範例輸出**：本課程中展示的範例輸出僅供參考。由於 Copilot CLI 的回應每次都會有所不同，你的結果在措辭、格式和細節上都會有所差異。請著重於*回傳資訊的類型*，而非完全相同的文字。

### 示範 1：幾秒完成程式碼審查

本課程包含帶有刻意程式碼品質問題的範例檔案。如果你在本機操作且尚未複製儲存庫，請執行下方 `git clone` 指令，進入 `copilot-cli-for-beginners` 資料夾，然後執行 `copilot` 指令。

```bash
# 如果你在本機操作且尚未複製，請先複製課程儲存庫
git clone https://github.com/github/copilot-cli-for-beginners
cd copilot-cli-for-beginners

# 啟動 Copilot
copilot
```

進入互動式 Copilot CLI 會話後，執行下列指令：

```
> Review @samples/book-app-project/book_app.py for code quality issues and suggest improvements
```

> 💡 **`@` 符號是做什麼用的？** `@` 符號告訴 Copilot CLI 讀取一個檔案。你會在第 02 章學到更多。現在只要照著指令輸入即可。

---

<details>
<summary>🎬 實際操作畫面</summary>

![Code Review Demo](assets/code-review-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

---

**重點**：專業的程式碼審查只需幾秒。人工審查會花……嗯……比這久得多！

---

### 示範 2：解釋令人困惑的程式碼

是否曾經盯著程式碼發呆，不知道它在做什麼？在 Copilot CLI 會話中試試這個：

```
> Explain what @samples/book-app-project/books.py does in simple terms
```

---

<details>
<summary>🎬 實際操作畫面</summary>

![Explain Code Demo](assets/explain-code-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

---

**會發生什麼事**：（你的輸出會不同）Copilot CLI 讀取檔案、理解程式碼，並用簡單英文解釋。

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

**重點**：複雜的程式碼也能像耐心的導師一樣解釋給你聽。

---

### 示範 3：產生可運作的程式碼

需要一個你本來要花 15 分鐘 Google 的函式？繼續在會話中輸入：

```
> Write a Python function that takes a list of books and returns statistics: 
  total count, number read, number unread, oldest and newest book
```

---

<details>
<summary>🎬 實際操作畫面</summary>

![Generate Code Demo](assets/generate-code-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

---

**會發生什麼事**：幾秒內產生完整、可運作的函式，直接複製貼上即可執行。

探索完畢後，離開會話：

```
> /exit
```

**重點**：立即滿足需求，且全程都在同一個連續會話中。

---

# 模式與指令

<img src="assets/modes-and-commands.png" alt="Futuristic control panel with glowing screens, dials, and equalizers representing Copilot CLI modes and commands" width="800"/>

你已經看過 Copilot CLI 能做什麼。現在來了解如何有效運用這些能力。關鍵在於知道不同情境該用哪一種互動模式。

> 💡 **注意**：Copilot CLI 也有一種 **自動駕駛（Autopilot）** 模式，可以自動執行任務而不需等待你的輸入。這很強大，但需要授權完整權限，並會自動使用 premium 請求。本課程聚焦於下方三種模式。等你熟悉基本操作後，我們會再介紹自動駕駛模式。

---

## 🧩 真實世界比喻：外出用餐

把使用 GitHub Copilot CLI 想像成外出用餐。從規劃行程到點餐，不同情境需要不同方式：

| 模式 | 用餐比喻 | 適用時機 |
|------|----------------|-------------|
| **規劃（Plan）** | 用 GPS 規劃去餐廳的路線 | 複雜任務——先規劃路線、檢查停靠點、同意計畫，再出發 |
| **互動（Interactive）** | 跟服務生對話 | 探索與反覆調整——提問、客製化、即時回饋 |
| **程式化（Programmatic）** | 得來速點餐 | 快速、明確的任務——留在原本環境，迅速取得結果 |

就像外出用餐一樣，你會自然學會什麼情境該用哪一種方式。

<img src="assets/ordering-food-analogy.png" alt="Three Ways to Use GitHub Copilot CLI - Plan Mode (GPS route to restaurant), Interactive Mode (talking to waiter), Programmatic Mode (drive-through)" width="800"/>

*根據任務選擇模式：規劃模式先規劃路線，互動模式適合來回討論，程式化模式適合快速一次性結果*

### 我應該從哪個模式開始？

**建議從互動模式開始。** 
- 你可以自由嘗試並追問
- 情境會隨對話自然累積
- 出錯時用 `/clear` 很容易重來

熟悉後可以嘗試：
- **程式化模式**（`copilot -p "<你的提示詞>"`）適合快速、單次提問
- **規劃模式**（`/plan`）適合在寫程式前先詳細規劃

---

## 三種模式

### 模式 1：互動模式（建議起手）

<img src="assets/interactive-mode.png" alt="Interactive Mode - Like talking to a waiter who can answer questions and adjust the order" width="250"/>

**最適合**：探索、反覆調整、多輪對話。就像和服務生對話，可以即時回饋、調整點餐內容。

啟動互動式會話：

```bash
copilot
```

如你目前所見，會出現一個提示符，讓你自然輸入內容。想查詢可用指令，只要輸入：

```
> /help
```

**關鍵洞見**：互動模式會保留情境。每則訊息都會建立在前一則之上，就像真實對話。

#### 互動模式範例

```bash
copilot

> Review @samples/book-app-project/utils.py and suggest improvements

> Add type hints to all functions

> Make the error handling more robust

> /exit
```

注意每個提示詞都延續前一個答案。你是在對話，而不是每次都從頭開始。

---

### 模式 2：規劃模式

<img src="assets/plan-mode.png" alt="Plan Mode - Like planning a route before a trip using GPS" width="250"/>

**最適合**：需要在執行前先檢查流程的複雜任務。就像出發前用 GPS 規劃路線。

規劃模式會協助你在寫程式前先產生逐步計畫。使用 `/plan` 指令，按下 **Shift+Tab** 可切換到規劃模式：

```bash
copilot

> /plan Add a "mark as read" command to the book app
```

> 💡 **小技巧**：**Shift+Tab** 可在模式間切換：互動 → 規劃 → 自動駕駛。在互動會話中隨時按下即可，不用輸入指令。

你也可以用 `--plan` 旗標直接啟動規劃模式：

```bash
copilot --plan
```

**規劃模式輸出範例**：（你的輸出可能不同）

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

**關鍵洞見**：規劃模式讓你在寫程式前先檢查、修改流程。計畫完成後，還能請 Copilot CLI 把它存成檔案，例如「Save this plan to `mark_as_read_plan.md`」就會建立一個包含計畫細節的 markdown 檔。

> 💡 **想挑戰更複雜的嗎？** 試試：`/plan Add search and filter capabilities to the book app`。規劃模式可從簡單功能一路擴展到完整應用程式。

> 📚 **自動駕駛模式**：你可能注意到 Shift+Tab 會切到第三種模式「自動駕駛」。在自動駕駛模式下，Copilot 會自動執行整個計畫，不會在每個步驟等你回覆——就像把任務交給同事並說「做完再告訴我」。典型流程是規劃 → 同意 → 自動駕駛，所以你要先學會寫計畫。你也可以用 `copilot --autopilot` 直接啟動。建議先熟悉互動與規劃模式，再參考[官方文件](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot)。

---

### 模式 3：程式化模式

<img src="assets/programmatic-mode.png" alt="Programmatic Mode - Like using a drive-through for a quick order" width="250"/>

**最適合**：自動化、腳本、CI/CD、單次指令。就像得來速點餐，不用和服務生互動。

用 `-p` 旗標執行一次性、不需互動的指令：

```bash
# 產生程式碼
copilot -p "Write a function that checks if a number is even or odd"

# 快速查詢
copilot -p "How do I read a JSON file in Python?"
```

**關鍵洞見**：程式化模式給你快速答案並自動結束。沒有對話，只有輸入 → 輸出。

<details>
<summary>📚 <strong>進階：在腳本中使用程式化模式</strong>（點擊展開）</summary>

熟悉後，你可以在 shell 腳本中使用 `-p`：

```bash
#!/bin/bash

# 自動產生提交訊息
COMMIT_MSG=$(copilot -p "Generate a commit message for: $(git diff --staged)")
git commit -m "$COMMIT_MSG"

# 審查檔案
copilot --allow-all -p "Review @myfile.py for issues"
```
> ⚠️ **關於 `--allow-all`**：這個旗標會略過所有權限提示，讓 Copilot CLI 可直接讀取檔案、執行指令、存取網址而不需詢問。這對程式化模式（`-p`）很重要，因為沒有互動會話可供你同意。只在你自己撰寫的提示詞、且信任的目錄下使用 `--allow-all`。不要用於不信任的輸入或敏感目錄。

</details>

---

## 必備斜線指令

剛開始使用 Copilot CLI 時，這些指令很值得先學：

| 指令 | 功能說明 | 適用時機 |
|---------|--------------|-------------|
| `/ask` | 提問但不影響對話歷史 | 想要快速答案又不想影響目前任務時 |
| `/clear` | 清除對話並重新開始 | 換主題時 |
| `/help` | 顯示所有可用指令 | 忘記指令時 |
| `/model` | 顯示或切換 AI 模型 | 想更換 AI 模型時 |
| `/plan` | 寫程式前先規劃 | 複雜功能時 |
| `/research` | 用 GitHub 與網路來源做深入研究 | 寫程式前需調查主題時 |
| `/exit` | 結束會話 | 完成時 |

> 💡 **`/ask` 與一般對話的差異**：一般你輸入的每則訊息都會成為對話歷史，影響後續回應。`/ask` 是「不留紀錄」的捷徑——很適合像 `/ask What does YAML mean?` 這種一次性問題，不會污染會話情境。

> 💡 **Tab 自動補齊**：輸入斜線指令時，按 **Tab** 可自動補齊指令名稱，或在子指令與參數間循環。當你記不起完整指令時特別好用。

這些就是入門必備！熟悉後可再探索更多指令。

> 📚 **官方文件**：[CLI 指令參考](https://docs.github.com/copilot/reference/cli-command-reference) 可查詢完整指令與旗標列表。

<details>
<summary>📚 <strong>進階指令</strong>（點擊展開）</summary>

> 💡 上述必備指令已涵蓋日常大部分需求。這份參考適合你想進一步探索時查閱。

### Agent 環境

| 指令 | 功能說明 |
|---------|--------------|
| `/agent` | 瀏覽並選擇可用的 Agent |
| `/env` | 顯示已載入的環境細節——有哪些指令、MCP 伺服器、Skill、Agent 與外掛 |
| `/init` | 為你的儲存庫初始化 Copilot 指令 |
| `/mcp` | 管理 MCP 伺服器設定 |
| `/settings` | 開啟互動式設定對話框，一次瀏覽與編輯所有使用者設定 |
| `/skills` | 管理 Skill 以增強能力 |

> 💡 Agent 介紹在 [第 04 章](../04-agents-custom-instructions/README.md)，Skill 介紹在 [第 05 章](../05-skills/README.md)，MCP 伺服器介紹在 [第 06 章](../06-mcp-servers/README.md)。

### 模型與子 Agent

| 指令 | 功能說明 |
|---------|--------------|
| `/delegate` | 將任務交給 GitHub Copilot 雲端 Agent |
| `/fleet` | 將複雜任務拆分為平行子任務，加速完成 |
| `/model` | 顯示或切換 AI 模型 |
| `/tasks` | 檢視背景子 Agent 與分離的 shell 會話 |

### 程式碼

| 指令 | 功能說明 |
|---------|--------------|
| `/diff` | 檢查目前目錄下的變更 |
| `/pr` | 操作目前分支的 Pull Request |
| `/research` | 用 GitHub 與網路來源做深入研究 |
| `/review` | 執行程式碼審查 Agent 分析變更 |
| `/terminal-setup` | 啟用多行輸入支援（shift+enter 與 ctrl+enter） |

### 權限

| 指令 | 功能說明 |
|---------|--------------|
| `/add-dir <directory>` | 將目錄加入允許清單 |
| `/allow-all [on\|off\|show]` | 自動同意所有權限提示；用 `on` 啟用、`off` 關閉、`show` 查詢狀態 |
| `/yolo` | `/allow-all on` 的快速別名——自動同意所有權限提示。 |
| `/cwd`, `/cd [directory]` | 顯示或切換工作目錄 |
| `/list-dirs` | 顯示所有允許的目錄 |

> ⚠️ **請小心使用**：`/allow-all` 與 `/yolo` 會略過確認提示。信任的專案很方便，但對不信任的程式碼要特別小心。

### 會話

| 指令 | 功能說明 |
|---------|--------------|
| `/clear` | 放棄目前會話（不儲存歷史），重新開始對話 |
| `/compact` | 摘要對話內容以減少情境用量（可加焦點指示，如 `/compact focus on the bug list`） |
| `/context` | 顯示情境窗口 Token 用量與視覺化 |
| `/keep-alive` | 防止系統進入睡眠，適合筆電長時間執行任務 |
| `/memory [on\|off\|show]` | 啟用、停用或檢視持久記憶——跨所有會話記住事實與偏好設定 |
| `/new` | 結束目前會話（儲存到歷史以供搜尋/繼續），並開始新對話 |
| `/resume` | 切換到其他會話（可指定會話 ID 或名稱） |
| `/rename` | 重新命名目前會話（不加名稱則自動產生） |
| `/rewind` | 開啟時間軸選擇器，回到對話中任一早期點 |
| `/usage` | 顯示會話用量統計與配額進度條 |
| `/session` | 顯示會話資訊與工作區摘要；用 `/session delete`、`/session delete <id>` 或 `/session delete-all` 刪除會話 |
| `/share` | 匯出會話為 markdown 檔、GitHub gist 或自含式 HTML 檔 |

### 顯示

| 指令 | 功能說明 |
|---------|--------------|
| `/statusline`（或 `/footer`） | 自訂會話底部狀態列顯示哪些項目（目錄、分支、努力值、情境窗口、配額） |
| `/theme` | 檢視或設定終端機主題 |
| `/voice` | 用本地語音辨識輸入提示詞——自然說話即可，不用打字 |

### 說明與回饋

| 指令 | 功能說明 |
|---------|--------------|
| `/app` | 直接從 CLI 開啟 GitHub 應用程式（或瀏覽器備用） |
| `/changelog` | 顯示 CLI 版本更新紀錄 |
| `/feedback` | 提交回饋給 GitHub |
| `/help` | 顯示所有可用指令 |

### 快速 Shell 指令

在提示詞前加 `!` 可直接執行 shell 指令，不經過 AI：

```bash
copilot

> !git status
# 直接執行 git status，不經過 AI

> !python -m pytest tests/
# 直接執行 pytest
```

### 切換模型

Copilot CLI 支援多種 AI 模型，包括 OpenAI、Anthropic、Google 等。你可用的模型取決於訂閱等級與地區。用 `/model` 查看並切換：

```bash
copilot
> /model

# 顯示可用模型並讓你選擇。選擇 Sonnet 4.5。
```

> 💡 **小技巧**：有些模型會消耗更多「premium 請求」。標記為 **1x**（如 Claude Sonnet 4.5）的模型很適合預設使用，效能好又省配額。倍率較高的模型會更快用完 premium 配額，建議留給真正需要時使用。

> 💡 **不知道該選哪個模型？** 從模型選單選擇 **`Auto`**，讓 Copilot 自動為每個會話挑選最佳模型。剛開始時這是很好的預設選擇，不用煩惱模型挑選。

</details>

---

# 練習

<img src="../assets/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

是時候把學到的知識實際應用了。

---

## ▶️ 自己動手試試

### 互動式探索

啟動 Copilot，並用追問提示詞反覆優化書籍應用程式：

```bash
copilot

> Review @samples/book-app-project/book_app.py - what could be improved?

> Refactor the if/elif chain into a more maintainable structure

> Add type hints to all the handler functions

> /exit
```

### 規劃一個功能

用 `/plan` 讓 Copilot CLI 在寫程式前先規劃實作步驟：

```bash
copilot

> /plan Add a search feature to the book app that can find books by title or author

# 檢查規劃內容
# 同意或修改
# 觀察逐步實作
```

### 用程式化模式自動化

`-p` 旗標讓你直接在終端機執行 Copilot CLI，無需進入互動模式。從儲存庫根目錄複製貼上下方腳本（不要在 Copilot 內執行），即可審查書籍應用程式的所有 Python 檔案。

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

完成示範後，試試這些變化題：

1. **互動挑戰**：啟動 `copilot` 並探索書籍應用程式。詢問 `@samples/book-app-project/books.py` 並連續請求三次改進建議。
2. **規劃模式挑戰**：執行 `/plan Add rating and review features to the book app`。仔細閱讀規劃內容。合理嗎？
3. **程式化挑戰**：執行 `copilot --allow-all -p "List all functions in @samples/book-app-project/book_app.py and describe what each does"`。第一次就成功了嗎？

---

## 💡 小技巧：用網頁或手機遠端控制 CLI 會話

GitHub Copilot CLI 支援**遠端會話**，讓你能從網頁瀏覽器（桌機或手機）或 GitHub Mobile app 監控並互動進行中的 CLI 會話，而不必待在終端機前。

用 `--remote` 旗標啟動遠端會話：

```bash
copilot --remote
```

Copilot CLI 會顯示一個連結並提供 QR code。用手機或桌機瀏覽器開啟連結，即可即時觀看會話、發送追問、檢查規劃、遠端操控 Agent。每個會話僅限本人存取，保護你的 Copilot CLI 會話安全。

你也可以在任何進行中的會話中隨時啟用遠端存取：

```
> /remote
```
更多關於遠端會話的細節可參見 [Copilot CLI 文件](https://docs.github.com/copilot/how-tos/copilot-cli/steer-remotely)。

---

## 📝 作業

### 主要挑戰：改進書籍應用程式的工具函式

實作範例著重於審查與重構 `book_app.py`。現在請在另一個檔案 `utils.py` 上練習相同技能：

1. 啟動互動式會話：`copilot`
2. 請 Copilot CLI 摘要檔案內容：「Summarize @samples/book-app-project/utils.py 並說明此檔案中每個函式的功能」
3. 請它加入輸入驗證：「為 `get_user_choice()` 增加驗證，使其能處理空白輸入與非數字項目」
4. 請它改善錯誤處理：「如果 `get_book_details()` 收到空字串作為書名會發生什麼事？請加入防護措施」
5. 請它補上註解：「為 `get_book_details()` 增加完整的註解，包含參數說明與回傳值」
6. 觀察情境如何在提示間傳遞。每次改進都會建立在前一次基礎上
7. 使用 `/exit` 離開

**成功標準**：你應該得到一份改進過的 `utils.py`，具備輸入驗證、錯誤處理與註解，全部透過多輪對話完成。

<details>
<summary>💡 提示（點擊展開）</summary>

**可嘗試的範例提示：**
```bash
> @samples/book-app-project/utils.py 此檔案中每個函式的功能是什麼？
> 為 get_user_choice() 增加驗證，使其能處理空白輸入與非數字項目
> 如果 get_book_details() 收到空字串作為書名會發生什麼事？請加入防護措施
> 為 get_book_details() 增加完整的註解，包含參數說明與回傳值
```

**常見問題：**
- 若 Copilot CLI 提問澄清問題，只需自然回答即可
- 情境會持續傳遞，每個提示都會建立在前一次基礎上
- 若想重新開始，請使用 `/clear`

</details>

### 加分挑戰：比較三種模式

範例中使用 `/plan` 進行搜尋功能，以及用 `-p` 批次審查。現在請在單一新任務上嘗試三種模式：為 `BookCollection` 類別新增 `list_by_year()` 方法：

1. **互動式**：`copilot` → 逐步請它設計並建立該方法
2. **計畫模式**：`/plan Add a list_by_year(start, end) method to BookCollection that filters books by publication year range`
3. **程式化模式**：`copilot --allow-all -p "@samples/book-app-project/books.py Add a list_by_year(start, end) method that returns books published between start and end year inclusive"`

**反思**：哪種模式最自然？你會在什麼情境下使用各種模式？

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生狀況 | 修正方式 |
|------|----------|----------|
| 輸入 `exit` 而非 `/exit` | Copilot CLI 將 "exit" 視為提示詞，而非指令 | 斜線指令皆以 `/` 開頭 |
| 用 `-p` 進行多輪對話 | 每次 `-p` 呼叫都是獨立的，無法記憶前次內容 | 多輪情境請用互動模式（`copilot`） |
| 忘記用引號包住含 `$` 或 `!` 的提示 | Shell 會先解析特殊字元，Copilot CLI 收不到 | 用引號包住提示：`copilot -p "What does $HOME mean?"` |
| 按一次 Esc 取消執行中的任務 | 單次 Esc 不再能取消進行中的工作（避免誤觸） | Copilot CLI 處理時請按 **Esc 兩次** 取消 |

### 疑難排解

**"Model not available"** - 你的訂閱可能不包含所有模型。請用 `/model` 查看可用模型。

**"Context too long"** - 你的對話已用滿情境窗口。請用 `/clear` 重設，或開啟新會話。

**"Rate limit exceeded"** - 請稍候幾分鐘再試。大量批次操作可考慮用程式化模式並加上延遲。

</details>

---

# 摘要

## 🔑 重點整理

1. **互動模式** 適合探索與反覆調整——情境會持續傳遞。就像和一個記得你之前說過什麼的人對話。
2. **計畫模式** 通常用於較複雜的任務。先審查再實作。
3. **程式化模式** 適合自動化。不需互動。
4. **基本指令**（`/ask`、`/help`、`/clear`、`/plan`、`/research`、`/model`、`/exit`）涵蓋大部分日常需求。

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

現在你已了解三種模式，接下來將學習如何讓 Copilot CLI 知道你的程式碼情境。

在 **[第 02 章：情境與對話](../02-context-conversations/README.md)** 中，你將學到：

- 用 `@` 語法引用檔案與目錄
- 用 `--resume` 與 `--continue` 管理會話
- 情境管理如何讓 Copilot CLI 真正強大

---

**[← 回到課程首頁](../README.md)** | **[繼續前往第 02 章 →](../02-context-conversations/README.md)**
