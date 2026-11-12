![Chapter 01: First Steps](assets/chapter-header.png)

> **觀看 AI 如何即時找出錯誤、解釋難懂的程式碼，並產生可運作的腳本。接著學會使用 GitHub Copilot CLI 的三種模式。**

魔法就在這一章開始！你將親身體驗為什麼開發者形容 GitHub Copilot CLI 就像隨時可聯絡的資深工程師。你會看到 AI 在幾秒內找出安全漏洞、用簡單易懂的英文解釋複雜程式碼，並立即產生可運作的腳本。然後你將學會三種互動模式（互動、規劃、程式化），讓你清楚知道每個任務該用哪一種。

> ⚠️ **先決條件**：請先完成 **[第 00 章：快速開始](../00-quick-start/README.md)**。你必須已安裝並驗證 GitHub Copilot CLI，才能執行下方的示範。

## 🎯 學習目標

在本章結束時，你將能夠：

- 透過實作示範體驗 GitHub Copilot CLI 帶來的生產力提升
- 為每個任務選擇正確的模式（互動、規劃或程式化）
- 使用 slash 指令控制你的會話

> ⏱️ **預估時間**：約 45 分鐘（閱讀 15 分鐘 + 實作 30 分鐘）

---

# 你的第一次 Copilot CLI 體驗

<img src="assets/first-copilot-experience.png" alt="Developer sitting at a desk with code on the monitor and glowing particles representing AI assistance" width="800"/>

直接動手，看看 Copilot CLI 能做什麼。

---

## 先暖身：你的第一個提示詞

在進入精彩的示範之前，先從一些你現在就能嘗試的簡單提示詞開始。**不需要任何程式碼儲存庫**！只要打開終端機並啟動 Copilot CLI：

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

不會用 Python？沒關係！直接問你慣用語言的問題即可。

你會發現這種互動非常自然。就像和同事聊天一樣問問題。探索結束後，輸入 `/exit` 離開會話。

**關鍵觀念**：GitHub Copilot CLI 是對話式的。你不需要特殊語法，只要用自然語言提問即可。

## 實際運作看看

現在來看看為什麼開發者會說這就像「隨時可聯絡的資深工程師」。

> 📖 **閱讀範例說明**：以 `>` 開頭的行是在 Copilot CLI 互動會話中輸入的提示詞。沒有 `>` 前綴的行則是在終端機執行的 shell 指令。

> 💡 **關於範例輸出**：本課程中的範例輸出僅供參考。由於 Copilot CLI 每次回應都可能不同，你的結果在措辭、格式和細節上都會有所差異。請專注於*回傳資訊的類型*，而非完全相同的文字。

### 示範 1：幾秒內完成程式碼審查

本課程提供了帶有刻意品質問題的範例檔案。如果你在本機操作且尚未 clone 儲存庫，請執行下方的 `git clone` 指令，進入 `copilot-cli-for-beginners` 資料夾，然後啟動 `copilot`。

```bash
# 如果你在本機操作且尚未 clone，請先複製課程儲存庫
git clone https://github.com/github/copilot-cli-for-beginners
cd copilot-cli-for-beginners

# 啟動 Copilot
copilot
```

進入 Copilot CLI 互動會話後，執行下列指令：

```
> Review @samples/book-app-project/book_app.py for code quality issues and suggest improvements
```

> 💡 **`@` 符號的用途？** `@` 符號告訴 Copilot CLI 讀取一個檔案。你會在第 02 章學到更多，現在只要照著指令輸入即可。

---

<details>
<summary>🎬 實際運作畫面！</summary>

