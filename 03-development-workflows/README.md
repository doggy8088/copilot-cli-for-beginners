![第 03 章：開發工作流程](assets/chapter-header.png)

> **如果 AI 能夠找出你根本沒想到要問的錯誤，會怎樣？**

在本章中，GitHub Copilot CLI 將成為你日常開發的主力工具。你會在日常依賴的工作流程中使用它：測試、重構、除錯，以及 Git 操作。

## 🎯 學習目標

完成本章後，你將能夠：

- 使用 Copilot CLI 執行全面的程式碼審查
- 安全地重構舊有程式碼
- 在 AI 協助下進行除錯
- 自動產生測試
- 將 Copilot CLI 整合進你的 git 工作流程

> ⏱️ **預估時間**：約 60 分鐘（閱讀 15 分鐘 + 實作 45 分鐘）

---

## 🧩 真實世界類比：木工師傅的工作流程

木工師傅不僅會使用工具，他們還有針對不同工作任務的*工作流程*：

<img src="assets/carpenter-workflow-steps.png" alt="工匠工作坊展示三條工作流程：製作家具（測量、切割、組裝、上漆）、修復損壞（評估、拆除、修補、比對）、品質檢查（檢查、測試接合、校正對齊）" width="800"/>

同樣地，開發者也有針對不同任務的工作流程。GitHub Copilot CLI 能強化這些流程，讓你在日常編碼中更有效率、更有成效。

---

# 五大工作流程

<img src="assets/five-workflows.png" alt="五個發光霓虹圖示，分別代表程式碼審查、測試、除錯、重構與 git 整合工作流程" width="800"/>

以下每個工作流程都是獨立的。你可以挑選符合當前需求的流程，也可以全部練習一遍。

---

## 選擇你的冒險

本章涵蓋開發者常用的五種工作流程。**不過，你不需要一次讀完全部！**每個流程都收納在下方可收合區塊中。請選擇最符合你需求、最適合你目前專案的流程。你隨時可以回來探索其他流程。

<img src="assets/five-workflows-swimlane.png" alt="五大開發工作流程：程式碼審查、重構、除錯、測試產生、Git 整合，以橫向泳道圖表示" width="800"/>

