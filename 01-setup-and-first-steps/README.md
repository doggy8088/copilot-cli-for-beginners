![Chapter 01: First Steps](images/chapter-header.png)

> **觀看 AI 如何即時找出錯誤、解釋令人困惑的程式碼，並產生可運作的腳本。接著學會三種不同的 GitHub Copilot CLI 使用方式。**

這一章就是魔法的起點！你將親身體驗為什麼開發者會形容 GitHub Copilot CLI 就像隨時可聯絡的資深工程師。你會看到 AI 在幾秒內找出安全性漏洞、用簡單易懂的英文解釋複雜程式碼，並立即產生可運作的腳本。然後你會學會三種互動模式（互動模式、規劃模式、程式化模式），讓你知道在任何任務下該用哪一種。

> ⚠️ **先決條件**：請先完成 **[第 00 章：快速開始](../00-quick-start/README.md)**。你需要先安裝並驗證 GitHub Copilot CLI，才能執行下方的示範。

## 🎯 學習目標

完成本章後，你將能夠：

- 透過實作示範，體驗 GitHub Copilot CLI 帶來的生產力提升
- 根據任務選擇正確的模式（互動、規劃或程式化）
- 使用斜線指令控制你的對話

> ⏱️ **預估時間**：約 45 分鐘（閱讀 15 分鐘 + 實作 30 分鐘）

---

# 你的第一個 Copilot CLI 體驗

<img src="images/first-copilot-experience.png" alt="Developer sitting at a desk with code on the monitor and glowing particles representing AI assistance" width="800"/>

直接開始，看看 Copilot CLI 能做到什麼。

---

## 先暖身：你的第一個提示詞

在進入精彩的示範之前，讓我們先從一些你現在就能嘗試的簡單提示詞開始。**不需要任何程式碼倉庫**！只要打開終端機並啟動 Copilot CLI：

```bash
copilot
```

試試這些新手友善的提示詞：

```
> 用簡單的說法解釋 Python 中的 dataclass 是什麼

> 寫一個函式，能根據特定鍵對字典列表進行排序

> Python 中 list 和 tuple 有什麼不同？

> 給我 5 個撰寫乾淨 Python 程式碼的最佳實踐
```

你不寫 Python？沒關係！只要問你想要語言的相關問題即可。

你會發現這種互動非常自然。就像問同事一樣直接提問。探索完畢後，輸入 `/exit` 離開對話。

**關鍵洞見**：GitHub Copilot CLI 是對話式的。你不需要特殊語法，只要用自然語言提問即可。

## 實際操作看看

現在來看看為什麼開發者會說這就像「隨時可聯絡的資深工程師」。

> 📖 **閱讀範例說明**：以 `>` 開頭的行是你在互動式 Copilot CLI 對話中輸入的提示詞。沒有 `>` 前綴的行則是在終端機執行的 shell 指令。

> 💡 **關於範例輸出**：本課程中的範例輸出僅供參考。由於 Copilot CLI 的回應每次都可能不同，你看到的內容在措辭、格式和細節上都會有所差異。請專注於*回傳資訊的類型*，而不是完全一樣的文字。

### 示範 1：幾秒內完成程式碼審查

本課程包含帶有刻意品質問題的範例檔案。如果你在本機操作且尚未 clone 倉庫，請執行下方的 `git clone` 指令，切換到 `copilot-cli-for-beginners` 資料夾，然後啟動 `copilot`。

```bash
# 如果你在本機操作且尚未 clone 倉庫，請執行
git clone https://github.com/github/copilot-cli-for-beginners
cd copilot-cli-for-beginners

# 啟動 Copilot
copilot
```

進入互動式 Copilot CLI 對話後，執行下列指令：

```
> Review @samples/book-app-project/book_app.py for code quality issues and suggest improvements
```

> 💡 **`@` 符號是做什麼用的？** `@` 符號告訴 Copilot CLI 讀取一個檔案。你會在第 02 章學到詳細內容。現在只要照著指令輸入即可。

---

<details>
<summary>🎬 實際操作畫面</summary>

