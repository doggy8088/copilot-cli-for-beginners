![Chapter 02: Context and Conversations](images/chapter-header.png)

> **如果 AI 能看到你的整個程式碼庫，而不是一次只看一個檔案，會怎樣？**

本章將解鎖 GitHub Copilot CLI 的真正威力：上下文（Context）。你將學習使用 `@` 語法來參照檔案和目錄，讓 Copilot CLI 深入理解你的程式碼庫。你將發現如何跨工作階段維護對話、幾天後從中斷處繼續工作，並親眼看到跨檔案分析如何找出單一檔案審查完全看不到的 bug。

## 🎯 學習目標

完成本章後，你將能夠：

- 使用 `@` 語法參照檔案、目錄和圖片
- 以 `--resume` 和 `--continue` 繼續先前的工作階段
- 理解[上下文視窗](../GLOSSARY.md#context-window)的運作方式
- 撰寫有效的多輪對話
- 管理多專案工作流程的目錄權限

> ⏱️ **預估時間**：約 50 分鐘（閱讀 20 分鐘 + 實作 30 分鐘）

---

## 🧩 現實生活類比：與同事協作

<img src="images/colleague-context-analogy.png" alt="Context Makes the Difference - Without vs With Context" width="800"/>

*就像你的同事一樣，Copilot CLI 不會讀心術。提供更多資訊能幫助人類和 Copilot 提供更有針對性的協助！*

想像向同事說明一個 bug：

> **沒有上下文**：「書籍應用程式壞了。」

> **有上下文**：「看看 `books.py`，特別是 `find_book_by_title` 函式。它沒有做大小寫不敏感的比對。」

要向 Copilot CLI 提供上下文，請使用 *`@` 語法*將 Copilot CLI 指向特定檔案。

---

# 必學：基本上下文

<img src="images/essential-basic-context.png" alt="Glowing code blocks connected by light trails representing how context flows through Copilot CLI conversations" width="800"/>

本節涵蓋有效使用上下文所需的一切。請先掌握這些基礎。

---

## @ 語法

`@` 符號用於在提示中參照檔案和目錄，這是你告訴 Copilot CLI「看看這個檔案」的方式。

> 💡 **備註**：本課程所有範例都使用此儲存庫內附的 `samples/` 資料夾，讓你可以直接嘗試每個指令。

### 立即試試（不需任何設定）

你可以用電腦上的任何檔案嘗試：

```bash
copilot

# 指向你有的任何檔案
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

| 模式 | 功能 | 使用範例 |
|------|------|---------|
| `@file.py` | 參照單一檔案 | `Review @samples/book-app-project/books.py` |
| `@folder/` | 參照目錄中的所有檔案 | `Review @samples/book-app-project/` |
| `@file1.py @file2.py` | 參照多個檔案 | `Compare @samples/book-app-project/book_app.py @samples/book-app-project/books.py` |

### 參照單一檔案

```bash
copilot

> Explain what @samples/book-app-project/utils.py does
```

---

<details>
<summary>🎬 看看實際效果！</summary>

<img src="images/file-context-demo.gif" alt="File Context Demo">

<em>示範輸出僅供參考，你的模型、工具與回應內容可能與此不同。</em>

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

## 跨檔案智慧分析

這正是上下文成為超能力的地方。單一檔案分析很有用，跨檔案分析則是革命性的。

<img src="images/cross-file-intelligence.png" alt="Cross-File Intelligence - comparing single-file vs cross-file analysis showing how analyzing files together reveals bugs, data flow, and patterns invisible in isolation" width="800"/>

### 示範：找出橫跨多個檔案的 Bug

```bash
copilot

> @samples/book-app-project/book_app.py @samples/book-app-project/books.py
>
> How do these files work together? What's the data flow?
```

> 💡 **進階選項**：若想進行以安全性為重點的跨檔案分析，可以試試 Python 安全性範例：
> ```bash
> > @samples/buggy-code/python/user_service.py @samples/buggy-code/python/payment_processor.py
> > Find security vulnerabilities that span BOTH files
> ```

---

<details>
<summary>🎬 看看實際效果！</summary>

<img src="images/multi-file-demo.gif" alt="Multi-File Demo">

<em>示範輸出僅供參考，你的模型、工具與回應內容可能與此不同。</em>

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

**為何重要**：單一檔案審查會錯過全局。只有跨檔案分析才能揭示：
- **重複程式碼**，應當整合
- **資料流模式**，顯示元件之間如何互動
- **架構問題**，影響可維護性

---

### 示範：60 秒內理解一個程式碼庫

<img src="images/codebase-understanding.png" alt="Split-screen comparison showing manual code review taking 1 hour versus AI-assisted analysis taking 10 seconds" width="800" />

剛接觸新專案？用 Copilot CLI 快速了解它。

```bash
copilot

> @samples/book-app-project/
>
> In one paragraph, what does this app do and what are its biggest quality issues?
```

**你會得到的內容**：
```
This is a CLI book collection manager that lets users add, list, remove, and
search books stored in a JSON file. The biggest quality issues are:

1. Duplicate display logic - show_books() and print_books() do the same thing
2. Inconsistent error handling - some errors raise exceptions, others return False
3. No input validation - year can be 0, empty strings accepted for title/author
4. Missing tests - no test coverage for critical functions like find_book_by_title

Priority fix: Consolidate duplicate display functions and add input validation.
```

**結果**：原本需要一個小時閱讀程式碼的事，壓縮成 10 秒。你確切知道該把注意力放在哪裡。

---

## 實際應用範例

### 範例一：帶上下文的程式碼審查

```bash
copilot

> @samples/book-app-project/books.py Review this file for potential bugs

# Copilot CLI 現在擁有完整的檔案內容，可以給出具體回饋：
# "Line 49: Case-sensitive comparison may miss books..."
# "Line 29: JSON decode errors are caught but data corruption isn't logged..."

> What about @samples/book-app-project/book_app.py?

# 現在審查 book_app.py，但仍然知道 books.py 的上下文
```

### 範例二：理解程式碼庫

```bash
copilot

> @samples/book-app-project/books.py What does this module do?

# Copilot CLI 讀取 books.py 並理解 BookCollection 類別

> @samples/book-app-project/ Give me an overview of the code structure

# Copilot CLI 掃描目錄並進行摘要

> How does the app save and load books?

# Copilot CLI 可以追蹤它已看過的程式碼
```

<details>
<summary>🎬 看看多輪對話的實際效果！</summary>

<img src="images/multi-turn-demo.gif" alt="Multi-Turn Demo">

<em>示範輸出僅供參考，你的模型、工具與回應內容可能與此不同。</em>

</details>

### 範例三：多檔案重構

```bash
copilot

> @samples/book-app-project/book_app.py @samples/book-app-project/utils.py
> I see duplicate display functions: show_books() and print_books(). Help me consolidate these.

# Copilot CLI 看到兩個檔案，可以建議如何合併重複的程式碼
```

---

## 工作階段管理

工作階段會在你工作時自動儲存，你可以繼續先前的工作階段從中斷處接著做。

### 工作階段自動儲存

每次對話都會自動儲存，只需正常離開：

```bash
copilot

> @samples/book-app-project/ Let's improve error handling across all modules

[... 進行一些工作 ...]

> /exit
```

### 繼續最近的工作階段

```bash
# 從上次中斷的地方繼續
copilot --continue
```

### 繼續特定工作階段

```bash
# 從清單中互動式選擇工作階段
copilot --resume

# 或依 ID 繼續特定工作階段
copilot --resume abc123
```

### 整理你的工作階段

為工作階段取有意義的名稱，以便日後找到：

```bash
copilot

> /rename book-app-review
# 工作階段已重新命名，方便識別
```

### 檢視和管理上下文

隨著你新增檔案和對話，Copilot CLI 的[上下文視窗](../GLOSSARY.md#context-window)會逐漸填滿。以下兩個指令可以幫助你掌控狀況：

```bash
copilot

> /context
Context usage: 45,000 / 128,000 tokens (35%)

> /clear
# 清除上下文並重新開始。切換話題時使用
```

> 💡 **何時使用 `/clear`**：若你一直在審查 `books.py`，想要切換去討論 `utils.py`，請先執行 `/clear`。否則舊話題的過時上下文可能會干擾新話題的回應。

---

### 從上次中斷的地方繼續

<img src="images/session-persistence-timeline.png" alt="Timeline showing how GitHub Copilot CLI sessions persist across days - start on Monday, resume on Wednesday with full context restored" width="800"/>

*工作階段在離開時自動儲存。幾天後繼續，完整上下文依然保留：檔案、問題和進度都被記住了。*

想像這個跨越多天的工作流程：

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
# 進行修正工作...

> /exit
```

```bash
# 週三：從完全相同的地方繼續
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

**強大之處**：幾天後，Copilot CLI 仍然記得：
- 你正在處理的確切檔案
- 問題的編號清單
- 你已解決的項目
- 你的對話上下文

無需重新說明，無需重新讀取檔案，直接繼續工作。

---

**🎉 你現在已掌握基礎知識！** `@` 語法、工作階段管理（`--continue`/`--resume`/`/rename`）和上下文指令（`/context`/`/clear`）已足以讓你高效工作。以下內容為選讀，準備好再回來探索。

---

# 選讀：深入探索

<img src="images/optional-going-deeper.png" alt="Abstract crystal cave in blue and purple tones representing deeper exploration of context concepts" width="800"/>

以下主題建立在上述基礎之上。**選擇你感興趣的，或直接跳到[實作練習](#practice)。**

| 我想了解… | 跳至 |
|---|---|
| 萬用字元模式與進階工作階段指令 | [更多 @ 模式與工作階段指令](#additional-patterns) |
| 在多個提示中建立上下文 | [上下文感知對話](#context-aware-conversations) |
| Token 上限與 `/compact` | [理解上下文視窗](#understanding-context-windows) |
| 如何選擇要參照的檔案 | [選擇要參照的內容](#choosing-what-to-reference) |
| 分析截圖與設計稿 | [使用圖片](#working-with-images) |

<details>
<summary><strong>更多 @ 模式與工作階段指令</strong></summary>
<a id="additional-patterns"></a>

### 更多 @ 模式

對進階用戶，Copilot CLI 支援萬用字元模式與圖片參照：

| 模式 | 功能 |
|------|------|
| `@folder/*.py` | 資料夾中所有 .py 檔案 |
| `@**/test_*.py` | 遞迴萬用字元：找出任何位置的所有測試檔案 |
| `@image.png` | 圖片檔案，用於 UI 審查 |

```bash
copilot

> Find all TODO comments in @samples/book-app-project/**/*.py
```

### 工作中切換工作階段

在互動式工作階段中使用 `/resume` 指令：

```bash
copilot

> /resume
# 顯示可切換的工作階段清單
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
# 將工作階段匯出為 Markdown 檔案

> /share gist
# 建立包含工作階段內容的 GitHub gist
```

</details>

<details>
<summary><strong>上下文感知對話</strong></summary>
<a id="context-aware-conversations"></a>

### 上下文感知對話

多輪對話相互建立時，魔法就發生了。

#### 範例：漸進式強化

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

注意每個提示如何建立在前一次的工作上，這就是上下文的威力。

</details>

<details>
<summary><strong>理解上下文視窗</strong></summary>
<a id="understanding-context-windows"></a>

### 理解上下文視窗

你已經從基礎知識中了解 `/context` 和 `/clear`。以下是上下文視窗運作方式的深入說明。

每個 AI 都有一個「上下文視窗」，即它能同時考量的文字量。

<img src="images/context-window-visualization.png" alt="Context Window Visualization" width="800"/>

*上下文視窗就像一張桌子：能放置的東西有限。檔案、對話歷史和系統提示都會佔用空間。*

#### 達到上限時會發生什麼

```bash
copilot

> /context

Context usage: 45,000 / 128,000 tokens (35%)

# 隨著你新增更多檔案和對話，這個數字會增長

> @large-codebase/

Context usage: 120,000 / 128,000 tokens (94%)

# 警告：即將達到上下文上限

> @another-large-file.py

Context limit reached. Older context will be summarized.
```

#### `/compact` 指令

當上下文快滿但又不想失去對話記錄時，`/compact` 可以摘要你的歷史記錄以釋放 token：

```bash
copilot

> /compact
# 摘要對話歷史，釋放上下文空間
# 你的重要發現和決策會被保留
```

#### 上下文效率技巧

| 情境 | 操作 | 原因 |
|------|------|------|
| 開始新話題 | `/clear` | 移除不相關的上下文 |
| 對話很長 | `/compact` | 摘要歷史，釋放 token |
| 需要特定檔案 | `@file.py` 而非 `@folder/` | 只載入需要的內容 |
| 達到上限 | 開始新工作階段 | 全新的 128K 上下文 |
| 多個話題 | 每個話題用 `/rename` | 方便繼續正確的工作階段 |

#### 大型程式碼庫的最佳實踐

1. **精確指定**：用 `@samples/book-app-project/books.py` 而非 `@samples/book-app-project/`
2. **話題間清除**：切換重點時使用 `/clear`
3. **使用 `/compact`**：摘要對話以釋放上下文
4. **使用多個工作階段**：每個功能或話題一個工作階段

</details>

<details>
<summary><strong>選擇要參照的內容</strong></summary>
<a id="choosing-what-to-reference"></a>

### 選擇要參照的內容

在上下文方面，不是所有檔案都平等。以下是明智選擇的方法：

#### 檔案大小考量

| 檔案大小 | 約略 [Token](../GLOSSARY.md#token) 數 | 策略 |
|---------|--------------------------------------|------|
| 小型（< 100 行） | ~500-1,500 tokens | 自由參照 |
| 中型（100-500 行） | ~1,500-7,500 tokens | 參照特定檔案 |
| 大型（500+ 行） | 7,500+ tokens | 謹慎選擇，使用特定檔案 |
| 超大型（1000+ 行） | 15,000+ tokens | 考慮拆分或鎖定特定章節 |

**具體範例：**
- 書籍應用程式的 4 個 Python 檔案合計 ≈ 2,000-3,000 tokens
- 典型的 Python 模組（200 行）≈ 3,000 tokens
- Flask API 檔案（400 行）≈ 6,000 tokens
- 你的 package.json ≈ 200-500 tokens
- 簡短的提示與回應 ≈ 500-1,500 tokens

> 💡 **程式碼的快速估算**：將程式碼行數乘以約 15 來估算 token 數。請注意這只是估算值。

#### 要包含什麼 vs. 排除什麼

**高價值**（包含這些）：
- 進入點（`book_app.py`、`main.py`、`app.py`）
- 你正在詢問的特定檔案
- 目標檔案直接匯入的檔案
- 設定檔（`requirements.txt`、`pyproject.toml`）
- 資料模型或 dataclass

**低價值**（考慮排除）：
- 生成的檔案（編譯輸出、打包的資源）
- Node modules 或 vendor 目錄
- 大型資料檔案或 fixture
- 與你的問題無關的檔案

#### 精確度的光譜

```
較不精確 ────────────────────────► 更精確
@samples/book-app-project/                      @samples/book-app-project/books.py:47-52
     │                                       │
     └─ 掃描所有內容                          └─ 只取你需要的
        （使用更多上下文）                        （保留上下文空間）
```

**何時選擇廣泛**（`@samples/book-app-project/`）：
- 初步探索程式碼庫
- 跨多個檔案尋找模式
- 架構審查

**何時選擇精確**（`@samples/book-app-project/books.py`）：
- 除錯特定問題
- 審查特定檔案的程式碼
- 詢問單一函式

#### 實際範例：分階段載入上下文

```bash
copilot

# 步驟一：從結構開始
> @package.json What frameworks does this project use?

# 步驟二：根據答案縮小範圍
> @samples/book-app-project/ Show me the project structure

# 步驟三：聚焦於重要的內容
> @samples/book-app-project/books.py Review the BookCollection class

# 步驟四：只在需要時加入相關檔案
> @samples/book-app-project/book_app.py @samples/book-app-project/books.py How does the CLI use the BookCollection?
```

這種分階段的方式讓上下文保持專注且高效。

</details>

<details>
<summary><strong>使用圖片</strong></summary>
<a id="working-with-images"></a>

### 使用圖片

你可以使用 `@` 語法在對話中加入圖片，也可以直接**從剪貼簿貼上**（Cmd+V / Ctrl+V）。Copilot CLI 可以分析截圖、設計稿和圖表，協助 UI 除錯、設計實作和錯誤分析。

```bash
copilot

> @images/screenshot.png What is happening in this image?

> @images/mockup.png Write the HTML and CSS to match this design. Place it in a new file called index.html and put the CSS in styles.css.
```

> 📖 **深入了解**：參見[附錄：額外上下文功能](../appendices/additional-context.md#working-with-images)，了解支援的格式、實際使用案例，以及將圖片與程式碼結合的技巧。

</details>

---

# 實作練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

是時候應用你的上下文與工作階段管理技能了。

---

## ▶️ 自行嘗試

### 完整專案審查

本課程包含你可以直接審查的範例檔案。啟動 Copilot 並執行以下提示：

```bash
copilot

> @samples/book-app-project/ Give me a code quality review of this project

# Copilot CLI 會找出以下問題：
# - 重複的顯示函式
# - 缺少輸入驗證
# - 不一致的錯誤處理
```

> 💡 **想用自己的檔案試試？** 建立一個小型 Python 專案（`mkdir -p my-project/src`），新增一些 .py 檔案，然後用 `@my-project/src/` 來審查它們。如果需要，你可以請 Copilot 為你建立範例程式碼！

### 工作階段工作流程

```bash
copilot

> /rename book-app-review
> @samples/book-app-project/books.py Let's add input validation for empty titles

[Copilot CLI 建議驗證方式]

> Implement that fix
> Now consolidate the duplicate display functions in @samples/book-app-project/
> /exit

# 稍後——從上次中斷的地方繼續
copilot --continue

> Generate tests for the changes we made
```

---

完成示範後，試試這些變化：

1. **跨檔案挑戰**：分析 book_app.py 和 books.py 如何協作：
   ```bash
   copilot
   > @samples/book-app-project/book_app.py @samples/book-app-project/books.py
   > What's the relationship between these files? Are there any code smells?
   ```

2. **工作階段挑戰**：開始一個工作階段，用 `/rename my-first-session` 命名，做些事情，用 `/exit` 離開，然後執行 `copilot --continue`。它記得你在做什麼嗎？

3. **上下文挑戰**：在工作階段中途執行 `/context`。你使用了多少 token？試試 `/compact` 後再次確認。（更多關於 `/compact` 的說明請見「深入探索」中的[理解上下文視窗](#understanding-context-windows)。）

**自我檢驗**：當你能解釋為何 `@folder/` 比個別開啟每個檔案更強大時，你就掌握了上下文的精髓。

---

## 📝 作業

### 主要挑戰：追蹤資料流

實作範例專注於程式碼品質審查和輸入驗證。現在在不同任務上練習相同的上下文技能——追蹤資料如何在應用程式中流動：

1. 啟動互動式工作階段：`copilot`
2. 同時參照 `books.py` 和 `book_app.py`：
   `@samples/book-app-project/books.py @samples/book-app-project/book_app.py Trace how a book goes from user input to being saved in data.json. What functions are involved at each step?`
3. 加入資料檔案以提供更多上下文：
   `@samples/book-app-project/data.json What happens if this JSON file is missing or corrupted? Which functions would fail?`
4. 請求跨檔案改善建議：
   `@samples/book-app-project/books.py @samples/book-app-project/utils.py Suggest a consistent error-handling strategy that works across both files.`
5. 重新命名工作階段：`/rename data-flow-analysis`
6. 以 `/exit` 離開，然後用 `copilot --continue` 繼續，並就資料流提出後續問題

**成功標準**：你能夠追蹤跨多個檔案的資料流、繼續已命名的工作階段，並取得跨檔案的改善建議。

<details>
<summary>💡 提示（點擊展開）</summary>

**開始時的範例：**
```bash
cd /path/to/copilot-cli-for-beginners
copilot
> @samples/book-app-project/books.py @samples/book-app-project/book_app.py Trace how a book goes from user input to being saved in data.json.
> @samples/book-app-project/data.json What happens if this file is missing or corrupted?
> /rename data-flow-analysis
> /exit
```

然後以以下方式繼續：`copilot --continue`

**實用指令：**
- `@file.py` - 參照單一檔案
- `@folder/` - 參照資料夾中所有檔案（注意結尾的 `/`）
- `/context` - 確認你使用了多少上下文
- `/rename <name>` - 命名工作階段以便輕鬆繼續

</details>

### 加分挑戰：上下文限制

1. 一次參照所有書籍應用程式檔案：`@samples/book-app-project/`
2. 針對不同檔案提出多個詳細問題（`books.py`、`utils.py`、`book_app.py`、`data.json`）
3. 執行 `/context` 查看使用量，填滿得有多快？
4. 練習使用 `/compact` 回收空間，然後繼續對話
5. 嘗試更精確的檔案參照（例如用 `@samples/book-app-project/books.py` 代替整個資料夾），看看它如何影響上下文使用量

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生的事 | 解決方式 |
|------|---------|---------|
| 忘記在檔名前加 `@` | Copilot CLI 將「books.py」視為純文字 | 使用 `@samples/book-app-project/books.py` 來參照檔案 |
| 期望工作階段自動保留 | 全新啟動 `copilot` 會失去所有先前上下文 | 使用 `--continue`（最後一個工作階段）或 `--resume`（選擇工作階段） |
| 參照目前目錄以外的檔案 | 出現「Permission denied」或「File not found」錯誤 | 使用 `/add-dir /path/to/directory` 授予存取權限 |
| 切換話題時不使用 `/clear` | 舊的上下文會干擾新話題的回應 | 開始不同任務前執行 `/clear` |

### 疑難排解

**「File not found」錯誤** - 確認你在正確的目錄中：

```bash
pwd  # 確認目前目錄
ls   # 列出檔案

# 然後啟動 Copilot 並使用相對路徑
copilot

> Review @samples/book-app-project/books.py
```

**「Permission denied」** - 將目錄加入允許清單：

```bash
copilot --add-dir /path/to/directory

# 或在工作階段中：
> /add-dir /path/to/directory
```

**上下文填滿得太快**：
- 更精確地指定檔案參照
- 在不同話題間使用 `/clear`
- 將工作分散到多個工作階段

</details>

---

# 摘要

## 🔑 重點整理

1. **`@` 語法**讓 Copilot CLI 獲得關於檔案、目錄和圖片的上下文
2. **多輪對話**隨著上下文累積而相互建立
3. **工作階段自動儲存**：使用 `--continue` 或 `--resume` 從中斷處繼續
4. **上下文視窗**有限制：使用 `/context`、`/clear` 和 `/compact` 管理它們
5. **權限旗標**（`--add-dir`、`--allow-all`）控制多目錄存取，請謹慎使用！
6. **圖片參照**（`@screenshot.png`）幫助以視覺方式除錯 UI 問題

> 📚 **官方文件**：[使用 Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli) — 取得關於上下文、工作階段和檔案操作的完整參考。

> 📋 **快速參考**：查看 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference) 以取得完整指令與快捷鍵列表。

---

## ➡️ 接下來

現在你能夠為 Copilot CLI 提供上下文，讓我們把它應用在真實的開發任務上。你剛剛學到的上下文技術（檔案參照、跨檔案分析和工作階段管理）是下一章強大工作流程的基礎。

在**[第 03 章：開發工作流程](../03-development-workflows/README.md)**中，你將學習：

- 程式碼審查工作流程
- 重構模式
- 除錯協助
- 測試生成
- Git 整合

---

**[← 回到第 01 章](../01-setup-and-first-steps/README.md)** | **[繼續前往第 03 章 →](../03-development-workflows/README.md)**