| 我想要... | 跳到 |
|---|---|
| 合併前審查程式碼 | [工作流程 1：程式碼審查](#workflow-1-code-review) |
| 清理雜亂或舊有程式碼 | [工作流程 2：重構](#workflow-2-refactoring) |
| 追蹤並修正錯誤 | [工作流程 3：除錯](#workflow-3-debugging) |
| 為我的程式碼產生測試 | [工作流程 4：測試產生](#workflow-4-test-generation) |
| 撰寫更好的提交與 PR | [工作流程 5：Git 整合](#workflow-5-git-integration) |
| 編碼前先做研究 | [快速技巧：規劃或編碼前先研究](#quick-tip-research-before-you-plan-or-code) |
| 看完整的錯誤修正流程 | [整合應用：完整錯誤修正流程](#putting-it-all-together-bug-fix-workflow) |

**請在下方選擇一個工作流程展開**，看看 GitHub Copilot CLI 如何強化你在該領域的開發流程。

---

<a id="workflow-1-code-review"></a>
<details>
<summary><strong>工作流程 1：程式碼審查</strong> - 審查檔案、使用 /review agent、建立嚴重性檢查清單</summary>

<img src="assets/code-review-swimlane-single.png" alt="程式碼審查流程：審查、發現問題、優先排序、產生檢查清單。" width="800"/>

### 基本審查

這個範例使用 `@` 符號參照檔案，讓 Copilot CLI 直接存取其內容進行審查。

```bash
copilot

> Review @samples/book-app-project/book_app.py for code quality
```

---

<details>
<summary>🎬 實際操作示範！</summary>

![Code Review Demo](assets/code-review-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

---

### 輸入驗證審查

請 Copilot CLI 專注於特定議題（例如輸入驗證），只要在提示中列出你關心的類別即可。

```text
copilot

> Review @samples/book-app-project/utils.py for input validation issues. Check for: missing validation, error handling gaps, and edge cases
```

### 跨檔案專案審查

用 `@` 參照整個目錄，讓 Copilot CLI 一次掃描專案內所有檔案。

```bash
copilot

> @samples/book-app-project/ Review this entire project. Create a markdown checklist of issues found, categorized by severity
```

### 互動式程式碼審查

利用多輪對話深入探討。先進行廣泛審查，再提出後續問題，無需重新開始。

```bash
copilot

> @samples/book-app-project/book_app.py Review this file for:
> - Input validation
> - Error handling
> - Code style and best practices

# Copilot CLI 提供詳細審查

> The user input handling - are there any edge cases I'm missing?

# Copilot CLI 顯示可能的問題，例如空字串、特殊字元

> Create a checklist of all issues found, prioritized by severity

# Copilot CLI 產生依嚴重性排序的行動項目
```

### 審查檢查清單範本

請 Copilot CLI 以特定格式（例如依嚴重性分類的 markdown 檢查清單）結構化輸出，方便你貼到 issue。

```bash
copilot

> Review @samples/book-app-project/ and create a markdown checklist of issues found, categorized by:
> - Critical (data loss risks, crashes)
> - High (bugs, incorrect behavior)
> - Medium (performance, maintainability)
> - Low (style, minor improvements)
```

### 了解 Git 變更（/review 很重要）

在使用 `/review` 指令前，你需要了解 git 變更的兩種類型：

| 變更類型 | 意義 | 如何查看 |
|-------------|---------------|------------|
| **已暫存變更** | 你用 `git add` 標記準備提交的檔案 | `git diff --staged` |
| **未暫存變更** | 你已修改但尚未加入的檔案 | `git diff` |

```bash
# 快速參考
git status           # 顯示已暫存與未暫存變更
git add file.py      # 將檔案加入暫存區
git diff             # 顯示未暫存變更
git diff --staged    # 顯示已暫存變更
```

### 使用 /review 指令

`/review` 指令會呼叫內建的**程式碼審查 agent**，專為分析已暫存與未暫存變更設計，能提供高訊噪比的回饋。用 slash 指令觸發專門的內建 agent，而非自由格式提示。

```bash
copilot

> /review
# 針對已暫存/未暫存變更啟動程式碼審查 agent
# 提供聚焦且可行的回饋

> /review Check for security issues in authentication
# 針對特定重點執行審查
```

> 💡 **提示**：程式碼審查 agent 在你有待處理變更時效果最佳。請用 `git add` 將檔案加入暫存區，以獲得更聚焦的審查。

</details>

---

<a id="workflow-2-refactoring"></a>
<details>
<summary><strong>工作流程 2：重構</strong> - 重組程式碼、分離關注點、改善錯誤處理</summary>

<img src="assets/refactoring-swimlane-single.png" alt="重構流程：評估程式碼、規劃變更、實作、驗證行為。" width="800"/>

### 簡單重構

> **先試試這個：** `@samples/book-app-project/book_app.py The command handling uses if/elif chains. Refactor it to use a dictionary dispatch pattern.`

從簡單的改善開始。請在書籍應用程式上試試這些範例。每個提示都用 `@` 參照檔案，並搭配明確的重構指示，讓 Copilot CLI 知道要改什麼。

```bash
copilot

> @samples/book-app-project/book_app.py The command handling uses if/elif chains. Refactor it to use a dictionary dispatch pattern.

> @samples/book-app-project/utils.py Add type hints to all functions

> @samples/book-app-project/book_app.py Extract the book display logic into utils.py for better separation of concerns
```

> 💡 **重構新手？** 先從加上型別註記或改善變數名稱等簡單請求開始，再挑戰複雜的轉換。

---

<details>
<summary>🎬 實際操作示範！</summary>

![Refactor Demo](assets/refactor-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

---

### 分離關注點

在單一提示中用多個 `@` 參照多個檔案，讓 Copilot CLI 能在重構時跨檔案移動程式碼。

```bash
copilot

> @samples/book-app-project/utils.py @samples/book-app-project/book_app.py
> The utils.py file has print statements mixed with logic. Refactor to separate display functions from data processing.
```

### 改善錯誤處理

提供兩個相關檔案並描述橫跨檔案的議題，讓 Copilot CLI 能建議一致的修正方式。

```bash
copilot

> @samples/book-app-project/utils.py @samples/book-app-project/books.py
> These files have inconsistent error handling. Suggest a unified approach using custom exceptions.
```

### 增加文件註解

用詳細的條列清單指定每個 docstring 應包含哪些內容。

```bash
copilot

> @samples/book-app-project/books.py Add comprehensive docstrings to all methods:
> - Include parameter types and descriptions
> - Document return values
> - Note any exceptions raised
> - Add usage examples
```

### 搭配測試安全重構

在多輪對話中串接兩個相關請求。先產生測試，再進行重構，讓測試成為安全網。

```bash
copilot

> @samples/book-app-project/books.py Before refactoring, generate tests for current behavior

# 先取得測試

> Now refactor the BookCollection class to use a context manager for file operations

# 有信心地重構——測試可驗證行為未變
```

</details>

---

<a id="workflow-3-debugging"></a>
<details>
<summary><strong>工作流程 3：除錯</strong> - 追蹤錯誤、安全稽核、跨檔案追蹤問題</summary>

<img src="assets/debugging-swimlane-single.png" alt="除錯流程：理解錯誤、定位根本原因、修正、測試。" width="800"/>

### 簡單除錯

> **先試試這個：** `@samples/book-app-buggy/books_buggy.py Users report that searching for "The Hobbit" returns no results even though it's in the data. Debug why.`

先描述問題所在。這裡是你可以在有錯誤的書籍應用程式上嘗試的常見除錯模式。每個提示都用 `@` 參照檔案，並搭配明確的症狀描述，讓 Copilot CLI 能定位並診斷錯誤。

```bash
copilot

# 模式：「預期 X，實際卻是 Y」
> @samples/book-app-buggy/books_buggy.py Users report that searching for "The Hobbit" returns no results even though it's in the data. Debug why.

# 模式：「非預期行為」
> @samples/book-app-buggy/book_app_buggy.py When I remove a book that doesn't exist, the app says it was removed. Help me find why.

# 模式：「結果錯誤」
> @samples/book-app-buggy/books_buggy.py When I mark one book as read, ALL books get marked. What's the bug?
```

> 💡 **除錯小技巧**：描述*症狀*（你看到什麼）和*預期*（應該發生什麼）。Copilot CLI 會幫你找出原因。

---

<details>
<summary>🎬 實際操作示範！</summary>

![Fix Bug Demo](assets/fix-bug-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

---

### 「錯誤偵探」——AI 找出*相關*錯誤

這正是情境感知除錯大顯身手的時候。請在有錯誤的書籍應用程式上試試這個情境。用 `@` 提供整個檔案，只描述使用者回報的症狀。Copilot CLI 會追蹤根本原因，還可能發現附近的其他錯誤。

```bash
copilot

> @samples/book-app-buggy/books_buggy.py
>
> Users report: "Finding books by author name doesn't work for partial names"
> Debug why this happens
```

**Copilot CLI 會這麼做**：
```
Root Cause: Line 80 uses exact match (==) instead of partial match (in).

Line 80: return [b for b in self.books if b.author == author]

The find_by_author function requires an exact match. Searching for "Tolkien"
won't find books by "J.R.R. Tolkien".

Fix: Change to case-insensitive partial match:
return [b for b in self.books if author.lower() in b.author.lower()]
```

**為什麼這很重要**：Copilot CLI 讀取整個檔案，理解你的錯誤回報情境，並給你明確的修正建議與說明。

> 💡 **加分**：因為 Copilot CLI 會分析整個檔案，經常能發現你沒問到的*其他*問題。例如在修正作者搜尋時，可能也會注意到 `find_book_by_title` 的大小寫問題！

### 真實世界安全性補充

除錯自己的程式碼很重要，理解生產環境應用程式的安全漏洞更是關鍵。試試這個範例：將 Copilot CLI 指向一個陌生檔案，請它稽核安全性問題。

```bash
copilot

> @samples/buggy-code/python/user_service.py Find all security vulnerabilities in this Python user service
```

這個檔案展示了你在生產應用中會遇到的真實安全模式。

> 💡 **你會遇到的常見安全術語：**
> - **SQL Injection**：當使用者輸入直接進入資料庫查詢，攻擊者可執行惡意指令
> - **Parameterized queries**：安全做法——用佔位符（`?`）將使用者資料與 SQL 指令分離
> - **Race condition**：兩個操作同時發生而互相干擾
> - **XSS（跨站腳本攻擊）**：攻擊者將惡意腳本注入網頁

---

### 了解錯誤

將堆疊追蹤直接貼到提示中，並加上 `@` 檔案參照，讓 Copilot CLI 能將錯誤對應到原始碼。

```bash
copilot

> I'm getting this error:
> AttributeError: 'NoneType' object has no attribute 'title'
>     at show_books (book_app.py:19)
>
> @samples/book-app-project/book_app.py Explain why and how to fix it
```

### 用測試案例除錯

描述精確的輸入與觀察到的輸出，讓 Copilot CLI 能根據具體、可重現的測試案例推理。

```bash
copilot

> @samples/book-app-buggy/books_buggy.py The remove_book function has a bug. When I try to remove "Dune",
> it also removes "Dune Messiah". Debug this: explain the root cause and provide a fix.
```

### 跨檔案追蹤問題

參照多個檔案，請 Copilot CLI 追蹤資料流，找出問題源頭。

```bash
copilot

> Users report that the book list numbering starts at 0 instead of 1.
> @samples/book-app-buggy/book_app_buggy.py @samples/book-app-buggy/books_buggy.py
> Trace through the list display flow and identify where the issue occurs
```

### 了解資料問題

同時提供資料檔與讀取該資料的程式碼，讓 Copilot CLI 在建議錯誤處理改善時能掌握全貌。

```bash
copilot

> @samples/book-app-project/data.json @samples/book-app-project/books.py
> Sometimes the JSON file gets corrupted and the app crashes. How should we handle this gracefully?
```

</details>

---

<a id="workflow-4-test-generation"></a>
<details>
<summary><strong>工作流程 4：測試產生</strong> - 自動產生全面測試與邊界案例</summary>

<img src="assets/test-gen-swimlane-single.png" alt="測試產生流程：分析函式、產生測試、涵蓋邊界案例、執行。" width="800"/>

> **先試試這個：** `@samples/book-app-project/books.py Generate pytest tests for all functions including edge cases`

### 「測試爆炸」——2 個測試 vs 15+ 個測試

開發者手動寫測試時，通常只會寫 2-3 個基本測試：
- 測試有效輸入
- 測試無效輸入
- 測試邊界案例

看看當你請 Copilot CLI 產生全面測試時會發生什麼！這個提示用條列清單搭配 `@` 檔案參照，引導 Copilot CLI 產生完整測試覆蓋：

```bash
copilot

> @samples/book-app-project/books.py Generate comprehensive pytest tests. Include tests for:
> - Adding books
> - Removing books
> - Finding by title
> - Finding by author
> - Marking as read
> - Edge cases with empty data
```

---

<details>
<summary>🎬 實際操作示範！</summary>

![Test Generation Demo](assets/test-gen-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

---

**你會得到**：15+ 個全面測試，包括：

```python
class TestBookCollection:
    # Happy path
    def test_add_book_creates_new_book(self):
        ...
    def test_list_books_returns_all_books(self):
        ...

    # Find operations
    def test_find_book_by_title_case_insensitive(self):
        ...
    def test_find_book_by_title_returns_none_when_not_found(self):
        ...
    def test_find_by_author_partial_match(self):
        ...
    def test_find_by_author_case_insensitive(self):
        ...

    # Edge cases
    def test_add_book_with_empty_title(self):
        ...
    def test_remove_nonexistent_book(self):
        ...
    def test_mark_as_read_nonexistent_book(self):
        ...

    # Data persistence
    def test_save_books_persists_to_json(self):
        ...
    def test_load_books_handles_missing_file(self):
        ...
    def test_load_books_handles_corrupted_json(self):
        ...

    # Special characters
    def test_add_book_with_unicode_characters(self):
        ...
    def test_find_by_author_with_special_characters(self):
        ...
```

**結果**：30 秒內就能獲得本來要花一小時思考與撰寫的邊界案例測試。

---

### 單元測試

針對單一函式，列出你想測試的輸入類別，讓 Copilot CLI 產生聚焦且完整的單元測試。

```bash
copilot

> @samples/book-app-project/utils.py Generate comprehensive pytest tests for get_book_details covering:
> - Valid input
> - Empty strings
> - Invalid year formats
> - Very long titles
> - Special characters in author names
```

### 執行測試

用白話問題詢問 Copilot CLI 工具鏈的用法。它會幫你產生正確的 shell 指令。

```bash
copilot

> How do I run the tests? Show me the pytest command.

# Copilot CLI 回應：
# cd samples/book-app-project && python -m pytest tests/
# 或要詳細輸出：python -m pytest tests/ -v
# 要看 print 輸出：python -m pytest tests/ -s
```

### 特定情境測試

列出進階或棘手情境，讓 Copilot CLI 超越單純的 happy path。

```bash
copilot

> @samples/book-app-project/books.py Generate tests for these scenarios:
> - Adding duplicate books (same title and author)
> - Removing a book by partial title match
> - Finding books when collection is empty
> - File permission errors during save
> - Concurrent access to the book collection
```

### 為現有檔案新增測試

請 Copilot CLI 為單一函式產生*額外*測試，補足你已有的案例。

```bash
copilot

> @samples/book-app-project/books.py
> Generate additional tests for the find_by_author function with edge cases:
> - Author name with hyphens (e.g., "Jean-Paul Sartre")
> - Author with multiple first names
> - Empty string as author
> - Author name with accented characters
```

</details>

---

<a id="workflow-5-git-integration"></a>
<details>
<summary><strong>工作流程 5：Git 整合</strong> - 提交訊息、PR 描述、/pr、/delegate 與 /diff</summary>

<img src="assets/git-integration-swimlane-single.png" alt="Git 整合流程：暫存變更、產生訊息、提交、建立 PR。" width="800"/>

> 💡 **本流程假設你已熟悉 git 基本操作**（暫存、提交、分支）。如果你對 git 還不熟，建議先練習前四個流程。

### 產生提交訊息

> **先試試這個：** `copilot -p "Generate a conventional commit message for: $(git diff --staged)"` — 先將變更加入暫存區，再執行這行，看看 Copilot CLI 幫你寫出什麼提交訊息。

這個範例用 `-p` 行內提示旗標，搭配 shell 指令替換，將 `git diff` 輸出直接傳給 Copilot CLI，讓它一次性產生提交訊息。`$(...)` 語法會執行括號內的指令，並將其輸出插入外部指令。

```bash

# 查看變更內容
git diff --staged

# 產生 [Conventional Commit](../GLOSSARY.md#conventional-commit) 格式的提交訊息
# （結構化訊息，如 "feat(books): add search" 或 "fix(data): handle empty input"）
copilot -p "Generate a conventional commit message for: $(git diff --staged)"

# 輸出範例："feat(books): add partial author name search
#
# - Update find_by_author to support partial matches
# - Add case-insensitive comparison
# - Improve user experience when searching authors"
```

---

<details>
<summary>🎬 實際操作示範！</summary>

![Git Integration Demo](assets/git-integration-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

---

### 說明變更內容

將 `git show` 輸出導入 `-p` 提示，取得上一個提交的白話摘要。

```bash
# 這次提交改了什麼？
copilot -p "Explain what this commit does: $(git show HEAD --stat)"
```

### PR 描述

結合 `git log` 輸出與結構化提示範本，自動產生完整的拉取請求（pull request）描述。

```bash
# 根據分支變更產生 PR 描述
copilot -p "Generate a pull request description for these changes:
$(git log main..HEAD --oneline)

Include:
- Summary of changes
- Why these changes were made
- Testing done
- Breaking changes? (yes/no)"
```

### 在互動模式下用 /pr 操作當前分支

如果你在 Copilot CLI 的互動模式下操作分支，可以用 `/pr` 指令管理拉取請求。用 `/pr` 來檢視 PR、建立新 PR、修正現有 PR，或讓 Copilot CLI 根據分支狀態自動決定。

```bash
copilot

> /pr [view|create|fix|auto]
```

### 推送前審查

在 `-p` 提示中用 `git diff main..HEAD`，快速檢查所有分支變更，作為推送前的 sanity check。

```bash
# 推送前最後檢查
copilot -p "Review these changes for issues before I push:
$(git diff main..HEAD)"
```

### 用 /delegate 處理背景任務

`/delegate` 指令會將工作交給 GitHub Copilot 雲端 agent。用 `/delegate` slash 指令（或 `&` 快捷鍵）將明確的任務交給背景 agent 處理。

```bash
copilot

> /delegate Add input validation to the login form

# 或用 & 前綴快捷鍵：
> & Fix the typo in the README header

# Copilot CLI：
# 1. 將你的變更提交到新分支
# 2. 開啟草稿 PR
# 3. 在 GitHub 背景處理
# 4. 完成後請你審查
```

這很適合你想專注其他工作時，讓明確任務在背景自動完成。

### 用 /diff 檢視會話變更

`/diff` 指令會顯示你本次會話期間所有變更。用這個 slash 指令，在提交前檢視 Copilot CLI 修改過的所有檔案差異。

```bash
copilot

# 做了一些變更後...
> /diff

# 顯示本會話所有被修改檔案的視覺化差異
# 很適合提交前審查
```

</details>

---

## 快速技巧：規劃或編碼前先研究

當你需要調查某個函式庫、了解最佳實踐，或探索陌生主題時，請用 `/research` 先進行深入研究，再開始寫程式：

```bash
copilot

> /research What are the best Python libraries for validating user input in CLI apps?
```

Copilot 會搜尋 GitHub 儲存庫與網路資源，然後回傳帶有參考資料的摘要。這在你準備開發新功能、想先做出明智決策時特別有用。你也可以用 `/share` 分享研究結果。> 💡 **提示**：`/research` 最適合在 `/plan` *之前* 使用。先研究解決方法，再規劃實作步驟。

---

## 整合應用：修復錯誤的工作流程

以下是一個完整的修復回報錯誤的工作流程：

```bash

# 1. 了解錯誤回報
copilot

> Users report: 'Finding books by author name doesn't work for partial names'
> @samples/book-app-project/books.py Analyze and identify the likely cause

# 2. 偵錯並修正（在同一會話中繼續）
> Based on the analysis, show me the find_by_author function and explain the issue

> Fix the find_by_author function to handle partial name matches

# 3. 針對修正產生測試
> @samples/book-app-project/books.py Generate pytest tests specifically for:
> - Full author name match
> - Partial author name match
> - Case-insensitive matching
> - Author name not found

# 離開互動式會話

> /exit

# 4. 執行 git add

# 將變更暫存，讓 git diff --staged 有內容可比對
git add .

# 5. 產生提交訊息
copilot -p "Generate commit message for: $(git diff --staged)"

# 範例輸出: "fix(books): support partial author name search"

# 6. 提交變更（可選）

git commit -m "<paste generated message>"
```

### 修復錯誤工作流程總結

| 步驟 | 動作 | Copilot 指令 |
|------|--------|-----------------|
| 1 | 了解錯誤 | `> [describe bug] @relevant-file.py Analyze the likely cause` |
| 2 | 分析與修正 | `> Show me the function and fix the issue` |
| 3 | 產生測試 | `> Generate tests for [specific scenarios]` |
| 4 | 暫存變更 | `git add .` |
| 5 | 產生提交訊息 | `copilot -p "Generate commit message for: $(git diff --staged)"` |
| 6 | 提交變更| `git commit -m "<paste generated message>"` |

---

# 練習

<img src="../assets/practice.png" alt="溫馨桌面擺設，螢幕顯示程式碼、檯燈、咖啡杯與耳機，準備動手練習" width="800"/>

現在輪到你實作這些工作流程。

---

## ▶️ 自己試試看

完成示範後，請嘗試以下變化：

1. **錯誤偵探挑戰**：請 Copilot CLI 偵錯 `samples/book-app-buggy/books_buggy.py` 中的 `mark_as_read` 函式。它有解釋為什麼這個函式會將*所有*書籍都標記為已讀，而不是只標記一本嗎？

2. **測試挑戰**：為書籍應用程式中的 `add_book` 函式產生測試。計算 Copilot CLI 包含了多少你原本沒想到的邊界情境。

3. **提交訊息挑戰**：對書籍應用程式的任一檔案做個小變更，暫存（`git add .`），然後執行：
   ```bash
   copilot -p "Generate a conventional commit message for: $(git diff --staged)"
   ```
   這個訊息比你自己快速寫的還要好嗎？

**自我檢查**：當你能解釋為什麼「debug this bug」比「find bugs」更有力時（情境很重要！），你就理解開發工作流程了！

---

## 📝 作業

### 主要挑戰：重構、測試並發佈

實作範例聚焦於 `find_book_by_title` 與程式碼審查。現在請在 `book-app-project` 中的其他函式練習相同的工作流程技巧：

1. **審查**：請 Copilot CLI 審查 `books.py` 中的 `remove_book()`，找出邊界情境與潛在問題：
   `@samples/book-app-project/books.py Review the remove_book() function. What happens if the title partially matches another book (e.g., "Dune" vs "Dune Messiah")? Are there any edge cases not handled?`
2. **重構**：請 Copilot CLI 改善 `remove_book()`，讓它能處理像是不分大小寫比對、找不到書時回傳有用訊息等邊界情境
3. **測試**：針對改良後的 `remove_book()` 產生 pytest 測試，涵蓋：
   - 移除存在的書籍
   - 不分大小寫的標題比對
   - 找不到書時回傳適當訊息
   - 從空的集合移除
4. **審查**：暫存變更後執行 `/review`，檢查是否還有遺漏的問題
5. **提交**：產生一則 conventional commit 訊息：
   `copilot -p "Generate a conventional commit message for: $(git diff --staged)"`

<details>
<summary>💡 提示（點擊展開）</summary>

**每個步驟的範例提示：**

```bash
copilot

# 步驟 1：審查
> @samples/book-app-project/books.py Review the remove_book() function. What edge cases are not handled?

# 步驟 2：重構
> Improve remove_book() to use case-insensitive matching and return a clear message when the book isn't found. Show me the before and after code.

# 步驟 3：測試
> Generate pytest tests for the improved remove_book() function, including:
> - Removing a book that exists
> - Case-insensitive matching ("dune" should remove "Dune")
> - Book not found returns appropriate response
> - Removing from an empty collection

# 步驟 4：審查
> /review

# 步驟 5：提交
> Generate a conventional commit message for this refactor
```

**提示：** 改善完 `remove_book()` 後，試著問 Copilot CLI：「這個檔案中還有哪些函式也適合做同樣的改善？」它可能會建議你對 `find_book_by_title()` 或 `find_by_author()` 做類似調整。

</details>

### 加分挑戰：用 Copilot CLI 建立一個應用程式

> 💡 **注意**：這個 GitHub Skills 練習使用 **Node.js** 而非 Python。你將練習的 GitHub Copilot CLI 技巧——建立議題、產生程式碼、從終端機協作——適用於任何語言。

這個練習會教你如何用 GitHub Copilot CLI 建立議題、產生程式碼，並在開發 Node.js 計算機應用程式時從終端機協作。你會安裝 CLI、使用範本與 Agent，並練習以指令列為主的反覆開發。

##### <img src="../assets/github-skills-logo.png" width="28" align="center" /> [開始「使用 Copilot CLI 建立應用程式」技能練習](https://github.com/skills/create-applications-with-the-copilot-cli)

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 結果 | 修正方式 |
|---------|--------------|-----|
| 使用模糊提示如「Review this code」 | 回饋很籠統，容易漏掉重點 | 具體說明：「Review for SQL injection, XSS, and auth issues」 |
| 沒用 `/review` 做程式碼審查 | 錯過最佳化的程式碼審查 Agent | 使用 `/review`，它專為高訊噪比輸出而設計 |
| 沒有情境就要求「find bugs」 | Copilot CLI 不知道你遇到什麼問題 | 描述症狀：「Users report X happens when Y」 |
| 產生測試時沒指定框架 | 測試可能用錯語法或斷言庫 | 指定：「Generate tests using Jest」或「using pytest」 |

### 疑難排解

**審查結果不完整**——請更明確說明要檢查什麼：

```bash
copilot

# 不要這樣：
> Review @samples/book-app-project/book_app.py

# 試試這樣：
> Review @samples/book-app-project/book_app.py for input validation, error handling, and edge cases
```

**測試與我的框架不符**——請指定框架：

```bash
copilot

> @samples/book-app-project/books.py Generate tests using pytest (not unittest)
```

**重構後行為改變**——請 Copilot CLI 保持原有行為：

```bash
copilot

> @samples/book-app-project/book_app.py Refactor command handling to use dictionary dispatch. IMPORTANT: Maintain identical external behavior - no breaking changes
```

</details>

---

# 小結

## 🔑 重要重點

<img src="assets/specialized-workflows.png" alt="每個任務的專業化工作流程：程式碼審查、重構、偵錯、測試與 Git 整合" width="800"/>

1. **程式碼審查**：用具體提示讓審查更全面
2. **重構**：先產生測試再重構更安全
3. **偵錯**：同時給 Copilot CLI 錯誤訊息與程式碼，效果最佳
4. **測試產生**：要涵蓋邊界情境與錯誤狀況
5. **Git 整合**：自動產生提交訊息與 PR 描述

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ✅ 檢查點：你已掌握核心技能

**恭喜！** 你現在已具備 GitHub Copilot CLI 的所有核心技能：

| 技能 | 章節 | 你現在可以... |
|-------|---------|----------------|
| 基本指令 | Ch 01 | 使用互動模式、規劃模式、程式化模式（-p）、slash 指令 |
| 情境 | Ch 02 | 用 `@` 引用檔案、管理會話、理解 context window |
| 工作流程 | Ch 03 | 程式碼審查、重構、偵錯、產生測試、與 git 整合 |

第 04-06 章介紹更多進階功能，非常值得學習。

---

## 🛠️ 建立你的個人工作流程

沒有唯一正確的 GitHub Copilot CLI 用法。以下是幾個在建立自己習慣時的建議：

> 📚 **官方文件**：[Copilot CLI 最佳實踐](https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices)，內含推薦工作流程與 GitHub 團隊的技巧。

- **遇到複雜任務先用 `/plan`**。先規劃再執行——好計畫帶來好成果。
- **保存有效的提示詞。** 當 Copilot CLI 出錯時，記下錯誤原因。久而久之，這會成為你的個人攻略本。
- **盡情嘗試。** 有些開發者喜歡長提示，有些偏好短提示加追問。多方嘗試，找出最適合自己的方式。

> 💡 **預告**：第 04、05 章將教你如何把最佳實踐寫成自動載入的自訂指令與技能。

---

## ➡️ 接下來

後續章節將介紹更多擴充 Copilot CLI 能力的功能：

| 章節 | 內容 | 適用時機 |
|---------|----------------|---------------------|
| Ch 04: Agents | 建立專業化 AI 角色 | 需要領域專家（前端、安全性）時 |
| Ch 05: Skills | 任務自動載入指令 | 經常重複相同提示時 |
| Ch 06: MCP | 連接外部服務 | 需要 GitHub、資料庫等即時資料時 |

**建議**：先用一週核心工作流程，有特定需求時再回來看第 04-06 章。

---

## 繼續進階主題

在 **[第 04 章：Agents 與自訂指令](../04-agents-custom-instructions/README.md)**，你將學到：

- 使用內建 Agent（`/plan`、`/review`）
- 用 `.agent.md` 檔案建立專業化 Agent（前端專家、安全審查員）
- 多 Agent 協作模式
- 專案標準的自訂指令檔案

---

**[← 回到第 02 章](../02-context-conversations/README.md)** | **[繼續前往第 04 章 →](../04-agents-custom-instructions/README.md)**