![Code Review Demo](images/code-review-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容可能與這裡顯示的不同。*

</details>

---

**重點**：專業的程式碼審查只需幾秒。人工審查則會花上……遠超這個時間！

---

### 示範 2：解釋令人困惑的程式碼

是否曾經盯著程式碼發呆，不知道它在做什麼？在 Copilot CLI 對話中試試這個：

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

**會發生什麼事**：（你的輸出會不同）Copilot CLI 會讀取檔案、理解程式碼，並用簡單易懂的英文解釋。

```
這是一個使用 Python dataclass 的書籍收藏管理模組。

你可以把它想像成一個數位書架：
- Book 是一個 dataclass —— 一種簡單儲存書籍資訊（書名、作者、年份、閱讀狀態）的方式
- BookCollection 管理整個收藏，並負責儲存/載入

主要組成：

1. @dataclass 裝飾器（第 8 行）
   - 自動產生 __init__、__repr__ 等方法
   - 讓 Python 資料結構定義更簡潔

2. BookCollection 類別（第 16 行）
   - 維護 Book 物件的列表
   - 用 JSON 檔案處理持久化
   - load_books() 從 data.json 讀取
   - save_books() 用 asdict() 寫入 data.json

3. 書籍操作：
   - add_book() —— 建立並儲存新書
   - find_book_by_title() —— 搜尋收藏
   - mark_as_read() —— 更新閱讀狀態
   - find_by_author() —— 依作者名稱篩選

常見流程：從 JSON 讀取 → 操作 Python 物件 → 寫回 JSON
```

**重點**：複雜程式碼也能像有耐心的導師一樣解釋給你聽。

---

### 示範 3：產生可運作的程式碼

需要一個本來要 Google 15 分鐘的函式？在同一個對話中繼續：

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

**會發生什麼事**：幾秒內產生一個完整、可用的函式，直接複製貼上就能執行。

探索完畢後，離開對話：

```
> /exit
```

**重點**：立即滿足需求，而且全程都在同一個連續對話中完成。

---

# 模式與指令

<img src="images/modes-and-commands.png" alt="Futuristic control panel with glowing screens, dials, and equalizers representing Copilot CLI modes and commands" width="800"/>

你已經看過 Copilot CLI 的強大功能。現在來了解*如何*有效運用這些能力。關鍵在於知道三種互動模式該用在哪些情境。

> 💡 **注意**：Copilot CLI 也有一個 **Autopilot** 模式，可以自動執行任務而不需等待你的輸入。這很強大，但需要授權完整權限，並會自動使用 premium 請求。本課程聚焦於下方三種模式。等你熟悉基礎後，我們會再介紹 Autopilot。

---

## 🧩 真實世界比喻：外出用餐

把使用 GitHub Copilot CLI 想像成外出用餐。從規劃行程到點餐，不同情境需要不同方式：

| 模式 | 用餐比喻 | 適用時機 |
|------|----------------|-------------|
| **規劃模式（Plan）** | 用 GPS 規劃去餐廳的路線 | 複雜任務——規劃路線、檢查停靠點、確認計畫後再出發 |
| **互動模式（Interactive）** | 和服務生對話 | 探索與反覆調整——提問、客製化、即時回饋 |
| **程式化模式（Programmatic）** | 得來速點餐 | 快速、明確的任務——留在原本環境，迅速取得結果 |

就像外出用餐一樣，你會自然學會什麼時候該用哪一種方式。

<img src="images/ordering-food-analogy.png" alt="Three Ways to Use GitHub Copilot CLI - Plan Mode (GPS route to restaurant), Interactive Mode (talking to waiter), Programmatic Mode (drive-through)" width="800"/>

*根據任務選擇模式：規劃模式適合先規劃路線，互動模式適合來回討論，程式化模式適合快速一次性結果*

### 我應該從哪個模式開始？

**從互動模式開始。** 
- 你可以自由嘗試、追問細節
- 情境會隨對話自然累積
- 出錯時用 `/clear` 很容易重來

熟悉後可以試試：
- **程式化模式**（`copilot -p "<你的提示詞>"`）適合快速、單次提問
- **規劃模式**（`/plan`）當你需要在動手寫程式前先詳細規劃

---

## 三種模式

### 模式 1：互動模式（建議從這裡開始）

<img src="images/interactive-mode.png" alt="Interactive Mode - Like talking to a waiter who can answer questions and adjust the order" width="250"/>

**最適合**：探索、反覆調整、多輪對話。就像和服務生對話，能即時回應、調整點餐內容。

啟動互動式對話：

```bash
copilot
```

如同前面示範，你會看到一個提示符，讓你自然輸入問題。想查詢可用指令，只要輸入：

```
> /help
```

**關鍵洞見**：互動模式會保留情境。每一則訊息都會建立在前一則基礎上，就像真實對話。

#### 互動模式範例

```bash
copilot

> Review @samples/book-app-project/utils.py and suggest improvements

> Add type hints to all functions

> Make the error handling more robust

> /exit
```

注意每個提示詞都建立在前一個答案之上。你是在進行一場對話，而不是每次都從頭開始。

---

### 模式 2：規劃模式

<img src="images/plan-mode.png" alt="Plan Mode - Like planning a route before a trip using GPS" width="250"/>

**最適合**：需要在執行前先檢查規劃的複雜任務。就像出發前用 GPS 規劃路線。

規劃模式會幫你在寫程式前先建立逐步計畫。使用 `/plan` 指令，按下 **Shift+Tab** 可切換到規劃模式：

```bash
copilot

> /plan Add a "mark as read" command to the book app
```

> 💡 **小技巧**：**Shift+Tab** 可在模式間切換：互動 → 規劃 → Autopilot。任何時候在互動式對話中都能按下切換，不用輸入指令。

你也可以用 `--plan` 旗標直接啟動 Copilot CLI 的規劃模式：

```bash
copilot --plan
```

**規劃模式輸出範例：**（你的輸出可能不同）

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

**關鍵洞見**：規劃模式讓你在寫任何程式碼前先檢查、調整計畫。計畫完成後，你甚至可以請 Copilot CLI 把它存成檔案，例如「Save this plan to `mark_as_read_plan.md`」就會產生一份包含計畫細節的 markdown 檔。

> 💡 **想挑戰更複雜的嗎？** 試試：`/plan Add search and filter capabilities to the book app`。規劃模式可從簡單功能一路擴展到完整應用程式。

> 📚 **Autopilot 模式**：你可能注意到 Shift+Tab 會切換到第三種模式 **Autopilot**。在 autopilot 模式下，Copilot 會自動執行整個計畫，不需你每步確認——就像把任務交給同事說「做完再告訴我」。典型流程是規劃 → 接受 → autopilot，所以你必須先學會寫好計畫。你也可以用 `copilot --autopilot` 直接啟動。建議先熟悉互動與規劃模式，再參考 [官方文件](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot)。

---

### 模式 3：程式化模式

<img src="images/programmatic-mode.png" alt="Programmatic Mode - Like using a drive-through for a quick order" width="250"/>

**最適合**：自動化、腳本、CI/CD、單次指令。就像得來速點餐，不用和服務生對話。

用 `-p` 旗標執行一次性、不需互動的指令：

```bash
# 產生程式碼
copilot -p "Write a function that checks if a number is even or odd"

# 快速查詢
copilot -p "How do I read a JSON file in Python?"
```

**關鍵洞見**：程式化模式給你快速答案後就結束。沒有對話，只有輸入 → 輸出。

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
> ⚠️ **關於 `--allow-all`**：這個旗標會跳過所有權限提示，讓 Copilot CLI 可以直接讀取檔案、執行指令、存取網址。這對於程式化模式（`-p`）很重要，因為沒有互動式對話可供你確認。只在你自己寫的提示詞、信任的目錄下使用 `--allow-all`。千萬不要用在不信任的輸入或敏感目錄。

</details>

---

## 必學斜線指令

這些指令很適合剛開始使用 Copilot CLI 時學習：

| 指令 | 功能說明 | 適用時機 |
|---------|--------------|-------------|
| `/ask` | 提出快速問題，不會影響對話歷史 | 想要快速答案又不想打亂目前任務時 |
| `/clear` | 清除對話，重新開始 | 換主題時 |
| `/help` | 顯示所有可用指令 | 忘記指令時 |
| `/model` | 顯示或切換 AI 模型 | 想更換 AI 模型時 |
| `/plan` | 在寫程式前先規劃工作 | 複雜功能時 |
| `/research` | 用 GitHub 和網路來源進行深入研究 | 需要在寫程式前調查主題時 |
| `/exit` | 結束對話 | 完成時 |

> 💡 **`/ask` 與一般聊天的差異**：通常你發送的每則訊息都會成為對話歷史的一部分，影響後續回應。`/ask` 是「不留紀錄」的捷徑——很適合像 `/ask What does YAML mean?` 這種單次提問，不會污染你的對話情境。

> 💡 **Tab 補全**：輸入斜線指令時，按 **Tab** 可自動補全指令名稱，或在子指令與參數間切換。當你記不起完整指令時特別好用。

這就是入門所需！熟悉後可以探索更多指令。

> 📚 **官方文件**：[CLI 指令參考](https://docs.github.com/copilot/reference/cli-command-reference) 可查詢完整指令與旗標列表。

<details>
<summary>📚 <strong>進階指令</strong>（點擊展開）</summary>

> 💡 上述必學指令涵蓋了日常大部分需求。這份參考適合你想進一步探索時查閱。

### Agent 環境

| 指令 | 功能說明 |
|---------|--------------|
| `/agent` | 瀏覽並選擇可用的 agent |
| `/env` | 顯示已載入的環境細節——有哪些指令、MCP 伺服器、技能、agent 與外掛 |
| `/init` | 為你的倉庫初始化 Copilot 指令 |
| `/mcp` | 管理 MCP 伺服器設定 |
| `/skills` | 管理技能以增強功能 |

> 💡 Agent 會在 [第 04 章](../04-agents-custom-instructions/README.md) 詳細介紹，技能在 [第 05 章](../05-skills/README.md)，MCP 伺服器在 [第 06 章](../06-mcp-servers/README.md)。

### 模型與子 agent

| 指令 | 功能說明 |
|---------|--------------|
| `/delegate` | 將任務交給 GitHub Copilot 雲端 agent |
| `/fleet` | 將複雜任務拆分為多個子任務並平行處理 |
| `/model` | 顯示或切換 AI 模型 |
| `/tasks` | 查看背景子 agent 與分離的 shell 對話 |

### 程式碼

| 指令 | 功能說明 |
|---------|--------------|
| `/diff` | 審查目前目錄下的變更 |
| `/pr` | 操作目前分支的 pull request |
| `/research` | 用 GitHub 和網路來源進行深入研究 |
| `/review` | 執行程式碼審查 agent 分析變更 |
| `/terminal-setup` | 啟用多行輸入支援（shift+enter 與 ctrl+enter） |

### 權限

| 指令 | 功能說明 |
|---------|--------------|
| `/add-dir <directory>` | 將目錄加入允許清單 |
| `/allow-all [on|off|show]` | 自動同意所有權限提示；用 `on` 啟用，`off` 關閉，`show` 檢查狀態 |
| `/yolo` | `/allow-all on` 的快速別名——自動同意所有權限提示。|
| `/cwd`, `/cd [directory]` | 檢視或切換工作目錄 |
| `/list-dirs` | 顯示所有允許的目錄 |

> ⚠️ **請小心使用**：`/allow-all` 與 `/yolo` 會跳過確認提示。適合信任的專案，但對於不信任的程式碼要特別小心。

### 對話

| 指令 | 功能說明 |
|---------|--------------|
| `/clear` | 放棄目前對話（不儲存歷史）並重新開始 |
| `/compact` | 摘要對話內容以減少情境用量 |
| `/context` | 顯示情境視窗 token 用量與視覺化 |
| `/keep-alive` | 防止 Copilot CLI 執行時系統進入睡眠——適合筆電長時間任務 |
| `/new` | 結束目前對話（儲存到歷史以供搜尋/繼續）並重新開始 |
| `/resume` | 切換到其他對話（可指定對話 ID 或名稱）|
| `/rename` | 重新命名目前對話（不輸入名稱則自動產生）|
| `/rewind` | 開啟時間軸選擇器，回到對話任意早期狀態 |
| `/usage` | 顯示對話用量統計 |
| `/session` | 顯示對話資訊與工作區摘要；用 `/session delete`、`/session delete <id>` 或 `/session delete-all` 移除對話 |
| `/share` | 將對話匯出為 markdown、GitHub gist 或自含式 HTML 檔案 |

### 顯示

| 指令 | 功能說明 |
|---------|--------------|
| `/statusline`（或 `/footer`） | 自訂狀態列顯示哪些項目（目錄、分支、effort、情境視窗、配額）|
| `/theme` | 查看或設定終端機主題 |

### 說明與回饋

| 指令 | 功能說明 |
|---------|--------------|
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

Copilot CLI 支援多種來自 OpenAI、Anthropic、Google 等的 AI 模型。你可用的模型取決於訂閱等級與地區。用 `/model` 查看並切換：

```bash
copilot
> /model

# 顯示可用模型並讓你選擇。選擇 Sonnet 4.5。
```

> 💡 **小技巧**：有些模型會消耗更多「premium 請求」。標記為 **1x**（如 Claude Sonnet 4.5）的模型很適合預設使用，既強大又高效。倍率更高的模型會更快用完 premium 配額，建議只在真的需要時使用。

> 💡 **不確定選哪個模型？** 選擇 **`Auto`** 讓 Copilot 自動為每個對話挑選最佳模型。這是入門時的好選擇，省去選擇模型的煩惱。

</details>

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

是時候把學到的內容實際操作一遍。

---

## ▶️ 自己動手試試

### 互動式探索

啟動 Copilot，並用追問提示詞反覆改進書籍應用程式：

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

# 檢查計畫
# 核准或修改
# 觀察它逐步實作
```

### 用程式化模式自動化

`-p` 旗標讓你直接從終端機執行 Copilot CLI，而不用進入互動模式。從倉庫根目錄複製貼上下列腳本到終端機（不是 Copilot 內），即可審查書籍應用程式下所有 Python 檔案。

```bash
# 審查書籍應用程式下所有 Python 檔案
for file in samples/book-app-project/*.py; do
  echo "Reviewing $file..."
  copilot --allow-all -p "Quick code quality review of @$file - critical issues only"
done
```

**PowerShell（Windows）：**

```powershell
# 審查書籍應用程式下所有 Python 檔案
Get-ChildItem samples/book-app-project/*.py | ForEach-Object {
  $relativePath = "samples/book-app-project/$($_.Name)";
  Write-Host "Reviewing $relativePath...";
  copilot --allow-all -p "Quick code quality review of @$relativePath - critical issues only" 
}
```

---

完成示範後，試試這些變化：

1. **互動挑戰**：啟動 `copilot` 並探索書籍應用程式。詢問 `@samples/book-app-project/books.py`，並連續三次請求改進建議。

2. **規劃模式挑戰**：執行 `/plan Add rating and review features to the book app`。仔細閱讀計畫內容。它合理嗎？

3. **程式化挑戰**：執行 `copilot --allow-all -p "List all functions in @samples/book-app-project/book_app.py and describe what each does"`。第一次就成功了嗎？

---

## 💡 小技巧：用網頁或手機遠端控制 CLI 對話

GitHub Copilot CLI 支援**遠端對話**，讓你能從網頁瀏覽器（桌機或手機）或 GitHub Mobile app 監控並互動正在執行的 CLI 對話，而不必親自在終端機前。

用 `--remote` 旗標啟動遠端對話：

```bash
copilot --remote
```

Copilot CLI 會顯示一個連結並提供 QR code。用手機或桌機瀏覽器開啟連結，即可即時觀看對話、發送追問、檢查計畫並遠端操作 agent。每個對話都是使用者專屬，你只能存取自己的 Copilot CLI 對話。

你也可以在任何時候於進行中的對話中啟用遠端存取：

```
> /remote
```

更多遠端對話細節請參考 [Copilot CLI 文件](https://docs.github.com/copilot/how-tos/copilot-cli/steer-remotely)。

---

## 📝 作業

### 主要挑戰：改進書籍應用程式的工具函式

前面的實作範例聚焦在審查與重構 `book_app.py`。現在請你將相同技巧應用到另一個檔案 `utils.py`：1. 啟動互動式工作階段：`copilot`
2. 請 Copilot CLI 摘要這個檔案：`@samples/book-app-project/utils.py What does each function in this file do?`
3. 請它加入輸入驗證：「為 `get_user_choice()` 加入驗證，讓它能處理空白輸入和非數字輸入」
4. 請它改善錯誤處理：「如果 `get_book_details()` 收到空字串作為書名會發生什麼事？請為此加入防呆機制。」
5. 請求加入文件字串：「為 `get_book_details()` 加入完整的文件字串，包含參數說明與回傳值」
6. 觀察情境如何在多次提示間傳遞。每次改進都會建立在前一次的基礎上
7. 使用 `/exit` 離開

**成功標準**：你應該會得到一個改進過的 `utils.py`，具備輸入驗證、錯誤處理和文件字串，且這些都是透過多輪對話逐步完成的。

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
- 如果 Copilot CLI 提出釐清問題，只要自然回答即可
- 情境會持續傳遞，因此每個提示都會建立在前一次的基礎上
- 如果想重新開始，請使用 `/clear`

</details>

### 加分挑戰：比較三種模式

範例中已經用 `/plan` 實作搜尋功能、用 `-p` 做批次審查。現在請針對新增 `list_by_year()` 方法到 `BookCollection` 類別這個新任務，嘗試三種模式：

1. **互動式**：`copilot` → 逐步請它設計並實作這個方法
2. **計畫模式**：`/plan Add a list_by_year(start, end) method to BookCollection that filters books by publication year range`
3. **程式化模式**：`copilot --allow-all -p "@samples/book-app-project/books.py Add a list_by_year(start, end) method that returns books published between start and end year inclusive"`

**反思**：哪一種模式最符合你的直覺？你會在什麼情境下使用哪一種？

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 結果 | 修正方式 |
|------|------|----------|
| 輸入 `exit` 而不是 `/exit` | Copilot CLI 會把 "exit" 當成提示詞，而不是指令 | 斜線指令一定要以 `/` 開頭 |
| 在多輪對話中使用 `-p` | 每次 `-p` 執行都是獨立的，沒有記憶前一次內容 | 需要情境累積請用互動模式（`copilot`） |
| 忘記用引號包住含 `$` 或 `!` 的提示 | Shell 會先解析特殊字元，Copilot CLI 收不到正確內容 | 用引號包住提示：`copilot -p "What does $HOME mean?"` |
| 按一次 Esc 想取消執行中任務 | 單次 Esc 不再能取消進行中的工作（避免誤觸） | Copilot CLI 處理時請按 **Esc 兩次** 取消 |

### 疑難排解

**"Model not available"** - 你的訂閱可能不包含所有模型。請用 `/model` 查看可用模型。

**"Context too long"** - 你的對話已用滿情境視窗。請用 `/clear` 重設，或開始新工作階段。

**"Rate limit exceeded"** - 請稍等幾分鐘再試。若需大量批次操作，可考慮用程式化模式並加上延遲。

</details>

---

# 摘要

## 🔑 重點整理

1. **互動模式** 適合探索與反覆調整——情境會持續傳遞。就像和一個記得你前面說過什麼的人對話。
2. **計畫模式** 通常用於較複雜的任務。會在執行前先讓你審查。
3. **程式化模式** 適合自動化，無需互動。
4. **常用指令**（`/ask`、`/help`、`/clear`、`/plan`、`/research`、`/model`、`/exit`）涵蓋大部分日常需求。

> 📋 **快速參考**：完整指令與快捷鍵請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

現在你已經了解三種模式，接下來要學習如何讓 Copilot CLI 取得你的程式碼情境。

在 **[第 02 章：情境與對話](../02-context-conversations/README.md)** 中，你將會學到：

- 用 `@` 語法參照檔案與目錄
- 用 `--resume` 和 `--continue` 管理工作階段
- 為什麼情境管理讓 Copilot CLI 如虎添翼

---

**[← 回到課程首頁](../README.md)** | **[繼續前往第 02 章 →](../02-context-conversations/README.md)**
