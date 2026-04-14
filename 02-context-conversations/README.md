![Chapter 02: Context and Conversations](images/chapter-header.png)

> **如果 AI 能看見你整個程式碼庫，而不只是單一檔案，會怎樣？**

在本章中，你將解鎖 GitHub Copilot CLI 的真正威力：情境（context）。你會學會使用 `@` 語法來參照檔案與目錄，讓 Copilot CLI 能深入理解你的程式碼庫。你將學會如何在多個工作階段間維持對話，幾天後能精確地從上次中斷的地方繼續，並見識跨檔案分析如何發現單檔檢查完全忽略的錯誤。

## 🎯 學習目標

完成本章後，你將能夠：

- 使用 `@` 語法參照檔案、目錄與圖片
- 透過 `--resume` 和 `--continue` 恢復先前的工作階段
- 了解 [情境窗口](../GLOSSARY.md#context-window) 的運作方式
- 撰寫有效的多輪對話
- 管理多專案工作流程下的目錄權限

> ⏱️ **預估時間**：約 50 分鐘（20 分鐘閱讀 + 30 分鐘實作）

---

## 🧩 真實世界比喻：與同事協作

<img src="images/colleague-context-analogy.png" alt="Context Makes the Difference - Without vs With Context" width="800"/>

*就像你的同事，Copilot CLI 不是讀心術專家。提供更多資訊能幫助人類與 Copilot 都給出更精準的協助！*

想像你要向同事解釋一個 bug：

> **沒有情境**：「書籍應用程式壞掉了。」

> **有情境**：「請看 `books.py`，特別是 `find_book_by_title` 函式。它沒有做不區分大小寫的比對。」

要為 Copilot CLI 提供情境，請*使用 `@` 語法*，將 Copilot CLI 指向特定檔案。

---

# 必備：基本情境

<img src="images/essential-basic-context.png" alt="Glowing code blocks connected by light trails representing how context flows through Copilot CLI conversations" width="800"/>

本節涵蓋你有效運用情境所需的一切。請先精通這些基礎。

---

## @ 語法

`@` 符號可在提示詞中參照檔案與目錄。這就是你告訴 Copilot CLI「請看這個檔案」的方式。

> 💡 **注意**：本課程所有範例皆使用本儲存庫內的 `samples/` 資料夾，你可以直接嘗試每個指令。

### 立即試試看（無需設定）

你可以用電腦上的任何檔案來嘗試：

```bash
copilot

# 指向你有的任一檔案
> Explain what @package.json does
> Summarize @README.md
> What's in @.gitignore and why?
```

> 💡 **沒有現成專案？** 快速建立一個測試檔案：
> ```bash
> echo "def greet(name): return 'Hello ' + name" > test.py
> copilot
> > What does @test.py do?
> ```

### 基本 @ 模式

| 模式 | 功能說明 | 範例用途 |
|---------|--------------|-------------|
| `@file.py` | 參照單一檔案 | `Review @samples/book-app-project/books.py` |
| `@folder/` | 參照目錄下所有檔案 | `Review @samples/book-app-project/` |
| `@file1.py @file2.py` | 參照多個檔案 | `Compare @samples/book-app-project/book_app.py @samples/book-app-project/books.py` |

### 參照單一檔案

```bash
copilot

> Explain what @samples/book-app-project/utils.py does
```

---

<details>
<summary>🎬 觀看實際操作！</summary>

![File Context Demo](images/file-context-demo.gif)

*展示結果會有所不同。你的模型、工具與回應可能與這裡不同。*

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

這正是情境成為超能力的地方。單檔分析很有用，跨檔案分析則能徹底改變結果。

<img src="images/cross-file-intelligence.png" alt="Cross-File Intelligence - comparing single-file vs cross-file analysis showing how analyzing files together reveals bugs, data flow, and patterns invisible in isolation" width="800"/>

### 範例：找出跨多檔案的錯誤

```bash
copilot

> @samples/book-app-project/book_app.py @samples/book-app-project/books.py
>
> How do these files work together? What's the data flow?
```

> 💡 **進階選項**：想做安全性導向的跨檔案分析，可嘗試 Python 安全性範例：
> ```bash
> > @samples/buggy-code/python/user_service.py @samples/buggy-code/python/payment_processor.py
> > Find security vulnerabilities that span BOTH files
> ```

---

<details>
<summary>🎬 觀看實際操作！</summary>

![Multi-File Demo](images/multi-file-demo.gif)

*展示結果會有所不同。你的模型、工具與回應可能與這裡不同。*

</details>

---

**Copilot CLI 發現的內容**：

```
Cross-Module Analysis
=====================

1. DATA FLOW PATTERN
   book_app.py creates BookCollection instance and calls methods
   books.py defines BookCollection class and manages data persistence

   Flow: book_app.py (UI) → books.py (business logic) → data.json (storage)

2. DUPLICATE DISPLAY FUNCTIONS
   book_app.py:9-21    show_books() function
   utils.py:28-36      print_books() function

   Impact: Two nearly identical functions doing the same thing. If you update
   one (like changing the format), you must remember to update the other.

3. INCONSISTENT ERROR HANDLING
   book_app.py handles ValueError from year conversion
   books.py silently returns None/False on errors

   Pattern: No unified approach to error handling across modules
```

**為什麼這很重要**：單檔檢查會錯過全貌，只有跨檔案分析才能發現：
- **重複程式碼**（應該合併）
- **資料流模式**（了解元件如何互動）
- **架構問題**（影響可維護性）

---

### 範例：60 秒了解一個程式碼庫

<img src="images/codebase-understanding.png" alt="Split-screen comparison showing manual code review taking 1 hour versus AI-assisted analysis taking 10 seconds" width="800" />

剛加入新專案？用 Copilot CLI 快速了解它。

```bash
copilot

> @samples/book-app-project/
>
> In one paragraph, what does this app do and what are its biggest quality issues?
```

**你會得到**：
```
This is a CLI book collection manager that lets users add, list, remove, and
search books stored in a JSON file. The biggest quality issues are:

1. Duplicate display logic - show_books() and print_books() do the same thing
2. Inconsistent error handling - some errors raise exceptions, others return False
3. No input validation - year can be 0, empty strings accepted for title/author
4. Missing tests - no test coverage for critical functions like find_book_by_title

Priority fix: Consolidate duplicate display functions and add input validation.
```

**結果**：原本要花一小時閱讀的程式碼，現在 10 秒就能掌握重點，馬上知道該聚焦在哪裡。

---

## 實用範例

### 範例 1：有情境的程式碼審查

```bash
copilot

> @samples/book-app-project/books.py Review this file for potential bugs

# Copilot CLI 現在有完整檔案內容，能給出具體建議：
# "Line 49: Case-sensitive comparison may miss books..."
# "Line 29: JSON decode errors are caught but data corruption isn't logged..."

> What about @samples/book-app-project/book_app.py?

# 現在審查 book_app.py，但仍保有 books.py 的情境
```

### 範例 2：理解一個程式碼庫

```bash
copilot

> @samples/book-app-project/books.py What does this module do?

# Copilot CLI 讀取 books.py 並理解 BookCollection 類別

> @samples/book-app-project/ Give me an overview of the code structure

# Copilot CLI 掃描目錄並摘要

> How does the app save and load books?

# Copilot CLI 能追蹤已讀過的程式碼
```

<details>
<summary>🎬 觀看多輪對話實例！</summary>

![Multi-Turn Demo](images/multi-turn-demo.gif)

*展示結果會有所不同。你的模型、工具與回應可能與這裡不同。*

</details>

### 範例 3：跨檔案重構

```bash
copilot

> @samples/book-app-project/book_app.py @samples/book-app-project/utils.py
> I see duplicate display functions: show_books() and print_books(). Help me consolidate these.

# Copilot CLI 同時看到兩個檔案，能建議如何合併重複程式碼
```

---

## 工作階段管理

每次工作階段都會自動儲存。你可以隨時恢復先前的工作階段，從中斷處繼續。

### 工作階段自動儲存

每次對話都會自動儲存。只要正常結束即可：

```bash
copilot

> @samples/book-app-project/ Let's improve error handling across all modules

[... 進行一些作業 ...]

> /exit
```

### 恢復最近的工作階段

```bash
# 從上次中斷處繼續
copilot --continue
```

### 恢復特定工作階段

```bash
# 互動式選擇要恢復的工作階段
copilot --resume

# 或用 ID 恢復特定工作階段
copilot --resume abc123
```

> 💡 **如何找到工作階段 ID？** 你不需要記住它們。執行 `copilot --resume` 不帶 ID 會顯示互動式清單，列出所有先前的工作階段、名稱、ID 及最後活動時間，直接選擇即可。
>
> **多個終端機怎麼辦？** 每個終端機視窗都是獨立的工作階段，有自己的情境。如果你同時開三個 Copilot CLI，就是三個不同的工作階段。從任一終端機執行 `--resume` 都能瀏覽全部。`--continue` 會自動接續最近結束的那個，不論在哪個終端機。
>
> **可以不中斷就切換工作階段嗎？** 可以。在現有工作階段內用 `/resume` 指令：
> ```
> > /resume
> # 顯示可切換的工作階段清單
> ```

### 組織你的工作階段

給工作階段有意義的名稱，方便日後查找：

```bash
copilot

> /rename book-app-review
# 工作階段已重新命名，方便辨識
```

### 檢查與管理情境

隨著你加入檔案與對話，Copilot CLI 的 [情境窗口](../GLOSSARY.md#context-window) 會逐漸填滿。有多個指令可協助你掌控：

```bash
copilot

> /context
Context usage: 62k/200k tokens (31%)

> /clear
# 放棄目前工作階段（不儲存歷史），開始全新對話

> /new
# 結束目前工作階段（會存入歷史以供搜尋/恢復），開始全新對話

> /rewind
# 開啟時間軸選擇器，可回溯到對話中的較早時間點
```

> 💡 **何時用 `/clear` 或 `/new`**：如果你剛審查完 books.py，想改討論 utils.py，請先執行 /new（或若不需保留歷史則用 /clear）。否則舊主題的情境可能會干擾新回應。

> 💡 **操作失誤或想嘗試不同路線？** 用 `/rewind`（或連按兩下 Esc）開啟**時間軸選擇器**，可回到對話中任一較早時間點，而不只最近一次。這在走錯路想回頭時很實用，無需全部重來。

---

### 從中斷處繼續

<img src="images/session-persistence-timeline.png" alt="Timeline showing how GitHub Copilot CLI sessions persist across days - start on Monday, resume on Wednesday with full context restored" width="800"/>

*結束時自動儲存。幾天後恢復，完整情境（檔案、議題、進度）全都記得。*

想像這樣的多天工作流程：

```bash
# 週一：開始書籍應用程式審查
copilot

> /rename book-app-review
> @samples/book-app-project/books.py
> Review and number all code quality issues

Quality Issues Found:
1. Duplicate display functions (book_app.py & utils.py) - MEDIUM
2. No input validation for empty strings - MEDIUM
3. Year can be 0 or negative - LOW
4. No type hints on all functions - LOW
5. Missing error logging - LOW

> Fix issue #1 (duplicate functions)
# 著手修正...

> /exit
```

```bash
# 週三：精確從上次中斷處繼續
copilot --continue

> What issues remain unfixed from our book app review?

Remaining issues from our book-app-review session:
2. No input validation for empty strings - MEDIUM
3. Year can be 0 or negative - LOW
4. No type hints on all functions - LOW
5. Missing error logging - LOW

Issue #1 (duplicate functions) was fixed on Monday.

> Let's tackle issue #2 next
```

**這有多強大**：幾天後，Copilot CLI 仍記得：
- 你當時正在處理的檔案
- 已編號的議題清單
- 哪些已經處理過
- 對話的完整情境

無需重新解釋、無需重讀檔案，直接繼續工作。

---

**🎉 你已掌握所有必備技巧！** `@` 語法、工作階段管理（`--continue`/`--resume`/`/rename`）、情境指令（`/context`/`/clear`）已足夠讓你高效工作。以下內容為進階選讀，隨時回來參考。

---

# 進階選讀：深入探索

<img src="images/optional-going-deeper.png" alt="Abstract crystal cave in blue and purple tones representing deeper exploration of context concepts" width="800"/>

以下主題建立在上述基礎之上。**挑你有興趣的看，或直接跳到 [練習](#practice)。**

| 我想學... | 跳至 |
|---|---|
| 萬用字元模式與進階工作階段指令 | [進階 @ 模式與工作階段指令](#additional-patterns) |
| 多輪提示下的情境延續 | [情境感知對話](#context-aware-conversations) |
| Token 限制與 `/compact` | [理解情境窗口](#understanding-context-windows) |
| 如何選擇要參照哪些檔案 | [選擇參照對象](#choosing-what-to-reference) |
| 分析截圖與設計稿 | [圖片應用](#working-with-images) |

<details>
<summary><strong>進階 @ 模式與工作階段指令</strong></summary>
<a id="additional-patterns"></a>

### 進階 @ 模式

對進階用戶，Copilot CLI 支援萬用字元模式與圖片參照：

| 模式 | 功能說明 |
|---------|--------------|
| `@folder/*.py` | 目錄下所有 .py 檔案 |
| `@**/test_*.py` | 遞迴萬用字元：尋找所有測試檔 |
| `@image.png` | 供 UI 審查的圖片檔案 |

```bash
copilot

> Find all TODO comments in @samples/book-app-project/**/*.py
```

### 檢視工作階段資訊

```bash
copilot

> /session
# 顯示目前工作階段細節與工作區摘要

> /usage
# 顯示工作階段使用量與統計
```

### 分享你的工作階段

```bash
copilot

> /share file ./my-session.md
# 匯出工作階段為 markdown 檔案

> /share gist
# 建立 GitHub gist 分享工作階段

> /share html
# 匯出為互動式 HTML 檔案
# 適合與同事分享報告或存檔參考
```

</details>

<details>
<summary><strong>情境感知對話</strong></summary>
<a id="context-aware-conversations"></a>

### 情境感知對話

魔法發生在你有多輪對話、每次都建立在前一次基礎上時。

#### 範例：漸進式增強

```bash
copilot

> @samples/book-app-project/books.py Review the BookCollection class

Copilot CLI: "The class looks functional, but I notice:
1. Missing type hints on some methods
2. No validation for empty title/author
3. Could benefit from better error handling"

> Add type hints to all methods

Copilot CLI: "Here's the class with complete type hints..."
[Shows typed version]

> Now improve error handling

Copilot CLI: "Building on the typed version, here's improved error handling..."
[Adds validation and proper exceptions]

> Generate tests for this final version

Copilot CLI: "Based on the class with types and error handling..."
[Generates comprehensive tests]
```

注意每個提示都建立在前一次成果之上。這就是情境的威力。

</details>

<details>
<summary><strong>理解情境窗口</strong></summary>
<a id="understanding-context-windows"></a>

### 理解情境窗口

你已從基礎學會 `/context` 與 `/clear`。這裡更深入說明情境窗口的運作。

每個 AI 都有一個「情境窗口」，即一次能考慮的文字量。

<img src="images/context-window-visualization.png" alt="Context Window Visualization" width="800"/>

*情境窗口就像一張桌子：一次只能放有限的東西。檔案、對話紀錄、系統提示都會佔空間。*

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

當情境快滿但又不想丟失對話時，`/compact` 會將歷史摘要，釋放 token 空間：

```bash
copilot

> /compact
# 摘要對話歷史，釋放情境空間
# 你的重點發現與決策會被保留
```

#### 情境效率小技巧

| 情境 | 行動 | 原因 |
|-----------|--------|-----|
| 開新主題 | `/clear` | 移除無關情境 |
| 走錯路 | `/rewind` | 回到任一較早時間點 |
| 對話很長 | `/compact` | 摘要歷史，釋放 token |
| 只需特定檔案 | `@file.py` 而非 `@folder/` | 只載入所需內容 |
| 達到上限 | `/new` 或 `/clear` | 全新情境 |
| 多主題 | 每主題用 `/rename` | 易於恢復正確工作階段 |

#### 大型程式碼庫最佳實踐

1. **具體明確**：用 `@samples/book-app-project/books.py` 取代 `@samples/book-app-project/`
2. **主題切換時清除情境**：切換焦點時用 `/new` 或 `/clear`
3. **善用 `/compact`**：摘要對話釋放情境
4. **多開工作階段**：每個功能或主題一個 session

</details>

<details>
<summary><strong>選擇參照對象</strong></summary>
<a id="choosing-what-to-reference"></a>

### 選擇參照對象

不是所有檔案都同等重要。以下是明智選擇的方法：

#### 檔案大小考量

| 檔案大小 | 約略 [Token 數](../GLOSSARY.md#token) | 策略 |
|-----------|-------------------|----------|
| 小（<100 行） | ~500-1,500 tokens | 可自由參照 |
| 中（100-500 行） | ~1,500-7,500 tokens | 參照特定檔案 |
| 大（500+ 行） | 7,500+ tokens | 謹慎選擇，精確參照 |
| 非常大（1000+ 行） | 15,000+ tokens | 考慮拆分或只針對區段 |

**具體例子：**
- 書籍 app 的 4 個 Python 檔合計 ≈ 2,000-3,000 tokens
- 一般 Python 模組（200 行）≈ 3,000 tokens
- Flask API 檔案（400 行）≈ 6,000 tokens
- 你的 package.json ≈ 200-500 tokens
- 短提示＋回應 ≈ 500-1,500 tokens

> 💡 **程式碼快速估算**：行數 × 15 ≈ token 數。僅供參考。

#### 包含與排除的選擇

**高價值**（建議包含）：
- 進入點（`book_app.py`、`main.py`、`app.py`）
- 你要詢問的特定檔案
- 目標檔案直接 import 的檔案
- 設定檔（`requirements.txt`、`pyproject.toml`）
- 資料模型或 dataclass

**低價值**（可考慮排除）：
- 產生的檔案（編譯輸出、打包資源）
- node_modules 或 vendor 目錄
- 大型資料檔或 fixture
- 與問題無關的檔案

#### 精確度光譜

```
較不精確 ────────────────────────► 較精確
@samples/book-app-project/                      @samples/book-app-project/books.py:47-52
     │                                       │
     └─ 掃描全部（佔較多情境）                └─ 只載入所需（節省情境）
```

**何時用廣泛參照**（`@samples/book-app-project/`）：
- 初次探索程式碼庫
- 尋找跨多檔案的模式
- 架構審查

**何時用精確參照**（`@samples/book-app-project/books.py`）：
- 偵錯特定問題
- 審查單一檔案
- 詢問單一函式

#### 實務範例：分階段載入情境

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
<summary><strong>圖片應用</strong></summary>
<a id="working-with-images"></a>

### 圖片應用

你可以用 `@` 語法在對話中加入圖片，或直接**從剪貼簿貼上**（Cmd+V / Ctrl+V）。Copilot CLI 能分析截圖、設計稿、流程圖，協助 UI 除錯、設計實作與錯誤分析。

```bash
copilot

> @images/screenshot.png What is happening in this image?

> @images/mockup.png Write the HTML and CSS to match this design. Place it in a new file called index.html and put the CSS in styles.css.
```

> 📖 **深入了解**：請參見 [進階情境功能](../appendices/additional-context.md#working-with-images)，了解支援格式、實用案例與圖片結合程式碼的技巧。

</details>

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

是時候實際應用你的情境與工作階段管理技巧了。

---

## ▶️ 自己動手試試

### 全專案審查

本課程已附範例檔案可直接審查。啟動 copilot 並執行下列提示：

```bash
copilot

> @samples/book-app-project/ Give me a code quality review of this project

# Copilot CLI 會找出像是：
# - 重複的顯示函式
# - 缺乏輸入驗證
# - 不一致的錯誤處理
```

> 💡 **想用自己的檔案試試？** 建立一個小型 Python 專案（`mkdir -p my-project/src`），新增一些 .py 檔，然後用 `@my-project/src/` 來審查。你也可以請 copilot 幫你產生範例程式碼！

### 工作階段流程

```bash
copilot

> /rename book-app-review
> @samples/book-app-project/books.py Let's add input validation for empty titles

[Copilot CLI 建議驗證方式]

> Implement that fix
> Now consolidate the duplicate display functions in @samples/book-app-project/
> /exit

# 之後 - 從中斷處繼續
copilot --continue

> Generate tests for the changes we made
```

---

完成範例後，請嘗試以下變化：

1. **跨檔案挑戰**：分析 book_app.py 與 books.py 如何協作：
   ```bash
   copilot
   > @samples/book-app-project/book_app.py @samples/book-app-project/books.py
   > What's the relationship between these files? Are there any code smells?
   ```

2. **工作階段挑戰**：啟動 session，使用 `/rename my-first-session` 命名，做些事後用 `/exit` 離開，再執行 `copilot --continue`。它還記得你在做什麼嗎？

3. **情境挑戰**：在 session 進行中執行 `/context`。你用了多少 token？試試 `/compact` 再看一次。（更多 `/compact` 用法見進階 [理解情境窗口](#understanding-context-windows)。）

**自我檢查**：當你能解釋為什麼 `@folder/` 比逐一開檔案強大時，就代表你已理解情境。

---

## 📝 作業

### 主要挑戰：追蹤資料流

前面的實作範例聚焦於程式碼品質審查與輸入驗證。現在請用同樣的情境技巧，練習追蹤資料如何在應用程式中流動：1. 啟動互動式工作階段：`copilot`
2. 同時引用 `books.py` 和 `book_app.py`：
   `@samples/book-app-project/books.py @samples/book-app-project/book_app.py Trace how a book goes from user input to being saved in data.json. What functions are involved at each step?`
3. 加入資料檔案以提供更多情境：
   `@samples/book-app-project/data.json What happens if this JSON file is missing or corrupted? Which functions would fail?`
4. 跨檔案提出改進建議：
   `@samples/book-app-project/books.py @samples/book-app-project/utils.py Suggest a consistent error-handling strategy that works across both files.`
5. 重新命名工作階段：`/rename data-flow-analysis`
6. 使用 `/exit` 離開，然後用 `copilot --continue` 恢復並詢問有關資料流程的後續問題

**成功標準**：你能夠追蹤資料在多個檔案間的流動、恢復命名工作階段，並獲得跨檔案建議。

<details>
<summary>💡 提示（點擊展開）</summary>

**開始操作：**
```bash
cd /path/to/copilot-cli-for-beginners
copilot
> @samples/book-app-project/books.py @samples/book-app-project/book_app.py Trace how a book goes from user input to being saved in data.json.
> @samples/book-app-project/data.json What happens if this file is missing or corrupted?
> /rename data-flow-analysis
> /exit
```

然後用：`copilot --continue` 恢復

**常用指令：**
- `@file.py` - 引用單一檔案
- `@folder/` - 引用資料夾內所有檔案（注意結尾的 `/`）
- `/context` - 檢查你使用了多少情境
- `/rename <name>` - 為工作階段命名，方便日後恢復

</details>

### 加分挑戰：情境限制

1. 使用 `@samples/book-app-project/` 一次引用所有書籍應用程式檔案
2. 對不同檔案（`books.py`、`utils.py`、`book_app.py`、`data.json`）提出多個詳細問題
3. 執行 `/context` 查看使用情況。情境多快就被填滿？
4. 練習使用 `/compact` 回收空間，然後繼續對話
5. 嘗試更精確地引用檔案（例如：`@samples/book-app-project/books.py` 而不是整個資料夾），觀察情境使用的變化

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生情況 | 修正方式 |
|------|----------|----------|
| 忘記在檔名前加上 `@` | Copilot CLI 將 "books.py" 視為純文字 | 使用 `@samples/book-app-project/books.py` 引用檔案 |
| 預期工作階段會自動保存 | 重新啟動 `copilot` 會失去所有先前情境 | 使用 `--continue`（上次工作階段）或 `--resume`（選擇工作階段） |
| 引用目前目錄外的檔案 | 出現 "Permission denied" 或 "File not found" 錯誤 | 使用 `/add-dir /path/to/directory` 授權存取 |
| 更換主題時未使用 `/clear` | 舊情境會混淆新主題的回應 | 在開始不同任務前執行 `/clear` |

### 疑難排解

**"File not found" 錯誤** - 請確認你在正確目錄：

```bash
pwd  # 檢查目前目錄
ls   # 列出檔案

# 然後啟動 copilot 並使用相對路徑
copilot

> Review @samples/book-app-project/books.py
```

**"Permission denied"** - 將目錄加入允許清單：

```bash
copilot --add-dir /path/to/directory

# 或在工作階段中：
> /add-dir /path/to/directory
```

**情境填滿太快**：
- 更精確地引用檔案
- 在不同主題間使用 `/clear`
- 將工作分散到多個工作階段

</details>

---

# 摘要

## 🔑 重點整理

1. **`@` 語法**讓 Copilot CLI 知道檔案、資料夾和圖片的情境
2. **多輪對話**會隨情境累積而互相延續
3. **工作階段自動保存**：用 `--continue` 或 `--resume` 接續未完成的進度
4. **情境窗口有限**：用 `/clear`、`/compact`、`/context`、`/new` 和 `/rewind` 管理
5. **權限旗標**（`--add-dir`、`--allow-all`）控制多目錄存取。請謹慎使用！
6. **圖片引用**（`@screenshot.png`）可視覺化協助 UI 除錯

> 📚 **官方文件**：[使用 Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli) 取得完整的情境、工作階段與檔案操作參考。

> 📋 **快速參考**：請參閱 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference) 取得完整指令與捷徑清單。

---

## ➡️ 下一步

現在你已經能夠為 Copilot CLI 提供情境，接下來就能在實際開發任務中發揮作用。你剛學到的情境技巧（檔案引用、跨檔案分析、工作階段管理）正是下一章強大工作流程的基礎。

在 **[第 03 章：開發工作流程](../03-development-workflows/README.md)**，你將學到：

- 程式碼審查工作流程
- 重構模式
- 除錯協助
- 測試產生
- Git 整合

---

**[← 回到第 01 章](../01-setup-and-first-steps/README.md)** | **[繼續前往第 03 章 →](../03-development-workflows/README.md)**
