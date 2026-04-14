![Chapter 01: First Steps](images/chapter-header.png)

> **觀看 AI 即時找出程式錯誤、解釋難懂的程式碼，並產生可執行的腳本。然後學習三種使用 GitHub Copilot CLI 的方式。**

這一章就是魔法的起點！你將親身體驗為什麼開發者形容 GitHub Copilot CLI 就像隨時能聯絡的資深工程師。你會看到 AI 在幾秒內找出安全性漏洞、用簡單易懂的英文解釋複雜程式碼，並即時產生可執行的腳本。接著，你將學會三種互動模式（互動模式、計畫模式、程式化模式），讓你清楚知道每個任務該用哪一種。

> ⚠️ **先決條件**：請先完成 **[第 00 章：快速開始](../00-quick-start/README.md)**。你必須先安裝並驗證 GitHub Copilot CLI，才能執行以下示範。

## 🎯 學習目標

完成本章後，你將能夠：

- 透過實作示範，體驗 GitHub Copilot CLI 帶來的生產力提升
- 根據任務選擇合適的模式（互動、計畫或程式化）
- 使用斜線指令控制你的對話

> ⏱️ **預估時間**：約 45 分鐘（閱讀 15 分鐘 + 實作 30 分鐘）

---

# 你的第一個 Copilot CLI 體驗

<img src="images/first-copilot-experience.png" alt="Developer sitting at a desk with code on the monitor and glowing particles representing AI assistance" width="800"/>

直接開始，看看 Copilot CLI 能做什麼。

---

## 熟悉操作：你的第一個提示詞

在進入令人驚豔的示範之前，先從一些簡單的提示詞開始，現在就可以嘗試。**不需要任何程式碼庫**！只要開啟終端機並啟動 Copilot CLI：

```bash
copilot
```

試試這些適合新手的提示詞：

```
> 用簡單的方式解釋 Python 中的 dataclass 是什麼

> 寫一個函式，將字典列表依指定鍵排序

> Python 中 list 和 tuple 有什麼差別？

> 給我 5 個撰寫乾淨 Python 程式碼的最佳實踐
```

不用 Python？沒問題！直接詢問你熟悉的語言相關問題即可。

你會發現這種互動很自然。就像問同事一樣直接提問。探索完畢後，輸入 `/exit` 離開對話。

**關鍵洞察**：GitHub Copilot CLI 是對話式的。你不需要特殊語法，只要用自然語言提問即可。

## 實際運作展示

現在來看看為什麼開發者說這就像「隨時能聯絡的資深工程師」。

> 📖 **閱讀範例說明**：以 `>` 開頭的行是你在 Copilot CLI 互動模式中輸入的提示詞。沒有 `>` 前綴的行則是你在終端機執行的 shell 指令。

> 💡 **關於範例輸出**：課程中的範例輸出僅供參考。因 Copilot CLI 回應每次都不同，你的結果在措辭、格式和細節上會有所差異。請專注於回傳資訊的「類型」，而非文字內容。

### 示範 1：秒級程式碼審查

課程提供了包含刻意程式碼品質問題的範例檔案。如果你在本機操作且尚未複製課程專案，請執行下方 `git clone` 指令，進入 `copilot-cli-for-beginners` 資料夾，然後啟動 Copilot。

```bash
# 如果你在本機操作且尚未複製課程專案，請執行
git clone https://github.com/github/copilot-cli-for-beginners
cd copilot-cli-for-beginners

# 啟動 Copilot
copilot
```

進入 Copilot CLI 互動模式後，執行下列提示：

```
> 審查 @samples/book-app-project/book_app.py 的程式碼品質問題並提出改善建議
```

> 💡 **`@` 符號是做什麼用的？** `@` 符號告訴 Copilot CLI 讀取檔案。你會在第 02 章學到詳細用法。現在只要照範例輸入即可。

---

<details>
<summary>🎬 實際運作展示！</summary>

