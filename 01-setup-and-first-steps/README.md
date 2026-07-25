<!--
---
id: CopilotCLI-01
title: !translate 入門第一步
description: !translate 透過實作體驗 GitHub Copilot CLI，並學習互動模式、規劃模式與程式化模式的適用時機。
audience: Developers / Students / Terminal users
slug: first-steps
weight: 2
---
-->

![Chapter 01: First Steps](assets/chapter-header.png)

> **觀看 AI 如何即時找出錯誤、解釋難懂的程式碼，並產生可運作的腳本。接著學會三種使用 GitHub Copilot CLI 的方式。**

魔法就在這一章開始！你將親身體驗為什麼開發者形容 GitHub Copilot CLI 就像隨時能請教的資深工程師。你會看到 AI 在幾秒內找出安全性漏洞、用簡單易懂的英文解釋複雜程式碼，並立即產生可運作的腳本。然後你會學會三種互動模式（互動模式、規劃模式、程式化模式），讓你知道在各種任務下該用哪一種。

> ⚠️ **先決條件**：請先完成 **[第 00 章：快速開始](../00-quick-start/README.md)**。你必須已安裝並驗證 GitHub Copilot CLI，才能執行下方的示範。

## 🎯 學習目標

完成本章後，你將能夠：

- 透過實作示範體驗 GitHub Copilot CLI 帶來的生產力提升
- 根據任務選擇正確的模式（互動、規劃或程式化）
- 使用 slash 指令控制你的會話

> ⏱️ **預估時間**：約 45 分鐘（閱讀 15 分鐘 + 實作 30 分鐘）

---

# 你的第一次 Copilot CLI 體驗

<img src="assets/first-copilot-experience.png" alt="Developer sitting at a desk with code on the monitor and glowing particles representing AI assistance" width="800"/>

馬上動手，看看 Copilot CLI 能做什麼。

---

## 先暖身：你的第一個提示詞

在進入精彩的示範之前，先從一些簡單的提示詞開始，現在就能試試看。**不需要任何程式碼儲存庫**！只要打開終端機並啟動 Copilot CLI：

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

不會用 Python？沒關係！直接問你想了解的語言相關問題即可。

你會發現這種互動非常自然。就像和同事對話一樣提問。探索完畢後，輸入 `/exit` 離開會話。

**關鍵觀念**：GitHub Copilot CLI 是對話式的。你不需要特殊語法，只要用自然語言提問即可。

## 實際體驗

現在來看看為什麼開發者說這就像「隨時請教的資深工程師」。

> 📖 **閱讀範例說明**：以 `>` 開頭的行是你在互動式 Copilot CLI 會話中輸入的提示詞。沒有 `>` 前綴的行則是在終端機執行的 shell 指令。

> 💡 **關於範例輸出**：本課程中的範例輸出僅供參考。由於 Copilot CLI 每次回應都會有所不同，你的結果在措辭、格式與細節上都可能不同。請專注於*回傳資訊的類型*，而非完全相同的文字。

### 示範 1：幾秒內完成程式碼審查

本課程包含一些刻意設計有程式碼品質問題的範例檔案。如果你在本機操作且尚未 clone 儲存庫，請執行下方 `git clone` 指令，切換到 `copilot-cli-for-beginners` 資料夾，然後啟動 `copilot`。

```bash
# 如果你在本機操作且尚未 clone，請先下載課程儲存庫
git clone https://github.com/github/copilot-cli-for-beginners
cd copilot-cli-for-beginners

# 啟動 Copilot
copilot
```

進入互動式 Copilot CLI 會話後，執行下列指令：

```
> Review @samples/book-app-project/book_app.py for code quality issues and suggest improvements
```

> 💡 **`@` 符號是做什麼用的？** `@` 符號告訴 Copilot CLI 讀取一個檔案。你會在第 02 章學到更多細節。現在只要照著輸入即可。

---

<details>
<summary>🎬 實際操作影片</summary>

![Code Review Demo](assets/code-review-demo.gif)

*示範輸出會有所不同。你的模型、工具與回應內容可能與這裡顯示的不同。*

</details>

---

**重點**：專業的程式碼審查只需幾秒。人工審查則需要……遠比這更久！

---

### 示範 2：解釋難懂的程式碼

是否曾經盯著程式碼發呆，不知道它在做什麼？在 Copilot CLI 會話中試試這個：

