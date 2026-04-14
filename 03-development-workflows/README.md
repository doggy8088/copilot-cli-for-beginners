![Chapter 03: Development Workflows](images/chapter-header.png)

> **如果 AI 能幫你找出你根本沒想到要問的錯誤，會怎麼樣？**

在本章節中，GitHub Copilot CLI 會成為你的日常主力工具。你將在每天依賴的工作流程中使用它：測試、重構、除錯，以及 Git。

## 🎯 學習目標

完成本章後，你將能夠：

- 使用 Copilot CLI 執行全面的程式碼審查
- 安全地重構舊有程式碼
- 利用 AI 協助除錯問題
- 自動產生測試
- 將 Copilot CLI 整合進你的 git 工作流程

> ⏱️ **預估時間**：約 60 分鐘（15 分鐘閱讀 + 45 分鐘實作）

---

## 🧩 真實世界比喻：木匠的工作流程

木匠不只是會用工具，他們針對不同工作有 *工作流程*：

<img src="images/carpenter-workflow-steps.png" alt="工匠工作坊展示三條工作流程：家具製作（測量、切割、組裝、完成）、損壞修復（評估、移除、修復、配色）、品質檢查（檢查、測試接合、校準對齊）" width="800"/>

同樣地，開發者也有針對不同任務的工作流程。GitHub Copilot CLI 能強化每一種流程，讓你在日常程式開發中更高效、更有成效。

---

# 五大工作流程

<img src="images/five-workflows.png" alt="五個發光霓虹圖示，代表程式碼審查、測試、除錯、重構、git 整合工作流程" width="800"/>

以下每個工作流程都是獨立的。你可以挑選符合目前需求的，也可以全部依序操作。

---

## 自由選擇你的冒險

本章涵蓋開發者常用的五種工作流程。**但你不必一次讀完所有內容！** 每個流程都收錄在下方可收合區塊中。挑選符合你需求、最適合目前專案的流程即可。你隨時可以回來探索其他流程。

<img src="images/five-workflows-swimlane.png" alt="五種開發工作流程：程式碼審查、重構、除錯、測試產生、Git 整合，以橫向泳道圖呈現" width="800"/>

