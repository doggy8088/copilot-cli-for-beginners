![第 02 章：情境與對話](assets/chapter-header.png)

> **如果 AI 能看見你的整個程式碼庫，而不是一次只看一個檔案，會怎麼樣？**

在本章，你將解鎖 GitHub Copilot CLI 的真正威力：情境。你將學會使用 `@` 語法來參照檔案與目錄，讓 Copilot CLI 深入理解你的程式碼庫。你會發現如何在多個會話間維持對話、在數天後精確地從上次中斷處繼續工作，以及跨檔案分析如何捕捉單檔審查完全漏掉的錯誤。

## 🎯 學習目標

本章結束時，你將能夠：

- 使用 `@` 語法參照檔案、目錄與圖片
- 用 `--resume` 和 `--continue` 恢復先前的會話
- 理解 [情境窗口](../GLOSSARY.md#context-window) 的運作方式
- 撰寫有效的多輪對話
- 管理多專案工作流程的目錄權限

> ⏱️ **預估時間**：約 50 分鐘（20 分鐘閱讀 + 30 分鐘實作）

---

## 🧩 真實世界比喻：與同事合作

<img src="assets/colleague-context-analogy.png" alt="情境帶來差異 - 無情境 vs 有情境" width="800"/>

*就像你的同事一樣，Copilot CLI 並不是讀心術高手。提供更多資訊能幫助人類和 Copilot 都能給出更精準的協助！*

想像你在向同事解釋一個錯誤：

> **沒有情境**：「書籍應用程式不能用。」

> **有情境**：「請看 `books.py`，特別是 `find_book_by_title` 函式。它沒有做不分大小寫的比對。」

要給 Copilot CLI 提供情境，請用 *`@` 語法* 指向特定檔案。

---

# 必備：基本情境用法

<img src="assets/essential-basic-context.png" alt="發光的程式碼區塊由光軌連接，象徵情境如何流動於 Copilot CLI 對話中" width="800"/>

本節涵蓋你有效運用情境所需的一切。先掌握這些基本功。

---

## @ 語法

`@` 符號用於在提示中參照檔案與目錄。這就是你告訴 Copilot CLI「請看這個檔案」的方式。

> 💡 **注意**：本課程所有範例都使用此儲存庫內的 `samples/` 資料夾，你可以直接嘗試每個指令。

### 立即體驗（無需設定）

你可以用你電腦上的任何檔案來試試看：

```bash
copilot

# 指向你擁有的任何檔案
> Explain what @package.json does
> Summarize @README.md
> What's in @.gitignore and why?
```

> 💡 **沒有現成專案？** 快速建立測試檔案：
> ```bash
> echo "def greet(name): return 'Hello ' + name" > test.py
> copilot
> > What does @test.py do?
> ```

### 基本 @ 模式

| 模式 | 功能說明 | 使用範例 |
|------|----------|----------|
| `@file.py` | 參照單一檔案 | `Review @samples/book-app-project/books.py` |
| `@folder/` | 參照目錄內所有檔案 | `Review @samples/book-app-project/` |
| `@file1.py @file2.py` | 參照多個檔案 | `Compare @samples/book-app-project/book_app.py @samples/book-app-project/books.py` |

### 參照單一檔案

```bash
copilot

> Explain what @samples/book-app-project/utils.py does
```

---

<details>
<summary>🎬 實際操作展示！</summary>

![檔案情境示範](assets/file-context-demo.gif)

*示範輸出會有所不同。你的模型、工具與回應可能與此不同。*

</details>

---

### 參照多個檔案

```bash
copilot

> Compare @samples/book-app-project/book_app.py and @samples/book-app-project/books.py for consistency
```

### 參照整個目錄

```bash
copilot

> Review all files in @samples/book-app-project/ for error handling
```

---

## 跨檔案智慧

這就是情境變成超能力的地方。單檔分析很有用，跨檔案分析則是質的飛躍。

<img src="assets/cross-file-intelligence.png" alt="跨檔案智慧 - 比較單檔與跨檔案分析，顯示一起分析檔案能揭露錯誤、資料流與獨立時看不到的模式" width="800"/>

### 示範：找出跨檔案的錯誤

```bash
copilot

> @samples/book-app-project/book_app.py @samples/book-app-project/books.py
>
> How do these files work together? What's the data flow?
```

> 💡 **進階選項**：想要安全性導向的跨檔案分析，可試試 Python 安全範例：
> ```bash
> > @samples/buggy-code/python/user_service.py @samples/buggy-code/python/payment_processor.py
> > Find security vulnerabilities that span BOTH files
> ```

---

<details>
<summary>🎬 實際操作展示！</summary>

![多檔案示範](assets/multi-file-demo.gif)

*示範輸出會有所不同。你的模型、工具與回應可能與此不同。*

</details>

---

**Copilot CLI 發現的內容**：

```
跨模組分析
==========

1. 資料流模式
   book_app.py 建立 BookCollection 實例並呼叫方法
   books.py 定義 BookCollection 類別並管理資料持久化

   流程：book_app.py（UI）→ books.py（商業邏輯）→ data.json（儲存）

2. 重複的顯示函式
   book_app.py:9-21    show_books() 函式
   utils.py:28-36      print_books() 函式

   影響：兩個幾乎相同的函式做同樣的事。如果你更新其中一個（例如更改格式），必須記得同步另一個。

3. 不一致的錯誤處理
   book_app.py 處理 year 轉換的 ValueError
   books.py 發生錯誤時靜默回傳 None/False

   模式：各模組間沒有統一的錯誤處理方式
```

**為什麼這很重要**：單檔審查會錯過全局問題。只有跨檔案分析才能揭露：
- **重複程式碼**，應該整合
- **資料流模式**，顯示元件如何互動
- **架構問題**，影響維護性

---

### 示範：60 秒了解程式碼庫

<img src="assets/codebase-understanding.png" alt="分割畫面比較人工審查需 1 小時，AI 協助分析只需 10 秒" width="800" />

初次接觸專案？用 Copilot CLI 快速了解它。

```bash
copilot

> @samples/book-app-project/
>
> In one paragraph, what does this app do and what are its biggest quality issues?
```

**你會得到**：
```
這是一個 CLI 書籍收藏管理器，讓使用者能新增、列出、移除與搜尋儲存在 JSON 檔案中的書籍。最大品質問題包括：

1. 重複顯示邏輯 - show_books() 和 print_books() 做同樣的事
2. 不一致的錯誤處理 - 有些錯誤會丟出例外，有些回傳 False
3. 沒有輸入驗證 - year 可以是 0，title/author 可接受空字串
4. 缺乏測試 - 關鍵函式如 find_book_by_title 沒有測試覆蓋

優先修正：整合重複顯示函式並加入輸入驗證。
```

**結果**：原本需一小時閱讀的程式碼，濃縮成 10 秒。你知道該聚焦在哪裡。

---

## 實用範例

### 範例 1：帶情境的程式碼審查

```bash
copilot

> @samples/book-app-project/books.py Review this file for potential bugs

# Copilot CLI 現在擁有完整檔案內容，能給出具體回饋：
# "Line 49: Case-sensitive comparison may miss books..."
# "Line 29: JSON decode errors are caught but data corruption isn't logged..."

> What about @samples/book-app-project/book_app.py?

# 現在審查 book_app.py，但仍記得 books.py 的情境
```

### 範例 2：理解程式碼庫

```bash
copilot

> @samples/book-app-project/books.py What does this module do?

# Copilot CLI 讀取 books.py 並理解 BookCollection 類別

> @samples/book-app-project/ Give me an overview of the code structure

# Copilot CLI 掃描目錄並摘要

> How does the app save and load books?

# Copilot CLI 能追蹤它已讀過的程式碼
```

<details>
<summary>🎬 看多輪對話實際操作！</summary>

![多輪對話示範](assets/multi-turn-demo.gif)

*示範輸出會有所不同。你的模型、工具與回應可能與此不同。*

</details>

### 範例 3：多檔案重構

```bash
copilot

> @samples/book-app-project/book_app.py @samples/book-app-project/utils.py
> I see duplicate display functions: show_books() and print_books(). Help me consolidate these.

# Copilot CLI 同時看到兩個檔案，能建議如何合併重複程式碼
```

---

## 會話管理

會話會自動儲存。你可以恢復先前的會話，從中斷處繼續。

### 會話自動儲存

每次對話都會自動儲存。只要正常離開即可：

```bash
copilot

> @samples/book-app-project/ Let's improve error handling across all modules

[... 進行一些工作 ...]

> /exit
```

### 恢復最近的會話

```bash
# 從上次中斷處繼續
copilot --continue
```

### 恢復特定會話

```bash
# 互動式選擇會話清單
copilot --resume

# -r 是 --resume 的簡寫（省打字！）
copilot -r

# 或用 ID 恢復特定會話
copilot --resume=abc123

# 或用你命名的會話名稱恢復
copilot --resume="my book app review"
```

> 💡 **怎麼找到會話 ID？** 不需要記住它們。執行 `copilot --resume` 不帶 ID 會顯示互動式清單，包含你所有先前會話、名稱、ID 與最後活躍時間。直接選你要的即可。
>
> **多個終端機怎麼辦？** 每個終端機視窗都是獨立會話，有自己的情境。如果你在三個終端機開啟 Copilot CLI，就是三個獨立會話。從任何終端機執行 `--resume` 都能瀏覽全部。`--continue` 旗標會先抓取目前工作目錄的會話；若沒有，則選最近活躍的會話。
>
> **能不重啟就切換會話嗎？** 可以。在活躍會話內用 `/resume` slash 指令：
> ```
> > /resume
> # 顯示可切換的會話清單
> ```

### 整理你的會話

給會話有意義的名稱，方便日後查找。你可以在啟動時命名會話，或在會話內隨時重新命名：

```bash
# 啟動時直接命名會話
copilot --name book-app-review

# 或在會話內重新命名
copilot

> /rename book-app-review
# 會話已重新命名，方便辨識
```

命名後，你可以直接用名稱恢復會話，無需瀏覽清單：

```bash
copilot --resume=book-app-review
```

要清除不再需要的會話，可在會話內用 `/session delete`：

```bash
copilot

> /session delete            # 刪除目前會話
> /session delete abc123     # 刪除指定 ID 的會話
> /session delete-all        # 刪除所有會話（請小心使用！）
```

### 跨會話持久記憶

會話會儲存你的對話歷史，但 **記憶** 更進一步，讓 Copilot CLI 能在*所有會話*間記住偏好與事實，而不僅限於單一會話。

```bash
copilot

> /memory show
# 顯示 Copilot CLI 目前記得你與專案的內容

> /memory on
# 開啟記憶（若你的帳號支援則預設開啟）

> /memory off
# 關閉記憶（若你偏好每次都全新開始）
```

例如，你告訴 Copilot CLI「我偏好用 pytest 做 Python 測試」，它能記住這個偏好，未來會自動套用。你不用每次重複。

> 💡 **記憶 vs. 會話**：會話儲存對話歷史，方便你恢復特定任務。記憶則儲存可重用的儲存庫事實與使用者偏好，Copilot 未來工作時可自動套用。想像會話是任務筆記本，記憶則是 Copilot 可帶著走的可重用情境。

### 檢查與管理情境

隨著你加入檔案與對話，Copilot CLI 的 [情境窗口](../GLOSSARY.md#context-window) 會逐漸填滿。有多種指令可協助你掌控：

```bash
copilot

> /context
Context usage: 62k/200k tokens (31%)

> /clear
# 放棄目前會話（不儲存歷史），開始全新對話

> /new
# 結束目前會話（儲存到歷史以便搜尋/恢復），開始全新對話

> /rewind
# 開啟時間軸選擇器，讓你回到對話中較早的某個點
```

> 💡 **何時用 `/clear` 或 `/new`**：如果你剛審查完 books.py，想切換討論 utils.py，先執行 /new（或 /clear 若不需會話歷史）。否則舊主題的情境可能會讓回應混亂。

> 💡 **犯錯或想嘗試不同路線？** 用 `/rewind`（或按兩次 Esc）開啟**時間軸選擇器**，可回到對話中任何較早的點，不只最近一次。這很適合走錯路時回溯，而不用完全重來。

---

### 從中斷處繼續

<img src="assets/session-persistence-timeline.png" alt="時間軸顯示 GitHub Copilot CLI 會話如何跨天持續 - 週一開始，週三恢復並完整還原情境" width="800"/>

*會話在你離開時自動儲存。數天後恢復，完整情境：檔案、問題、進度都記得。*

想像這樣的多日工作流程：

```bash
# 週一：一開始就命名書籍應用程式審查會話
copilot --name book-app-review

> @samples/book-app-project/books.py
> Review and number all code quality issues

品質問題清單：
1. 重複顯示函式（book_app.py & utils.py）- 中等
2. 空字串未驗證 - 中等
3. year 可為 0 或負數 - 低
4. 所有函式缺少型別提示 - 低
5. 缺乏錯誤紀錄 - 低

> Fix issue #1 (duplicate functions)
# 著手修正...

> /exit
```

```bash
# 週三：精確從上次命名的會話繼續
copilot --resume=book-app-review

> What issues remain unfixed from our book app review?

book-app-review 會話剩餘未修正問題：
2. 空字串未驗證 - 中等
3. year 可為 0 或負數 - 低
4. 所有函式缺少型別提示 - 低
5. 缺乏錯誤紀錄 - 低

第 1 項（重複函式）已於週一修正。

> Let's tackle issue #2 next
```

**這有多強大**：數天後，Copilot CLI 記得：
- 你正在處理的檔案
- 編號的問題清單
- 已處理哪些項目
- 對話的情境

不用重新解釋、不用重讀檔案，直接繼續工作。

---

**🎉 你已掌握必備技能！** `@` 語法、會話管理（`--name`/`--continue`/`--resume`/`/rename`）、情境指令（`/context`/`/clear`）足以讓你高效工作。以下內容為選修，準備好時再回來。

---

# 選修：深入探索

<img src="assets/optional-going-deeper.png" alt="藍紫色調的抽象水晶洞穴，象徵深入探索情境概念" width="800"/>

這些主題建立在上述必備技能之上。**挑你感興趣的，或直接跳到 [實作練習](#practice)。**

| 我想學... | 跳到 |
|---|---|
| 萬用字元模式與進階會話指令 | [進階 @ 模式與會話指令](#additional-patterns) |
| 多輪提示如何累積情境 | [情境感知對話](#context-aware-conversations) |
| Token 限制與 `/compact` | [理解情境窗口](#understanding-context-windows) |
| 如何挑選要參照的檔案 | [挑選參照內容](#choosing-what-to-reference) |
| 分析截圖與設計稿 | [圖片操作](#working-with-images) |

<details>
<summary><strong>進階 @ 模式與會話指令</strong></summary>
<a id="additional-patterns"></a>

### 進階 @ 模式

進階用戶可用萬用字元模式與圖片參照：

| 模式 | 功能說明 |
|------|----------|
| `@folder/*.py` | 資料夾內所有 .py 檔案 |
| `@**/test_*.py` | 遞迴萬用字元：找出所有測試檔 |
| `@image.png` | 圖片檔案用於 UI 審查 |

```bash
copilot

> Find all TODO comments in @samples/book-app-project/**/*.py
```

### 檢視會話資訊

```bash
copilot

> /session
# 顯示目前會話詳細資訊與工作區摘要

> /usage
# 顯示會話統計與使用狀況
```

### 分享你的會話

```bash
copilot

> /share file ./my-session.md
# 將會話匯出為 markdown 檔案

> /share gist
# 建立 GitHub gist 儲存會話

> /share html
# 匯出為自包含互動式 HTML 檔案
# 適合分享精美會話報告給團隊或存檔參考
```

</details>

<details>
<summary><strong>情境感知對話</strong></summary>
<a id="context-aware-conversations"></a>

### 情境感知對話

魔法發生在多輪對話能互相累積時。

#### 範例：漸進式強化

```bash
copilot

> @samples/book-app-project/books.py Review the BookCollection class

Copilot CLI: "這個類別功能正常，但我發現：
1. 有些方法缺少型別提示
2. title/author 沒有空字串驗證
3. 錯誤處理可再加強"

> Add type hints to all methods

Copilot CLI: "這是加上完整型別提示的類別..."
[顯示加型別的版本]

> Now improve error handling

Copilot CLI: "在加型別版本基礎上，這是改進的錯誤處理..."
[加入驗證與適當例外]

> Generate tests for this final version

Copilot CLI: "根據加型別與錯誤處理的類別..."
[產生完整測試]
```

注意每個提示都建立在前一次成果之上。這就是情境的威力。

</details>

<details>
<summary><strong>理解情境窗口</strong></summary>
<a id="understanding-context-windows"></a>

### 理解情境窗口

你已從必備技能學會 `/context` 與 `/clear`。這裡更深入說明情境窗口的運作。

每個 AI 都有「情境窗口」，即一次能考量的文字量。

<img src="assets/context-window-visualization.png" alt="情境窗口視覺化" width="800"/>

*情境窗口就像桌子：一次只能放有限東西。檔案、對話歷史、系統提示都佔空間。*

#### 達到上限時會發生什麼

```bash
copilot

> /context

Context usage: 45,000 / 128,000 tokens (35%)

# 加入更多檔案與對話，這個數字會增加

> @large-codebase/

Context usage: 120,000 / 128,000 tokens (94%)

# 警告：接近情境上限

> @another-large-file.py

Context limit reached. Older context will be summarized.
```

#### `/compact` 指令

情境快滿但不想失去對話時，`/compact` 會摘要你的歷史，釋放 token 空間：

```bash
copilot

> /compact
# 摘要對話歷史，釋放情境空間
# 你的關鍵發現與決策會保留
```

你也可以給 `/compact` 選擇性聚焦指令，決定摘要時優先保留哪些內容：

```bash
copilot

> /compact focus on the list of bugs we found and decisions made
# 摘要歷史，讓錯誤清單與決策突出
```

> 💡 **何時用聚焦指令**：若你的對話涵蓋多主題，聚焦指令能讓 `/compact` 保留最相關部分，避免失去主線。

#### 情境效率小技巧

| 情境 | 行動 | 原因 |
|------|------|------|
| 開始新主題 | `/clear` | 移除無關情境 |
| 走錯路 | `/rewind` | 回到較早的任何點 |
| 長對話 | `/compact` | 摘要歷史，釋放 token |
| 需特定檔案 | `@file.py` 而非 `@folder/` | 只載入所需內容 |
| 達到上限 | `/new` 或 `/clear` | 全新情境 |
| 多主題 | 每主題用 `/rename` | 容易恢復正確會話 |

#### 大型程式碼庫最佳實踐

1. **具體**：用 `@samples/book-app-project/books.py` 取代 `@samples/book-app-project/`
2. **主題間清除情境**：切換焦點時用 `/new` 或 `/clear`
3. **用 `/compact`**：摘要對話，釋放情境空間
4. **多會話並行**：每個功能或主題用一個會話

</details>

<details>
<summary><strong>挑選參照內容</strong></summary>
<a id="choosing-what-to-reference"></a>

### 挑選參照內容

不是所有檔案都適合納入情境。以下是明智選擇的方法：

#### 檔案大小考量

| 檔案大小 | 約略 [Token](../GLOSSARY.md#token) | 策略 |
|----------|-------------------|------|
| 小型（<100 行） | ~500-1,500 tokens | 可自由參照 |
| 中型（100-500 行） | ~1,500-7,500 tokens | 參照特定檔案 |
| 大型（500+ 行） | 7,500+ tokens | 精選，鎖定特定檔案 |
| 超大型（1000+ 行） | 15,000+ tokens | 考慮拆分或只針對區段 |

**具體範例：**
- 書籍應用程式的 4 個 Python 檔案合計 ≈ 2,000-3,000 tokens
- 一般 Python 模組（200 行） ≈ 3,000 tokens
- Flask API 檔案（400 行） ≈ 6,000 tokens
- 你的 package.json ≈ 200-500 tokens
- 短提示 + 回應 ≈ 500-1,500 tokens

> 💡 **程式碼快速估算**：行數 × 15 ≈ token 數。僅供參考。

#### 包含與排除什麼

**高價值**（建議納入）：
- 進入點（`book_app.py`、`main.py`、`app.py`）
- 你詢問的特定檔案
- 目標檔案直接 import 的檔案
- 設定檔（`requirements.txt`、`pyproject.toml`）
- 資料模型或 dataclass

**低價值**（可考慮排除）：
- 產生的檔案（編譯輸出、打包資產）
- node modules 或 vendor 目錄
- 大型資料檔或測試資料
- 與問題無關的檔案

#### 具體性光譜

```
越不具體 ────────────────────────► 越具體
@samples/book-app-project/                      @samples/book-app-project/books.py:47-52
     │                                       │
     └─ 掃描全部                             └─ 只針對所需
        （佔用更多情境）                        （節省情境）
```

**何時用廣泛參照**（`@samples/book-app-project/`）：
- 初次探索程式碼庫
- 尋找跨多檔案的模式
- 架構審查

**何時用具體參照**（`@samples/book-app-project/books.py`）：
- 偵錯特定問題
- 審查特定檔案
- 詢問單一函式

#### 實用範例：分階段情境載入

```bash
copilot

# 步驟 1：先看結構
> @package.json What frameworks does this project use?

# 步驟 2：根據答案縮小範圍
> @samples/book-app-project/ Show me the project structure

# 步驟 3：聚焦重點
> @samples/book-app-project/books.py Review the BookCollection class

# 步驟 4：只在需要時加入相關檔案
> @samples/book-app-project/book_app.py @samples/book-app-project/books.py How does the CLI use the BookCollection?
```

這種分階段方式能讓情境聚焦且高效。

</details>

<details>
<summary><strong>圖片操作</strong></summary>
<a id="working-with-images"></a>

### 圖片操作

你可以用 `@` 語法在對話中加入圖片，或直接**從剪貼簿貼上**（Cmd+V / Ctrl+V）。Copilot CLI 能分析截圖、設計稿與圖表，協助 UI 偵錯、設計實作與錯誤分析。

```bash
copilot

> @assets/screenshot.png What is happening in this image?

```> @assets/mockup.png 撰寫 HTML 和 CSS 以符合此設計。請將其放在一個名為 index.html 的新檔案中，並將 CSS 放在 styles.css。

```

> 📖 **深入學習**：請參閱 [進階情境功能](../appendices/additional-context.md#working-with-images) 以了解支援的格式、實用案例，以及將圖片與程式碼結合的技巧。

</details>

---

# 練習

<img src="../assets/practice.png" alt="溫馨的書桌擺設，螢幕顯示程式碼，檯燈、咖啡杯與耳機準備好進行實作練習" width="800"/>

是時候運用你的情境與會話管理技能了。

---

## ▶️ 自行嘗試

### 專案完整審查

本課程提供可直接檢視的範例檔案。啟動 copilot 並執行下列提示：

```bash
copilot

> @samples/book-app-project/ 請幫我進行這個專案的程式碼品質審查

# Copilot CLI 會找出以下問題：
# - 重複的顯示函式
# - 缺少輸入驗證
# - 不一致的錯誤處理
```

> 💡 **想用自己的檔案試試看嗎？** 建立一個小型 Python 專案（`mkdir -p my-project/src`），加入一些 .py 檔案，然後用 `@my-project/src/` 來審查它們。如果需要，也可以請 copilot 幫你產生範例程式碼！

### 會話工作流程

```bash
copilot

> /rename book-app-review
> @samples/book-app-project/books.py 我們來為空白書名加入輸入驗證

[Copilot CLI 建議驗證方式]

> 實作這個修正
> 現在整合 @samples/book-app-project/ 中重複的顯示函式
> /exit

# 之後 - 從上次中斷處繼續
copilot --continue

> 為我們做過的變更產生測試
```

---

完成示範後，請嘗試以下變化題：

1. **跨檔案挑戰**：分析 book_app.py 和 books.py 如何協同運作：
   ```bash
   copilot
   > @samples/book-app-project/book_app.py @samples/book-app-project/books.py
   > 這兩個檔案有什麼關聯？有沒有什麼程式碼異味？
   ```

2. **會話挑戰**：啟動一個會話，用 `/rename my-first-session` 命名，進行一些操作，然後用 `/exit` 離開，再執行 `copilot --continue`。它還記得你在做什麼嗎？

3. **情境挑戰**：在會話中途執行 `/context`。你用了多少 token？試試 `/compact` 再檢查一次。（更多關於 `/compact` 的說明，請見 Going Deeper 章節的 [理解情境窗口](#understanding-context-windows)。）

**自我檢查**：當你能解釋為什麼 `@folder/` 比逐一開啟每個檔案更強大時，就代表你已經理解情境的運作。

---

## 📝 作業

### 主要挑戰：追蹤資料流

前面的實作範例著重於程式碼品質審查與輸入驗證。現在請用相同的情境技巧，練習另一個任務：追蹤資料在應用程式中的流動方式：

1. 啟動互動式會話：`copilot`
2. 同時參照 `books.py` 和 `book_app.py`：
   `@samples/book-app-project/books.py @samples/book-app-project/book_app.py 請追蹤一本書從使用者輸入到儲存到 data.json 的流程。每個步驟涉及哪些函式？`
3. 加入資料檔案以提供更多情境：
   `@samples/book-app-project/data.json 如果這個 JSON 檔案遺失或損毀會發生什麼事？哪些函式會失敗？`
4. 請求跨檔案的改進建議：
   `@samples/book-app-project/books.py @samples/book-app-project/utils.py 請建議一個能在兩個檔案中都適用的一致性錯誤處理策略。`
5. 重新命名會話：`/rename data-flow-analysis`
6. 用 `/exit` 離開，再用 `copilot --continue` 回到會話，並針對資料流提出後續問題

**成功標準**：你能跨多個檔案追蹤資料流動、恢復已命名的會話，並獲得跨檔案的建議。

<details>
<summary>💡 提示（點擊展開）</summary>

**開始練習：**
```bash
cd /path/to/copilot-cli-for-beginners
copilot
> @samples/book-app-project/books.py @samples/book-app-project/book_app.py 請追蹤一本書從使用者輸入到儲存到 data.json 的流程。
> @samples/book-app-project/data.json 如果這個檔案遺失或損毀會發生什麼事？
> /rename data-flow-analysis
> /exit
```

然後用：`copilot --continue` 恢復會話

**實用指令：**
- `@file.py` - 參照單一檔案
- `@folder/` - 參照資料夾內所有檔案（注意結尾的 `/`）
- `/context` - 檢查目前使用的情境量
- `/rename <name>` - 幫會話命名，方便日後繼續

</details>

### 加分挑戰：情境限制

1. 用 `@samples/book-app-project/` 一次參照所有書籍應用程式檔案
2. 針對不同檔案（如 `books.py`、`utils.py`、`book_app.py`、`data.json`）提出多個詳細問題
3. 執行 `/context` 查看使用情況。填滿得有多快？
4. 練習使用 `/compact` 釋放空間，然後繼續對話
5. 嘗試更精確地指定檔案（例如用 `@samples/book-app-project/books.py` 取代整個資料夾），觀察對情境使用量的影響

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生情況 | 解決方法 |
|---------|--------------|-----|
| 忘記在檔名前加 `@` | Copilot CLI 將 "books.py" 當成純文字處理 | 請用 `@samples/book-app-project/books.py` 參照檔案 |
| 以為會話會自動保存 | 重新啟動 `copilot` 會失去所有先前情境 | 請用 `--continue`（回到上次會話）或 `--resume`（選擇會話） |
| 參照當前目錄外的檔案 | 出現 "Permission denied" 或 "File not found" 錯誤 | 用 `/add-dir /path/to/directory` 開放目錄存取權限 |
| 換主題時沒用 `/clear` | 舊情境會干擾新主題的回應 | 換任務前請先執行 `/clear` |

### 疑難排解

**"File not found" 錯誤** - 請確認你在正確的目錄下：

```bash
pwd  # 檢查目前目錄
ls   # 列出檔案

# 然後啟動 copilot 並用相對路徑
copilot

> Review @samples/book-app-project/books.py
```

**"Permission denied"** - 請將目錄加入允許清單：

```bash
copilot --add-dir /path/to/directory

# 或在會話中：
> /add-dir /path/to/directory
```

**情境很快就被填滿**：
- 更精確地指定檔案
- 不同主題間用 `/clear`
- 將工作分散到多個會話

</details>

---

# 小結

## 🔑 重點整理

1. **`@` 語法** 讓 Copilot CLI 知道哪些檔案、資料夾與圖片要納入情境
2. **多輪對話** 會隨著情境累積而逐步深入
3. **會話自動儲存**：啟動時用 `--name` 命名，日後用 `--resume=<name>` 恢復，或用 `--continue` 回到最近一次會話
4. **情境窗口有限**：用 `/clear`、`/compact`、`/context`、`/new`、`/rewind` 管理。用 `/compact focus on <topic>` 指定要保留的重點
5. **持久記憶**（`/memory`）讓 Copilot CLI 能跨*所有*會話記住偏好與事實——不只限於當前會話
6. **權限旗標**（`--add-dir`、`--allow-all`）可控管多目錄存取，請謹慎使用！
7. **圖片參照**（`@screenshot.png`）有助於視覺化除錯 UI 問題

> 📚 **官方文件**：[使用 Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli) 取得完整的情境、會話與檔案操作參考。

> 📋 **快速參考**：請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference) 以取得完整指令與快捷鍵列表。

---

## ➡️ 下一步

現在你已經學會如何為 Copilot CLI 提供情境，接下來就要將這些技巧應用在實際的開發任務上。你剛學到的情境技巧（檔案參照、跨檔案分析、會話管理）正是下一章強大工作流程的基礎。

在 **[第三章：開發工作流程](../03-development-workflows/README.md)** 中，你將學到：

- 程式碼審查工作流程
- 重構模式
- 除錯協助
- 測試產生
- Git 整合

---

**[← 回到第一章](../01-setup-and-first-steps/README.md)** | **[繼續前往第三章 →](../03-development-workflows/README.md)**
