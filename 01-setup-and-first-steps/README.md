![Chapter 01: First Steps](images/chapter-header.png)

> **觀看 AI 即時找出錯誤、解釋難懂程式碼、並產生可運作的腳本。接著學習三種使用 GitHub Copilot CLI 的方式。**

這一章就是魔法的開始！你將親身體驗為什麼開發者形容 GitHub Copilot CLI 就像隨時有資深工程師待命。你會看到 AI 在幾秒內找出安全性漏洞、用簡單易懂的語言解釋複雜程式碼，並即時產生可運作的腳本。然後你將學會三種互動模式（互動模式、規劃模式、程式化模式），讓你知道任何任務該用哪一種。

> ⚠️ **先決條件**：請先完成 **[第 00 章：快速開始](../00-quick-start/README.md)**。你必須已安裝並驗證 GitHub Copilot CLI，才能執行以下示範。

## 🎯 學習目標

本章結束時，你將能夠：

- 透過實作示範，體驗 GitHub Copilot CLI 帶來的生產力提升
- 根據任務選擇適合的模式（互動、規劃、程式化）
- 使用斜線指令控制你的對話

> ⏱️ **預估時間**：約 45 分鐘（15 分鐘閱讀 + 30 分鐘實作）

---

# 你的第一個 Copilot CLI 體驗

<img src="images/first-copilot-experience.png" alt="Developer sitting at a desk with code on the monitor and glowing particles representing AI assistance" width="800"/>

直接上手，看看 Copilot CLI 能做什麼。

---

## 熟悉操作：你的第一個提示詞

在進入精彩示範之前，先從一些簡單的提示詞開始，現在就可以嘗試。**不需要任何程式碼庫**！只要打開終端機並啟動 Copilot CLI：

```bash
copilot
```

試試這些適合初學者的提示詞：

```
> Explain what a dataclass is in Python in simple terms

> Write a function that sorts a list of dictionaries by a specific key

> What's the difference between a list and a tuple in Python?

> Give me 5 best practices for writing clean Python code
```

不用 Python？沒問題！直接問你想要的語言相關問題即可。

你會發現操作非常自然。就像問同事一樣直接提問。探索完畢後，輸入 `/exit` 離開對話。

**關鍵洞察**：GitHub Copilot CLI 是對話式的。你不需要特殊語法，只要用自然語言提問即可。

## 實際運作展示

現在來看看為什麼開發者說這就像「隨時有資深工程師待命」。

> 📖 **閱讀範例說明**：以 `>` 開頭的行是你在 Copilot CLI 互動模式中輸入的提示詞。沒有 `>` 前綴的行則是你在終端機執行的 shell 指令。

> 💡 **關於範例輸出**：本課程中的範例輸出僅供參考。因為 Copilot CLI 的回應每次都不同，你的結果在措辭、格式和細節上都會有所差異。請專注於回傳的「資訊類型」，而非完全相同的文字。

### 示範 1：秒級程式碼審查

課程提供了帶有刻意程式碼品質問題的範例檔案。如果你在本機操作且尚未 clone 課程 repo，請執行下方 `git clone` 指令，切換到 `copilot-cli-for-beginners` 資料夾，然後啟動 Copilot。

```bash
# 若你在本機操作且尚未 clone 課程 repo，請執行
git clone https://github.com/github/copilot-cli-for-beginners
cd copilot-cli-for-beginners

# 啟動 Copilot
copilot
```

進入 Copilot CLI 互動模式後，執行下列提示：

```
> Review @samples/book-app-project/book_app.py for code quality issues and suggest improvements
```

> 💡 **`@` 符號是做什麼用的？** `@` 符號告訴 Copilot CLI 讀取檔案。你會在第 02 章學到詳細用法。現在只要照著指令輸入即可。

---

<details>
<summary>🎬 實際運作展示</summary>

