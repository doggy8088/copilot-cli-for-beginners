<!--
---
id: CopilotCLI-02
title: !translate 情境與對話
description: !translate 使用檔案與目錄情境、繼續先前的會話，並學習如何用 GitHub Copilot CLI 撰寫有效的多輪對話。
audience: Developers / Students / Terminal users
slug: context-and-conversations
weight: 3
---
-->

![Chapter 02: Context and Conversations](assets/chapter-header.png)

> **如果 AI 能一次看見你的整個程式碼庫，而不是只能看一個檔案，會怎樣？**

在本章中，你將解鎖 GitHub Copilot CLI 的真正威力：情境。你會學會使用 `@` 語法來引用檔案與目錄，讓 Copilot CLI 能深入理解你的程式碼庫。你將學會如何在多個會話間維持對話、在數天後精確地從上次中斷處繼續工作，並了解跨檔案分析如何發現單檔案檢查完全無法察覺的錯誤。

## 🎯 學習目標

在本章結束時，你將能夠：

- 使用 `@` 語法引用檔案、目錄與圖片
- 透過 `--resume` 與 `--continue` 繼續先前的會話
- 理解 [context window](../GLOSSARY.md#context-window) 的運作方式
- 撰寫有效的多輪對話
- 管理多專案工作流程下的目錄權限

> ⏱️ **預估時間**：約 50 分鐘（閱讀 20 分鐘 + 實作 30 分鐘）

---

## 🧩 真實世界類比：與同事協作

<img src="assets/colleague-context-analogy.png" alt="Context Makes the Difference - Without vs With Context" width="800"/>

*就像你的同事一樣，Copilot CLI 不是讀心術專家。提供更多資訊能幫助人類與 Copilot 都給出更精準的協助！*

想像你要向同事解釋一個 bug：

> **沒有情境**：「書籍應用程式壞掉了。」

> **有情境**：「請看 `books.py`，特別是 `find_book_by_title` 函式。它沒有做不分大小寫的比對。」

要給 Copilot CLI 提供情境，請用 *`@` 語法* 指定特定檔案。

---

# 必備：基礎情境

<img src="assets/essential-basic-context.png" alt="Glowing code blocks connected by light trails representing how context flows through Copilot CLI conversations" width="800"/>

本節涵蓋你有效運用情境所需的一切。先掌握這些基礎。

---

## @ 語法

`@` 符號用於在提示詞中引用檔案與目錄。這就是你告訴 Copilot CLI「請看這個檔案」的方式。

> 💡 **注意**：本課程所有範例皆使用本儲存庫內的 `samples/` 資料夾，你可以直接嘗試每個指令。

### 立即試試看（無需額外設定）

你可以用電腦上的任何檔案來試試看：

```bash
copilot

# 指定你擁有的任意檔案
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
| `@file.py` | 引用單一檔案 | `Review @samples/book-app-project/books.py` |
| `@folder/` | 引用目錄下所有檔案 | `Review @samples/book-app-project/` |
| `@file1.py @file2.py` | 引用多個檔案 | `Compare @samples/book-app-project/book_app.py @samples/book-app-project/books.py` |

### 引用單一檔案

```bash
copilot

> Explain what @samples/book-app-project/utils.py does
```

---

<details>
<summary>🎬 實際操作影片！</summary>

![File Context Demo](assets/file-context-demo.gif)

*Demo 輸出內容會有所不同。你的模型、工具與回應可能與此處展示不同。*

</details>

---

### 引用多個檔案

```bash
copilot

> Compare @samples/book-app-project/book_app.py and @samples/book-app-project/books.py for consistency
```

### 引用整個目錄

```bash
copilot

> Review all files in @samples/book-app-project/ for error handling
```

---

## 跨檔案智慧

這就是情境成為超能力的地方。單檔案分析很有用，跨檔案分析則能徹底改變你的開發方式。

<img src="assets/cross-file-intelligence.png" alt="Cross-File Intelligence - comparing single-file vs cross-file analysis showing how analyzing files together reveals bugs, data flow, and patterns invisible in isolation" width="800"/>

### 範例：找出橫跨多檔案的錯誤

```bash
copilot

> @samples/book-app-project/book_app.py @samples/book-app-project/books.py
>
> How do these files work together? What's the data flow?
```

> 💡 **進階選項**：想做安全性導向的跨檔案分析，請試試 Python 安全範例：
> ```
> > @samples/buggy-code/python/user_service.py @samples/buggy-code/python/payment_processor.py
> > Find security vulnerabilities that span BOTH files
> ```

---

<details>
<summary>🎬 實際操作影片！</summary>

![Multi-File Demo](assets/multi-file-demo.gif)

*Demo 輸出內容會有所不同。你的模型、工具與回應可能與此處展示不同。*

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

**為什麼這很重要**：單檔案檢查會錯失全貌，只有跨檔案分析才能揭露：
- **重複程式碼**：應該合併的功能
- **資料流模式**：顯示元件間如何互動
- **架構問題**：影響可維護性的設計缺陷

---

### 範例：60 秒內理解一個程式碼庫

<img src="assets/codebase-understanding.png" alt="Split-screen comparison showing manual code review taking 1 hour versus AI-assisted analysis taking 10 seconds" width="800" />

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

**結果**：原本需要一小時閱讀的程式碼，濃縮成 10 秒鐘。你馬上知道該聚焦在哪裡。

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
<summary>🎬 看看多輪對話的實際操作！</summary>

![Multi-Turn Demo](assets/multi-turn-demo.gif)

*Demo 輸出內容會有所不同。你的模型、工具與回應可能與此處展示不同。*

</details>

### 範例 3：多檔案重構

```bash
copilot

> @samples/book-app-project/book_app.py @samples/book-app-project/utils.py
> I see duplicate display functions: show_books() and print_books(). Help me consolidate these.

# Copilot CLI 能同時看到兩個檔案，並建議如何合併重複程式碼
```

---

## 會話管理

會話會自動儲存。你可以隨時繼續先前的會話，從中斷處接續。

### 會話自動儲存

每次對話都會自動儲存。只要正常離開即可：

```bash
copilot

> @samples/book-app-project/ Let's improve error handling across all modules

[... 進行一些工作 ...]

> /exit
```

### 繼續最近的會話

```bash
# 從上次中斷處繼續
copilot --continue
```

### 繼續特定會話

```bash
# 互動式選擇會話清單
copilot --resume

# -r 是 --resume 的簡寫（省點打字！）
copilot -r

# 或用會話 ID 直接繼續
copilot --resume=abc123

# 或用你命名的會話名稱繼續
copilot --resume="my book app review"
```

> 💡 **如何找到會話 ID？** 你不需要記住它們。執行 `copilot --resume`（不帶 ID）會顯示互動式清單，包含所有先前會話、名稱、ID 與最後活動時間。直接選你要的即可。
>
> **多個終端機怎麼辦？** 每個終端機視窗都是獨立會話、各自擁有情境。如果你在三個終端機開啟 Copilot CLI，就是三個獨立會話。從任一終端機執行 `--resume` 都能瀏覽全部。`--continue` 旗標會優先抓取目前工作目錄的會話；若無則選最近活動的會話。
>
> **可以不用重啟就切換會話嗎？** 可以。在活動會話中用 `/resume` slash 指令：
> ```
> > /resume
> # 顯示可切換的會話清單
> ```

### 組織你的會話

給會話取有意義的名稱，方便日後查找。你可以在啟動時命名，也能隨時在會話中重新命名：

```bash
# 啟動時直接命名會話
copilot --name book-app-review

# 或在會話中重新命名
copilot

> /rename book-app-review
# 會話已重新命名，方便識別
```

會話命名後，你可以直接用名稱繼續，無需瀏覽清單：

```bash
copilot --resume=book-app-review
```

要清理不需要的會話，可在會話中用 `/session delete`：

```bash
copilot

> /session delete            # 刪除目前會話
> /session delete abc123     # 刪除指定 ID 的會話
> /session delete-all        # 刪除所有會話（請小心使用！）
```

### 跨會話持久記憶

會話會儲存你的對話歷史，但**記憶**更進一步，讓 Copilot CLI 能在*所有會話*間記住偏好與事實，而不僅限於單一會話。

```bash
copilot

> /memory show
# 顯示 Copilot CLI 目前記住的你與專案資訊

> /memory on
# 啟用記憶（若帳號支援，預設為開啟）

> /memory off
# 關閉記憶（若你偏好每次都從零開始）
```

例如，你告訴 Copilot CLI「我偏好 Python 測試用 pytest」，它會記住這個偏好，未來自動套用。你不必重複設定。

> 💡 **記憶 vs. 會話**：會話儲存對話歷史，方便你繼續特定任務。記憶則儲存可重複使用的儲存庫事實與使用者偏好，Copilot 能在未來自動套用。把會話想成任務筆記本，記憶則是 Copilot 可攜帶的可重用情境。

### 檢查與管理情境

隨著你加入檔案與對話，Copilot CLI 的 [context window](../GLOSSARY.md#context-window) 會逐漸填滿。有多種指令可協助你掌控：

```bash
copilot

> /context
Context usage: 62k/200k tokens (31%)

> /clear
# 放棄目前會話（不儲存歷史），開始新對話

> /new
# 結束目前會話（儲存到歷史以供搜尋/繼續），開始新對話

> /rewind
# 開啟時間軸選擇器，可回溯到對話中的任一早期點
```

> 💡 **何時用 `/clear` 或 `/new`**：如果你剛審查完 books.py，想切換討論 utils.py，先執行 /new（或 /clear 若不需保留歷史）。否則舊主題的情境可能讓回應混亂。

> 💡 **操作錯誤或想嘗試不同路徑？** 用 `/rewind`（或連按兩次 Esc）開啟**時間軸選擇器**，可回溯到對話中任一早期點，不只最近一次。回溯時 Copilot CLI 會詢問你要還原對話還是連同 Copilot 修改過的檔案一併還原——不需 git 儲存庫。這很適合走錯路想回頭但又不想全部重來的情境。

---

### 從中斷處繼續

<img src="assets/session-persistence-timeline.png" alt="Timeline showing how GitHub Copilot CLI sessions persist across days - start on Monday, resume on Wednesday with full context restored" width="800"/>

*會話在你離開時自動儲存。數天後繼續時，完整情境（檔案、議題、進度）都會被記住。*

想像這樣的多日工作流程：

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
# 進行修正...

> /exit
```

```bash
# 週三：直接用名稱精確繼續
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
- 你正在處理的檔案
- 編號的議題清單
- 哪些已經處理過
- 你的對話情境

無需重複解釋、無需重讀檔案，直接繼續工作。

---

**🎉 你已掌握所有必備技巧！** `@` 語法、會話管理（`--name`/`--continue`/`--resume`/`/rename`）、情境指令（`/context`/`/clear`）已足夠讓你高效工作。以下內容為進階選讀，隨時回來參考。

---

# 進階選讀：更深入的運用

<img src="assets/optional-going-deeper.png" alt="Abstract crystal cave in blue and purple tones representing deeper exploration of context concepts" width="800"/>

這些主題建立在前述基礎之上。**挑你有興趣的閱讀，或直接跳到 [實作練習](#practice)。**

| 我想學... | 跳到 |
|---|---|
| 萬用字元模式與進階會話指令 | [進階 @ 模式與會話指令](#additional-patterns) |
| 跨多個提示詞累積情境 | [情境感知對話](#context-aware-conversations) |
| Token 限制與 `/compact` | [理解 context window](#understanding-context-windows) |
| 如何選擇要引用哪些檔案 | [選擇引用對象](#choosing-what-to-reference) |
| 分析截圖與設計稿 | [圖片運用](#working-with-images) |

<details>
<summary><strong>進階 @ 模式與會話指令</strong></summary>
<a id="additional-patterns"></a>

### 進階 @ 模式

對進階用戶，Copilot CLI 支援萬用字元模式與圖片引用：

| 模式 | 功能說明 |
|---------|--------------|
| `@folder/*.py` | 目錄下所有 .py 檔案 |
| `@**/test_*.py` | 遞迴萬用字元：尋找所有測試檔 |
| `@image.png` | 圖片檔案，用於 UI 審查 |

```bash
copilot

> Find all TODO comments in @samples/book-app-project/**/*.py
```

### 檢視會話資訊

```bash
copilot

> /session
# 顯示目前會話細節與工作區摘要

> /usage
# 顯示會話統計與使用量
```

### 分享你的會話

```bash
copilot

> /share file ./my-session.md
# 將會話匯出為 markdown 檔案

> /share gist
# 建立 GitHub gist，分享會話內容

> /share html
# 匯出為自包含互動式 HTML 檔案
# 適合與團隊分享精美報告或留存參考
```

</details>

<details>
<summary><strong>情境感知對話</strong></summary>
<a id="context-aware-conversations"></a>

### 情境感知對話

當你進行多輪、逐步累積的對話時，魔法就會發生。

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

你會發現每個提示詞都建立在前一次的成果上。這就是情境的威力。

</details>

<details>
<summary><strong>理解 context window</strong></summary>
<a id="understanding-context-windows"></a>

### 理解 context window

你已從基礎學會 `/context` 與 `/clear`。這裡更深入說明 context window 的運作。

每個 AI 都有一個「context window」，即一次能考量的文字量。

<img src="assets/context-window-visualization.png" alt="Context Window Visualization" width="800"/>

*context window 就像一張桌子：一次只能放有限的東西。檔案、對話歷史、系統提示都會佔空間。*

#### 達到上限時會發生什麼

```bash
copilot

> /context

Context usage: 45,000 / 128,000 tokens (35%)

# 加入更多檔案與對話，這個數字會增加

> @large-codebase/

Context usage: 120,000 / 128,000 tokens (94%)

# 警告：接近 context 上限

> @another-large-file.py

Context limit reached. Older context will be summarized.
```

#### `/compact` 指令

當你的情境快滿了又不想失去對話內容時，`/compact` 會自動摘要歷史，釋放 token 空間：

```bash
copilot

> /compact
# 摘要對話歷史，釋放 context 空間
# 你的重點發現與決策會被保留
```

你也可以給 `/compact` 加上聚焦指示，指定摘要時優先保留哪些內容：

```bash
copilot

> /compact focus on the list of bugs we found and decisions made
# 摘要歷史，重點保留 bug 清單與決策
```

> 💡 **何時用聚焦指示**：若你的對話涵蓋多主題，聚焦指示能讓 `/compact` 優先保留對你下一步最重要的內容，不會斷線。

#### 情境效率小技巧

| 情境 | 行動 | 原因 |
|-----------|--------|-----|
| 開始新主題 | `/clear` | 移除無關情境 |
| 走錯路 | `/rewind` | 回溯對話（可選擇還原檔案） |
| 對話很長 | `/compact` | 摘要歷史，釋放 token |
| 只需特定檔案 | `@file.py` 而非 `@folder/` | 只載入所需內容 |
| 達到上限 | `/new` 或 `/clear` | 全新情境 |
| 多主題 | 每主題用 `/rename` | 容易繼續正確會話 |

#### 大型程式碼庫最佳實踐

1. **明確指定**：用 `@samples/book-app-project/books.py` 取代 `@samples/book-app-project/`
2. **主題切換時清除情境**：用 `/new` 或 `/clear`
3. **善用 `/compact`**：摘要對話釋放空間
4. **多會話並行**：每個功能或主題用一個會話

</details>

<details>
<summary><strong>選擇引用對象</strong></summary>
<a id="choosing-what-to-reference"></a>

### 選擇引用對象

不是所有檔案都同等重要。以下是明智選擇的方式：

#### 檔案大小考量

| 檔案大小 | 約略 [Token 數](../GLOSSARY.md#token) | 策略 |
|-----------|-------------------|----------|
| 小（<100 行） | ~500-1,500 tokens | 可自由引用 |
| 中（100-500 行） | ~1,500-7,500 tokens | 指定特定檔案 |
| 大（500+ 行） | 7,500+ tokens | 謹慎選擇、聚焦特定檔案 |
| 超大（1000+ 行） | 15,000+ tokens | 考慮拆分或只針對區段 |

**具體範例：**
- 書籍應用的 4 個 Python 檔案合計 ≈ 2,000-3,000 tokens
- 一般 Python 模組（200 行）≈ 3,000 tokens
- Flask API 檔案（400 行）≈ 6,000 tokens
- 你的 package.json ≈ 200-500 tokens
- 短提示 + 回應 ≈ 500-1,500 tokens

> 💡 **程式碼 token 粗估法**：行數 × 15 ≈ token 數。僅供參考。

#### 包含與排除的取捨

**高價值**（應納入）：
- 進入點（`book_app.py`、`main.py`、`app.py`）
- 你要詢問的特定檔案
- 目標檔案直接 import 的檔案
- 設定檔（`requirements.txt`、`pyproject.toml`）
- 資料模型或 dataclass

**低價值**（可考慮排除）：
- 產生的檔案（編譯輸出、打包資產）
- node_modules 或 vendor 目錄
- 大型資料檔或測試資料
- 與問題無關的檔案

#### 明確度光譜

```
越不明確 ────────────────────────► 越明確
@samples/book-app-project/                      @samples/book-app-project/books.py:47-52
     │                                       │
     └─ 掃描全部                             └─ 只取所需
        （佔用更多情境）                        （節省情境）
```

**何時用廣泛引用**（`@samples/book-app-project/`）：
- 初步探索程式碼庫
- 尋找跨多檔案的模式
- 架構審查

**何時用精確引用**（`@samples/book-app-project/books.py`）：
- 偵錯特定問題
- 審查單一檔案
- 詢問單一函式

#### 實用範例：分階段載入情境

```bash
copilot

# 步驟 1：先看結構
> @package.json What frameworks does this project use?

# 步驟 2：根據回應聚焦
> @samples/book-app-project/ Show me the project structure

# 步驟 3：聚焦重點
> @samples/book-app-project/books.py Review the BookCollection class

# 步驟 4：只在需要時加入相關檔案
> @samples/book-app-project/book_app.py @samples/book-app-project/books.py How does the CLI use the BookCollection?
```

這種分階段方式能讓情境聚焦且高效。

</details>

<details>
<summary><strong>圖片運用</strong></summary>
<a id="working-with-images"></a>

### 圖片運用

你可以使用 `@` 語法在對話中插入圖片，或直接**從剪貼簿貼上**（Cmd+V / Ctrl+V）。Copilot CLI 能分析螢幕截圖、設計稿和圖表，協助 UI 除錯、設計實作與錯誤分析。

```bash
copilot

> @assets/screenshot.png 這張圖片發生了什麼事？

> @assets/mockup.png 請撰寫符合這個設計的 HTML 和 CSS。將 HTML 放在新檔案 index.html，CSS 放在 styles.css。
```

> 📖 **深入了解**：請參閱[進階情境功能](../appendices/additional-context.md#working-with-images)，了解支援的格式、實用案例，以及圖片與程式碼結合的技巧。

</details>

---

# 練習

<img src="../assets/practice.png" alt="溫馨的書桌擺設，螢幕顯示程式碼、檯燈、咖啡杯與耳機，準備好動手練習" width="800"/>

是時候運用你的情境與會話管理技巧了。

---

## ▶️ 自己動手試試

### 專案全面審查

本課程提供可直接檢閱的範例檔案。啟動 copilot 並執行下方提示：

```bash
copilot

> @samples/book-app-project/ 請幫我審查這個專案的程式碼品質

# Copilot CLI 會找出像是：
# - 重複的顯示函式
# - 缺少輸入驗證
# - 不一致的錯誤處理
```

> 💡 **想用自己的檔案試試嗎？** 建立一個小型 Python 專案（`mkdir -p my-project/src`），新增一些 .py 檔案，然後用 `@my-project/src/` 來審查。你也可以請 copilot 幫你產生範例程式碼！

### 會話工作流程

```bash
copilot

> /rename book-app-review
> @samples/book-app-project/books.py 我們來為空白書名加入輸入驗證

[Copilot CLI 建議驗證方法]

> 實作這個修正
> 現在整合 @samples/book-app-project/ 中重複的顯示函式
> /exit

# 之後 - 從上次進度繼續
copilot --continue

> 為我們做的變更產生測試
```

---

完成示範後，試試這些變化題：

1. **跨檔案挑戰**：分析 book_app.py 和 books.py 如何協作：
   ```bash
   copilot
   > @samples/book-app-project/book_app.py @samples/book-app-project/books.py
   > 這兩個檔案有什麼關聯？有沒有任何程式碼異味？
   ```

2. **會話挑戰**：啟動一個會話，用 `/rename my-first-session` 命名，做些事情後用 `/exit` 離開，再用 `copilot --continue`。它還記得你在做什麼嗎？

3. **情境挑戰**：在會話中途執行 `/context`。你用了多少 token？試試 `/compact` 再檢查一次。（更多 `/compact` 用法請見 Going Deeper 的[理解情境窗口](#understanding-context-windows)。）

**自我檢查**：當你能解釋為什麼 `@folder/` 比逐一開啟每個檔案更強大時，就代表你已經理解情境了。

---

## 📝 作業

### 主要挑戰：追蹤資料流

前面的實作範例聚焦於程式碼品質審查與輸入驗證。現在請用相同的情境技巧，練習追蹤資料在應用程式中的流動：

1. 啟動互動式會話：`copilot`
2. 同時參照 `books.py` 和 `book_app.py`：
   `@samples/book-app-project/books.py @samples/book-app-project/book_app.py 請追蹤一本書從使用者輸入到儲存進 data.json 的流程。每個步驟涉及哪些函式？`
3. 加入資料檔案以獲得更多情境：
   `@samples/book-app-project/data.json 如果這個 JSON 檔案遺失或損毀會發生什麼事？哪些函式會失敗？`
4. 請求跨檔案的改進建議：
   `@samples/book-app-project/books.py @samples/book-app-project/utils.py 請建議一個能在兩個檔案間一致運作的錯誤處理策略。`
5. 重新命名會話：`/rename data-flow-analysis`
6. 用 `/exit` 離開，然後用 `copilot --continue` 回到會話，針對資料流再追問

**成功標準**：你能跨多個檔案追蹤資料流、恢復命名會話，並獲得跨檔案的建議。

<details>
<summary>💡 提示（點擊展開）</summary>

**開始步驟：**
```bash
cd /path/to/copilot-cli-for-beginners
copilot
> @samples/book-app-project/books.py @samples/book-app-project/book_app.py 請追蹤一本書從使用者輸入到儲存進 data.json 的流程。
> @samples/book-app-project/data.json 如果這個檔案遺失或損毀會發生什麼事？
> /rename data-flow-analysis
> /exit
```

然後用：`copilot --continue` 回到會話

**實用指令：**
- `@file.py` - 參照單一檔案
- `@folder/` - 參照資料夾內所有檔案（注意結尾 `/`）
- `/context` - 檢查目前使用多少情境
- `/rename <name>` - 幫會話命名，方便之後繼續

</details>

### 加分挑戰：情境上限

1. 用 `@samples/book-app-project/` 一次參照所有書籍應用程式檔案
2. 針對不同檔案（`books.py`、`utils.py`、`book_app.py`、`data.json`）提出多個詳細問題
3. 執行 `/context` 檢查使用量。填滿得有多快？
4. 練習用 `/compact` 釋放空間，然後繼續對話
5. 嘗試更精確地指定檔案（例如用 `@samples/book-app-project/books.py` 取代整個資料夾），觀察情境使用量的變化

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生情況 | 解法 |
|------|----------|------|
| 忘記在檔名前加 `@` | Copilot CLI 把 "books.py" 當成純文字 | 用 `@samples/book-app-project/books.py` 參照檔案 |
| 以為會話會自動保存 | 重新啟動 `copilot` 會失去所有先前情境 | 用 `--continue`（回到上次會話）或 `--resume`（選擇會話） |
| 參照目前目錄外的檔案 | 出現 "Permission denied" 或 "File not found" 錯誤 | 用 `/add-dir /path/to/directory` 開放存取權限 |
| 換主題時沒用 `/clear` | 舊情境會干擾新主題的回應 | 換任務前先執行 `/clear` |

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

**情境很快就用完**：
- 更精確地指定檔案
- 不同主題間用 `/clear`
- 將工作分散到多個會話

</details>

---

# 小結

## 🔑 重點整理

1. **`@` 語法** 讓 Copilot CLI 知道你要參照哪些檔案、資料夾與圖片
2. **多輪對話** 會隨著情境累積而更有深度
3. **會話自動儲存**：啟動時用 `--name` 命名，之後用 `--resume=<name>` 回復，或用 `--continue` 回到最近一次會話
4. **情境窗口有限**：用 `/clear`、`/compact`、`/context`、`/new`、`/rewind` 管理。用 `/compact focus on <topic>` 指定摘要重點
5. **持久記憶**（`/memory`）讓 Copilot CLI 能跨*所有*會話記住偏好與事實——不限於當前會話
6. **權限旗標**（`--add-dir`、`--allow-all`）控制多目錄存取。請謹慎使用！
7. **圖片參照**（`@screenshot.png`）有助於視覺化除錯 UI 問題

> 📚 **官方文件**：[使用 Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli) 取得完整的情境、會話與檔案操作參考。

> 📋 **快速參考**：請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference) 取得完整指令與快捷鍵列表。

---

## ➡️ 下一步

現在你已經會給 Copilot CLI 提供情境，接下來要將這些技巧應用在實際開發任務上。你剛學到的情境技巧（檔案參照、跨檔案分析、會話管理）正是下一章強大工作流程的基礎。

在 **[第 03 章：開發工作流程](../03-development-workflows/README.md)**，你將學到：

- 程式碼審查工作流程
- 重構模式
- 除錯協助
- 測試產生
- Git 整合

---

**[← 回到第 01 章](../01-setup-and-first-steps/README.md)** | **[繼續前往第 03 章 →](../03-development-workflows/README.md)**