| 我想要... | 跳到 |
|---|---|
| 合併前審查程式碼 | [工作流程 1：程式碼審查](#workflow-1-code-review) |
| 清理雜亂或舊有程式碼 | [工作流程 2：重構](#workflow-2-refactoring) |
| 追蹤並修正錯誤 | [工作流程 3：除錯](#workflow-3-debugging) |
| 為我的程式碼產生測試 | [工作流程 4：測試產生](#workflow-4-test-generation) |
| 撰寫更好的提交與 PR | [工作流程 5：Git 整合](#workflow-5-git-integration) |
| 撰寫程式前先研究 | [快速提示：先研究再規劃或撰寫程式](#quick-tip-research-before-you-plan-or-code) |
| 看完整的錯誤修復流程 | [整合應用：完整錯誤修復流程](#putting-it-all-together-bug-fix-workflow) |

**選擇下方任一工作流程展開**，看看 GitHub Copilot CLI 如何強化你在該領域的開發流程。

---

<a id="workflow-1-code-review"></a>
<details>
<summary><strong>工作流程 1：程式碼審查</strong> - 審查檔案、使用 /review agent、建立嚴重程度檢查清單</summary>

<img src="images/code-review-swimlane-single.png" alt="程式碼審查流程：審查、識別問題、優先排序、產生檢查清單。" width="800"/>

### 基本審查

此範例使用 `@` 符號引用檔案，讓 Copilot CLI 能直接存取內容進行審查。

```bash
copilot

> Review @samples/book-app-project/book_app.py for code quality
```

---

<details>
<summary>🎬 實際操作展示</summary>

![Code Review Demo](images/code-review-demo.gif)

*展示結果會有所不同。你的模型、工具與回應可能與此不同。*

</details>

---

### 輸入驗證審查

請 Copilot CLI 專注於特定議題（如輸入驗證），只需在提示中列出你關心的分類即可。

```text
copilot

> Review @samples/book-app-project/utils.py for input validation issues. Check for: missing validation, error handling gaps, and edge cases
```

### 跨檔案專案審查

用 `@` 引用整個目錄，讓 Copilot CLI 一次掃描專案所有檔案。

```bash
copilot

> @samples/book-app-project/ Review this entire project. Create a markdown checklist of issues found, categorized by severity
```

### 互動式程式碼審查

利用多輪對話深入探討。先做廣泛審查，再追問細節，無需重新開始。

```bash
copilot

> @samples/book-app-project/book_app.py Review this file for:
> - Input validation
> - Error handling
> - Code style and best practices

# Copilot CLI 提供詳細審查

> The user input handling - are there any edge cases I'm missing?

# Copilot CLI 顯示空字串、特殊字元等潛在問題

> Create a checklist of all issues found, prioritized by severity

# Copilot CLI 產生優先排序的行動項目清單
```

### 審查檢查清單範本

請 Copilot CLI 以特定格式產出結果（如嚴重程度分類的 Markdown 檢查清單，可貼到 issue）。

```bash
copilot

> Review @samples/book-app-project/ and create a markdown checklist of issues found, categorized by:
> - Critical (data loss risks, crashes)
> - High (bugs, incorrect behavior)
> - Medium (performance, maintainability)
> - Low (style, minor improvements)
```

### 了解 Git 變更（/review 很重要）

在使用 `/review` 指令前，你需要了解 git 的兩種變更：

| 變更類型 | 意義 | 如何查看 |
|-------------|---------------|------------|
| **已暫存變更** | 用 `git add` 標記為下次提交的檔案 | `git diff --staged` |
| **未暫存變更** | 已修改但尚未加入的檔案 | `git diff` |

```bash
# 快速參考
git status           # 顯示已暫存與未暫存變更
git add file.py      # 將檔案加入暫存區
git diff             # 顯示未暫存變更
git diff --staged    # 顯示已暫存變更
```

### 使用 /review 指令

`/review` 指令會呼叫內建的**程式碼審查 agent**，專為分析已暫存與未暫存變更設計，能產生高訊號、低雜訊的回饋。用斜線指令觸發專屬 agent，無需自由格式提示。

```bash
copilot

> /review
# 針對已暫存／未暫存變更啟動程式碼審查 agent
# 提供聚焦且可行的回饋

> /review Check for security issues in authentication
# 針對特定議題執行審查
```

> 💡 **提示**：程式碼審查 agent 最適合你有待處理變更時使用。用 `git add` 暫存檔案可讓審查更聚焦。

</details>

---

<a id="workflow-2-refactoring"></a>
<details>
<summary><strong>工作流程 2：重構</strong> - 重組程式碼、分離關注點、改善錯誤處理</summary>

<img src="images/refactoring-swimlane-single.png" alt="重構流程：評估程式碼、規劃變更、實作、驗證行為。" width="800"/>

### 簡單重構

> **先試試這個：** `@samples/book-app-project/book_app.py The command handling uses if/elif chains. Refactor it to use a dictionary dispatch pattern.`

從簡單的改善開始。可在書籍應用程式上嘗試這些範例。每個提示都用 `@` 檔案引用搭配明確重構指令，讓 Copilot CLI 清楚知道要改什麼。

```bash
copilot

> @samples/book-app-project/book_app.py The command handling uses if/elif chains. Refactor it to use a dictionary dispatch pattern.

> @samples/book-app-project/utils.py Add type hints to all functions

> @samples/book-app-project/book_app.py Extract the book display logic into utils.py for better separation of concerns
```

> 💡 **重構新手？** 可先從加上型別提示或改善變數名稱等簡單請求開始，再挑戰複雜轉換。

---

<details>
<summary>🎬 實際操作展示</summary>

![Refactor Demo](images/refactor-demo.gif)

*展示結果會有所不同。你的模型、工具與回應可能與此不同。*

</details>

---

### 分離關注點

在同一提示中用 `@` 引用多個檔案，讓 Copilot CLI 能在重構時移動程式碼。

```bash
copilot

> @samples/book-app-project/utils.py @samples/book-app-project/book_app.py
> The utils.py file has print statements mixed with logic. Refactor to separate display functions from data processing.
```

### 改善錯誤處理

提供兩個相關檔案並描述跨檔案議題，讓 Copilot CLI 建議一致的修正方式。

```bash
copilot

> @samples/book-app-project/utils.py @samples/book-app-project/books.py
> These files have inconsistent error handling. Suggest a unified approach using custom exceptions.
```

### 增加文件註解

用詳細的條列清單指定每個 docstring 應包含的內容。

```bash
copilot

> @samples/book-app-project/books.py Add comprehensive docstrings to all methods:
> - Include parameter types and descriptions
> - Document return values
> - Note any exceptions raised
> - Add usage examples
```

### 搭配測試安全重構

在多輪對話中串連兩個相關請求。先產生測試，再重構，有測試做安全網。

```bash
copilot

> @samples/book-app-project/books.py Before refactoring, generate tests for current behavior

# 先取得測試

> Now refactor the BookCollection class to use a context manager for file operations

# 有信心重構——測試可驗證行為是否維持
```

</details>

---

<a id="workflow-3-debugging"></a>
<details>
<summary><strong>工作流程 3：除錯</strong> - 追蹤錯誤、資安審查、跨檔案追蹤問題</summary>

<img src="images/debugging-swimlane-single.png" alt="除錯流程：理解錯誤、定位根本原因、修正、測試。" width="800"/>

### 簡單除錯

> **先試試這個：** `@samples/book-app-buggy/books_buggy.py Users report that searching for "The Hobbit" returns no results even though it's in the data. Debug why.`

先描述問題所在。這裡是你可以在 buggy 書籍應用程式上嘗試的常見除錯模式。每個提示都用 `@` 檔案引用搭配明確症狀描述，讓 Copilot CLI 能定位並診斷錯誤。

```bash
copilot

# 模式：「預期 X，實際 Y」
> @samples/book-app-buggy/books_buggy.py Users report that searching for "The Hobbit" returns no results even though it's in the data. Debug why.

# 模式：「非預期行為」
> @samples/book-app-buggy/book_app_buggy.py When I remove a book that doesn't exist, the app says it was removed. Help me find why.

# 模式：「結果錯誤」
> @samples/book-app-buggy/books_buggy.py When I mark one book as read, ALL books get marked. What's the bug?
```

> 💡 **除錯提示**：描述*症狀*（你看到什麼）和*預期*（應該發生什麼）。Copilot CLI 會幫你找出原因。

---

<details>
<summary>🎬 實際操作展示</summary>

![Fix Bug Demo](images/fix-bug-demo.gif)

*展示結果會有所不同。你的模型、工具與回應可能與此不同。*

</details>

---

### 「錯誤偵探」——AI 找出相關錯誤

這就是情境感知除錯的威力。用 buggy 書籍應用程式試試這個情境。用 `@` 提供整個檔案，只描述使用者回報的症狀。Copilot CLI 會追蹤根本原因，甚至發現附近其他錯誤。

```bash
copilot

> @samples/book-app-buggy/books_buggy.py
>
> Users report: "Finding books by author name doesn't work for partial names"
> Debug why this happens
```

**Copilot CLI 的做法**：
```
根本原因：第 80 行使用精確比對（==）而非部分比對（in）。

Line 80: return [b for b in self.books if b.author == author]

find_by_author 函式要求精確比對。搜尋 "Tolkien" 找不到 "J.R.R. Tolkien" 的書。

修正：改為不分大小寫的部分比對：
return [b for b in self.books if author.lower() in b.author.lower()]
```

**為什麼重要**：Copilot CLI 讀完整檔案，理解你的錯誤回報情境，給你明確修正和清楚解釋。

> 💡 **加分**：Copilot CLI 分析整個檔案時，常會發現你沒問到的*其他*問題。例如修正作者搜尋時，也可能注意到 `find_book_by_title` 的大小寫問題！

### 真實世界資安補充

除錯自己的程式很重要，理解生產環境應用程式的資安漏洞更關鍵。試試這個範例：指向陌生檔案，請 Copilot CLI 審查資安問題。

```bash
copilot

> @samples/buggy-code/python/user_service.py Find all security vulnerabilities in this Python user service
```

此檔案展示你在生產應用程式會遇到的真實資安模式。

> 💡 **常見資安術語：**
> - **SQL Injection**：使用者輸入直接進資料庫查詢，攻擊者可執行惡意指令
> - **Parameterized queries**：安全替代方案——用佔位符（`?`）分離使用者資料與 SQL 指令
> - **Race condition**：兩個操作同時發生，互相干擾
> - **XSS（跨站腳本攻擊）**：攻擊者將惡意腳本注入網頁

---

### 了解錯誤

直接將 stack trace 貼到提示中，搭配 `@` 檔案引用，讓 Copilot CLI 將錯誤對應到原始程式碼。

```bash
copilot

> I'm getting this error:
> AttributeError: 'NoneType' object has no attribute 'title'
>     at show_books (book_app.py:19)
>
> @samples/book-app-project/book_app.py Explain why and how to fix it
```

### 用測試案例除錯

描述精確輸入與觀察到的輸出，讓 Copilot CLI 有具體可重現的測試案例推理。

```bash
copilot

> @samples/book-app-buggy/books_buggy.py The remove_book function has a bug. When I try to remove "Dune",
> it also removes "Dune Messiah". Debug this: explain the root cause and provide a fix.
```

### 跨檔案追蹤問題

引用多個檔案，請 Copilot CLI 追蹤資料流，找出問題源頭。

```bash
copilot

> Users report that the book list numbering starts at 0 instead of 1.
> @samples/book-app-buggy/book_app_buggy.py @samples/book-app-buggy/books_buggy.py
> Trace through the list display flow and identify where the issue occurs
```

### 了解資料問題

同時提供資料檔案與讀取它的程式碼，讓 Copilot CLI 建議更完整的錯誤處理改善。

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

<img src="images/test-gen-swimlane-single.png" alt="測試產生流程：分析函式、產生測試、涵蓋邊界案例、執行。" width="800"/>

> **先試試這個：** `@samples/book-app-project/books.py Generate pytest tests for all functions including edge cases`

### 「測試爆炸」——2 個測試 vs 15+ 個測試

開發者手動寫測試時，通常只寫 2-3 個基本測試：
- 測試有效輸入
- 測試無效輸入
- 測試邊界案例

看看當你請 Copilot CLI 產生全面測試時會發生什麼！這個提示用條列清單搭配 `@` 檔案引用，指引 Copilot CLI 產生完整測試覆蓋：

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
<summary>🎬 實際操作展示</summary>

![Test Generation Demo](images/test-gen-demo.gif)

*展示結果會有所不同。你的模型、工具與回應可能與此不同。*

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

**結果**：30 秒內得到邊界案例測試，原本要花一小時思考與撰寫。

---

### 單元測試

針對單一函式，列出你想測試的輸入類型，讓 Copilot CLI 產生聚焦且完整的單元測試。

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

用白話問題詢問你的工具鏈，Copilot CLI 能幫你產生正確 shell 指令。

```bash
copilot

> How do I run the tests? Show me the pytest command.

# Copilot CLI 回覆：
# cd samples/book-app-project && python -m pytest tests/
# 或要詳細輸出：python -m pytest tests/ -v
# 要看 print：python -m pytest tests/ -s
```

### 特定情境測試

列出進階或棘手情境，讓 Copilot CLI 不只測試順利流程。

```bash
copilot

> @samples/book-app-project/books.py Generate tests for these scenarios:
> - Adding duplicate books (same title and author)
> - Removing a book by partial title match
> - Finding books when collection is empty
> - File permission errors during save
> - Concurrent access to the book collection
```

### 增加現有檔案測試

請求*額外*測試單一函式，讓 Copilot CLI 產生新案例補足現有測試。

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
<summary><strong>工作流程 5：Git 整合</strong> - 提交訊息、PR 描述、/pr、/delegate、/diff</summary>

<img src="images/git-integration-swimlane-single.png" alt="Git 整合流程：暫存變更、產生訊息、提交、建立 PR。" width="800"/>

> 💡 **此流程假設你熟悉 git 基本操作**（暫存、提交、分支）。若你對 git 不熟，建議先嘗試前四個流程。

### 產生提交訊息

> **先試試這個：** `copilot -p "Generate a conventional commit message for: $(git diff --staged)"` — 先暫存一些變更，再執行這個指令，看看 Copilot CLI 如何撰寫提交訊息。

此範例用 `-p` 行內提示旗標搭配 shell 指令替換，將 `git diff` 輸出直接傳給 Copilot CLI，一次產生提交訊息。`$(...)` 語法會執行括號內指令，並將結果插入外部指令。

```bash

# 查看變更內容
git diff --staged

# 用 [Conventional Commit](../GLOSSARY.md#conventional-commit) 格式產生提交訊息
#（結構化訊息如 "feat(books): add search" 或 "fix(data): handle empty input"）
copilot -p "Generate a conventional commit message for: $(git diff --staged)"

# 輸出："feat(books): add partial author name search
#
# - Update find_by_author to support partial matches
# - Add case-insensitive comparison
# - Improve user experience when searching authors"
```

---

<details>
<summary>🎬 實際操作展示</summary>

![Git Integration Demo](images/git-integration-demo.gif)

*展示結果會有所不同。你的模型、工具與回應可能與此不同。*

</details>

---

### 解釋變更

將 `git show` 輸出導入 `-p` 提示，取得上一個提交的白話摘要。

```bash
# 這次提交改了什麼？
copilot -p "Explain what this commit does: $(git show HEAD --stat)"
```

### PR 描述

結合 `git log` 輸出與結構化提示範本，自動產生完整的 pull request 描述。

```bash
# 用分支變更產生 PR 描述
copilot -p "Generate a pull request description for these changes:
$(git log main..HEAD --oneline)

Include:
- Summary of changes
- Why these changes were made
- Testing done
- Breaking changes? (yes/no)"
```

### 在互動模式用 /pr 操作目前分支

若你在 Copilot CLI 互動模式下操作分支，可用 `/pr` 指令處理 pull request。用 `/pr` 查看 PR、建立新 PR、修正現有 PR，或讓 Copilot CLI 根據分支狀態自動決定。

```bash
copilot

> /pr [view|create|fix|auto]
```

### 推送前審查

用 `git diff main..HEAD` 搭配 `-p` 提示，快速檢查所有分支變更，確保推送前沒問題。

```bash
# 推送前最後檢查
copilot -p "Review these changes for issues before I push:
$(git diff main..HEAD)"
```

### 用 /delegate 處理背景任務

`/delegate` 指令會將工作交給 GitHub Copilot 雲端 agent。用 `/delegate` 斜線指令（或 `&` 快捷前綴）將明確任務交給背景 agent。

```bash
copilot

> /delegate Add input validation to the login form

# 或用 & 快捷方式：
> & Fix the typo in the README header

# Copilot CLI：
# 1. 將你的變更提交到新分支
# 2. 開啟草稿 PR
# 3. 在 GitHub 背景作業
# 4. 完成後請你審查
```

這很適合你想專注其他工作時，將明確任務交給 AI 處理。

### 用 /diff 審查本次工作階段變更

`/diff` 指令會顯示本次工作階段所有變更。用此斜線指令可在提交前檢視 Copilot CLI 修改過的所有檔案差異。

```bash
copilot

# 修改完後...
> /diff

# 顯示本次工作階段所有檔案的視覺化差異
# 很適合提交前審查
```

</details>

---

## 快速提示：先研究再規劃或撰寫程式

當你需要調查函式庫、了解最佳實踐或探索陌生主題時，可用 `/research` 先進行深入研究再寫程式：

```bash
copilot

> /research What are the best Python libraries for validating user input in CLI apps?
```

Copilot 會搜尋 GitHub 儲存庫與網路來源，並回傳摘要與參考資料。這在你要開始新功能前很有用，可先做出明智決策。你也可以用 `/share` 分享結果。

> 💡 **提示**：`/research` 適合在 `/plan` 之前使用。先研究方法，再規劃實作。

---

## 整合應用：完整錯誤修復流程

這是一個修正回報錯誤的完整流程：

```bash

# 1. Understand the bug report
copilot

```> 使用者回報：「以作者名稱搜尋書籍時，無法用部分名稱找到」
> @samples/book-app-project/books.py 分析並找出可能原因

# 2. 偵錯問題（在同一個 session 繼續）
> 根據分析，請顯示 find_by_author 函式並說明問題

> 修正 find_by_author 函式，使其能處理部分名稱比對

# 3. 產生修正用的測試
> @samples/book-app-project/books.py 針對以下情境產生 pytest 測試：
> - 完整作者名稱比對
> - 部分作者名稱比對
> - 不區分大小寫比對
> - 找不到作者名稱

# 4. 產生提交訊息
copilot -p "Generate commit message for: $(git diff --staged)"

# 輸出："fix(books): support partial author name search"
```

### 修正錯誤工作流程摘要

| 步驟 | 動作 | Copilot 指令 |
|------|------|--------------|
| 1 | 了解錯誤 | `> [describe bug] @relevant-file.py Analyze the likely cause` |
| 2 | 取得詳細分析 | `> Show me the function and explain the issue` |
| 3 | 實作修正 | `> Fix the [specific issue]` |
| 4 | 產生測試 | `> Generate tests for [specific scenarios]` |
| 5 | 提交 | `copilot -p "Generate commit message for: $(git diff --staged)"` |

---

# 練習

<img src="../images/practice.png" alt="溫暖的書桌擺設，螢幕顯示程式碼、檯燈、咖啡杯與耳機，準備好實作練習" width="800"/>

現在輪到你實際應用這些工作流程。

---

## ▶️ 自己動手試試看

完成示範後，嘗試以下變化題：

1. **錯誤偵探挑戰**：請 Copilot CLI 偵錯 `samples/book-app-buggy/books_buggy.py` 中的 `mark_as_read` 函式。它有解釋為什麼這個函式會把所有書都標記為已讀，而不是只標記一本嗎？

2. **測試挑戰**：為書籍應用程式的 `add_book` 函式產生測試。數數看 Copilot CLI 包含了多少你沒想到的邊界情境。

3. **提交訊息挑戰**：對書籍應用程式的任一檔案做一點小修改，將其暫存（`git add .`），然後執行：
   ```bash
   copilot -p "Generate a conventional commit message for: $(git diff --staged)"
   ```
   產生的訊息比你自己隨手寫的還好嗎？

**自我檢查**：當你能解釋為什麼「debug this bug」比「find bugs」更強大（情境很重要！），就代表你理解開發工作流程了！

---

## 📝 作業

### 主要挑戰：重構、測試並發佈

實作範例聚焦於 `find_book_by_title` 和程式碼審查。現在請你在 `book-app-project` 其他函式上練習相同的工作流程技巧：

1. **審查**：請 Copilot CLI 審查 `books.py` 中的 `remove_book()`，檢查邊界情境與潛在問題：
   `@samples/book-app-project/books.py Review the remove_book() function. What happens if the title partially matches another book (e.g., "Dune" vs "Dune Messiah")? Are there any edge cases not handled?`
2. **重構**：請 Copilot CLI 改進 `remove_book()`，讓它能處理像是不區分大小寫比對，以及當找不到書時能回傳有用的回饋
3. **測試**：針對改良後的 `remove_book()` 函式產生 pytest 測試，涵蓋：
   - 移除已存在的書
   - 不區分大小寫的標題比對
   - 找不到書時回傳適當回饋
   - 從空的集合中移除
4. **審查**：將你的變更暫存後執行 `/review`，檢查是否還有遺漏的問題
5. **提交**：產生一則符合 Conventional Commit 格式的提交訊息：
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

**小技巧：** 改進完 `remove_book()` 後，試著問 Copilot CLI：「這個檔案裡還有哪些函式也適合做同樣的改進？」它可能會建議你也改進 `find_book_by_title()` 或 `find_by_author()`。

</details>

### 進階挑戰：用 Copilot CLI 建立一個應用程式

> 💡 **注意**：這個 GitHub Skills 練習使用 **Node.js**，而不是 Python。你將練習的 GitHub Copilot CLI 技巧——建立議題、產生程式碼、從終端機協作——適用於任何語言。

這個練習會教你如何用 GitHub Copilot CLI 從終端機建立議題、產生程式碼並協作，一邊打造一個 Node.js 計算機應用程式。你會安裝 CLI、使用範本與 Agent，並練習以指令列為主的迭代式開發。

##### <img src="../images/github-skills-logo.png" width="28" align="center" /> [開始「使用 Copilot CLI 建立應用程式」技能練習](https://github.com/skills/create-applications-with-the-copilot-cli)

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 會發生什麼 | 修正方式 |
|------|------------|----------|
| 使用模糊的提示詞如 "Review this code" | 得到很泛泛的回饋，錯過具體問題 | 要具體：「Review for SQL injection, XSS, and auth issues」 |
| 沒用 `/review` 進行程式碼審查 | 錯過最佳化的程式碼審查 Agent | 使用 `/review`，它專為高訊噪比設計 |
| 只說 "find bugs" 沒有情境 | Copilot CLI 不知道你遇到什麼問題 | 說明症狀：「Users report X happens when Y」 |
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

**測試不符合我的框架**——請指定測試框架：

```bash
copilot

> @samples/book-app-project/books.py Generate tests using pytest (not unittest)
```

**重構改變了行為**——請 Copilot CLI 保持行為一致：

```bash
copilot

> @samples/book-app-project/book_app.py Refactor command handling to use dictionary dispatch. IMPORTANT: Maintain identical external behavior - no breaking changes
```

</details>

---

# 小結

## 🔑 重要重點

<img src="images/specialized-workflows.png" alt="每個任務的專業工作流程：程式碼審查、重構、偵錯、測試與 Git 整合" width="800"/>

1. **程式碼審查**：用具體的提示詞讓審查更全面
2. **重構**：先產生測試再重構，風險更低
3. **偵錯**：同時給 Copilot CLI 錯誤現象和程式碼，效果最好
4. **測試產生**：要涵蓋邊界情境與錯誤狀況
5. **Git 整合**：自動產生提交訊息與 PR 描述

> 📋 **快速參考**：[GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference) 可查詢完整指令與捷徑。

---

## ✅ 檢查點：你已掌握核心技能

**恭喜！** 你現在已具備 GitHub Copilot CLI 的所有核心技能：

| 技能 | 章節 | 你現在可以... |
|------|------|---------------|
| 基本指令 | Ch 01 | 使用互動模式、規劃模式、程式化模式（-p）與斜線指令 |
| 情境 | Ch 02 | 以 `@` 參照檔案、管理 session、理解 context window |
| 工作流程 | Ch 03 | 審查程式碼、重構、偵錯、產生測試、與 git 整合 |

第 04-06 章會介紹更多進階功能，值得進一步學習。

---

## 🛠️ 建立你的個人工作流程

沒有單一「正確」的 GitHub Copilot CLI 使用方式。以下是一些建立自己習慣的建議：

> 📚 **官方文件**：[Copilot CLI 最佳實踐](https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices)，內含推薦工作流程與 GitHub 官方技巧。

- **遇到複雜任務先用 `/plan`**。先規劃再執行，計劃好成果更好。
- **保存效果好的提示詞。** 當 Copilot CLI 出錯時，記下錯誤原因。久而久之會變成你的個人攻略本。
- **盡情嘗試。** 有些開發者喜歡長提示詞，有些偏好短提示詞加追問。多試幾種，看看哪種最順手。

> 💡 **預告**：第 04、05 章會教你如何把最佳實踐寫成自動載入的自訂指令與技能。

---

## ➡️ 接下來

後續章節會介紹更多擴充 Copilot CLI 能力的功能：

| 章節 | 內容 | 適用時機 |
|------|------|----------|
| Ch 04: Agents | 建立專業 AI 角色 | 需要領域專家（前端、安全性）時 |
| Ch 05: Skills | 任務自動載入指令 | 常常重複相同提示時 |
| Ch 06: MCP | 連接外部服務 | 需要 GitHub、資料庫等即時資料時 |

**建議**：先用一週核心工作流程，有進階需求時再回來看 04-06 章。

---

## 繼續進階主題

在 **[第 04 章：Agents 與自訂指令](../04-agents-custom-instructions/README.md)**，你將學到：

- 使用內建 agent（如 `/plan`、`/review`）
- 用 `.agent.md` 檔案建立專業 agent（前端專家、安全稽核員）
- 多 agent 協作模式
- 專案標準的自訂指令檔案

---

**[← 回到第 02 章](../02-context-conversations/README.md)** | **[繼續前往第 04 章 →](../04-agents-custom-instructions/README.md)**