![Code Review Demo](images/code-review-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容都可能與此不同。*

</details>

---

**重點**：專業程式碼審查只需幾秒。人工審查可能要花...嗯...更多時間！

---

### 示範 2：解釋難懂程式碼

是否曾經盯著程式碼發呆，不知道它在做什麼？在 Copilot CLI 對話中試試這個：

```
> Explain what @samples/book-app-project/books.py does in simple terms
```

---

<details>
<summary>🎬 實際運作展示</summary>

![Explain Code Demo](images/explain-code-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容都可能與此不同。*

</details>

---

**發生什麼事**：（你的輸出會不同）Copilot CLI 讀取檔案、理解程式碼，並用簡單易懂的語言解釋。

```
這是一個使用 Python dataclass 的書籍收藏管理模組。

可以想像成數位書架：
- Book 是 dataclass —— 一種簡單儲存書籍資訊（書名、作者、年份、閱讀狀態）的方式
- BookCollection 管理整個收藏並負責儲存／讀取

主要組件：

1. @dataclass 裝飾器（第 8 行）
   - 自動產生 __init__、__repr__ 等方法
   - 用於乾淨定義 Python 資料結構

2. BookCollection 類別（第 16 行）
   - 維護 Book 物件清單
   - 處理 JSON 檔案 I/O 持久化
   - load_books() 從 data.json 讀取
   - save_books() 用 asdict() 寫入 data.json

3. 書籍操作：
   - add_book() —— 新增並儲存書籍
   - find_book_by_title() —— 搜尋收藏
   - mark_as_read() —— 更新閱讀狀態
   - find_by_author() —— 依作者名稱篩選

常見流程：從 JSON 讀取 → 操作 Python 物件 → 寫回 JSON
```

**重點**：複雜程式碼也能像耐心導師一樣被解釋清楚。

---

### 示範 3：產生可運作程式碼

需要一個你可能要 google 15 分鐘的函式？在同一個對話中：

```
> Write a Python function that takes a list of books and returns statistics: 
  total count, number read, number unread, oldest and newest book
```

---

<details>
<summary>🎬 實際運作展示</summary>

![Generate Code Demo](images/generate-code-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容都可能與此不同。*

</details>

---

**發生什麼事**：幾秒內產生完整、可運作的函式，你可以直接複製貼上執行。

探索完畢後，離開對話：

```
> /exit
```

**重點**：即時滿足，而且你全程都在同一個連續對話中。

---

# 模式與指令

<img src="images/modes-and-commands.png" alt="Futuristic control panel with glowing screens, dials, and equalizers representing Copilot CLI modes and commands" width="800"/>

你剛剛看到了 Copilot CLI 能做什麼。現在來了解「如何」有效使用這些能力。關鍵在於知道三種互動模式，並根據情境選擇。

> 💡 **注意**：Copilot CLI 還有一種 **自動駕駛（Autopilot）模式**，能自動執行任務而不需等待你的輸入。這很強大，但需要授權完整權限，並會自動使用 premium 請求。本課程聚焦於下方三種模式。等你熟悉基礎後，我們會再介紹自動駕駛模式。

---

## 🧩 真實世界比喻：外出用餐

把使用 GitHub Copilot CLI 想成外出用餐。從規劃行程到點餐，不同情境需要不同方式：

| 模式 | 用餐比喻 | 適用時機 |
|------|----------|----------|
| **規劃模式** | GPS 導航到餐廳 | 複雜任務——規劃路線、檢查停靠點、同意計畫再出發 |
| **互動模式** | 與服務生對話 | 探索與反覆調整——提問、客製化、即時回饋 |
| **程式化模式** | 得來速點餐 | 快速、明確任務——留在原環境，迅速取得結果 |

就像用餐一樣，你會自然學會何時用哪種方式最適合。

<img src="images/ordering-food-analogy.png" alt="Three Ways to Use GitHub Copilot CLI - Plan Mode (GPS route to restaurant), Interactive Mode (talking to waiter), Programmatic Mode (drive-through)" width="800"/>

*根據任務選擇模式：規劃模式適合先規劃流程，互動模式適合來回協作，程式化模式適合快速單次結果*

### 我應該從哪個模式開始？

**建議先從互動模式開始。**
- 可以自由嘗試並追問
- 情境會隨對話自然累積
- 用 `/clear` 很容易修正錯誤

熟悉後再嘗試：
- **程式化模式**（`copilot -p "<你的提示詞>"`）適合快速單次問題
- **規劃模式**（`/plan`）適合需要詳細規劃再開始寫程式的情境

---

## 三種模式

### 模式 1：互動模式（從這裡開始）

<img src="images/interactive-mode.png" alt="Interactive Mode - Like talking to a waiter who can answer questions and adjust the order" width="250"/>

**最適合**：探索、反覆調整、多輪對話。就像和服務生對話，可以即時回饋並調整點餐內容。

啟動互動模式：

```bash
copilot
```

如同前面示範，你會看到一個提示符號，可以自然輸入問題。想查詢可用指令，只要輸入：

```
> /help
```

**關鍵洞察**：互動模式會保留情境。每個訊息都會建立在前一個基礎上，就像真實對話。

#### 互動模式範例

```bash
copilot

> Review @samples/book-app-project/utils.py and suggest improvements

> Add type hints to all functions

> Make the error handling more robust

> /exit
```

注意每個提示都建立在前一個答案上。你是在對話，而不是每次都從頭開始。

---

### 模式 2：規劃模式

<img src="images/plan-mode.png" alt="Plan Mode - Like planning a route before a trip using GPS" width="250"/>

**最適合**：複雜任務，需要先檢查流程再執行。就像出發前用 GPS 規劃路線。

規劃模式幫你在寫程式前先產生逐步計畫。使用 `/plan` 指令，按 **Shift+Tab** 切換到規劃模式：

```bash
copilot

> /plan Add a "mark as read" command to the book app
```

> 💡 **提示**：**Shift+Tab** 可在模式間切換：互動 → 規劃 → 自動駕駛。任何時候都能在互動模式中按此鍵切換，不需輸入指令。

你也可以直接用 `--plan` 旗標啟動 Copilot CLI 的規劃模式：

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

**關鍵洞察**：規劃模式讓你在寫程式前先檢查並修改流程。計畫完成後，還能請 Copilot CLI 把計畫存成檔案，例如「Save this plan to `mark_as_read_plan.md`」會建立一個包含計畫細節的 markdown 檔。

> 💡 **想要更複雜的計畫？** 試試：`/plan Add search and filter capabilities to the book app`。規劃模式可從簡單功能擴展到完整應用程式。

> 📚 **自動駕駛模式**：你可能注意到 Shift+Tab 會切換到第三種模式——**自動駕駛（Autopilot）**。在自動駕駛模式下，Copilot 會自動執行整個計畫，不需每步都等你確認——就像把任務交給同事並說「完成後再通知我」。典型流程是規劃 → 同意 → 自動駕駛，因此你要先熟悉寫計畫。也可以用 `copilot --autopilot` 直接啟動。建議先熟悉互動與規劃模式，再參考 [官方文件](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot)。

---

### 模式 3：程式化模式

<img src="images/programmatic-mode.png" alt="Programmatic Mode - Like using a drive-through for a quick order" width="250"/>

**最適合**：自動化、腳本、CI/CD、單次指令。就像得來速點餐，不需和服務生對話。

用 `-p` 旗標執行一次性指令，不需互動：

```bash
# 產生程式碼
copilot -p "Write a function that checks if a number is even or odd"

# 快速查詢
copilot -p "How do I read a JSON file in Python?"
```

**關鍵洞察**：程式化模式給你快速答案並自動結束。不需對話，只要輸入 → 輸出。

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
> ⚠️ **關於 `--allow-all`**：此旗標會跳過所有權限提示，讓 Copilot CLI 可讀取檔案、執行指令、存取網址而不需確認。這對程式化模式（`-p`）很重要，因為沒有互動對話可批准動作。只在你自己寫的提示詞、信任的目錄下使用。不要用於不信任的輸入或敏感目錄。

</details>

---

## 必備斜線指令

這些指令很適合剛開始學 Copilot CLI 時熟悉：

| 指令 | 功能說明 | 適用時機 |
|------|----------|----------|
| `/ask` | 快速提問，不會影響對話歷史 | 想要快速答案又不想干擾目前任務時 |
| `/clear` | 清除對話，重新開始 | 換主題時 |
| `/help` | 顯示所有可用指令 | 忘記指令時 |
| `/model` | 顯示或切換 AI 模型 | 想換模型時 |
| `/plan` | 寫程式前先規劃流程 | 複雜功能時 |
| `/research` | 用 GitHub 與網路來源深度研究 | 寫程式前需要調查主題時 |
| `/exit` | 結束對話 | 完成時 |

> 💡 **`/ask` 與一般對話差異**：通常你每次輸入的訊息都會成為持續對話的一部分，影響後續回應。`/ask` 是「不記錄」的捷徑——適合像 `/ask What does YAML mean?` 這種快速單次提問，不會污染你的對話情境。

這就是入門的全部！熟悉後可以探索更多指令。

> 📚 **官方文件**：[CLI 指令參考](https://docs.github.com/copilot/reference/cli-command-reference) 可查詢完整指令與旗標列表。

<details>
<summary>📚 <strong>其他指令</strong>（點擊展開）</summary>

> 💡 上述必備指令涵蓋日常大部分操作。這份參考適合你準備探索更多功能時使用。

### Agent 環境

| 指令 | 功能說明 |
|------|----------|
| `/agent` | 瀏覽並選擇可用的 Agent |
| `/env` | 顯示已載入的環境細節——有哪些指令、MCP 伺服器、技能、Agent、外掛 |
| `/init` | 初始化 Copilot 指令到你的 repo |
| `/mcp` | 管理 MCP 伺服器設定 |
| `/skills` | 管理技能，增強能力 |

> 💡 Agent 介紹在 [第 04 章](../04-agents-custom-instructions/README.md)，技能在 [第 05 章](../05-skills/README.md)，MCP 伺服器在 [第 06 章](../06-mcp-servers/README.md)。

### 模型與子 Agent

| 指令 | 功能說明 |
|------|----------|
| `/delegate` | 交由 GitHub Copilot 雲端 Agent 處理任務 |
| `/fleet` | 將複雜任務拆分為平行子任務，加速完成 |
| `/model` | 顯示或切換 AI 模型 |
| `/tasks` | 查看背景子 Agent 與分離 shell 對話 |

### 程式碼

| 指令 | 功能說明 |
|------|----------|
| `/diff` | 審查目前目錄的變更 |
| `/pr` | 操作目前分支的 pull request |
| `/research` | 用 GitHub 與網路來源進行深度研究 |
| `/review` | 執行程式碼審查 Agent 分析變更 |
| `/terminal-setup` | 啟用多行輸入（shift+enter 與 ctrl+enter） |

### 權限

| 指令 | 功能說明 |
|------|----------|
| `/add-dir <directory>` | 將目錄加入允許清單 |
| `/allow-all [on|off|show]` | 自動批准所有權限提示；用 `on` 啟用、`off` 關閉、`show` 檢查目前狀態 |
| `/yolo` | `/allow-all on` 的快速別名——自動批准所有權限提示 |
| `/cwd`, `/cd [directory]` | 查看或切換工作目錄 |
| `/list-dirs` | 顯示所有允許目錄 |

> ⚠️ **請小心使用**：`/allow-all` 與 `/yolo` 會跳過確認提示。適合信任專案，但對不信任程式碼要小心。

### 對話

| 指令 | 功能說明 |
|------|----------|
| `/clear` | 放棄目前對話（不儲存歷史），重新開始 |
| `/compact` | 對話摘要，減少情境用量 |
| `/context` | 顯示情境窗口 token 用量與視覺化 |
| `/new` | 結束目前對話（儲存到歷史以便搜尋／繼續），重新開始 |
| `/resume` | 切換到其他對話（可指定對話 ID） |
| `/rename` | 重新命名目前對話（省略名稱則自動產生） |
| `/rewind` | 開啟時間軸選擇器，回到對話任意早期點 |
| `/usage` | 顯示對話用量與統計資料 |
| `/session` | 顯示對話資訊與工作區摘要 |
| `/share` | 將對話匯出為 markdown 檔、GitHub gist 或自包含 HTML 檔 |

### 說明與回饋

| 指令 | 功能說明 |
|------|----------|
| `/changelog` | 顯示 CLI 版本更新紀錄 |
| `/feedback` | 提交回饋給 GitHub |
| `/help` | 顯示所有可用指令 |
| `/theme` | 查看或設定終端機主題 |

### 快速 shell 指令

直接在 Copilot CLI 前綴 `!` 執行 shell 指令，不經 AI 處理：

```bash
copilot

> !git status
# 直接執行 git status，不經 AI

> !python -m pytest tests/
# 直接執行 pytest
```

### 切換模型

Copilot CLI 支援多種 AI 模型（OpenAI、Anthropic、Google 等）。可用模型取決於你的訂閱方案與地區。用 `/model` 查詢並切換：

```bash
copilot
> /model

# 顯示可用模型並讓你選擇。選擇 Sonnet 4.5。
```

> 💡 **提示**：有些模型會消耗更多「premium 請求」。標記 **1x**（如 Claude Sonnet 4.5）的模型很適合預設使用，既強大又高效。倍率較高的模型會更快用完 premium 配額，建議留給真正需要時再用。

</details>

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

是時候將學到的內容實際操作了。

---

## ▶️ 自己動手試試

### 互動探索

啟動 Copilot 並用追問提示反覆改善書籍應用程式：

```bash
copilot

> Review @samples/book-app-project/book_app.py - what could be improved?

> Refactor the if/elif chain into a more maintainable structure

> Add type hints to all the handler functions

> /exit
```

### 規劃功能

用 `/plan` 讓 Copilot CLI 在寫程式前先規劃實作流程：

```bash
copilot

> /plan Add a search feature to the book app that can find books by title or author

# 檢查計畫
# 同意或修改
# 觀察逐步實作
```

### 用程式化模式自動化

`-p` 旗標讓你直接在終端機執行 Copilot CLI，不需進入互動模式。從 repo 根目錄複製貼上下列腳本，批次審查書籍應用程式所有 Python 檔案。

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

1. **互動挑戰**：啟動 `copilot` 並探索書籍應用程式。詢問 `@samples/book-app-project/books.py`，連續要求改善三次。
2. **規劃模式挑戰**：執行 `/plan Add rating and review features to the book app`。仔細閱讀計畫，是否合理？
3. **程式化挑戰**：執行 `copilot --allow-all -p "List all functions in @samples/book-app-project/book_app.py and describe what each does"`。第一次就成功嗎？

---

## 💡 提示：用網頁或手機遠端控制 CLI 對話

GitHub Copilot CLI 支援 **遠端對話**，讓你能在網頁瀏覽器（桌機或手機）或 GitHub Mobile app 上監控並互動，不需親自在終端機操作。

用 `--remote` 旗標啟動遠端對話：

```bash
copilot --remote
```

Copilot CLI 會顯示連結並提供 QR code。用手機或桌機瀏覽器開啟連結，即可即時觀看對話、追問提示、檢查計畫、遠端操控 Agent。每個 session 都是使用者專屬，只能存取自己的 Copilot CLI 對話。

也可以在任何進行中的對話隨時啟用遠端存取：

```
> /remote
```

更多遠端對話細節請參考 [Copilot CLI 文件](https://docs.github.com/copilot/how-tos/copilot-cli/steer-remotely)。

---

## 📝 作業

### 主題挑戰：改善書籍應用程式的工具函式

前面示範聚焦於審查與重構 `book_app.py`。現在請你練習同樣技巧於另一個檔案 `utils.py`：

1. 啟動互動對話：`copilot`
2. 請 Copilot CLI 摘要檔案內容：`@samples/book-app-project/utils.py What does each function in this file do?`
3. 請它加上輸入驗證：「Add validation to `get_user_choice()` so it handles empty input and non-numeric entries」
4. 請它改善錯誤處理：「What happens if `get_book_details()` receives an empty string for the title? Add guards for that.」
5. 請它加上 docstring：「Add a comprehensive docstring to `get_book_details()` with parameter descriptions and return values」
6. 觀察情境如何在提示間傳遞，每次改善都建立在前一次基礎上
7. 用 `/exit` 結束

**成功標準**：你應該得到一份改善過的 `utils.py`，包含輸入驗證、錯誤處理與 docstring，全部透過多輪對話完成。

<details>
<summary>💡 提示（點擊展開）</summary>

**可嘗試的範例提示詞：**
```bash
> @samples/book-app-project/utils.py What does each function in this file do?
> Add validation to get_user_choice() so it handles empty input and non-numeric entries
> What happens if get_book_details() receives an empty string for the title? Add guards for that.
> Add a comprehensive docstring to get_book_details() with parameter descriptions and return values
```

</details>
**常見問題：**
- 如果 Copilot CLI 提問澄清問題，只需自然回答即可
- 情境會延續，因此每個提示都會建立在前一次的基礎上
- 若想重新開始，請使用 `/clear`

</details>

### 加分挑戰：比較三種模式

範例中使用 `/plan` 來設計搜尋功能，並用 `-p` 進行批次審查。現在請在同一個新任務上嘗試三種模式：為 `BookCollection` 類別新增 `list_by_year()` 方法：

1. **互動模式**：`copilot` → 逐步請 Copilot 設計並建立此方法
2. **計畫模式**：`/plan Add a list_by_year(start, end) method to BookCollection that filters books by publication year range`
3. **程式化模式**：`copilot --allow-all -p "@samples/book-app-project/books.py Add a list_by_year(start, end) method that returns books published between start and end year inclusive"`

**反思**：哪一種模式最自然？你會在什麼情境下使用各種模式？

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生狀況 | 修正方式 |
|------|----------|----------|
| 輸入 `exit` 而非 `/exit` | Copilot CLI 將 "exit" 視為提示詞，而非指令 | 斜線指令皆以 `/` 開頭 |
| 使用 `-p` 進行多輪對話 | 每次 `-p` 呼叫都是獨立的，無法記憶前一次內容 | 若需延續情境，請用互動模式（`copilot`） |
| 忘記用引號包住含 `$` 或 `!` 的提示詞 | Shell 會先解析特殊字元，Copilot CLI 無法收到完整內容 | 用引號包住提示：`copilot -p "What does $HOME mean?"` |

### 疑難排解

**「模型不可用」**－你的訂閱方案可能不包含所有模型。請用 `/model` 查看可用模型。

**「情境過長」**－你的對話已用滿情境窗口。請用 `/clear` 重設，或開始新會話。

**「超過速率限制」**－請稍等幾分鐘再試。若需批次操作且有延遲，可考慮用程式化模式。

</details>

---

# 摘要

## 🔑 重點整理

1. **互動模式**適合探索與反覆嘗試——情境會延續。就像和一個記得你說過什麼的人對話。
2. **計畫模式**通常用於較複雜的任務。先審查再實作。
3. **程式化模式**適合自動化。不需互動。
4. **基本指令**（`/ask`, `/help`, `/clear`, `/plan`, `/research`, `/model`, `/exit`）涵蓋日常大部分需求。

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

現在你已了解三種模式，接下來學習如何讓 Copilot CLI 知道你的程式碼情境。

在 **[第 02 章：情境與對話](../02-context-conversations/README.md)**，你將學到：

- 用 `@` 語法引用檔案與目錄
- 用 `--resume` 和 `--continue` 管理會話
- 情境管理如何讓 Copilot CLI 真正強大

---

**[← 回到課程首頁](../README.md)** | **[繼續前往第 02 章 →](../02-context-conversations/README.md)**