```
> Explain what @samples/book-app-project/books.py does in simple terms
```

---

<details>
<summary>🎬 實際操作影片</summary>

![Explain Code Demo](assets/explain-code-demo.gif)

*示範輸出會有所不同。你的模型、工具與回應內容可能與這裡顯示的不同。*

</details>

---

**實際發生的事**：（你的輸出會不同）Copilot CLI 會讀取檔案、理解程式碼，並用簡單易懂的英文解釋。

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

**重點**：複雜的程式碼也能像有耐心的導師一樣被清楚解釋。

---

### 示範 3：產生可運作的程式碼

需要一個你本來要 Google 15 分鐘的函式？在同一個會話中繼續：

```
> Write a Python function that takes a list of books and returns statistics: 
  total count, number read, number unread, oldest and newest book
```

---

<details>
<summary>🎬 實際操作影片</summary>

![Generate Code Demo](assets/generate-code-demo.gif)

*示範輸出會有所不同。你的模型、工具與回應內容可能與這裡顯示的不同。*

</details>

---

**實際發生的事**：幾秒內就產生一個完整、可運作的函式，直接複製貼上即可執行。

探索完畢後，離開會話：

```
> /exit
```

**重點**：立即滿足需求，而且全程都在同一個連續會話中完成。

---

# 模式與指令

<img src="assets/modes-and-commands.png" alt="Futuristic control panel with glowing screens, dials, and equalizers representing Copilot CLI modes and commands" width="800"/>

你剛剛已經看到 Copilot CLI 的強大功能。現在來了解*如何*有效運用這些能力。關鍵在於知道三種互動模式該用在哪些情境。

> 💡 **注意**：Copilot CLI 還有一個 **Autopilot** 模式，可以自動執行任務而不需等待你的輸入。這很強大，但需要授予完整權限，並會自動使用 premium 請求。本課程聚焦於下方三種模式。等你熟悉基本操作後，我們會再介紹 Autopilot。

---

## 🧩 真實世界比喻：外出用餐

把使用 GitHub Copilot CLI 想像成外出用餐。從規劃行程到點餐，不同情境需要不同方式：

| 模式 | 用餐比喻 | 適用時機 |
|------|----------------|-------------|
| **規劃模式** | 用 GPS 規劃前往餐廳的路線 | 複雜任務——先規劃路線、檢查停靠點、確認方案再出發 |
| **互動模式** | 和服務生對話 | 探索與反覆調整——提問、客製化、即時回饋 |
| **程式化模式** | 得來速點餐 | 快速、明確的任務——留在原本環境，迅速取得結果 |

就像外出用餐一樣，你會自然學會什麼時候該用哪種方式。

<img src="assets/ordering-food-analogy.png" alt="Three Ways to Use GitHub Copilot CLI - Plan Mode (GPS route to restaurant), Interactive Mode (talking to waiter), Programmatic Mode (drive-through)" width="800"/>

*根據任務選擇模式：規劃模式適合先規劃路線，互動模式適合來回討論，程式化模式適合快速一次性結果*

### 我該從哪個模式開始？

**建議從互動模式開始。** 
- 可以自由嘗試並追問細節
- 情境會隨對話自然累積
- 出錯時用 `/clear` 很容易重來

熟悉後可以試試：
- **程式化模式**（`copilot -p "<你的提示詞>"`）適合快速、單次提問
- **規劃模式**（`/plan`）適合需要先詳細規劃再動手寫程式的情境

---

## 三種模式介紹

### 模式一：互動模式（建議從這裡開始）

<img src="assets/interactive-mode.png" alt="Interactive Mode - Like talking to a waiter who can answer questions and adjust the order" width="250"/>

**最適合**：探索、反覆調整、多輪對話。就像和服務生對話，能即時回應、調整需求。

啟動互動式會話：

```bash
copilot
```

如同前面示範，你會看到一個可以自然輸入的提示符。想查詢可用指令，只要輸入：

```
> /help
```

**關鍵觀念**：互動模式會保留情境。每則訊息都會建立在前一則基礎上，就像真實對話。

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

### 模式二：規劃模式

<img src="assets/plan-mode.png" alt="Plan Mode - Like planning a route before a trip using GPS" width="250"/>

**最適合**：需要先檢查方案再執行的複雜任務。就像出發前用 GPS 規劃路線。

