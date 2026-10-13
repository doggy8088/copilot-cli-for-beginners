![Chapter 01: First Steps](assets/chapter-header.png)

> **觀看 AI 如何即時找出錯誤、解釋難懂的程式碼，並產生可運作的腳本。接著學習 GitHub Copilot CLI 的三種使用方式。**

這一章就是魔法的起點！你將親身體驗為什麼開發者會形容 GitHub Copilot CLI 就像有一位資深工程師隨傳隨到。你會看到 AI 在幾秒內找出安全性漏洞、用簡單易懂的英文解釋複雜程式碼，並立即產生可運作的腳本。然後你會學會三種互動模式（互動、規劃、程式化），讓你能針對任何任務選擇最合適的方式。

> ⚠️ **先決條件**：請先完成 **[第 00 章：快速開始](../00-quick-start/README.md)**。你需要安裝並驗證 GitHub Copilot CLI，才能執行下方的示範。

## 🎯 學習目標

完成本章後，你將能夠：

- 透過實作示範體驗 GitHub Copilot CLI 帶來的生產力提升
- 根據任務選擇正確的模式（互動、規劃或程式化）
- 使用 slash 指令來控制你的會話

> ⏱️ **預估時間**：約 45 分鐘（閱讀 15 分鐘 + 實作 30 分鐘）

---

# 你的第一次 Copilot CLI 體驗

<img src="assets/first-copilot-experience.png" alt="Developer sitting at a desk with code on the monitor and glowing particles representing AI assistance" width="800"/>

直接動手，看看 Copilot CLI 能做些什麼。

---

## 先暖身：你的第一個提示詞

在進入精彩的示範之前，先從一些你現在就能嘗試的簡單提示詞開始。**不需要任何程式碼儲存庫**！只要打開終端機並啟動 Copilot CLI：

```bash
copilot
```

試試這些新手友善的提示詞：

```
> 用簡單的方式解釋 Python 中的 dataclass 是什麼

> 寫一個函式，能根據特定鍵排序字典組成的清單

> Python 中 list 和 tuple 有什麼不同？

> 給我 5 個撰寫乾淨 Python 程式碼的最佳實踐
```

不用 Python 也沒關係！只要問你想要的語言相關問題即可。

你會發現這種互動非常自然。就像問同事一樣提出問題。探索完畢後，輸入 `/exit` 離開會話。

**關鍵觀念**：GitHub Copilot CLI 是對話式的。你不需要特殊語法，只要用自然語言提問即可。

## 實際看看效果

現在來看看為什麼開發者會說這就像「資深工程師隨傳隨到」。

> 📖 **閱讀範例說明**：以 `>` 開頭的行是你在互動式 Copilot CLI 會話中輸入的提示詞。沒有 `>` 前綴的行則是你在終端機執行的 shell 指令。

> 💡 **關於範例輸出**：本課程中的範例輸出僅供參考。由於 Copilot CLI 的回應每次都會有所不同，你的結果在措辭、格式和細節上都可能不一樣。請著重於*回傳資訊的類型*，而非完全相同的文字。

### 示範 1：幾秒內完成程式碼審查

本課程包含一些有意設計程式碼品質問題的範例檔案。如果你在本機操作且尚未 clone 儲存庫，請執行下方的 `git clone` 指令，進入 `copilot-cli-for-beginners` 資料夾，然後啟動 `copilot`。

```bash
# 如果你在本機操作且尚未 clone，請先複製課程儲存庫
git clone https://github.com/github/copilot-cli-for-beginners
cd copilot-cli-for-beginners

# 啟動 Copilot
copilot
```

進入互動式 Copilot CLI 會話後，執行以下指令：

```
> 檢查 @samples/book-app-project/book_app.py 的程式碼品質問題並提出改進建議
```

> 💡 **`@` 符號是做什麼用的？** `@` 符號告訴 Copilot CLI 讀取一個檔案。你會在第 02 章學到詳細用法。現在只要照著指令輸入即可。

---

<details>
<summary>🎬 實際操作影片</summary>

