![Chapter 02: Context and Conversations](images/chapter-header.png)

> **如果 AI 能看見你整個程式碼庫，而不只是一次一個檔案，會怎樣？**

在本章中，你將解鎖 GitHub Copilot CLI 的真正威力：情境。你會學會使用 `@` 語法來參照檔案和目錄，讓 Copilot CLI 能深入理解你的程式碼庫。你會學到如何在多個工作階段中維持對話、在數天後精確地從上次中斷處繼續工作，並見識跨檔案分析如何發現單檔審查完全忽略的錯誤。

## 🎯 學習目標

完成本章後，你將能夠：

- 使用 `@` 語法參照檔案、目錄和圖片
- 使用 `--resume` 和 `--continue` 恢復先前的工作階段
- 了解 [情境窗口](../GLOSSARY.md#context-window) 的運作方式
- 撰寫有效的多輪對話
- 管理多專案工作流程的目錄權限

> ⏱️ **預估時間**：約 50 分鐘（20 分鐘閱讀 + 30 分鐘實作）

---

## 🧩 真實世界類比：和同事協作

<img src="images/colleague-context-analogy.png" alt="Context Makes the Difference - Without vs With Context" width="800"/>

*就像你的同事一樣，Copilot CLI 不是讀心術專家。提供更多資訊能幫助人類和 Copilot 都給出更精準的協助！*

想像你要向同事解釋一個錯誤：

> **沒有情境**：「書籍應用程式壞掉了。」

> **有情境**：「請看 `books.py`，特別是 `find_book_by_title` 函式。它沒有做不分大小寫比對。」

要為 Copilot CLI 提供情境，請使用 *`@` 語法* 指定特定檔案。

---

# 必備：基本情境

<img src="images/essential-basic-context.png" alt="Glowing code blocks connected by light trails representing how context flows through Copilot CLI conversations" width="800"/>

本節涵蓋你有效運用情境所需的一切。請先掌握這些基本功。

---

## @ 語法

`@` 符號用於在提示詞中參照檔案和目錄。這就是你告訴 Copilot CLI「請看這個檔案」的方式。

> 💡 **注意**：本課程所有範例皆使用此儲存庫內的 `samples/` 資料夾，你可以直接嘗試每個指令。

### 立即試試（無需設定）

你可以用電腦上的任何檔案來嘗試：

```bash
copilot

# 指定你有的任意檔案
> Explain what @package.json does
> Summarize @README.md
> What's in @.gitignore and why?
```

> 💡 **手邊沒有專案？** 快速建立一個測試檔案：
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
<summary>🎬 實際操作示範！</summary>

![File Context Demo](images/file-context-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

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

這就是情境成為超能力的地方。單檔分析很有用，跨檔案分析則能帶來質變。

<img src="images/cross-file-intelligence.png" alt="Cross-File Intelligence - comparing single-file vs cross-file analysis showing how analyzing files together reveals bugs, data flow, and patterns invisible in isolation" width="800"/>

### 示範：找出跨檔案錯誤

```bash
copilot

> @samples/book-app-project/book_app.py @samples/book-app-project/books.py
>
> How do these files work together? What's the data flow?
```

> 💡 **進階選項**：想做安全性導向的跨檔案分析，請嘗試 Python 安全範例：
> ```bash
> > @samples/buggy-code/python/user_service.py @samples/buggy-code/python/payment_processor.py
> > Find security vulnerabilities that span BOTH files
> ```

---

<details>
<summary>🎬 實際操作示範！</summary>

![Multi-File Demo](images/multi-file-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

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

**為什麼這很重要**：單檔審查會忽略大局。只有跨檔案分析才能發現：
- **重複程式碼** 應該整合
- **資料流模式** 顯示元件如何互動
- **架構問題** 影響可維護性

---

### 示範：60 秒快速理解程式碼庫

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

**結果**：原本要花一小時閱讀程式碼，現在 10 秒壓縮完成。你能立刻知道重點在哪。

---

## 實用範例

### 範例 1：有情境的程式碼審查

```bash
copilot

> @samples/book-app-project/books.py Review this file for potential bugs

# Copilot CLI 現在擁有完整檔案內容，能給出具體回饋：
# "Line 49: Case-sensitive comparison may miss books..."
# "Line 29: JSON decode errors are caught but data corruption isn't logged..."

> What about @samples/book-app-project/book_app.py?

# 現在審查 book_app.py，但仍保有 books.py 的情境
```

### 範例 2：理解程式碼庫

```bash
copilot

> @samples/book-app-project/books.py What does this module do?

# Copilot CLI 讀取 books.py 並理解 BookCollection 類別

> @samples/book-app-project/ Give me an overview of the code structure

# Copilot CLI 掃描目錄並摘要

> How does the app save and load books?

# Copilot CLI 能追蹤已讀取過的程式碼
```

<details>
<summary>🎬 多輪對話示範！</summary>

![Multi-Turn Demo](images/multi-turn-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

### 範例 3：多檔案重構

```bash
copilot

> @samples/book-app-project/book_app.py @samples/book-app-project/utils.py
> I see duplicate display functions: show_books() and print_books(). Help me consolidate these.

# Copilot CLI 同時看到兩個檔案，能建議如何合併重複程式碼
```

---

## 工作階段管理

工作階段會自動儲存。你可以隨時恢復先前的工作階段，從中斷處繼續。

### 工作階段自動儲存

每次對話都會自動儲存。只需正常結束即可：

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
# 互動式選擇工作階段
copilot --resume

# 或用 ID 恢復特定工作階段
copilot --resume=abc123

# 或用你命名的名稱恢復
copilot --resume="my book app review"
```

> 💡 **如何找到工作階段 ID？** 你不需要記住它們。執行 `copilot --resume`（不帶 ID）會顯示互動式清單，列出所有先前的工作階段、名稱、ID 及最後活動時間。直接選擇你要的即可。
>
> **多個終端機怎麼辦？** 每個終端機視窗都是獨立的工作階段，擁有自己的情境。如果你在三個終端機開啟 Copilot CLI，就是三個獨立的工作階段。從任一終端機執行 `--resume` 可瀏覽全部。`--continue` 旗標會優先選取目前工作目錄的工作階段，若無則選最近活動的。
>
> **可以不重啟就切換工作階段嗎？** 可以。在活動中的工作階段內使用 `/resume` 指令：
> ```
> > /resume
> # 顯示可切換的工作階段清單
> ```

### 組織你的工作階段

給工作階段有意義的名稱，方便日後查找。你可以在啟動時命名，或在工作階段中隨時重新命名：

```bash
# 啟動時直接命名
copilot --name book-app-review

# 或在工作階段內重新命名
copilot

> /rename book-app-review
# 工作階段已重新命名，方便辨識
```

命名後，你可以直接用名稱恢復，不必瀏覽清單：

```bash
copilot --resume=book-app-review
```

要清理不需要的工作階段，可在工作階段內用 `/session delete`：

```bash
copilot

> /session delete            # 刪除目前工作階段
> /session delete abc123     # 依 ID 刪除特定工作階段
> /session delete-all        # 刪除所有工作階段（請小心使用！）
```

### 跨工作階段的持久記憶

工作階段會儲存你的對話紀錄，但 **記憶** 更進一步，讓 Copilot CLI 能跨所有工作階段記住偏好和事實，而不只限於單一工作階段。

```bash
copilot

> /memory show
# 顯示 Copilot CLI 目前記得哪些你和專案的資訊

> /memory on
# 啟用記憶功能（若帳號支援則預設開啟）

> /memory off
# 關閉記憶功能（若你希望每次都是全新開始）
```

例如，你告訴 Copilot CLI「我偏好用 pytest 做 Python 測試」，它就能記住這個偏好，未來自動套用。你無需重複說明。

> 💡 **記憶 vs. 工作階段**：工作階段儲存對話紀錄，方便你恢復特定任務。記憶則儲存可重複使用的儲存庫事實和使用者偏好，Copilot 可在未來自動應用。把工作階段想成任務筆記本，記憶則是 Copilot 可延續的共用情境。

### 檢查與管理情境

隨著你加入檔案和對話，Copilot CLI 的 [情境窗口](../GLOSSARY.md#context-window) 會逐漸填滿。有多個指令可協助你掌控：

```bash
copilot

> /context
Context usage: 62k/200k tokens (31%)

> /clear
# 放棄目前工作階段（不儲存歷史），開始全新對話

> /new
# 結束目前工作階段（儲存到歷史以供搜尋/恢復），開始新對話

> /rewind
# 開啟時間軸選擇器，可回溯到對話中的較早時間點
```

> 💡 **何時用 `/clear` 或 `/new`**：如果你剛審查完 books.py，想改討論 utils.py，請先執行 /new（或 /clear 若不需保留歷史）。否則舊主題的情境可能讓回應混亂。

> 💡 **犯錯或想換個方式？** 用 `/rewind`（或連按兩下 Esc）開啟**時間軸選擇器**，可回到對話中任意較早的時間點，不只最近一次。這很適合走錯路想回頭，卻不想全部重來時使用。

---

### 從中斷處繼續

<img src="images/session-persistence-timeline.png" alt="Timeline showing how GitHub Copilot CLI sessions persist across days - start on Monday, resume on Wednesday with full context restored" width="800"/>

*結束時自動儲存工作階段。數天後恢復，情境完整：檔案、議題、進度全都記得。*

想像這樣的多天工作流程：

```bash
# 週一：一開始就用名稱啟動書籍應用程式審查
copilot --name book-app-review

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
# 週三：用名稱精確恢復進度
copilot --resume=book-app-review

> What issues remain unfixed from our book app review?

Remaining issues from our book-app-review session:
2. No input validation for empty strings - MEDIUM
3. Year can be 0 or negative - LOW
4. No type hints on all functions - LOW
5. Missing error logging - LOW

Issue #1 (duplicate functions) was fixed on Monday.

> Let's tackle issue #2 next
```

**這有多強大**：數天後，Copilot CLI 仍記得：
- 你當時正在處理的檔案
- 編號的議題清單
- 哪些已經解決
- 你的對話情境

無需重複解釋，無需重讀檔案，只管繼續工作。

---

**🎉 你已掌握所有必備技巧！** `@` 語法、工作階段管理（`--name`/`--continue`/`--resume`/`/rename`）、情境指令（`/context`/`/clear`）已足夠讓你高效工作。以下內容為進階選讀，準備好再回來即可。

---

# 進階選讀：更深入探索

<img src="images/optional-going-deeper.png" alt="Abstract crystal cave in blue and purple tones representing deeper exploration of context concepts" width="800"/>

這些主題建立在上面必備技巧之上。**挑你有興趣的看，或直接跳到[練習](#practice)。**

| 我想學... | 跳到 |
|---|---|
| 萬用字元模式與進階工作階段指令 | [進階 @ 模式與工作階段指令](#additional-patterns) |
| 多輪提示如何累積情境 | [情境感知對話](#context-aware-conversations) |
| Token 限制與 `/compact` | [理解情境窗口](#understanding-context-windows) |
| 如何挑選要參照哪些檔案 | [選擇參照對象](#choosing-what-to-reference) |
| 分析截圖與設計稿 | [處理圖片](#working-with-images) |

<details>
<summary><strong>進階 @ 模式與工作階段指令</strong></summary>
<a id="additional-patterns"></a>

### 進階 @ 模式

進階用戶可使用萬用字元模式與圖片參照：

| 模式 | 功能說明 |
|---------|--------------|
| `@folder/*.py` | 目錄下所有 .py 檔案 |
| `@**/test_*.py` | 遞迴萬用字元：找出所有 test 檔案 |
| `@image.png` | 圖片檔案，用於 UI 審查 |

```bash
copilot

> Find all TODO comments in @samples/book-app-project/**/*.py
```

### 檢視工作階段資訊

```bash
copilot

> /session
# 顯示目前工作階段詳情與工作區摘要

> /usage
# 顯示工作階段指標與統計
```

### 分享你的工作階段

```bash
copilot

> /share file ./my-session.md
# 將工作階段匯出為 markdown 檔案

> /share gist
# 建立 GitHub gist，內容為此工作階段

> /share html
# 匯出為獨立互動式 HTML 檔案
# 適合與同事分享精美報告或存檔參考
```

</details>

<details>
<summary><strong>情境感知對話</strong></summary>
<a id="context-aware-conversations"></a>

### 情境感知對話

魔法發生在你進行多輪、彼此累積的對話時。

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

注意每個提示都建立在前一輪的成果上。這就是情境的威力。

</details>

<details>
<summary><strong>理解情境窗口</strong></summary>
<a id="understanding-context-windows"></a>

### 理解情境窗口

你已從必備技巧學過 `/context` 和 `/clear`。這裡更深入說明情境窗口如何運作。

每個 AI 都有一個「情境窗口」，即一次能考慮的文字量。

<img src="images/context-window-visualization.png" alt="Context Window Visualization" width="800"/>

*情境窗口就像一張桌子：一次只能放這麼多東西。檔案、對話紀錄、系統提示都會佔空間。*

#### 達到上限時會發生什麼

```bash
copilot

> /context

Context usage: 45,000 / 128,000 tokens (35%)

# 加入更多檔案和對話，這個數字會增加

> @large-codebase/

Context usage: 120,000 / 128,000 tokens (94%)

# 警告：接近情境上限

> @another-large-file.py

Context limit reached. Older context will be summarized.
```

#### `/compact` 指令

當情境快滿但你不想失去對話內容時，`/compact` 會摘要你的歷史，釋放 token 空間：

```bash
copilot

> /compact
# 摘要對話歷史，釋放情境空間
# 你的重點發現與決策會被保留
```

你也可以給 `/compact` 加上聚焦指示，讓摘要時優先保留重點：

```bash
copilot

> /compact focus on the list of bugs we found and decisions made
# 摘要歷史，保留 bug 清單與決策重點
```

> 💡 **何時用聚焦指示**：如果對話涵蓋多主題，聚焦指示可讓 `/compact` 優先保留對你下一步最重要的部分，避免斷線。

#### 情境效率小技巧

| 情境 | 行動 | 原因 |
|-----------|--------|-----|
| 開新主題 | `/clear` | 移除無關情境 |
| 走錯路 | `/rewind` | 回到任意較早時間點 |
| 對話很長 | `/compact` | 摘要歷史，釋放 token |
| 只需特定檔案 | `@file.py` 非 `@folder/` | 只載入所需內容 |
| 達到上限 | `/new` 或 `/clear` | 全新情境 |
| 多主題 | 每主題用 `/rename` | 易於恢復正確工作階段 |

#### 大型程式碼庫最佳實踐

1. **具體指定**：用 `@samples/book-app-project/books.py` 取代 `@samples/book-app-project/`
2. **主題切換時清空情境**：切換焦點時用 `/new` 或 `/clear`
3. **善用 `/compact`**：摘要對話釋放情境空間
4. **多工作階段並行**：每個功能或主題用一個工作階段

</details>

<details>
<summary><strong>選擇參照對象</strong></summary>
<a id="choosing-what-to-reference"></a>

### 選擇參照對象

不是所有檔案都同等重要。以下是明智選擇的方式：

#### 檔案大小考量

| 檔案大小 | 約略 [Token 數](../GLOSSARY.md#token) | 策略 |
|-----------|-------------------|----------|
| 小（<100 行） | ~500-1,500 tokens | 可自由參照 |
| 中（100-500 行） | ~1,500-7,500 tokens | 參照特定檔案 |
| 大（500+ 行） | 7,500+ tokens | 謹慎選擇，聚焦特定檔案 |
| 超大（1000+ 行） | 15,000+ tokens | 考慮拆分或只針對區段 |

**具體例子：**
- 書籍應用程式的 4 個 Python 檔案合計約 2,000-3,000 tokens
- 典型 Python 模組（200 行）約 3,000 tokens
- Flask API 檔案（400 行）約 6,000 tokens
- 你的 package.json 約 200-500 tokens
- 短提示 + 回應約 500-1,500 tokens

> 💡 **快速估算程式碼 token 數**：行數乘以約 15，即為大致 token 數。僅供參考。

#### 包含與排除的取捨

**高價值**（應納入）：
- 進入點（`book_app.py`、`main.py`、`app.py`）
- 你要詢問的特定檔案
- 目標檔案直接 import 的檔案
- 設定檔（`requirements.txt`、`pyproject.toml`）
- 資料模型或 dataclass

**低價值**（可考慮排除）：
- 產生的檔案（編譯輸出、bundle 資產）
- node_modules 或 vendor 目錄
- 大型資料檔或測試資料
- 與問題無關的檔案

#### 具體程度光譜

```
較不具體 ────────────────────────► 較具體
@samples/book-app-project/                      @samples/book-app-project/books.py:47-52
     │                                       │
     └─ 掃描全部                            └─ 只載入所需
        （佔用較多情境）                       （節省情境空間）
```

**何時用廣泛參照**（`@samples/book-app-project/`）：
- 初次探索程式碼庫
- 尋找跨多檔案的模式
- 架構審查

**何時用精確參照**（`@samples/book-app-project/books.py`）：
- 偵錯特定問題
- 審查特定檔案
- 詢問單一函式

#### 實用範例：分階段載入情境

```bash
copilot

# 第 1 步：先看結構
> @package.json What frameworks does this project use?

# 第 2 步：根據答案縮小範圍
> @samples/book-app-project/ Show me the project structure

# 第 3 步：聚焦重點
> @samples/book-app-project/books.py Review the BookCollection class

# 第 4 步：只在需要時加入相關檔案
> @samples/book-app-project/book_app.py @samples/book-app-project/books.py How does the CLI use the BookCollection?
```

這種分階段方式能讓情境聚焦且高效。

</details>

<details>
<summary><strong>處理圖片</strong></summary>
<a id="working-with-images"></a>

### 處理圖片

你可以用 `@` 語法在對話中加入圖片，或直接**從剪貼簿貼上**（Cmd+V / Ctrl+V）。Copilot CLI 能分析截圖、設計稿和圖表，協助 UI 除錯、設計實作和錯誤分析。

```bash
copilot

> @images/screenshot.png What is happening in this image?

> @images/mockup.png Write the HTML and CSS to match this design. Place it in a new file called index.html and put the CSS in styles.css.
```

> 📖 **深入了解**：請參閱 [進階情境功能](../appendices/additional-context.md#working-with-images)，了解支援格式、實用案例及圖片與程式碼結合的技巧。

</details>

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

是時候實際應用你的情境與工作階段管理技能了。

---

## ▶️ 自己動手試試看

### 專案全面檢視

本課程附有範例檔案，你可以直接檢閱。啟動 copilot 並執行下列提示：

```bash
copilot

> @samples/book-app-project/ 給我這個專案的程式碼品質檢查

# Copilot CLI 會找出像是：
# - 重複的顯示函式
# - 缺少輸入驗證
# - 不一致的錯誤處理
```

> 💡 **想用自己的檔案試試看嗎？** 建立一個小型 Python 專案（`mkdir -p my-project/src`），加入一些 .py 檔案，然後用 `@my-project/src/` 來檢查它們。如果你想，也可以請 copilot 幫你產生範例程式碼！

### 工作階段流程

```bash
copilot

> /rename book-app-review
> @samples/book-app-project/books.py 我們來為空白標題加上輸入驗證

[Copilot CLI 建議驗證方法]

> 實作這個修正
> 現在整合 @samples/book-app-project/ 中重複的顯示函式
> /exit

# 稍後 - 從上次進度繼續
copilot --continue

> 針對我們做的變更產生測試
```

---

完成示範後，試試以下變化：

1. **跨檔案挑戰**：分析 book_app.py 和 books.py 如何協同運作：
   ```bash
   copilot
   > @samples/book-app-project/book_app.py @samples/book-app-project/books.py
   > 這兩個檔案有什麼關聯？有沒有任何程式碼異味？
   ```

2. **工作階段挑戰**：啟動一個工作階段，用 `/rename my-first-session` 命名，做些事情後用 `/exit` 離開，再用 `copilot --continue`。它還記得你在做什麼嗎？

3. **情境挑戰**：在工作階段中執行 `/context`。你用了多少 token？試試 `/compact` 再檢查一次。（更多 `/compact` 用法請見 Going Deeper 的 [理解情境窗口](#understanding-context-windows)）

**自我檢查**：當你能解釋為什麼 `@folder/` 比逐一開啟每個檔案更強大時，就代表你理解情境了。

---

## 📝 作業

### 主要挑戰：追蹤資料流

前面的實作範例著重於程式碼品質檢查與輸入驗證。現在請用相同的情境技巧，練習追蹤資料如何在應用程式中流動：

1. 啟動互動式工作階段：`copilot`
2. 同時參照 `books.py` 和 `book_app.py`：
   `@samples/book-app-project/books.py @samples/book-app-project/book_app.py 追蹤一本書如何從使用者輸入被儲存到 data.json。每個步驟會用到哪些函式？`
3. 加入資料檔案以獲得更多情境：
   `@samples/book-app-project/data.json 如果這個 JSON 檔案遺失或損毀會發生什麼事？哪些函式會失敗？`
4. 請求跨檔案的改進建議：
   `@samples/book-app-project/books.py @samples/book-app-project/utils.py 建議一個可在兩個檔案間一致運作的錯誤處理策略。`
5. 重新命名工作階段：`/rename data-flow-analysis`
6. 用 `/exit` 離開，然後用 `copilot --continue` 繼續，並針對資料流提出後續問題

**成功標準**：你能跨多個檔案追蹤資料、恢復已命名的工作階段，並獲得跨檔案建議。

<details>
<summary>💡 提示（點擊展開）</summary>

**開始練習：**
```bash
cd /path/to/copilot-cli-for-beginners
copilot
> @samples/book-app-project/books.py @samples/book-app-project/book_app.py 追蹤一本書如何從使用者輸入被儲存到 data.json。
> @samples/book-app-project/data.json 如果這個檔案遺失或損毀會發生什麼事？
> /rename data-flow-analysis
> /exit
```

然後用：`copilot --continue` 繼續

**實用指令：**
- `@file.py` - 參照單一檔案
- `@folder/` - 參照資料夾內所有檔案（注意結尾的 `/`）
- `/context` - 檢查你用了多少情境
- `/rename <name>` - 幫你的工作階段命名，方便之後繼續

</details>

### 進階挑戰：情境限制

1. 用 `@samples/book-app-project/` 一次參照所有書籍應用程式檔案
2. 針對不同檔案（`books.py`、`utils.py`、`book_app.py`、`data.json`）提出多個詳細問題
3. 執行 `/context` 檢查使用量。填滿得有多快？
4. 練習用 `/compact` 回收空間，然後繼續對話
5. 嘗試更精確地指定檔案（例如用 `@samples/book-app-project/books.py` 取代整個資料夾），觀察情境使用量的變化

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 會發生什麼事 | 修正方式 |
|------|--------------|----------|
| 忘記在檔名前加 `@` | Copilot CLI 會把 "books.py" 當成純文字 | 用 `@samples/book-app-project/books.py` 參照檔案 |
| 以為工作階段會自動保留 | 重新啟動 `copilot` 會遺失所有先前情境 | 用 `--continue`（上次工作階段）或 `--resume`（選擇一個工作階段） |
| 參照目前目錄外的檔案 | 出現 "Permission denied" 或 "File not found" 錯誤 | 用 `/add-dir /path/to/directory` 開放存取權限 |
| 換主題時沒用 `/clear` | 舊情境會混淆新主題的回應 | 換任務前先執行 `/clear` |

### 疑難排解

**"File not found" 錯誤** - 確認你在正確目錄下：

```bash
pwd  # 檢查目前目錄
ls   # 列出檔案

# 然後啟動 copilot 並用相對路徑
copilot

> Review @samples/book-app-project/books.py
```

**"Permission denied"** - 將目錄加入允許清單：

```bash
copilot --add-dir /path/to/directory

# 或在工作階段中：
> /add-dir /path/to/directory
```

**情境很快就滿了**：
- 更精確地指定檔案
- 不同主題間用 `/clear`
- 將工作分散到多個工作階段

</details>

---

# 小結

## 🔑 重點整理

1. **`@` 語法** 讓 Copilot CLI 取得檔案、資料夾與圖片的情境
2. **多輪對話** 會隨著情境累積而彼此關聯
3. **工作階段自動儲存**：啟動時用 `--name` 命名，之後用 `--resume=<name>` 恢復，或用 `--continue` 接續最近的工作階段
4. **情境窗口有限**：用 `/clear`、`/compact`、`/context`、`/new`、`/rewind` 管理。用 `/compact focus on <topic>` 決定摘要保留哪些內容
5. **持久記憶**（`/memory`）讓 Copilot CLI 能跨*所有*工作階段記住偏好與事實——不只限於當前工作階段
6. **權限旗標**（`--add-dir`、`--allow-all`）控制多目錄存取。請謹慎使用！
7. **圖片參照**（`@screenshot.png`）有助於視覺化除錯 UI 問題

> 📚 **官方文件**：[使用 Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli) 取得情境、工作階段與檔案操作的完整參考。

> 📋 **快速參考**：請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference) 取得所有指令與捷徑清單。

---

## ➡️ 接下來

現在你已經會給 Copilot CLI 提供情境，接下來就要把這些技巧用在實際開發任務上。你剛學到的情境技巧（檔案參照、跨檔案分析、工作階段管理）正是下一章強大工作流程的基礎。

在 **[第 03 章：開發工作流程](../03-development-workflows/README.md)**，你會學到：

- 程式碼審查流程
- 重構模式
- 除錯協助
- 測試產生
- Git 整合

---

**[← 回到第 01 章](../01-setup-and-first-steps/README.md)** | **[繼續前往第 03 章 →](../03-development-workflows/README.md)**