規劃模式會協助你在寫程式前先產生逐步計畫。使用 `/plan` 指令，按下 **Shift+Tab** 可切換到規劃模式：

```bash
copilot

> /plan Add a "mark as read" command to the book app
```

> 💡 **小技巧**：**Shift+Tab** 可在模式間切換：互動 → 規劃 → Autopilot。隨時在互動會話中按下即可，不需輸入指令。

你也可以用 `--plan` 旗標直接啟動 Copilot CLI 的規劃模式：

```bash
copilot --plan
```

**規劃模式輸出範例：**（你的結果可能不同）

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

**關鍵觀念**：規劃模式讓你在寫程式前先檢查與調整方案。在規劃模式下，Copilot CLI 只會**唯讀**，不會編輯任何檔案或執行會改變工作區的指令，直到你同意並進入實作階段。這讓你能安全地停留在「思考」階段，直到準備好為止。規劃完成後，你甚至可以請 Copilot CLI 把計畫存成檔案，例如「Save this plan to `mark_as_read_plan.md`」就會產生一份包含計畫細節的 markdown 檔。

> 💡 **想挑戰更複雜的任務？** 試試：`/plan Add search and filter capabilities to the book app`。規劃模式可從簡單功能一路擴展到完整應用程式。

> 📚 **Autopilot 模式**：你可能注意到 Shift+Tab 會切換到第三種模式 **Autopilot**。在 autopilot 模式下，Copilot 會自動執行整個計畫，不需你每步確認——就像把任務交給同事說「做完再跟我說」。典型流程是規劃 → 同意 → autopilot，所以你必須先學會寫好計畫。你也可以用 `copilot --autopilot` 直接進入 autopilot。建議先熟悉互動與規劃模式，再參考 [官方文件](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot)。

---

### 模式三：程式化模式

<img src="assets/programmatic-mode.png" alt="Programmatic Mode - Like using a drive-through for a quick order" width="250"/>

**最適合**：自動化、腳本、CI/CD、單次指令。就像得來速點餐，不需和服務生互動。

用 `-p` 旗標執行一次性、不需互動的指令：

```bash
# 產生程式碼
copilot -p "Write a function that checks if a number is even or odd"

# 快速查詢
copilot -p "How do I read a JSON file in Python?"
```

**關鍵觀念**：程式化模式給你快速答案後就結束。沒有對話，只有輸入 → 輸出。

<details>
<summary>📚 <strong>進階應用：在腳本中使用程式化模式</strong>（點擊展開）</summary>

熟悉後，你可以在 shell 腳本中用 `-p`：

```bash
#!/bin/bash

# 自動產生提交訊息
COMMIT_MSG=$(copilot -p "Generate a commit message for: $(git diff --staged)")
git commit -m "$COMMIT_MSG"

# 審查檔案
copilot --allow-all -p "Review @myfile.py for issues"
```
> ⚠️ **關於 `--allow-all`**：這個旗標會跳過所有權限提示，讓 Copilot CLI 可直接讀取檔案、執行指令、存取網址。這對程式化模式（`-p`）很重要，因為沒有互動會話可供你確認。只有在你自己撰寫提示詞、且目錄可信時才使用 `--allow-all`。切勿用於不可信輸入或敏感目錄。

</details>

---

## 必學 Slash 指令

這些指令很適合剛開始使用 Copilot CLI 時學習：

| 指令 | 功能說明 | 適用時機 |
|---------|--------------|-------------|
| `/ask` | 提問但不影響對話歷史 | 想快速獲得答案又不想干擾目前任務時 |
| `/clear` | 清除對話並重新開始 | 換主題時 |
| `/help` | 顯示所有可用指令 | 忘記指令時 |
| `/model` | 顯示或切換 AI 模型 | 想更換 AI 模型時 |
| `/plan` | 寫程式前先規劃 | 複雜功能時 |
| `/refine` | 將雜亂的提示詞重寫成清楚聚焦的版本 | 覺得提示詞太亂、想要更好結果時 |
| `/research` | 深入研究 GitHub 與網路資料 | 需要先調查主題再寫程式時 |
| `/exit` | 結束會話 | 完成時 |

> 💡 **`/ask` 與一般對話的差異**：通常你發送的每則訊息都會成為對話歷史的一部分，影響後續回應。`/ask` 則是「不留紀錄」的捷徑——很適合像 `/ask What does YAML mean?` 這種單次提問，不會污染會話情境。