![Code Review Demo](assets/code-review-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容可能與此不同。*

</details>

---

**重點**：專業的程式碼審查只需幾秒。手動審查會花……遠比這久的時間！

---

### 示範 2：解釋難懂的程式碼

是否曾經盯著程式碼發呆，不知道它在做什麼？在 Copilot CLI 會話中試試這個：

```
> Explain what @samples/book-app-project/books.py does in simple terms
```

---

<details>
<summary>🎬 實際運作畫面！</summary>

![Explain Code Demo](assets/explain-code-demo.gif)

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

**重點**：複雜的程式碼也能像耐心的導師一樣解釋給你聽。

---

### 示範 3：產生可運作的程式碼

需要一個你本來要 Google 15 分鐘的函式？繼續在會話中輸入：

```
> Write a Python function that takes a list of books and returns statistics: 
  total count, number read, number unread, oldest and newest book
```

---

<details>
<summary>🎬 實際運作畫面！</summary>

![Generate Code Demo](assets/generate-code-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容可能與此不同。*

</details>

---

**會發生什麼事**：幾秒內產生完整、可運作的函式，直接複製貼上即可執行。

探索完畢後，離開會話：

```
> /exit
```

**重點**：立即滿足需求，而且全程都在同一個會話中。

---

# 模式與指令

<img src="assets/modes-and-commands.png" alt="Futuristic control panel with glowing screens, dials, and equalizers representing Copilot CLI modes and commands" width="800"/>

你已經看過 Copilot CLI 的強大功能。現在來了解*如何*有效運用這些能力。關鍵在於知道不同情境該用哪一種互動模式。

> 💡 **注意**：Copilot CLI 也有一種 **Autopilot** 模式，可以自動執行任務而不等待你的輸入。這很強大，但需要授予完整權限，並會自動使用 premium 請求。本課程聚焦於下方三種模式。等你熟悉基本操作後，我們會再介紹 Autopilot。

---

## 🧩 真實世界比喻：外出用餐

把使用 GitHub Copilot CLI 想像成外出用餐。從規劃行程到點餐，不同情境需要不同方式：

| 模式 | 用餐比喻 | 適用時機 |
|------|----------------|-------------|
| **規劃** | 用 GPS 規劃去餐廳的路線 | 複雜任務——先規劃路線、檢查停靠點、同意計畫，再出發 |
| **互動** | 和服務生對話 | 探索與反覆調整——問問題、客製化、即時回饋 |
| **程式化** | 得來速點餐 | 快速、明確的任務——留在原本環境，迅速取得結果 |

就像外出用餐一樣，你會自然學會每種方式適合什麼情境。

<img src="assets/ordering-food-analogy.png" alt="Three Ways to Use GitHub Copilot CLI - Plan Mode (GPS route to restaurant), Interactive Mode (talking to waiter), Programmatic Mode (drive-through)" width="800"/>

*根據任務選擇模式：規劃用於先規劃路線，互動用於雙向協作，程式化用於快速一次性結果*

### 我該從哪個模式開始？

**從互動模式開始。** 
- 你可以自由嘗試並追問
- 情境會隨對話自然累積
- 出錯也能用 `/clear` 輕鬆重來

熟悉後，可以嘗試：
- **程式化模式**（`copilot -p "<your prompt>"`）適合快速、一次性的問題
- **規劃模式**（`/plan`）適合需要事前詳細規劃的任務

---

## 三種模式

### 模式 1：互動模式（建議先從這裡開始）

<img src="assets/interactive-mode.png" alt="Interactive Mode - Like talking to a waiter who can answer questions and adjust the order" width="250"/>

**最適合**：探索、反覆調整、多輪對話。就像和服務生對話，能即時回應、調整需求。

啟動互動會話：

```bash
copilot
```

如同前面所見，你會看到一個提示符，能自然輸入問題。想查詢可用指令，只要輸入：

```
> /help
```

**關鍵觀念**：互動模式會保留情境。每則訊息都會建立在前一則之上，就像真實對話。

#### 互動模式範例

```bash
copilot

> Review @samples/book-app-project/utils.py and suggest improvements

> Add type hints to all functions

> Make the error handling more robust

> /exit
```

你會發現每個提示詞都建立在前一個答案之上。這是一場對話，而不是每次都從頭開始。

---

### 模式 2：規劃模式

<img src="assets/plan-mode.png" alt="Plan Mode - Like planning a route before a trip using GPS" width="250"/>

**最適合**：需要在執行前先檢查方案的複雜任務。就像出發前用 GPS 規劃路線。

規劃模式會幫你在寫程式前先產生逐步計畫。使用 `/plan` 指令，按下 **Shift+Tab** 可切換到規劃模式：

```bash
copilot

> /plan Add a "mark as read" command to the book app
```

> 💡 **小技巧**：**Shift+Tab** 可在模式間循環切換：互動 → 規劃 → Autopilot。隨時在互動會話中按下即可，不必輸入指令。

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

**關鍵觀念**：規劃模式讓你在寫程式前先檢查和修改方案。在規劃模式下，Copilot CLI 是**唯讀**的，不會修改任何檔案或執行會改變工作區的指令，直到你同意並進入實作階段。這讓你能安全地停留在「思考」階段，直到準備好為止。計畫完成後，你甚至可以請 Copilot CLI 把它存成檔案，例如「Save this plan to `mark_as_read_plan.md`」就會產生一份包含計畫細節的 markdown 檔案。

> 💡 **想挑戰更複雜的任務？** 試試：`/plan Add search and filter capabilities to the book app`。規劃模式可從簡單功能一路擴展到完整應用程式。

> 📚 **Autopilot 模式**：你可能注意到 Shift+Tab 會切換到第三種模式 **Autopilot**。在 autopilot 模式下，Copilot 會自動執行整個計畫，不會在每個步驟等你確認——就像把任務交給同事並說「做完再告訴我」。典型流程是規劃 → 同意 → autopilot，也就是你必須先會寫計畫。你也可以用 `copilot --autopilot` 直接啟動，或用 `/autopilot <objective>`（例如 `/autopilot Add a search command to the book app`）設定目標。也能用 `copilot --plan --mode autopilot` 結合規劃與 autopilot，先產生計畫再自動執行。建議先熟悉互動與規劃模式，準備好後再參考 [官方文件](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot)。

---

### 模式 3：程式化模式

<img src="assets/programmatic-mode.png" alt="Programmatic Mode - Like using a drive-through for a quick order" width="250"/>

**最適合**：自動化、腳本、CI/CD、單次指令。就像得來速點餐，不用和服務生對話。

用 `-p` 旗標執行一次性、無需互動的指令：

```bash
# 產生程式碼
copilot -p "Write a function that checks if a number is even or odd"

# 快速查詢
copilot -p "How do I read a JSON file in Python?"
```

**關鍵觀念**：程式化模式給你快速答案並結束。不會對話，只有輸入 → 輸出。

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
> ⚠️ **關於 `--allow-all`**：這個旗標會跳過所有權限提示，讓 Copilot CLI 可直接讀取檔案、執行指令、存取 URL。這對程式化模式（`-p`）很重要，因為沒有互動會話可供你確認。只在你自己寫的提示詞和信任的目錄下使用 `--allow-all`。千萬不要用在不信任的輸入或敏感目錄。

</details>

---

## 必學 Slash 指令

這些指令很適合剛開始學 Copilot CLI 時先熟悉：

| 指令 | 功能說明 | 適用時機 |
|---------|--------------|-------------|
| `/ask` | 提問但不影響對話歷史 | 想快速獲得答案又不想干擾目前任務時 |
| `/clear` | 清除對話並重新開始 | 換主題時 |
| `/config` | 查看或設定持久化預設值（如預設模型） | 想讓設定套用到所有未來會話時 |
| `/help` | 顯示所有可用指令 | 忘記指令時 |
| `/model` | 顯示或切換目前會話的 AI 模型 | 想更換 AI 模型時 |
| `/plan` | 在寫程式前先規劃工作 | 複雜功能時 |
| `/refine` | 將雜亂的提示詞重寫成清楚、聚焦的內容 | 提示詞寫得不夠精確時 |
| `/research` | 深度研究 GitHub 與網路資源 | 需要先調查主題再寫程式時 |
| `/exit` | 結束會話 | 完成時 |

> 💡 **`/ask` 與一般聊天的差異**：一般訊息都會成為對話的一部分並影響後續回應。`/ask` 則是「不留紀錄」的捷徑，適合像 `/ask What does YAML mean?` 這種不想污染會話情境的快速提問。

> 💡 **`/refine` 幫你優化提示詞**：不確定提示詞是否夠清楚？先隨意輸入，再用 `/refine` 讓 Copilot 幫你重寫成精確、結構良好的提示詞。這對剛接觸 AI 工具、還不熟悉如何寫好提示詞時特別有用。

> 💡 **Tab 自動補全**：輸入 slash 指令時，按 **Tab** 可自動補全指令名稱或在子指令、參數間循環。忘記指令名稱時特別方便。

> 💡 **Copilot 忙碌時也能排隊輸入提示詞**：如果 Copilot 正在執行任務，你想到下一步想做什麼，直接輸入並按 Enter 即可。Copilot 會在目前任務結束後自動執行，不用等它閒下來。

這就是入門的全部內容！熟悉後可以探索更多指令。

> 📚 **官方文件**：[CLI 指令參考](https://docs.github.com/copilot/reference/cli-command-reference) 提供完整指令與旗標清單。

<details>
<summary>📚 <strong>進階指令</strong>（點擊展開）</summary>

> 💡 上述必學指令已涵蓋日常大部分需求。這份參考適合你準備好進一步探索時查閱。

### Agent 環境

| 指令 | 功能說明 |
|---------|--------------|
| `/agent` | 瀏覽並選擇可用的 Agent |
| `/env` | 顯示已載入的環境細節——有哪些指令、MCP 伺服器、Skill、Agent 與外掛啟用中 |
| `/init` | 為你的儲存庫初始化 Copilot 指令 |
| `/instructions` | 檢視並管理目前會話已載入的所有指令檔 |
| `/mcp` | 開啟外掛儀表板（聚焦於 MCP 伺服器）；用 `/mcp config` 啟動 MCP 設定精靈 |
| `/plugin` | 開啟外掛儀表板，瀏覽、安裝、啟用與更新外掛 |
| `/settings` | 開啟互動式對話方塊，一次瀏覽與編輯所有使用者設定 |
| `/skills` | 開啟外掛儀表板（聚焦於 Skill），探索與管理技能 |
| `/subagents` | 檢視並管理目前會話中執行的子 Agent |

> 💡 Agent 相關內容詳見 [第 04 章](../04-agents-custom-instructions/README.md)，Skill 相關內容詳見 [第 05 章](../05-skills/README.md)，MCP 伺服器詳見 [第 06 章](../06-mcp-servers/README.md)。

### 模型與子 Agent

| 指令 | 功能說明 |
|---------|--------------|
| `/config` | 查看或設定持久化預設值（如 `/config model` 設定所有未來會話的預設模型） |
| `/delegate` | 將任務交給 GitHub Copilot 雲端 Agent |
| `/fleet` | 將複雜任務拆分成多個子任務並行處理，加速完成 |
| `/model` | 僅切換目前會話的 AI 模型 |
| `/tasks` | 檢視背景子 Agent 與分離的 shell 會話 |

### 程式碼

| 指令 | 功能說明 |
|---------|--------------|
| `/code` | 在 VS Code 開啟目前會話（需安裝 VS Code） |
| `/diff` | 審查目前目錄的變更內容 |
| `/pr` | 操作目前分支的 Pull Request |
| `/research` | 透過 GitHub 與網路資源進行深度研究 |
| `/review` | 執行程式碼審查 Agent 分析變更 |
| `/terminal-setup` | 啟用多行輸入支援（shift+enter 與 ctrl+enter） |

### 權限

| 指令 | 功能說明 |
|---------|--------------|
| `/add-dir <directory>` | 將目錄加入允許清單 |
| `/allow-all [on\|off\|show]` | 自動同意所有權限提示；用 `on` 啟用，`off` 關閉，`show` 查詢狀態 |
| `/permissions` | 切換審核模式（互動、規劃、autopilot），控制 Copilot 可自動執行的範圍 |
| `/yolo` | `/allow-all on` 的快速別名——自動同意所有權限提示 |
| `/cwd`, `/cd [directory]` | 查看或切換工作目錄 |
| `/list-dirs` | 顯示所有允許的目錄 |

> ⚠️ **請小心使用**：`/allow-all` 與 `/yolo` 會跳過確認提示。適合信任的專案，但對不信任的程式碼要特別小心。

### 會話

| 指令 | 功能說明 |
|---------|--------------|
| `/clear` | 放棄目前會話（不儲存歷史）並開始新對話 |
| `/compact` | 摘要對話內容以減少情境用量（可加聚焦指令，如 `/compact focus on the bug list`） |
| `/context` | 顯示情境視窗 token 用量與視覺化圖表 |
| `/keep-alive` | 防止 Copilot CLI 執行時系統進入睡眠——適合筆電長時間任務 |
| `/memory [on\|off\|show]` | 啟用、停用或檢視持久記憶——跨所有會話記住事實與偏好 |
| `/new` | 結束目前會話（儲存到歷史以便搜尋／繼續）並開始新對話 |
| `/resume` | 切換到其他會話（可指定會話 ID 或名稱） |
| `/rename` | 重新命名目前會話（不加名稱則自動產生） |
| `/rewind` | 開啟時間軸選擇器，回溯到對話早期任何時點；可選擇還原 Copilot 修改過的檔案（即使沒用 git 也可用） |
| `/usage` | 顯示會話用量統計，包括配額進度條 |
| `/session` | 顯示會話資訊與工作區摘要；用 `/session delete`、`/session delete <id>` 或 `/session delete-all` 刪除會話 |
| `/share` | 匯出會話為 markdown 檔、GitHub gist 或自包含 HTML 檔 |
| `/every <interval> <prompt>` | 排程提示詞定期執行（如 `/every 1h summarize new commits`）。間隔可用自然語言。`/loop` 是 `/every` 的別名。 |
| `/after <time> <prompt>` | 排程提示詞延遲執行一次（如 `/after 30m run tests`）。時間可用自然語言。 |

> 💡 **Sessions 分頁**：Copilot CLI 互動 UI 頂部有 **Sessions 分頁**。你可以用它同時檢視並切換多個會話。在 Sessions 分頁按 `n` 可開新會話而不關閉現有會話。

### 顯示

| 指令 | 功能說明 |
|---------|--------------|
| `/statusline`（或 `/footer`） | 自訂狀態列顯示哪些項目（目錄、分支、effort、情境視窗、配額） |
| `/theme` | 查看或設定終端機主題 |
| `/vim` | 啟用或停用 Vim 模式，在編輯器中用 vim 鍵綁定（如 `hjkl` 移動，`i`、`a`、`o` 插入模式） |
| `/voice` | 用本地語音辨識輸入提示詞——直接說話而非打字 |

### 說明與回饋

| 指令 | 功能說明 |
|---------|--------------|
| `/app` | 直接從 CLI 開啟 GitHub app（或瀏覽器備用） |
| `/changelog` | 顯示 CLI 版本更新紀錄 |
| `/feedback` | 提交回饋給 GitHub |
| `/help` | 顯示所有可用指令 |

### 快速 Shell 指令

在提示詞前加 `!` 可直接執行 shell 指令，不經 AI 處理：

```bash
copilot

> !git status
# 直接執行 git status，不經 AI

> !python -m pytest tests/
# 直接執行 pytest
```

### 切換模型

Copilot CLI 支援多種來自 OpenAI、Anthropic、Google 等的 AI 模型。你能用哪些模型取決於你的訂閱等級與地區。用 `/model` 查看選項並切換：

```bash
copilot
> /model

# 顯示可用模型並讓你選擇。例如：GPT-6 Sol、GPT-6 Luna、Claude Sonnet 5.5、Claude Opus 5.5。
```

> 💡 **會話 vs. 持久模型**：`/model` 指令只會改變**目前會話**的模型。新會話會回到預設。若要設定所有未來會話的預設模型，請在會話中用 `/config model`，或直接在 shell 用 `copilot config` 指令（不需進入會話）：```bash
# 從終端機設定你的預設模型（在 Copilot 會話之外）
copilot config set model claude-sonnet-5.5

# 檢視你所有儲存的設定
copilot config list

# 移除設定並恢復為預設值
copilot config remove model
```

> 💡 **提示**：Copilot CLI 的使用量是以 **GitHub AI 點數** 計算。所消耗的點數取決於你選擇的模型，以及任務所用的 token 數量。功能越強大的模型可能花費越多，因此日常任務建議使用輕量模型，將強大的推理模型留給複雜工作。執行 `/usage` 可查看目前會話已用多少 AI 點數。

> 💡 **不確定要選哪個模型？** 從模型選擇器中選擇 **`Auto`**，讓 Copilot 自動為每次會話挑選最佳可用模型。如果你剛開始使用、不想煩惱模型選擇，這是很棒的預設選項。

> 💡 **模型家族捷徑**：你也可以直接在 `/model` 選擇器中輸入簡短的家族別名——像是 `opus`、`sonnet`、`haiku`、`gpt` 或 `gemini`——而不用從完整清單中捲動選擇。Copilot 會自動為你挑選該家族中最佳可用模型。

> 💡 **模型選擇器導覽**：模型選擇器現在會將模型分組顯示——**最近使用**、**推薦**、**新上架**——讓你能快速找到上次用過的模型，或嘗試最新推出的選項。在選擇器中可用 **Shift+Tab** 切換分組檢視。

### 自動路由層級

Copilot CLI 內建 **Auto** 路由層級，能智慧地為每個任務挑選最佳模型：

```bash
copilot

> /model
# 選擇 "Auto"，讓 Copilot 根據速度與成本自動挑選最佳模型
```

自動路由會根據你的任務複雜度，在快速（輕量）與強大（具推理能力）模型間做平衡選擇。如果你的組織有設定受管的 Auto 政策，你可能會看到 **Strict** 模式或允許使用者覆寫的路由偏好選項。

> 💡 **新模型上線**：Copilot CLI 現在支援 **GPT-6 Astra**、**GPT-6.1 Sol**、**GPT-6 Luna**、**Claude Opus 5.5**，以及既有模型。快到 `/model` 選擇器中試試看！

### 使用 `copilot config` 管理設定

除了互動式 `/config` slash 指令外，你也可以用 `copilot config` 指令，直接從終端機管理 Copilot CLI 設定：

```bash
# 列出所有目前設定
copilot config list

# 讀取特定設定
copilot config read model
copilot config read editorMode

# 設定預設值
copilot config set model opus        # 將預設模型設為 Claude Opus
copilot config set editorMode vim    # 預設啟用 Vim 模式

# 移除自訂設定（恢復預設值）
copilot config remove model
```

這對於撰寫腳本、設定新機器，或在互動會話之外管理設定很有用。用 `copilot config` 管理的設定會儲存在 `~/.copilot/config.json`，並套用到所有未來會話。

### 自訂 Transcript 檢視模式

你可以透過設定 transcript 檢視模式，控制 Copilot 如何顯示工具活動與推理過程：

```bash
copilot

> /settings
# 找到 "Transcript view" 選項，設為 "concise"

# 或直接在 ~/.copilot/config.json 設定：
# "transcriptView": "concise"
```

**檢視選項：**
- **Default**：展開顯示所有工具呼叫與推理步驟
- **Concise**：將相關工具活動分組為可收合的工作摘要，減少視覺雜訊，同時保留細節可查

精簡檢視很適合想專注於高層進度、不想被中間步驟淹沒時使用。

### 會話前環境選擇

啟動 Copilot CLI 時，現在可以在第一個提示前切換 **本地** 或 **雲端** 執行模式：

```bash
copilot
# Copilot 啟動後，按 Ctrl+E 開啟環境選擇器
# 選擇：Local（在本機執行）或 Cloud（遠端執行）
```

這功能很適合你在不同工作型態間切換——像是在本機互動作業，或讓背景任務跑在雲端。你的選擇會套用到本次會話，直到你再次切換。

</details>

---

# 練習

<img src="../assets/practice.png" alt="溫暖桌面擺設，螢幕顯示程式碼、檯燈、咖啡杯與耳機，準備動手練習" width="800"/>

是時候把你學到的知識實際操作一遍了。

---

## ▶️ 自己動手試試看

### 互動式探索

啟動 Copilot，並用後續提示詞反覆優化書籍應用程式：

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
# 核准或修改
# 觀察它逐步實作
```

### 用程式化模式自動化

`-p` 旗標讓你直接從終端機執行 Copilot CLI 指令，無需進入互動模式。將下列腳本複製貼到終端機（不是 Copilot 內），從專案根目錄批次檢查書籍應用程式所有 Python 檔案。

```bash
# 檢查書籍應用程式所有 Python 檔案
for file in samples/book-app-project/*.py; do
  echo "Reviewing $file..."
  copilot --allow-all -p "Quick code quality review of @$file - critical issues only"
done
```

**PowerShell (Windows)：**

```powershell
# 檢查書籍應用程式所有 Python 檔案
Get-ChildItem samples/book-app-project/*.py | ForEach-Object {
  $relativePath = "samples/book-app-project/$($_.Name)";
  Write-Host "Reviewing $relativePath...";
  copilot --allow-all -p "Quick code quality review of @$relativePath - critical issues only" 
}
```

---

完成示範後，試試這些變化：

1. **互動挑戰**：啟動 `copilot` 並探索書籍應用程式。詢問 `@samples/book-app-project/books.py`，連續請求三次改進建議。
2. **規劃模式挑戰**：執行 `/plan Add rating and review features to the book app`。仔細閱讀規劃內容，看看是否合理。
3. **程式化挑戰**：執行 `copilot --allow-all -p "List all functions in @samples/book-app-project/book_app.py and describe what each does"`。第一次就成功了嗎？

---

## 💡 提示：用網頁或手機遠端控制 CLI 會話

GitHub Copilot CLI 支援 **遠端會話**，讓你能從網頁瀏覽器（桌機或手機）或 GitHub Mobile app 監控並互動進行中的 CLI 會話，不必坐在終端機前。

用 `--remote` 旗標啟動遠端會話：

```bash
copilot --remote
```

Copilot CLI 會顯示一個連結並提供 QR code。用手機或桌機瀏覽器開啟連結，即可即時觀看會話、發送後續提示、檢查規劃、遠端引導 agent。會話是使用者專屬的，你只能存取自己的 Copilot CLI 會話。

你也可以在進行中的會話隨時啟用遠端存取：

```
> /remote
```

更多遠端會話細節請參見 [Copilot CLI 文件](https://docs.github.com/copilot/how-tos/copilot-cli/steer-remotely)。

---

## 📝 作業

### 主要挑戰：改進 Book App 的公用程式

前面的動手範例聚焦在檢查與重構 `book_app.py`。現在請用同樣技巧練習另一個檔案 `utils.py`：

1. 啟動互動式會話：`copilot`
2. 請 Copilot CLI 摘要此檔案內容：「Summarize @samples/book-app-project/utils.py and explain what each function in this file does」
3. 請它加入輸入驗證：「Add validation to `get_user_choice()` so it handles empty input and non-numeric entries」
4. 請它改進錯誤處理：「What happens if `get_book_details()` receives an empty string for the title? Add guards for that.」
5. 請它補上 docstring：「Add a comprehensive docstring to `get_book_details()` with parameter descriptions and return values」
6. 觀察情境如何在多個提示間延續。每次改進都會建立在前一次基礎上
7. 用 `/exit` 離開

**成功標準**：你應該會得到一個改進過的 `utils.py`，具備輸入驗證、錯誤處理與 docstring，且這些都是透過多輪對話逐步完成。

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
- 如果 Copilot CLI 反問你細節，直接自然回答即可
- 情境會自動延續，每個提示都會建立在前一個基礎上
- 若想重來，請用 `/clear`

</details>

### 進階挑戰：比較三種模式

範例用 `/plan` 實作搜尋功能、用 `-p` 批次檢查。現在請針對新增 `list_by_year()` 方法到 `BookCollection` 類別這個新任務，三種模式都試試：

1. **互動式**：`copilot` → 請它一步步設計並實作此方法
2. **規劃**：`/plan Add a list_by_year(start, end) method to BookCollection that filters books by publication year range`
3. **程式化**：`copilot --allow-all -p "@samples/book-app-project/books.py Add a list_by_year(start, end) method that returns books published between start and end year inclusive"`

**反思**：哪種模式最自然？你會在什麼情境下用哪一種？

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 會發生什麼 | 修正方式 |
|------|------------|----------|
| 輸入 `exit` 而非 `/exit` | Copilot CLI 會把 "exit" 當成提示詞，不是指令 | Slash 指令都要以 `/` 開頭 |
| 用 `-p` 進行多輪對話 | 每次 `-p` 都是獨立執行，彼此無記憶 | 多輪對話請用互動模式（`copilot`） |
| 忘記用引號包住含 `$` 或 `!` 的提示 | Shell 會先解析特殊字元，Copilot CLI 收不到 | 用單引號包住提示：`copilot -p 'What does $HOME mean?'` |
| 按一次 Esc 取消執行中任務 | 現在單按 Esc 不會取消進行中工作（避免誤觸） | Copilot CLI 處理時請連按 **Esc 兩次** 取消 |

### 疑難排解

**"Model not available"** - 你的訂閱可能不含所有模型。用 `/model` 查看可用模型。

**"Context too long"** - 你的對話已用滿 context window。請用 `/new` 開新會話。

**"Rate limit exceeded"** - 請稍候幾分鐘再試。批次作業可考慮用程式化模式並加延遲。

</details>

---

# 小結

## 🔑 重點整理

1. **互動模式** 適合探索與反覆調整——情境會自動延續。就像和一個記得你說過什麼的人對話。
2. **規劃模式** 通常用於較複雜任務。實作前可先審查規劃。
3. **程式化模式** 適合自動化。無需互動。
4. **常用指令**（`/ask`、`/help`、`/clear`、`/new`、`/plan`、`/research`、`/model`、`/exit`）涵蓋日常大部分需求。

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

現在你已了解三種模式，接下來要學習如何讓 Copilot CLI 取得你的程式碼情境。

在 **[第 02 章：情境與對話](../02-context-conversations/README.md)**，你將學到：

- 用 `@` 語法引用檔案與目錄
- 用 `--resume` 與 `--continue` 管理會話
- 為什麼情境管理讓 Copilot CLI 如虎添翼

---

**[← 回課程首頁](../README.md)** | **[繼續前往第 02 章 →](../02-context-conversations/README.md)**