![Code Review Demo](images/code-review-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容可能與此不同。*

</details>

---

**重點**：專業的程式碼審查只需幾秒。人工審查則需要……嗯……遠比這久！

---

### 示範 2：解釋難懂的程式碼

是否曾經盯著程式碼發呆，不知道它在做什麼？在 Copilot CLI 對話中試試這個：

```
> 用簡單方式解釋 @samples/book-app-project/books.py 的功能
```

---

<details>
<summary>🎬 實際運作展示！</summary>

![Explain Code Demo](images/explain-code-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容可能與此不同。*

</details>

---

**會發生什麼事**：（你的輸出會不同）Copilot CLI 讀取檔案、理解程式碼，並用簡單易懂的英文解釋。

```
這是一個使用 Python dataclass 管理書籍收藏的模組。

可以把它想成數位書櫃：
- Book 是 dataclass —— 一種簡單儲存書籍資訊（標題、作者、年份、閱讀狀態）的方式
- BookCollection 管理整個收藏並負責儲存／讀取

主要組件：

1. @dataclass 裝飾器（第 8 行）
   - 自動產生 __init__、__repr__ 等方法
   - 用於乾淨定義 Python 資料結構

2. BookCollection 類別（第 16 行）
   - 維護 Book 物件列表
   - 用 JSON 檔案 I/O 處理持久化
   - load_books() 從 data.json 讀取
   - save_books() 用 asdict() 寫入 data.json

3. 書籍操作：
   - add_book() —— 新增並儲存書籍
   - find_book_by_title() —— 搜尋收藏
   - mark_as_read() —— 更新閱讀狀態
   - find_by_author() —— 依作者名稱篩選

常見流程：從 JSON 讀取 → 操作 Python 物件 → 寫回 JSON
```

**重點**：複雜程式碼也能像耐心導師一樣解釋得清楚易懂。

---

### 示範 3：產生可執行程式碼

需要一個你可能要 Google 15 分鐘的函式？在同一個對話中：

```
> 寫一個 Python 函式，接受書籍列表並回傳統計資訊：
  總數、已讀數量、未讀數量、最舊和最新書籍
```

---

<details>
<summary>🎬 實際運作展示！</summary>

![Generate Code Demo](images/generate-code-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應內容可能與此不同。*

</details>

---

**會發生什麼事**：幾秒內產生完整、可執行的函式，直接複製貼上即可運行。

探索完畢後，離開對話：

```
> /exit
```

**重點**：即時滿足需求，而且全程都在同一個連續對話中。

---

# 模式與指令

<img src="images/modes-and-commands.png" alt="Futuristic control panel with glowing screens, dials, and equalizers representing Copilot CLI modes and commands" width="800"/>

你已經看到 Copilot CLI 能做什麼。現在來了解如何有效運用這些能力。關鍵在於知道三種互動模式，並根據情境選擇。

> 💡 **注意**：Copilot CLI 還有一種 **自動駕駛（Autopilot）模式**，可自動執行任務而不需等待你的輸入。這很強大，但需授權完整權限，並會自動使用高級請求。本課程聚焦於下方三種模式。等你熟悉基礎後，我們會再介紹自動駕駛模式。

---

## 🧩 真實世界比喻：外出用餐

使用 GitHub Copilot CLI 就像外出用餐。從規劃行程到點餐，不同情境需要不同方式：

| 模式 | 用餐比喻 | 適用時機 |
|------|----------|----------|
| **計畫模式** | 用 GPS 規劃路線到餐廳 | 複雜任務——規劃路線、檢查停靠點、同意計畫再出發 |
| **互動模式** | 與服務生對話 | 探索與反覆調整——提問、客製化、即時回饋 |
| **程式化模式** | 得來速點餐 | 快速、明確任務——留在原本環境，快速取得結果 |

就像用餐一樣，你會自然學會何時該用哪種方式。

<img src="images/ordering-food-analogy.png" alt="Three Ways to Use GitHub Copilot CLI - Plan Mode (GPS route to restaurant), Interactive Mode (talking to waiter), Programmatic Mode (drive-through)" width="800"/>

*根據任務選擇模式：計畫模式適合先規劃，互動模式適合來回協作，程式化模式適合快速單次結果*

### 我應該從哪個模式開始？

**建議先從互動模式開始。**
- 可以自由嘗試並追問
- 情境會隨對話自然累積
- 出錯時用 `/clear` 很容易重來

熟悉後可嘗試：
- **程式化模式**（`copilot -p "<你的提示>"`）適合快速單次問題
- **計畫模式**（`/plan`）適合需要詳細規劃再進行的任務

---

## 三種模式介紹

### 模式 1：互動模式（建議起點）

<img src="images/interactive-mode.png" alt="Interactive Mode - Like talking to a waiter who can answer questions and adjust the order" width="250"/>

**最適合**：探索、反覆調整、多輪對話。就像與服務生對話，可以即時回饋並調整點餐。

啟動互動模式：

```bash
copilot
```

如同前面示範，你會看到提示符號，可以自然輸入。若需指令說明，輸入：

```
> /help
```

**關鍵洞察**：互動模式會保留情境。每則訊息都會延續前面的內容，就像真實對話。

#### 互動模式範例

```bash
copilot

> 審查 @samples/book-app-project/utils.py 並提出改善建議

> 為所有函式加上型別提示

> 強化錯誤處理機制

> /exit
```

注意每個提示都建立在前一個答案之上。你是在對話，不是每次都從頭開始。

---

### 模式 2：計畫模式

<img src="images/plan-mode.png" alt="Plan Mode - Like planning a route before a trip using GPS" width="250"/>

**最適合**：複雜任務，需要先審查方案再執行。就像出發前用 GPS 規劃路線。

計畫模式協助你在撰寫程式碼前先建立步驟計畫。使用 `/plan` 指令，按 **Shift+Tab** 可切換到計畫模式：

```bash
copilot

> /plan 為書籍應用程式新增「標記為已讀」指令
```

> 💡 **提示**：**Shift+Tab** 可在模式間切換：互動 → 計畫 → 自動駕駛。任何時候都能在互動模式下按此鍵切換，不需輸入指令。

你也可以用 `--plan` 旗標直接啟動計畫模式：

```bash
copilot --plan
```

**計畫模式輸出範例**：（你的輸出可能不同）

```
📋 實作計畫

步驟 1：更新 book_app.py 的指令處理器
  - 新增 "mark" 指令的 elif 分支
  - 建立 handle_mark_as_read() 函式

步驟 2：實作處理函式
  - 提示使用者輸入書名
  - 呼叫 collection.mark_as_read(title)
  - 顯示成功／失敗訊息

步驟 3：更新說明文字
  - 將 "mark" 加入可用指令列表
  - 文件化指令用法

步驟 4：測試流程
  - 新增一本書
  - 標記為已讀
  - 確認列表輸出狀態變化

是否要開始實作？ [Y/n]
```

**關鍵洞察**：計畫模式讓你在寫程式前先審查並修改方案。計畫完成後，還能請 Copilot CLI 將計畫存檔，例如「將此計畫存到 `mark_as_read_plan.md`」會建立包含細節的 markdown 檔案。

> 💡 **想要更複雜的範例？** 試試：`/plan 為書籍應用程式新增搜尋與篩選功能`。計畫模式可從簡單功能擴展到完整應用。

> 📚 **自動駕駛模式**：你可能注意到 Shift+Tab 會切換到第三種模式——自動駕駛。自動駕駛模式下，Copilot 會自動依計畫執行所有步驟，不需每步都等你確認——就像把任務交給同事說「完成後再通知我」。典型流程是計畫 → 同意 → 自動駕駛，因此你要先熟悉撰寫計畫。也可用 `copilot --autopilot` 直接啟動。建議先熟悉互動與計畫模式，再參考 [官方文件](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot)。

---

### 模式 3：程式化模式

<img src="images/programmatic-mode.png" alt="Programmatic Mode - Like using a drive-through for a quick order" width="250"/>

**最適合**：自動化、腳本、CI/CD、單次指令。就像得來速點餐，不需與服務生對話。

用 `-p` 旗標執行一次性指令，不需互動：

```bash
# 產生程式碼
copilot -p "寫一個判斷數字是偶數或奇數的函式"

# 快速查詢
copilot -p "Python 如何讀取 JSON 檔案？"
```

**關鍵洞察**：程式化模式給你快速答案後即結束。沒有對話，只有輸入 → 輸出。

<details>
<summary>📚 <strong>進階：在腳本中使用程式化模式</strong>（點擊展開）</summary>

熟悉後可在 shell 腳本中使用 `-p`：

```bash
#!/bin/bash

# 自動產生提交訊息
COMMIT_MSG=$(copilot -p "為以下內容產生提交訊息：$(git diff --staged)")
git commit -m "$COMMIT_MSG"

# 審查檔案
copilot --allow-all -p "審查 @myfile.py 的問題"
```
> ⚠️ **關於 `--allow-all`**：此旗標會跳過所有權限提示，讓 Copilot CLI 讀取檔案、執行指令、存取網址而不需確認。程式化模式（`-p`）無互動對話，因此必須用此旗標。僅在你自己撰寫提示、且目錄可信時使用。切勿用於不可信輸入或敏感目錄。

</details>

---

## 必備斜線指令

這些指令適用於互動模式。**先學這六個就夠了**——涵蓋 90% 日常需求：

| 指令 | 功能說明 | 適用時機 |
|------|----------|----------|
| `/clear` | 清除對話並重新開始 | 換主題時 |
| `/help` | 顯示所有可用指令 | 忘記指令時 |
| `/model` | 顯示或切換 AI 模型 | 想換模型時 |
| `/plan` | 撰寫程式前先規劃 | 複雜功能時 |
| `/research` | 用 GitHub 與網路來源深入研究 | 撰寫程式前需調查主題時 |
| `/exit` | 結束對話 | 完成時 |

這就是入門必備！熟悉後可探索更多指令。

> 📚 **官方文件**：[CLI 指令參考](https://docs.github.com/copilot/reference/cli-command-reference)，完整指令與旗標列表。

<details>
<summary>📚 <strong>進階指令</strong>（點擊展開）</summary>

> 💡 上述必備指令已涵蓋大部分日常需求。這份參考適合你準備探索更多時使用。

### Agent 環境

| 指令 | 功能說明 |
|------|----------|
| `/agent` | 瀏覽並選擇可用 Agent |
| `/init` | 初始化 Copilot 指令至你的專案 |
| `/mcp` | 管理 MCP 伺服器設定 |
| `/skills` | 管理技能以增強能力 |

> 💡 Agent 詳解見 [第 04 章](../04-agents-custom-instructions/README.md)，技能見 [第 05 章](../05-skills/README.md)，MCP 伺服器見 [第 06 章](../06-mcp-servers/README.md)。

### 模型與子 Agent

| 指令 | 功能說明 |
|------|----------|
| `/delegate` | 交由 GitHub Copilot 雲端 Agent 處理任務 |
| `/fleet` | 將複雜任務拆分為多個平行子任務加速完成 |
| `/model` | 顯示或切換 AI 模型 |
| `/tasks` | 查看背景子 Agent 與分離 shell 對話 |

### 程式碼

| 指令 | 功能說明 |
|------|----------|
| `/diff` | 審查目前目錄的程式碼變更 |
| `/pr` | 操作目前分支的 pull request |
| `/research` | 用 GitHub 與網路來源進行深入研究 |
| `/review` | 執行程式碼審查 Agent 分析變更 |
| `/terminal-setup` | 啟用多行輸入（shift+enter 與 ctrl+enter） |

### 權限

| 指令 | 功能說明 |
|------|----------|
| `/add-dir <目錄>` | 將目錄加入允許清單 |
| `/allow-all [on|off|show]` | 自動批准所有權限提示；用 `on` 啟用、`off` 關閉、`show` 檢查狀態 |
| `/yolo` | `/allow-all on` 的快速別名——自動批准所有權限提示 |
| `/cwd`, `/cd [目錄]` | 查看或切換工作目錄 |
| `/list-dirs` | 顯示所有允許目錄 |

> ⚠️ **請謹慎使用**：`/allow-all` 與 `/yolo` 會跳過確認提示。適合可信專案，但不可信程式碼要小心。

### 對話

| 指令 | 功能說明 |
|------|----------|
| `/clear` | 放棄目前對話（不儲存歷史），重新開始 |
| `/compact` | 對話摘要，減少情境用量 |
| `/context` | 顯示情境窗口 token 用量與視覺化 |
| `/new` | 結束目前對話（儲存到歷史以便搜尋／繼續），重新開始 |
| `/resume` | 切換到其他對話（可指定對話 ID） |
| `/rename` | 重新命名目前對話（省略名稱則自動產生） |
| `/rewind` | 開啟時間軸選擇器，回溯到任意早期對話 |
| `/usage` | 顯示對話用量與統計 |
| `/session` | 顯示對話資訊與工作區摘要 |
| `/share` | 將對話匯出為 markdown、GitHub gist 或自包含 HTML 檔案 |

### 說明與回饋

| 指令 | 功能說明 |
|------|----------|
| `/changelog` | 顯示 CLI 版本更新紀錄 |
| `/feedback` | 提交回饋給 GitHub |
| `/help` | 顯示所有可用指令 |
| `/theme` | 查看或設定終端機主題 |

### 快速 shell 指令

在提示詞前加 `!` 可直接執行 shell 指令，不經 AI 處理：

```bash
copilot

> !git status
# 直接執行 git status，不經 AI 處理

> !python -m pytest tests/
# 直接執行 pytest
```

### 切換模型

Copilot CLI 支援多種 AI 模型（OpenAI、Anthropic、Google 等）。可用模型取決於你的訂閱方案與地區。用 `/model` 查看選項並切換：

```bash
copilot
> /model

# 顯示可用模型並讓你選擇。例如選擇 Sonnet 4.5。
```

> 💡 **提示**：有些模型會消耗更多「高級請求」。標記 **1x**（如 Claude Sonnet 4.5）的模型是很好的預設選擇，既強大又高效。倍率較高的模型會更快用完高級配額，建議留給特殊需求時使用。

</details>

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

是時候將學到的內容實際操作了。

---

## ▶️ 自己動手試試

### 互動探索

啟動 Copilot，利用追問提示反覆改善書籍應用程式：

```bash
copilot

> 審查 @samples/book-app-project/book_app.py - 哪些地方可以改善？

> 將 if/elif 鏈重構為更易維護的結構

> 為所有處理函式加上型別提示

> /exit
```

### 規劃功能

用 `/plan` 讓 Copilot CLI 在寫程式前先規劃實作方案：

```bash
copilot

> /plan 為書籍應用程式新增搜尋功能，可依書名或作者查找

# 審查計畫
# 同意或修改
# 觀察逐步實作
```

### 用程式化模式自動化

`-p` 旗標讓你直接在終端機執行 Copilot CLI，不需進入互動模式。將下列腳本貼到終端機（非 Copilot 對話）並在專案根目錄執行，可批次審查書籍應用程式所有 Python 檔案。

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

1. **互動挑戰**：啟動 `copilot`，探索書籍應用程式。詢問 `@samples/book-app-project/books.py`，並連續請求三次改善建議。
2. **計畫模式挑戰**：執行 `/plan 為書籍應用程式新增評分與評論功能`。仔細閱讀計畫，是否合理？
3. **程式化挑戰**：執行 `copilot --allow-all -p "列出 @samples/book-app-project/book_app.py 所有函式並描述各自功能"`。第一次就成功了嗎？

---

## 💡 提示：用網頁或手機遠端控制 CLI 對話

GitHub Copilot CLI 支援 **遠端對話**，讓你能在網頁瀏覽器（桌機或手機）或 GitHub Mobile app 上監控並互動，不需在終端機前。

用 `--remote` 旗標啟動遠端對話：

```bash
copilot --remote
```

Copilot CLI 會顯示連結並提供 QR code。用手機或桌機瀏覽器開啟連結，即可即時觀看對話、追問、審查計畫並遠端操控 Agent。每個對話都是使用者專屬，你只能存取自己的 Copilot CLI 對話。

也可在進行中的對話隨時啟用遠端存取：

```
> /remote
```

更多遠端對話細節請參考 [Copilot CLI 文件](https://docs.github.com/copilot/how-tos/copilot-cli/steer-remotely)。

---

## 📝 作業

### 主挑戰：改善書籍應用程式的工具函式

前面示範聚焦於審查與重構 `book_app.py`。現在請你練習同樣技巧於另一個檔案 `utils.py`：

1. 啟動互動對話：`copilot`
2. 請 Copilot CLI 摘要檔案內容：`@samples/book-app-project/utils.py 此檔案每個函式分別做什麼？`
3. 請它加上輸入驗證：「為 `get_user_choice()` 增加驗證，能處理空輸入與非數字輸入」
4. 請它改善錯誤處理：「若 `get_book_details()` 收到空字串書名會怎麼樣？加上防護」
5. 請它加上 docstring：「為 `get_book_details()` 增加完整 docstring，包含參數說明與回傳值」
6. 觀察情境如何在提示間延續。每次改善都建立在前一次基礎上
7. 用 `/exit` 結束

**成功標準**：你應該得到一份改善後的 `utils.py`，包含輸入驗證、錯誤處理與 docstring，全部透過多輪對話完成。

<details>
<summary>💡 提示（點擊展開）</summary>

**可嘗試的範例提示：**
```bash
> @samples/book-app-project/utils.py 此檔案每個函式分別做什麼？
> 為 get_user_choice() 增加驗證，能處理空輸入與非數字輸入
> 若 get_book_details() 收到空字串書名會怎麼樣？加上防護
> 為 get_book_details() 增加完整 docstring，包含參數說明與回傳值
```

**常見問題：**
- 若 Copilot CLI 提問澄清問題，只需自然回答即可
- 情境會延續，每個提示都建立在前一個基礎上
- 若想重來可用 `/clear`

</details>

### 加分挑戰：比較三種模式

範例已用 `/plan` 規劃搜尋功能、用 `-p` 批次審查。現在請你針對新增 `list_by_year()` 方法到 `BookCollection` 類別這個新任務，分別用三種模式嘗試：1. **互動模式**：`copilot` → 請它一步步設計並建立方法  
2. **規劃模式**：`/plan Add a list_by_year(start, end) method to BookCollection that filters books by publication year range`  
3. **程式化模式**：`copilot --allow-all -p "@samples/book-app-project/books.py Add a list_by_year(start, end) method that returns books published between start and end year inclusive"`

**反思**：哪一種模式最自然？你會在什麼情境下使用每一種？

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 結果 | 修正方式 |
|------|------|----------|
| 輸入 `exit` 而不是 `/exit` | Copilot CLI 會把 "exit" 當成提示詞，而不是指令 | 斜線指令一律以 `/` 開頭 |
| 在多輪對話中使用 `-p` | 每次 `-p` 執行都是獨立的，不會記住先前的內容 | 需要累積情境的對話請用互動模式（`copilot`） |
| 忘記用引號包住含 `$` 或 `!` 的提示詞 | Shell 會在 Copilot CLI 處理前先解讀特殊字元 | 用引號包住提示詞：`copilot -p "What does $HOME mean?"` |

### 疑難排解

**"Model not available"** - 你的訂閱方案可能不包含所有模型。請用 `/model` 查看可用模型。

**"Context too long"** - 你的對話已用滿情境窗口。請用 `/clear` 重設，或開始新會話。

**"Rate limit exceeded"** - 請稍候幾分鐘再試。大量自動化作業可考慮用程式化模式並加上延遲。

</details>

---

# 摘要

## 🔑 重點整理

1. **互動模式** 適合探索與反覆嘗試——情境會持續累積。就像和一個會記得你說過什麼的人對話。
2. **規劃模式** 通常用於較複雜的任務。實作前可先檢查規劃內容。
3. **程式化模式** 用於自動化。不需互動。
4. **主要指令**（`/help`、`/clear`、`/plan`、`/research`、`/model`、`/exit`）涵蓋大部分日常需求。

> 📋 **快速參考**：完整指令與快捷鍵請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 接下來

現在你已了解三種模式，接下來我們要學習如何讓 Copilot CLI 取得你的程式碼情境。

在 **[第 02 章：情境與對話](../02-context-conversations/README.md)**，你將學到：

- 使用 `@` 語法參照檔案與目錄
- 用 `--resume` 和 `--continue` 管理會話
- 為什麼情境管理讓 Copilot CLI 如虎添翼

---

**[← 回到課程首頁](../README.md)** | **[繼續前往第 02 章 →](../02-context-conversations/README.md)**