> 💡 **`/refine` 幫你優化提示詞**：不確定你的提示詞夠不夠清楚？先照直覺輸入，再用 `/refine` 讓 Copilot 幫你重寫成精確、結構良好的提示詞。這對剛接觸 AI 工具、還在學習如何寫好提示詞時特別有用。

> 💡 **Tab 自動補全**：輸入 slash 指令時按 **Tab** 可自動補全指令名稱，或切換可用子指令與參數。忘記指令名稱時特別好用。

這就是入門的全部內容！熟悉後可以再探索更多指令。

> 📚 **官方文件**：[CLI 指令參考](https://docs.github.com/copilot/reference/cli-command-reference)（完整指令與旗標列表）

<details>
<summary>📚 <strong>進階指令</strong>（點擊展開）</summary>

> 💡 上述必學指令已涵蓋日常大部分需求。這份參考適合你準備進一步探索時查閱。

### Agent 環境

| 指令 | 功能說明 |
|---------|--------------|
| `/agent` | 瀏覽並選擇可用的 agent |
| `/env` | 顯示已載入的環境細節——包含指令、MCP 伺服器、技能、agent、外掛等 |
| `/init` | 初始化儲存庫的 Copilot 指令 |
| `/mcp` | 管理 MCP 伺服器設定 |
| `/settings` | 開啟互動式設定對話，一次瀏覽與編輯所有使用者設定 |
| `/skills` | 管理技能以增強功能 |

> 💡 agent 介紹請見 [第 04 章](../04-agents-custom-instructions/README.md)，技能請見 [第 05 章](../05-skills/README.md)，MCP 伺服器請見 [第 06 章](../06-mcp-servers/README.md)。

### 模型與子 agent

| 指令 | 功能說明 |
|---------|--------------|
| `/delegate` | 將任務交給 GitHub Copilot 雲端 agent |
| `/fleet` | 將複雜任務拆分為多個子任務並平行處理 |
| `/model` | 顯示或切換 AI 模型 |
| `/tasks` | 檢視背景子 agent 與分離的 shell 會話 |

### 程式碼

| 指令 | 功能說明 |
|---------|--------------|
| `/diff` | 審查目前目錄下的變更 |
| `/pr` | 操作目前分支的 pull request |
| `/research` | 透過 GitHub 與網路來源進行深入研究 |
| `/review` | 執行程式碼審查 agent 分析變更 |
| `/terminal-setup` | 啟用多行輸入支援（shift+enter 與 ctrl+enter） |

### 權限

| 指令 | 功能說明 |
|---------|--------------|
| `/add-dir <directory>` | 將目錄加入允許清單 |
| `/allow-all [on\|off\|show]` | 自動同意所有權限提示；用 `on` 啟用、`off` 關閉、`show` 檢查目前狀態 |
| `/yolo` | `/allow-all on` 的快速別名——自動同意所有權限提示。|
| `/cwd`, `/cd [directory]` | 檢視或切換工作目錄 |
| `/list-dirs` | 顯示所有允許的目錄 |

> ⚠️ **請小心使用**：`/allow-all` 與 `/yolo` 會跳過確認提示。適合可信專案，但不可信程式碼請務必小心。

### 會話

| 指令 | 功能說明 |
|---------|--------------|
| `/clear` | 放棄目前會話（不儲存歷史）並重新開始 |
| `/compact` | 摘要對話內容以減少情境用量（可加聚焦指令，例如 `/compact focus on the bug list`） |
| `/context` | 顯示 context window token 用量與視覺化圖示 |
| `/keep-alive` | 防止 Copilot CLI 執行時系統進入睡眠——適合筆電長時間任務 |
| `/memory [on\|off\|show]` | 啟用、停用或檢視持久記憶——跨所有會話記住事實與偏好 |
| `/new` | 結束目前會話（儲存到歷史以便搜尋/繼續）並重新開始 |
| `/resume` | 切換到其他會話（可指定會話 ID 或名稱） |
| `/rename` | 重新命名目前會話（省略名稱則自動產生） |
| `/rewind` | 開啟時間軸選擇器，回溯到對話中任一早期狀態 |
| `/usage` | 顯示會話用量統計與配額進度條 |
| `/session` | 顯示會話資訊與工作區摘要；可用 `/session delete`、`/session delete <id>` 或 `/session delete-all` 刪除會話 |
| `/share` | 匯出會話為 markdown、GitHub gist 或自含式 HTML 檔 |
| `/every <interval> <prompt>` | 排程提示詞定期執行（例如 `/every 1h summarize new commits`）。間隔可用自然語言。`/loop` 是 `/every` 的別名。|
| `/after <time> <prompt>` | 排程提示詞延遲一次執行（例如 `/after 30m run tests`）。時間可用自然語言。|

### 顯示

| 指令 | 功能說明 |
|---------|--------------|
| `/statusline`（或 `/footer`） | 自訂會話底部狀態列顯示項目（目錄、分支、effort、context window、配額等） |
| `/theme` | 檢視或設定終端機主題 |
| `/voice` | 以本地語音辨識輸入提示詞——用說的取代打字 |

### 說明與回饋

| 指令 | 功能說明 |
|---------|--------------|
| `/app` | 直接從 CLI 開啟 GitHub app（或瀏覽器備用） |
| `/changelog` | 顯示 CLI 版本更新紀錄 |
| `/feedback` | 提交意見給 GitHub |
| `/help` | 顯示所有可用指令 |

### 快速 Shell 指令

在提示詞前加上 `!` 可直接執行 shell 指令（不經 AI）：

```bash
copilot

> !git status
# 直接執行 git status，不經 AI

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

> 💡 **小技巧**：有些模型會消耗更多「premium 請求」。標記為 **1x**（如 Claude Sonnet 4.5）的模型很適合預設使用，效能與效率兼具。高倍率模型會更快用完 premium 配額，建議留給特別需求時使用。

> 💡 **不確定選哪個模型？** 選擇 **`Auto`** 讓 Copilot 自動為每個會話挑選最佳模型。剛開始時這是很好的預設選項，無需煩惱模型選擇。

> 💡 **模型家族快捷鍵**：你也可以在 `/model` 選單直接輸入簡短家族別名——如 `opus`、`sonnet`、`haiku`、`gpt` 或 `gemini`，Copilot 會自動幫你挑選該家族中最適合的模型。

</details>

---

# 練習

<img src="../assets/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

是時候把學到的內容實際操作一遍。

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

# 檢查計畫
# 同意或修改
# 觀察逐步實作
```

### 用程式化模式自動化

`-p` 旗標讓你直接在終端機執行 Copilot CLI，不需進入互動模式。從儲存庫根目錄複製貼上下列腳本，即可審查書籍應用程式中的所有 Python 檔案。

```bash
# 審查書籍應用程式中的所有 Python 檔案
for file in samples/book-app-project/*.py; do
  echo "Reviewing $file..."
  copilot --allow-all -p "Quick code quality review of @$file - critical issues only"
done
```

**PowerShell (Windows):**
```powershell
# 檢查書籍應用程式中的所有 Python 檔案
Get-ChildItem samples/book-app-project/*.py | ForEach-Object {
  $relativePath = "samples/book-app-project/$($_.Name)";
  Write-Host "Reviewing $relativePath...";
  copilot --allow-all -p "Quick code quality review of @$relativePath - critical issues only" 
}
```

---

完成示範後，請嘗試以下變化：

1. **互動挑戰**：啟動 `copilot` 並探索書籍應用程式。詢問關於 `@samples/book-app-project/books.py`，並連續三次請求改進建議。

2. **計畫模式挑戰**：執行 `/plan Add rating and review features to the book app`。仔細閱讀計畫內容。這個計畫合理嗎？

3. **程式化挑戰**：執行 `copilot --allow-all -p "List all functions in @samples/book-app-project/book_app.py and describe what each does"`。它第一次就成功了嗎？

---

## 💡 提示：從網頁或行動裝置控制你的 CLI 會話

GitHub Copilot CLI 支援**遠端會話**，讓你可以從網頁瀏覽器（桌機或行動裝置）或 GitHub Mobile app 監控並互動執行中的 CLI 會話，而不必親自在終端機前。

使用 `--remote` 旗標啟動遠端會話：

```bash
copilot --remote
```

Copilot CLI 會顯示一個連結並提供 QR code。用手機或桌機瀏覽器分頁開啟該連結，即可即時觀看會話、傳送後續提示、檢視計畫並遠端引導 agent。會話是使用者專屬的，因此你只能存取自己的 Copilot CLI 會話。

你也可以在任何時候於進行中的會話內啟用遠端存取：

```
> /remote
```

更多關於遠端會話的細節，請參見 [Copilot CLI 文件](https://docs.github.com/copilot/how-tos/copilot-cli/steer-remotely)。

---

## 📝 作業

### 主要挑戰：改進書籍應用程式的工具程式

實作範例聚焦於檢查與重構 `book_app.py`。現在請將相同技能應用於另一個檔案 `utils.py`：

1. 啟動互動會話：`copilot`
2. 請 Copilot CLI 摘要此檔案：「Summarize @samples/book-app-project/utils.py and explain what each function in this file does」
3. 請它加入輸入驗證：「Add validation to `get_user_choice()` so it handles empty input and non-numeric entries」
4. 請它改進錯誤處理：「What happens if `get_book_details()` receives an empty string for the title? Add guards for that.」
5. 請它補上 docstring：「Add a comprehensive docstring to `get_book_details()` with parameter descriptions and return values」
6. 觀察情境如何在提示之間傳遞。每次改進都會建立在前一次基礎上
7. 使用 `/exit` 離開

**成功標準**：你應該會得到一個改進過的 `utils.py`，具備輸入驗證、錯誤處理與 docstring，且這些都是透過多輪對話逐步完成的。

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
- 如果 Copilot CLI 提出釐清問題，只需自然回答即可
- 情境會持續傳遞，因此每個提示都會建立在前一個基礎上
- 若想重新開始，請使用 `/clear`

</details>

### 加分挑戰：比較三種模式

範例中 `/plan` 用於搜尋功能，`-p` 用於批次檢查。現在請針對新增 `list_by_year()` 方法到 `BookCollection` 類別這個新任務，三種模式都試一次：

1. **互動模式**：`copilot` → 逐步請它設計並實作該方法
2. **計畫模式**：`/plan Add a list_by_year(start, end) method to BookCollection that filters books by publication year range`
3. **程式化模式**：`copilot --allow-all -p "@samples/book-app-project/books.py Add a list_by_year(start, end) method that returns books published between start and end year inclusive"`

**反思**：哪一種模式最自然？你會在什麼情境下使用哪一種？

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生情況 | 修正方式 |
|---------|--------------|-----|
| 輸入 `exit` 而非 `/exit` | Copilot CLI 將 "exit" 當作提示詞而非指令 | 斜線指令一律以 `/` 開頭 |
| 用 `-p` 進行多輪對話 | 每次 `-p` 呼叫都是獨立的，不會記住前一次內容 | 多輪對話請用互動模式（`copilot`） |
| 忘記用引號包住含 `$` 或 `!` 的提示 | Shell 會在 Copilot CLI 處理前先解讀特殊字元 | 用單引號包住提示：`copilot -p 'What does $HOME mean?'` |
| 按一次 Esc 取消執行中任務 | 單次 Esc 不再能取消進行中的工作（避免誤觸） | Copilot CLI 處理時請按 **Esc 兩次** 取消 |

### 疑難排解

**"Model not available"** - 你的訂閱可能不包含所有模型。請用 `/model` 查看可用模型。

**"Context too long"** - 你的對話已用滿 context window。請用 `/clear` 重設，或開啟新會話。

**"Rate limit exceeded"** - 請稍候幾分鐘再試。批次作業可考慮用程式化模式並加上延遲。

</details>

---

# 摘要

## 🔑 重點整理

1. **互動模式** 適合探索與反覆調整——情境會持續傳遞。就像和一個記得你說過什麼的人對話。
2. **計畫模式** 通常用於較複雜的任務。實作前先審查計畫。
3. **程式化模式** 適合自動化。不需互動。
4. **常用指令**（`/ask`、`/help`、`/clear`、`/plan`、`/research`、`/model`、`/exit`）涵蓋大多數日常需求。

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

現在你已了解三種模式，接下來將學習如何讓 Copilot CLI 瞭解你的程式碼情境。

在 **[第 02 章：情境與對話](../02-context-conversations/README.md)**，你將學到：

- 使用 `@` 語法參照檔案與目錄
- 用 `--resume` 和 `--continue` 管理會話
- 為什麼情境管理讓 Copilot CLI 如虎添翼

---

**[← 回到課程首頁](../README.md)** | **[繼續前往第 02 章 →](../02-context-conversations/README.md)**