![Code Review Demo](assets/code-review-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

---

**重點**：專業的程式碼審查只需幾秒。手動審查的話……肯定要花更多時間！

---

### 示範 2：解釋難懂的程式碼

是否曾經盯著程式碼發呆，不知道它在做什麼？在 Copilot CLI 會話中試試這個：

```
> 用簡單的方式解釋 @samples/book-app-project/books.py 的功能
```

---

<details>
<summary>🎬 實際操作影片</summary>

![Explain Code Demo](assets/explain-code-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

---

**會發生什麼事**：（你的輸出會不同）Copilot CLI 會讀取檔案、理解程式碼，並用簡單易懂的英文解釋。

```
這是一個使用 Python dataclass 的書籍收藏管理模組。

可以把它想像成一個數位書架：
- Book 是一個 dataclass —— 一種簡單儲存書籍資訊（書名、作者、年份、閱讀狀態）的方法
- BookCollection 管理整個收藏並負責儲存/載入

主要元件：

1. @dataclass 裝飾器（第 8 行）
   - 自動產生 __init__、__repr__ 等方法
   - 讓 Python 資料結構定義更簡潔

2. BookCollection 類別（第 16 行）
   - 維護 Book 物件的清單
   - 使用 JSON 檔案 I/O 處理持久化
   - load_books() 從 data.json 讀取
   - save_books() 用 asdict() 寫入 data.json

3. 書籍操作：
   - add_book() —— 建立並儲存新書
   - find_book_by_title() —— 搜尋收藏
   - mark_as_read() —— 更新閱讀狀態
   - find_by_author() —— 依作者名稱篩選

常見流程：從 JSON 讀取 → 操作 Python 物件 → 寫回 JSON
```

**重點**：複雜的程式碼也能像耐心的導師一樣解釋給你聽。

---

### 示範 3：產生可運作的程式碼

需要一個你本來要 Google 15 分鐘的函式嗎？在同一個會話中試試：

```
> 寫一個 Python 函式，接收書籍清單並回傳統計資料：
  總數、已讀數、未讀數、最舊和最新的書
```

---

<details>
<summary>🎬 實際操作影片</summary>

![Generate Code Demo](assets/generate-code-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

---

**會發生什麼事**：幾秒內產生一個完整、可運作的函式，直接複製貼上就能用。

探索完畢後，離開會話：

```
> /exit
```

**重點**：即時滿足，而且你全程都在同一個連續會話中。

---

# 模式與指令

<img src="assets/modes-and-commands.png" alt="Futuristic control panel with glowing screens, dials, and equalizers representing Copilot CLI modes and commands" width="800"/>

你已經看過 Copilot CLI 能做什麼。現在來了解*如何*有效運用這些能力。關鍵在於知道三種互動模式該用在哪些情境。

> 💡 **注意**：Copilot CLI 也有一個 **Autopilot** 模式，可以自動執行任務而不等待你的輸入。這很強大，但需要授權完整權限，並會自動使用高級請求。本課程聚焦於下方三種模式。等你熟悉基礎後，我們會再介紹 Autopilot。

---

## 🧩 真實世界比喻：外出用餐

把使用 GitHub Copilot CLI 想像成外出用餐。從規劃行程到點餐，不同情境需要不同方式：

| 模式 | 用餐比喻 | 適用時機 |
|------|----------|----------|
| **規劃** | 用 GPS 規劃去餐廳的路線 | 複雜任務——規劃路線、檢查停靠點、同意計畫再出發 |
| **互動** | 跟服務生對話 | 探索與反覆調整——提問、客製化、即時回饋 |
| **程式化** | 得來速點餐 | 快速、明確的任務——留在原本環境，迅速取得結果 |

就像外出用餐一樣，你會自然學會什麼時候該用哪種方式。

<img src="assets/ordering-food-analogy.png" alt="Three Ways to Use GitHub Copilot CLI - Plan Mode (GPS route to restaurant), Interactive Mode (talking to waiter), Programmatic Mode (drive-through)" width="800"/>

*根據任務選擇模式：規劃模式適合先規劃路線，互動模式適合來回討論，程式化模式適合快速一次性結果*

### 我該從哪個模式開始？

**建議從互動模式開始。** 
- 可以自由嘗試並追問細節
- 情境會隨對話自然累積
- 出錯也能用 `/clear` 輕鬆重來

熟悉後可以試試：
- **程式化模式**（`copilot -p "<你的提示詞>"`）適合快速、單次提問
- **規劃模式**（`/plan`）適合需要先詳細規劃再寫程式的情境

---

## 三種模式介紹

### 模式 1：互動模式（建議先從這裡開始）

<img src="assets/interactive-mode.png" alt="Interactive Mode - Like talking to a waiter who can answer questions and adjust the order" width="250"/>

**最適合**：探索、反覆調整、多輪對話。就像和服務生對話，可以即時提問、給回饋、隨時調整。

啟動互動式會話：

```bash
copilot
```

如你目前所見，會出現一個提示符號讓你自然輸入。想查詢可用指令，只要輸入：

```
> /help
```

**關鍵觀念**：互動模式會保留情境。每則訊息都會建立在前一則基礎上，就像真實對話一樣。

#### 互動模式範例

```bash
copilot

> 檢查 @samples/book-app-project/utils.py 並提出改進建議

> 為所有函式加上型別註記

> 讓錯誤處理更健全

> /exit
```

可以看到每個提示詞都建立在前一個答案之上。你是在進行一場對話，而不是每次都從頭開始。

---

### 模式 2：規劃模式

<img src="assets/plan-mode.png" alt="Plan Mode - Like planning a route before a trip using GPS" width="250"/>

**最適合**：需要在執行前先檢查整體做法的複雜任務。就像出發前用 GPS 規劃路線。

規劃模式會幫你在寫程式前先產生逐步計畫。使用 `/plan` 指令，按 **Shift+Tab** 可切換到規劃模式：

```bash
copilot

> /plan 為書籍應用程式新增「標記為已讀」指令
```

> 💡 **小技巧**：**Shift+Tab** 可在模式間切換：互動 → 規劃 → Autopilot。隨時在互動會話中按下即可，不必輸入指令。

你也可以用 `--plan` 旗標直接進入規劃模式：

```bash
copilot --plan
```

**規劃模式輸出範例：**（你的輸出可能不同）

```
📋 實作計畫

步驟 1：更新 book_app.py 的指令處理器
  - 新增 "mark" 指令的 elif 分支
  - 建立 handle_mark_as_read() 函式

步驟 2：實作處理函式
  - 提示使用者輸入書名
  - 呼叫 collection.mark_as_read(title)
  - 顯示成功/失敗訊息

步驟 3：更新說明文字
  - 在可用指令清單中加入 "mark"
  - 文件化指令用法

步驟 4：測試流程
  - 新增一本書
  - 標記為已讀
  - 確認清單輸出中的狀態有變更

要繼續實作嗎？[Y/n]
```

**關鍵觀念**：規劃模式讓你在寫任何程式碼前先檢查並修改做法。規劃模式下，Copilot CLI 是**唯讀**的，不會編輯任何檔案或執行會改變工作區的指令，直到你同意並進入實作階段。這讓你能安全地停留在「思考」階段，直到準備好為止。計畫完成後，你甚至可以請 Copilot CLI 把它存成檔案，例如「將此計畫存成 `mark_as_read_plan.md`」，就會產生一份包含計畫細節的 markdown 檔案。

> 💡 **想挑戰更複雜的任務？** 試試：`/plan 為書籍應用程式新增搜尋與篩選功能`。規劃模式可從簡單功能一路擴展到完整應用程式。

> 📚 **Autopilot 模式**：你可能注意到 Shift+Tab 會切換到第三種模式 **Autopilot**。在 autopilot 模式下，Copilot 會自動執行整個計畫，不會在每個步驟都等你確認——就像把任務交給同事並說「做完再告訴我」。典型流程是規劃 → 同意 → autopilot，也就是你必須先會寫計畫。你也可以用 `copilot --autopilot` 直接啟動 autopilot，或用 `/autopilot <目標>`（例如 `/autopilot 為書籍應用程式新增搜尋指令`）。也可以結合規劃與 autopilot，執行 `copilot --plan --mode autopilot`，Copilot 會先產生計畫再自動實作，不會暫停等你同意。建議先熟悉互動與規劃模式，再參考 [官方文件](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot)。

---

### 模式 3：程式化模式

<img src="assets/programmatic-mode.png" alt="Programmatic Mode - Like using a drive-through for a quick order" width="250"/>

**最適合**：自動化、腳本、CI/CD、單次指令。就像得來速點餐，不用和服務生對話。

用 `-p` 旗標執行一次性、無需互動的指令：

```bash
# 產生程式碼
copilot -p "寫一個判斷數字是偶數還是奇數的函式"

# 快速查詢
copilot -p "Python 如何讀取 JSON 檔案？"
```

**關鍵觀念**：程式化模式給你快速答案後直接結束。沒有對話，只有輸入 → 輸出。

<details>
<summary>📚 <strong>進階：在腳本中使用程式化模式</strong>（點擊展開）</summary>

熟悉後，你可以在 shell 腳本中用 `-p`：

```bash
#!/bin/bash

# 自動產生提交訊息
COMMIT_MSG=$(copilot -p "為以下內容產生 commit 訊息：$(git diff --staged)")
git commit -m "$COMMIT_MSG"

# 審查檔案
copilot --allow-all -p "檢查 @myfile.py 有無問題"
```
> ⚠️ **關於 `--allow-all`**：這個旗標會略過所有權限提示，讓 Copilot CLI 可以直接讀取檔案、執行指令、存取網址而不需詢問。這對於程式化模式（`-p`）很重要，因為沒有互動會話可供你同意。只在你自己寫的提示詞、信任的目錄下使用 `--allow-all`。不要用在不信任的輸入或敏感目錄。

</details>

---

## 必學 Slash 指令

這些指令很適合剛開始使用 Copilot CLI 時學起來：

| 指令 | 功能說明 | 適用時機 |
|------|----------|----------|
| `/ask` | 提問但不影響對話歷史 | 想要快速得到答案又不想干擾目前任務時 |
| `/clear` | 清除對話並重新開始 | 換主題時 |
| `/config` | 檢視或設定持久化預設值（如預設模型） | 想讓設定套用到所有未來會話時 |
| `/help` | 顯示所有可用指令 | 忘記指令時 |
| `/model` | 顯示或切換目前會話的 AI 模型 | 想更換 AI 模型時 |
| `/plan` | 在寫程式前先規劃工作 | 複雜功能時 |
| `/refine` | 將雜亂的提示詞重寫成清楚、聚焦的內容 | 提示詞太亂想要更好結果時 |
| `/research` | 使用 GitHub 與網路資源進行深度研究 | 需要先調查主題再寫程式時 |
| `/exit` | 結束會話 | 完成時 |

> 💡 **`/ask` 與一般對話的差異**：一般來說你輸入的每則訊息都會成為對話歷史的一部分，影響未來回應。`/ask` 則是「不留紀錄」的捷徑。很適合像 `/ask YAML 是什麼意思？` 這種臨時問題，不會污染會話情境。

> 💡 **`/refine` 幫你優化提示詞**：不確定自己的提示詞夠不夠清楚？先照想法打出來，再用 `/refine` 讓 Copilot 幫你重寫成精確、結構良好的提示詞。這對剛接觸 AI 工具、還在學習如何寫好提示詞時特別有用。

> 💡 **Tab 自動補全**：輸入 slash 指令時，按 **Tab** 可自動補全指令名稱，或在可用子指令與參數間切換。忘記指令名稱時特別方便。

> 💡 **Copilot 忙碌時也能排隊輸入**：如果 Copilot 正在執行任務，你想到下一步要做什麼，可以直接輸入並按 Enter。Copilot 會在目前任務結束後自動執行，不用等它閒下來。

這就是入門的全部內容！熟悉後可以再探索更多指令。

> 📚 **官方文件**：[CLI 指令參考](https://docs.github.com/copilot/reference/cli-command-reference)（完整指令與旗標清單）

<details>
<summary>📚 <strong>進階指令</strong>（點擊展開）</summary>

> 💡 上述必學指令已涵蓋日常大部分需求。這份參考適合你準備進一步探索時查閱。

### Agent 環境

| 指令 | 功能說明 |
|------|----------|
| `/agent` | 瀏覽並選擇可用的 agent |
| `/env` | 顯示已載入的環境細節——目前啟用的指令、MCP 伺服器、技能、agent 與外掛 |
| `/init` | 為你的儲存庫初始化 Copilot 指令 |
| `/instructions` | 檢視與管理目前會話已載入的所有指令檔 |
| `/mcp` | 開啟外掛儀表板（聚焦於 MCP 伺服器）；用 `/mcp config` 啟動 MCP 設定精靈 |
| `/plugin` | 開啟外掛儀表板，瀏覽、安裝、啟用與更新外掛 |
| `/settings` | 開啟互動式對話框，一次瀏覽與編輯所有使用者設定 |
| `/skills` | 開啟外掛儀表板（聚焦於技能），探索與管理技能 |
| `/subagents` | 檢視與管理目前會話中執行的子 agent |

> 💡 agent 會在 [第 04 章](../04-agents-custom-instructions/README.md) 詳細介紹，技能在 [第 05 章](../05-skills/README.md)，MCP 伺服器在 [第 06 章](../06-mcp-servers/README.md) 介紹。

### 模型與子 agent

| 指令 | 功能說明 |
|------|----------|
| `/config` | 檢視或設定持久化預設值（如 `/config model` 設定所有未來會話的預設模型） |
| `/delegate` | 將任務交給 GitHub Copilot 雲端 agent |
| `/fleet` | 將複雜任務拆分為平行子任務，加速完成 |
| `/model` | 僅切換目前會話的 AI 模型 |
| `/tasks` | 檢視背景子 agent 與分離的 shell 會話 |

### 程式碼

| 指令 | 功能說明 |
|------|----------|
| `/diff` | 檢查目前目錄的變更 |
| `/pr` | 操作目前分支的 pull request |
| `/research` | 使用 GitHub 與網路資源進行深度研究 |
| `/review` | 執行程式碼審查 agent 分析變更 |
| `/terminal-setup` | 啟用多行輸入支援（shift+enter 與 ctrl+enter） |

### 權限

| 指令 | 功能說明 |
|------|----------|
| `/add-dir <directory>` | 將目錄加入允許清單 |
| `/allow-all [on\|off\|show]` | 自動同意所有權限提示；用 `on` 啟用、`off` 關閉、`show` 檢查目前狀態 |
| `/permissions` | 切換審核模式（互動、規劃、autopilot），控制 Copilot 可自動執行的範圍 |
| `/yolo` | `/allow-all on` 的快速別名——自動同意所有權限提示。|
| `/cwd`, `/cd [directory]` | 檢視或切換工作目錄 |
| `/list-dirs` | 顯示所有允許的目錄 |

> ⚠️ **請小心使用**：`/allow-all` 與 `/yolo` 會略過確認提示。適合信任的專案，但對於不信任的程式碼請務必小心。

### 會話

| 指令 | 功能說明 |
|------|----------|
| `/clear` | 放棄目前會話（不儲存歷史）並重新開始對話 |
| `/compact` | 摘要對話內容以減少情境用量（可加聚焦指示，如 `/compact focus on the bug list`） |
| `/context` | 顯示情境視窗 token 用量與視覺化圖表 |
| `/keep-alive` | 防止 Copilot CLI 執行時系統進入睡眠——適合筆電長時間任務 |
| `/memory [on\|off\|show]` | 啟用、停用或檢視持久記憶——跨所有會話記住事實與偏好 |
| `/new` | 結束目前會話（儲存到歷史以供搜尋/繼續）並重新開始對話 |
| `/resume` | 切換到其他會話（可指定會話 ID 或名稱） |
| `/rename` | 重新命名目前會話（省略名稱則自動產生） |
| `/rewind` | 開啟時間軸選擇器，回復到對話中任一早期狀態；可選擇還原 Copilot 修改過的檔案（即使沒用 git 也可用） |
| `/usage` | 顯示會話用量統計與配額進度條 |
| `/session` | 顯示會話資訊與工作區摘要；用 `/session delete`、`/session delete <id>` 或 `/session delete-all` 刪除會話 |
| `/share` | 匯出會話為 markdown 檔、GitHub gist 或自含式 HTML 檔 |
| `/every <interval> <prompt>` | 排程定期執行提示詞（如 `/every 1h summarize new commits`）。間隔可用自然語言。`/loop` 是 `/every` 的別名。|
| `/after <time> <prompt>` | 排程延遲一次執行提示詞（如 `/after 30m run tests`）。時間可用自然語言。|

> 💡 **會話分頁**：互動式 Copilot CLI UI 頂端有 **Sessions 分頁**。你可以用它同時檢視並切換多個會話。在 Sessions 分頁按 `n` 可開新會話而不關閉現有會話。

### 顯示

| 指令 | 功能說明 |
|------|----------|
| `/statusline`（或 `/footer`） | 自訂底部狀態列顯示哪些項目（目錄、分支、effort、情境視窗、配額） |
| `/theme` | 檢視或設定終端機主題 |
| `/vim` | 啟用或停用 Vim 模式，在 composer 中用 vim 鍵綁定（如 `hjkl` 移動、`i`、`a`、`o` 插入模式） |
| `/voice` | 使用本地語音辨識輸入提示詞——自然說話即可 |

### 說明與回饋

| 指令 | 功能說明 |
|------|----------|
| `/app` | 直接從 CLI 開啟 GitHub app（或瀏覽器備用） |
| `/changelog` | 顯示 CLI 版本更新紀錄 |
| `/feedback` | 回報意見給 GitHub |
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

Copilot CLI 支援多種 AI 模型，包括 OpenAI、Anthropic、Google 等。你能用哪些模型取決於訂閱方案與地區。用 `/model` 查看並切換：

```bash
copilot
> /model

# 顯示可用模型並讓你選擇。例如：GPT-6 Sol、GPT-6 Luna、Claude Sonnet 5.5、Claude Opus 5.5。
```

> 💡 **會話 vs. 持久模型**：`/model` 只會改變**目前會話**的模型。新會話會回到預設。若要設定所有未來會話的預設模型，請在會話中用 `/config model`，或在一般 shell（非 Copilot 會話）用 `copilot config` 指令：

```bash
# 在終端機（非 Copilot 會話）設定預設模型
copilot config set model claude-sonnet-5.5

# 檢視所有已儲存設定
copilot config list
```# 移除設定並恢復為預設值
copilot config remove model
```

> 💡 **提示**：Copilot CLI 的使用量是以 **GitHub AI Credits** 來計算。所消耗的點數取決於你選擇的模型以及任務所用的 token 數量。功能更強大的模型可能會花費更多，因此建議日常任務使用較輕量的模型，將高推理能力的模型留給複雜工作。執行 `/usage` 可查看目前會話已用的 AI credits。

> 💡 **不確定該選哪個模型？** 從模型選擇器中選擇 **`Auto`**，讓 Copilot 自動為每個會話挑選最佳可用模型。如果你剛開始使用且不想煩惱模型選擇，這是很棒的預設選項。

> 💡 **模型家族捷徑**：你也可以直接在 `/model` 選擇器中輸入簡短的家族別名，例如 `opus`、`sonnet`、`haiku`、`gpt` 或 `gemini`，無需捲動完整清單。Copilot 會自動為你挑選該家族中最佳可用的模型。

> 💡 **模型選擇器導覽**：模型選擇器現在會將模型分組顯示 —— **最近使用**、**推薦** 和 **新上線** —— 讓你能快速找到上次用過的模型，或嘗試最新推出的選項。在選擇器內可用 **Shift+Tab** 切換分組檢視。

### Auto Routing 層級

Copilot CLI 提供一個 **Auto** 路由層級，能智慧地為每個任務選擇最佳模型：

```bash
copilot

> /model
# 選擇 "Auto"，讓 Copilot 根據速度與成本自動挑選最適合的模型
```

Auto 路由會考量你的任務複雜度，在快速（輕量）與強大（具推理能力）的模型間平衡速度與能力。如果你的組織有設定受管的 Auto 政策，可能會看到 **Strict** 模式或可由使用者覆寫的路由偏好設定。

> 💡 **新模型上線**：Copilot CLI 現已支援 **GPT-6 Astra**、**GPT-6.1 Sol**、**GPT-6 Luna** 和 **Claude Opus 5.5**，除了既有模型外都可在 `/model` 選擇器中試用！

### 使用 `copilot config` 管理設定

除了互動式的 `/config` slash 指令外，你也可以在終端機中用 `copilot config` 指令管理 Copilot CLI 設定：

```bash
# 列出所有目前設定
copilot config list

# 讀取特定設定
copilot config read model
copilot config read editorMode

# 設定預設值
copilot config set model opus        # 將預設模型設為 Claude Opus
copilot config set editorMode vim    # 預設啟用 Vim 模式

# 移除自訂設定（恢復為預設值）
copilot config remove model
```

這對於腳本自動化、設定新機器，或在互動會話外管理設定都很實用。用 `copilot config` 管理的設定會儲存在 `~/.copilot/config.json`，並套用到所有未來會話。

### 自訂逐字稿檢視模式

你可以透過設定逐字稿檢視模式，控制 Copilot 如何顯示工具活動與推理過程：

```bash
copilot

> /settings
# 找到 "Transcript view" 選項並設為 "concise"

# 或直接在 ~/.copilot/config.json 設定：
# "transcriptView": "concise"
```

**檢視選項：**
- **Default**：顯示所有工具呼叫與推理步驟，全部展開
- **Concise**：將相關工具活動分組為可收合的工作摘要，減少視覺雜訊，同時保留細節可查

精簡檢視適合想專注於高層進度、不想被中間步驟淹沒時使用。

### 啟動前選擇執行環境

啟動 Copilot CLI 時，現在可以在第一個提示前切換 **本地** 或 **雲端** 執行模式：

```bash
copilot
# Copilot 啟動後，按下 Ctrl+E 開啟環境選擇器
# 選擇：Local（在本機執行）或 Cloud（遠端執行）
```

這個功能適合你在不同工作型態間切換 —— 例如在本機互動作業，或讓背景任務在雲端執行。你的選擇會套用到整個會話，直到你再次切換為止。

</details>

---

# 練習

<img src="../assets/practice.png" alt="溫馨書桌擺設，螢幕顯示程式碼、檯燈、咖啡杯與耳機，準備動手練習" width="800"/>

是時候將你學到的知識付諸實踐了。

---

## ▶️ 自己動手試試看

### 互動式探索

啟動 Copilot，並用後續提示反覆改進書籍應用程式：

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

### 用 Programmatic Mode 自動化

`-p` 旗標讓你直接從終端機執行 Copilot CLI，無需進入互動模式。將下列腳本複製貼上到終端機（不是 Copilot 內），從專案根目錄批次審查書籍應用程式的所有 Python 檔案。

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

1. **互動挑戰**：啟動 `copilot` 並探索書籍應用程式。詢問 `@samples/book-app-project/books.py` 並連續請求三次改進建議。
2. **規劃模式挑戰**：執行 `/plan Add rating and review features to the book app`。仔細閱讀規劃內容。這樣的規劃合理嗎？
3. **程式化挑戰**：執行 `copilot --allow-all -p "List all functions in @samples/book-app-project/book_app.py and describe what each does"`。第一次就成功了嗎？

---

## 💡 提示：從網頁或行動裝置遠端控制 CLI 會話

GitHub Copilot CLI 支援 **遠端會話**，讓你能從網頁瀏覽器（桌機或手機）或 GitHub Mobile app 監控並互動進行中的 CLI 會話，無需親自坐在終端機前。

用 `--remote` 旗標啟動遠端會話：

```bash
copilot --remote
```

Copilot CLI 會顯示一個連結並提供 QR code。用手機或桌機瀏覽器開啟連結，即可即時觀看會話、發送後續提示、檢查規劃並遠端引導 agent。會話是使用者專屬的，你只能存取自己的 Copilot CLI 會話。

你也可以在任何進行中的會話中隨時啟用遠端存取：

```
> /remote
```

更多遠端會話細節可參見 [Copilot CLI 文件](https://docs.github.com/copilot/how-tos/copilot-cli/steer-remotely)。

---

## 📝 作業

### 主要挑戰：改進 Book App 的工具程式

前面的實作範例聚焦於審查與重構 `book_app.py`。現在請你用相同技巧練習另一個檔案 `utils.py`：

1. 啟動互動會話：`copilot`
2. 請 Copilot CLI 摘要檔案內容：「Summarize @samples/book-app-project/utils.py and explain what each function in this file does」
3. 請它加入輸入驗證：「Add validation to `get_user_choice()` so it handles empty input and non-numeric entries」
4. 請它改進錯誤處理：「What happens if `get_book_details()` receives an empty string for the title? Add guards for that.」
5. 請它補上 docstring：「Add a comprehensive docstring to `get_book_details()` with parameter descriptions and return values」
6. 觀察情境如何在多次提示間傳遞。每次改進都會建立在前一次基礎上
7. 用 `/exit` 結束

**成功標準**：你應該會得到一個改進過的 `utils.py`，具備輸入驗證、錯誤處理與 docstring，且全程透過多輪對話完成。

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
- 如果 Copilot CLI 提問澄清問題，只需自然回答即可
- 情境會持續傳遞，每個提示都會建立在前一個基礎上
- 若想重新開始，請用 `/clear`

</details>

### 加分挑戰：比較三種模式

前面範例用 `/plan` 實作搜尋功能、用 `-p` 批次審查。現在請你針對新增 `list_by_year()` 方法到 `BookCollection` 類別這個新任務，三種模式都試一次：

1. **互動式**：`copilot` → 請它一步步設計並實作這個方法
2. **規劃模式**：`/plan Add a list_by_year(start, end) method to BookCollection that filters books by publication year range`
3. **程式化模式**：`copilot --allow-all -p "@samples/book-app-project/books.py Add a list_by_year(start, end) method that returns books published between start and end year inclusive"`

**反思**：哪一種模式最自然？你會在什麼情境下用哪一種？

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生情況 | 修正方式 |
|------|----------|----------|
| 輸入 `exit` 而非 `/exit` | Copilot CLI 將 "exit" 當成一般提示詞，而非指令 | Slash 指令一律以 `/` 開頭 |
| 用 `-p` 進行多輪對話 | 每次 `-p` 執行都是獨立的，無法記憶前一次內容 | 多輪對話請用互動模式（`copilot`） |
| 忘記用引號包住含 `$` 或 `!` 的提示 | Shell 會在 Copilot CLI 處理前就解讀特殊字元 | 用單引號包住提示：`copilot -p 'What does $HOME mean?'` |
| 按一次 Esc 取消執行中任務 | 為避免誤觸，單次 Esc 不再能取消進行中的工作 | Copilot CLI 處理時請連按 **Esc 兩次** 取消 |

### 疑難排解

**"Model not available"** - 你的訂閱可能不包含所有模型。用 `/model` 查看可用模型。

**"Context too long"** - 你的對話已用滿 context window。請用 `/new` 開啟新會話。

**"Rate limit exceeded"** - 請稍等幾分鐘再試。批次作業可考慮用程式化模式並加上延遲。

</details>

---

# 小結

## 🔑 重點整理

1. **互動模式** 適合探索與反覆改進 —— 情境會持續傳遞。就像和一個記得你說過什麼的人對話。
2. **規劃模式** 通常用於較複雜的任務。實作前先審查計畫。
3. **程式化模式** 適合自動化，無需互動。
4. **常用指令**（`/ask`、`/help`、`/clear`、`/new`、`/plan`、`/research`、`/model`、`/exit`）涵蓋日常大部分需求。

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 接下來

現在你已了解三種模式，接下來要學習如何讓 Copilot CLI 取得你的程式碼情境。

在 **[第 02 章：情境與對話](../02-context-conversations/README.md)**，你將學到：

- 用 `@` 語法引用檔案與目錄
- 用 `--resume` 與 `--continue` 管理會話
- 為什麼情境管理讓 Copilot CLI 如虎添翼

---

**[← 回到課程首頁](../README.md)** | **[繼續前往第 02 章 →](../02-context-conversations/README.md)**
