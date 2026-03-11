![Chapter 03: Development Workflows](images/chapter-header.png)

> **如果 AI 能找出你連問都不知道該問的 bug，會怎樣？**

在本章中，GitHub Copilot CLI 將成為你的日常主力工具。你將在每天都要仰賴的工作流程中使用它：測試、重構、除錯和 Git。

## 🎯 學習目標

完成本章後，你將能夠：

- 使用 Copilot CLI 執行全面的程式碼審查
- 安全地重構遺留程式碼
- 在 AI 協助下除錯問題
- 自動生成測試
- 將 Copilot CLI 整合到你的 git 工作流程中

> ⏱️ **預估時間**：約 60 分鐘（閱讀 15 分鐘 + 實作 45 分鐘）

---

## 🧩 現實生活類比：木匠的工作流程

木匠不只是知道如何使用工具，他們對不同工作有不同的*工作流程*：

<img src="images/carpenter-workflow-steps.png" alt="Craftsman workshop showing three workflow lanes: Building Furniture (Measure, Cut, Assemble, Finish), Fixing Damage (Assess, Remove, Repair, Match), and Quality Check (Inspect, Test Joints, Check Alignment)" width="800"/>

同樣地，開發者對不同任務有不同的工作流程。GitHub Copilot CLI 強化了這些工作流程，讓你在日常編程任務中更有效率。

---

# 五大工作流程

<img src="images/five-workflows.png" alt="Five glowing neon icons representing code review, testing, debugging, refactoring, and git integration workflows" width="800"/>

以下每個工作流程都是自成一體的。選擇符合你當前需求的，或全部逐一完成。

---

## 自選冒險

本章涵蓋開發者通常使用的五種工作流程。**不過你不需要一次全部閱讀！** 每個工作流程都在下方的可折疊區塊中獨立呈現。選擇最符合你需求、最適合你目前專案的項目，其他的可以之後再回來探索。

<img src="images/five-workflows-swimlane.png" alt="Five Development Workflows: Code Review, Refactoring, Debugging, Test Generation, and Git Integration shown as horizontal swimlanes" width="800"/>

| 我想要… | 跳至 |
|---|---|
| 在合併前審查程式碼 | [工作流程一：程式碼審查](#workflow-1-code-review) |
| 整理混亂或遺留的程式碼 | [工作流程二：重構](#workflow-2-refactoring) |
| 追蹤並修復一個 bug | [工作流程三：除錯](#workflow-3-debugging) |
| 為我的程式碼生成測試 | [工作流程四：測試生成](#workflow-4-test-generation) |
| 撰寫更好的提交訊息和 PR | [工作流程五：Git 整合](#workflow-5-git-integration) |
| 寫程式前先研究 | [快速提示：規劃或寫程式前先研究](#quick-tip-research-before-you-plan-or-code) |
| 看一個完整的 bug 修復工作流程 | [綜合應用：Bug 修復工作流程](#putting-it-all-together-bug-fix-workflow) |

**點擊下方的工作流程展開**，看看 GitHub Copilot CLI 如何在該領域強化你的開發流程。

---

<a id="workflow-1-code-review"></a>
<details markdown="1">
<summary><strong>工作流程一：程式碼審查</strong> - 審查檔案、使用 /review agent、建立嚴重性檢查清單</summary>

<img src="images/code-review-swimlane-single.png" alt="Code review workflow: review, identify issues, prioritize, generate checklist." width="800"/>

### 基本審查

此範例使用 `@` 符號參照檔案，讓 Copilot CLI 直接取得其內容進行審查。

```bash
copilot

> Review @samples/book-app-project/book_app.py for code quality
```

---

<details>
<summary>🎬 看看實際效果！</summary>

<img src="images/code-review-demo.gif" alt="Code Review Demo">

<em>示範輸出僅供參考，你的模型、工具與回應內容可能與此不同。</em>

</details>

---

### 輸入驗證審查

在提示中列出你關心的類別，請 Copilot CLI 將審查重點放在特定問題上（此處為輸入驗證）。

```text
copilot

> Review @samples/book-app-project/utils.py for input validation issues. Check for: missing validation, error handling gaps, and edge cases
```


### 跨檔案專案審查

使用 `@` 參照整個目錄，讓 Copilot CLI 一次掃描專案中的每個檔案。

```bash
copilot

> @samples/book-app-project/ Review this entire project. Create a markdown checklist of issues found, categorized by severity
```

### 互動式程式碼審查

使用多輪對話深入探索。從廣泛的審查開始，然後在不重新啟動的情況下追問後續問題。

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

# Copilot CLI 生成按優先順序排列的行動項目
```

### 審查清單範本

請 Copilot CLI 以特定格式（此處為按嚴重性分類的 Markdown 清單，可貼入 issue）輸出結果。

```bash
copilot

> Review @samples/book-app-project/ and create a markdown checklist of issues found, categorized by:
> - Critical (data loss risks, crashes)
> - High (bugs, incorrect behavior)
> - Medium (performance, maintainability)
> - Low (style, minor improvements)
```

### 理解 Git 變更（使用 /review 的重要前置知識）

在使用 `/review` 指令前，你需要了解 git 中的兩種變更類型：

| 變更類型 | 含義 | 如何查看 |
|---------|------|---------|
| **已暫存的變更** | 已用 `git add` 標記要納入下次提交的檔案 | `git diff --staged` |
| **未暫存的變更** | 已修改但尚未新增的檔案 | `git diff` |

```bash
# 快速參考
git status           # 顯示已暫存和未暫存的變更
git add file.py      # 暫存一個檔案準備提交
git diff             # 顯示未暫存的變更
git diff --staged    # 顯示已暫存的變更
```

### 使用 /review 指令

`/review` 指令會呼叫內建的**程式碼審查 agent**，專門用於分析已暫存和未暫存的變更，輸出高訊噪比的結果。使用斜線指令來觸發專門的內建 agent，而非撰寫自由格式的提示。

```bash
copilot

> /review
# 對已暫存/未暫存的變更呼叫程式碼審查 agent
# 提供聚焦、可行的回饋

> /review Check for security issues in authentication
# 針對特定重點執行審查
```

> 💡 **提示**：程式碼審查 agent 在你有待處理的變更時效果最好。用 `git add` 暫存你的檔案，可以獲得更有針對性的審查。

</details>

---

<a id="workflow-2-refactoring"></a>
<details>
<summary><strong>工作流程二：重構</strong> - 重整程式碼結構、分離關注點、改善錯誤處理</summary>

<img src="images/refactoring-swimlane-single.png" alt="Refactoring workflow: assess code, plan changes, implement, verify behavior." width="800"/>

### 簡單重構

> **先試試這個：** `@samples/book-app-project/book_app.py The command handling uses if/elif chains. Refactor it to use a dictionary dispatch pattern.`

從直接的改善開始。在書籍應用程式上嘗試這些提示。每個提示都使用 `@` 檔案參照搭配具體的重構指示，讓 Copilot CLI 確切知道要改什麼。

```bash
copilot

> @samples/book-app-project/book_app.py The command handling uses if/elif chains. Refactor it to use a dictionary dispatch pattern.

> @samples/book-app-project/utils.py Add type hints to all functions

> @samples/book-app-project/book_app.py Extract the book display logic into utils.py for better separation of concerns
```

> 💡 **重構新手？** 從簡單的請求開始，例如新增型別提示或改善變數名稱，再處理複雜的轉換。

---

<details>
<summary>🎬 看看實際效果！</summary>

<img src="images/refactor-demo.gif" alt="Refactor Demo">

<em>示範輸出僅供參考，你的模型、工具與回應內容可能與此不同。</em>

</details>

---

### 分離關注點

在單一提示中使用 `@` 參照多個檔案，讓 Copilot CLI 可以在重構過程中在檔案間移動程式碼。

```bash
copilot

> @samples/book-app-project/utils.py @samples/book-app-project/book_app.py
> The utils.py file has print statements mixed with logic. Refactor to separate display functions from data processing.
```

### 改善錯誤處理

提供兩個相關檔案並描述橫切關注點，讓 Copilot CLI 建議跨兩個檔案的一致修復方案。

```bash
copilot

> @samples/book-app-project/utils.py @samples/book-app-project/books.py
> These files have inconsistent error handling. Suggest a unified approach using custom exceptions.
```

### 新增文件

使用詳細的條列清單明確指定每個 docstring 應包含的內容。

```bash
copilot

> @samples/book-app-project/books.py Add comprehensive docstrings to all methods:
> - Include parameter types and descriptions
> - Document return values
> - Note any exceptions raised
> - Add usage examples
```

### 帶測試的安全重構

在多輪對話中串接兩個相關請求。先生成測試，再以這些測試作為安全網進行重構。

```bash
copilot

> @samples/book-app-project/books.py Before refactoring, generate tests for current behavior

# 先取得測試

> Now refactor the BookCollection class to use a context manager for file operations

# 有了測試，可以放心重構——測試會驗證行為是否保留
```

</details>

---

<a id="workflow-3-debugging"></a>
<details>
<summary><strong>工作流程三：除錯</strong> - 追蹤 bug、安全性稽核、跨檔案追蹤問題</summary>

<img src="images/debugging-swimlane-single.png" alt="Debugging workflow: understand error, locate root cause, fix, test." width="800"/>

### 簡單除錯

> **先試試這個：** `@samples/book-app-buggy/books_buggy.py Users report that searching for "The Hobbit" returns no results even though it's in the data. Debug why.`

從描述問題開始。以下是你可以在有 bug 的書籍應用程式上嘗試的常見除錯模式。每個提示都將 `@` 檔案參照與清晰的症狀描述搭配，讓 Copilot CLI 能夠定位並診斷 bug。

```bash
copilot

# 模式：「預期 X，但得到 Y」
> @samples/book-app-buggy/books_buggy.py Users report that searching for "The Hobbit" returns no results even though it's in the data. Debug why.

# 模式：「意外的行為」
> @samples/book-app-buggy/book_app_buggy.py When I remove a book that doesn't exist, the app says it was removed. Help me find why.

# 模式：「錯誤的結果」
> @samples/book-app-buggy/books_buggy.py When I mark one book as read, ALL books get marked. What's the bug?
```

> 💡 **除錯技巧**：描述*症狀*（你看到的）和*預期*（應該發生的）。Copilot CLI 會搞定其餘的。

---

<details>
<summary>🎬 看看實際效果！</summary>

<img src="images/fix-bug-demo.gif" alt="Fix Bug Demo">

<em>示範輸出僅供參考，你的模型、工具與回應內容可能與此不同。</em>

</details>

---

### 「Bug 偵探」——AI 找到相關的 Bug

這是上下文感知除錯大放異彩的地方。在有 bug 的書籍應用程式上嘗試這個情境。透過 `@` 提供整個檔案，並只描述使用者回報的症狀。Copilot CLI 會追蹤根本原因，甚至可能發現附近的其他 bug。

```bash
copilot

> @samples/book-app-buggy/books_buggy.py
>
> Users report: "Finding books by author name doesn't work for partial names"
> Debug why this happens
```

**Copilot CLI 的回應**：
```
Root Cause: Line 80 uses exact match (==) instead of partial match (in).

Line 80: return [b for b in self.books if b.author == author]

The find_by_author function requires an exact match. Searching for "Tolkien"
won't find books by "J.R.R. Tolkien".

Fix: Change to case-insensitive partial match:
return [b for b in self.books if author.lower() in b.author.lower()]
```

**為何重要**：Copilot CLI 讀取整個檔案、理解 bug 回報的上下文，並給出有具體說明的精確修復方案。

> 💡 **加分**：因為 Copilot CLI 分析了整個檔案，它通常會發現你沒有詢問的*其他*問題。例如，在修復作者搜尋的同時，Copilot CLI 可能還會注意到 `find_book_by_title` 中的大小寫敏感 bug！

### 現實世界安全性補充

在除錯自己的程式碼的同時，理解生產應用程式中的安全漏洞也至關重要。試試這個範例：將 Copilot CLI 指向一個陌生的檔案，請它稽核安全問題。

```bash
copilot

> @samples/buggy-code/python/user_service.py Find all security vulnerabilities in this Python user service
```

這個檔案示範了你在生產應用程式中會遇到的真實安全模式。

> 💡 **你會遇到的常見安全術語：**
> - **SQL Injection（SQL 注入）**：將使用者輸入直接放入資料庫查詢，讓攻擊者得以執行惡意指令
> - **Parameterized queries（參數化查詢）**：安全的替代方案——佔位符（`?`）將使用者資料與 SQL 指令分離
> - **Race condition（競態條件）**：兩個操作同時發生並相互干擾
> - **XSS（跨站腳本攻擊）**：攻擊者將惡意腳本注入網頁

---

### 理解錯誤訊息

將堆疊追蹤直接貼入提示，並搭配 `@` 檔案參照，讓 Copilot CLI 能夠將錯誤對應到原始程式碼。

```bash
copilot

> I'm getting this error:
> AttributeError: 'NoneType' object has no attribute 'title'
>     at show_books (book_app.py:19)
>
> @samples/book-app-project/book_app.py Explain why and how to fix it
```

### 帶測試案例的除錯

描述確切的輸入和觀察到的輸出，給 Copilot CLI 一個具體且可重現的測試案例來推理。

```bash
copilot

> @samples/book-app-buggy/books_buggy.py The remove_book function has a bug. When I try to remove "Dune",
> it also removes "Dune Messiah". Debug this: explain the root cause and provide a fix.
```

### 跨程式碼追蹤問題

參照多個檔案並請 Copilot CLI 跨越它們追蹤資料流，以找出問題的源頭。

```bash
copilot

> Users report that the book list numbering starts at 0 instead of 1.
> @samples/book-app-buggy/book_app_buggy.py @samples/book-app-buggy/books_buggy.py
> Trace through the list display flow and identify where the issue occurs
```

### 理解資料問題

將資料檔案與讀取它的程式碼一起包含，讓 Copilot CLI 在建議錯誤處理改善時能夠掌握全貌。

```bash
copilot

> @samples/book-app-project/data.json @samples/book-app-project/books.py
> Sometimes the JSON file gets corrupted and the app crashes. How should we handle this gracefully?
```

</details>

---

<a id="workflow-4-test-generation"></a>
<details>
<summary><strong>工作流程四：測試生成</strong> - 自動生成全面的測試和邊界案例</summary>

<img src="images/test-gen-swimlane-single.png" alt="Test Generation workflow: analyze function, generate tests, include edge cases, run." width="800"/>

> **先試試這個：** `@samples/book-app-project/books.py Generate pytest tests for all functions including edge cases`

### 「測試爆炸」——2 個測試 vs 15+ 個測試

開發者手動撰寫測試時，通常會建立 2-3 個基本測試：
- 測試有效輸入
- 測試無效輸入
- 測試一個邊界案例

看看請 Copilot CLI 生成全面測試時會發生什麼！這個提示使用結構化的條列清單搭配 `@` 檔案參照，引導 Copilot CLI 提供完整的測試覆蓋：

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
<summary>🎬 看看實際效果！</summary>

<img src="images/test-gen-demo.gif" alt="Test Generation Demo">

<em>示範輸出僅供參考，你的模型、工具與回應內容可能與此不同。</em>

</details>

---

**你會得到的內容**：15+ 個全面的測試，包括：

```python
class TestBookCollection:
    # 正常路徑
    def test_add_book_creates_new_book(self):
        ...
    def test_list_books_returns_all_books(self):
        ...

    # 搜尋操作
    def test_find_book_by_title_case_insensitive(self):
        ...
    def test_find_book_by_title_returns_none_when_not_found(self):
        ...
    def test_find_by_author_partial_match(self):
        ...
    def test_find_by_author_case_insensitive(self):
        ...

    # 邊界案例
    def test_add_book_with_empty_title(self):
        ...
    def test_remove_nonexistent_book(self):
        ...
    def test_mark_as_read_nonexistent_book(self):
        ...

    # 資料持久化
    def test_save_books_persists_to_json(self):
        ...
    def test_load_books_handles_missing_file(self):
        ...
    def test_load_books_handles_corrupted_json(self):
        ...

    # 特殊字元
    def test_add_book_with_unicode_characters(self):
        ...
    def test_find_by_author_with_special_characters(self):
        ...
```

**結果**：30 秒內，你得到了原本需要一個小時才能想出並撰寫的邊界案例測試。

---

### 單元測試

針對單一函式並列舉你想測試的輸入類別，讓 Copilot CLI 生成聚焦、完整的單元測試。

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

對 Copilot CLI 提出關於你工具鏈的白話問題，它可以為你生成正確的 shell 指令。

```bash
copilot

> How do I run the tests? Show me the pytest command.

# Copilot CLI 回應：
# cd samples/book-app-project && python -m pytest tests/
# 或使用詳細輸出：python -m pytest tests/ -v
# 查看 print 陳述式：python -m pytest tests/ -s
```

### 針對特定情境的測試

列出你想涵蓋的進階或棘手情境，讓 Copilot CLI 超越正常路徑。

```bash
copilot

> @samples/book-app-project/books.py Generate tests for these scenarios:
> - Adding duplicate books (same title and author)
> - Removing a book by partial title match
> - Finding books when collection is empty
> - File permission errors during save
> - Concurrent access to the book collection
```

### 在現有檔案中新增測試

請求針對單一函式的*額外*測試，讓 Copilot CLI 生成補充現有測試的新案例。

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
<summary><strong>工作流程五：Git 整合</strong> - 提交訊息、PR 描述、/delegate 和 /diff</summary>

<img src="images/git-integration-swimlane-single.png" alt="Git Integration workflow: stage changes, generate message, commit, create PR." width="800"/>

> 💡 **此工作流程假設你具備基本 git 操作知識**（暫存、提交、分支）。若你剛接觸 git，請先試試其他四個工作流程。

### 生成提交訊息

> **先試試這個：** `copilot -p "Generate a conventional commit message for: $(git diff --staged)"` — 暫存一些變更，然後執行這個指令看 Copilot CLI 為你撰寫提交訊息。

此範例使用 `-p` 內聯提示旗標搭配 shell 指令替換，將 `git diff` 輸出直接傳入 Copilot CLI，一次性生成提交訊息。`$(...)` 語法會執行括號內的指令並將其輸出插入外層指令。

```bash

# 查看變更內容
git diff --staged

# 使用[慣例提交](../GLOSSARY.md#conventional-commit)格式生成提交訊息
# （結構化訊息如「feat(books): add search」或「fix(data): handle empty input」）
copilot -p "Generate a conventional commit message for: $(git diff --staged)"

# 輸出：「feat(books): add partial author name search
#
# - Update find_by_author to support partial matches
# - Add case-insensitive comparison
# - Improve user experience when searching authors」
```

---

<details>
<summary>🎬 看看實際效果！</summary>

<img src="images/git-integration-demo.gif" alt="Git Integration Demo">

<em>示範輸出僅供參考，你的模型、工具與回應內容可能與此不同。</em>

</details>

---

### 解釋變更內容

將 `git show` 的輸出傳入 `-p` 提示，取得最後一次提交的白話文摘要。

```bash
# 這次提交改了什麼？
copilot -p "Explain what this commit does: $(git show HEAD --stat)"
```

### PR 描述

將 `git log` 輸出與結構化提示範本結合，自動生成完整的 pull request 描述。

```bash
# 根據分支變更生成 PR 描述
copilot -p "Generate a pull request description for these changes:
$(git log main..HEAD --oneline)

Include:
- Summary of changes
- Why these changes were made
- Testing done
- Breaking changes? (yes/no)"
```

### 推送前審查

在 `-p` 提示中使用 `git diff main..HEAD`，對所有分支變更進行推送前的快速健全性檢查。

```bash
# 推送前的最後檢查
copilot -p "Review these changes for issues before I push:
$(git diff main..HEAD)"
```

### 使用 /delegate 執行背景任務

`/delegate` 指令將工作移交給 GitHub 上的 Copilot 編程 agent。使用 `/delegate` 斜線指令（或 `&` 快捷前綴）將定義明確的任務卸載給背景 agent。

```bash
copilot

> /delegate Add input validation to the login form

# 或使用 & 前綴快捷方式：
> & Fix the typo in the README header

# Copilot CLI：
# 1. 將你的變更提交到新分支
# 2. 開啟一個草稿 pull request
# 3. 在 GitHub 背景作業
# 4. 完成後請你審查
```

這對你想要在專注於其他工作時完成的任務非常實用。

### 使用 /diff 審查工作階段變更

`/diff` 指令顯示你目前工作階段中所做的所有變更。使用此斜線指令，在提交前查看 Copilot CLI 修改過的所有內容。

```bash
copilot

# 進行一些變更後…
> /diff

# 顯示本工作階段所有已修改檔案的視覺化差異
# 提交前審查的好工具
```

</details>

---

## 快速提示：規劃或寫程式前先研究 {#quick-tip-research-before-you-plan-or-code}

當你需要調查某個函式庫、了解最佳實踐或探索陌生主題時，在撰寫任何程式碼前先使用 `/research` 執行深度研究：

```bash
copilot

> /research What are the best Python libraries for validating user input in CLI apps?
```

Copilot 搜尋 GitHub 儲存庫和網路資源，然後返回有來源參考的摘要。當你即將開始一個新功能並想先做出明智決定時，這非常有用。你可以使用 `/share` 分享結果。

> 💡 **提示**：`/research` 在 `/plan` *之前*效果很好——先研究方法，再規劃實作。

---

## 綜合應用：Bug 修復工作流程 {#putting-it-all-together-bug-fix-workflow}

以下是修復一個回報 bug 的完整工作流程：

```bash

# 1. 理解 bug 回報
copilot

> Users report: 'Finding books by author name doesn't work for partial names'
> @samples/book-app-project/books.py Analyze and identify the likely cause

# 2. 除錯問題（在同一工作階段中繼續）
> Based on the analysis, show me the find_by_author function and explain the issue

> Fix the find_by_author function to handle partial name matches

# 3. 為修復生成測試
> @samples/book-app-project/books.py Generate pytest tests specifically for:
> - Full author name match
> - Partial author name match
> - Case-insensitive matching
> - Author name not found

# 4. 生成提交訊息
copilot -p "Generate commit message for: $(git diff --staged)"

# 輸出：「fix(books): support partial author name search」
```

### Bug 修復工作流程摘要

| 步驟 | 操作 | Copilot 指令 |
|------|------|------------|
| 1 | 理解 bug | `> [描述 bug] @relevant-file.py Analyze the likely cause` |
| 2 | 取得詳細分析 | `> Show me the function and explain the issue` |
| 3 | 實作修復 | `> Fix the [specific issue]` |
| 4 | 生成測試 | `> Generate tests for [specific scenarios]` |
| 5 | 提交 | `copilot -p "Generate commit message for: $(git diff --staged)"` |

---

# 實作練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

現在輪到你應用這些工作流程了。

---

## ▶️ 自行嘗試

完成示範後，試試這些變化：

1. **Bug 偵探挑戰**：請 Copilot CLI 除錯 `samples/book-app-buggy/books_buggy.py` 中的 `mark_as_read` 函式。它有解釋為何該函式將所有書籍都標記為已讀而不是只標記一本嗎？

2. **測試挑戰**：為書籍應用程式中的 `add_book` 函式生成測試。數一數 Copilot CLI 包含了多少你不會想到的邊界案例。

3. **提交訊息挑戰**：對書籍應用程式的任一檔案做一個小變更，暫存它（`git add .`），然後執行：
   ```bash
   copilot -p "Generate a conventional commit message for: $(git diff --staged)"
   ```
   這個訊息比你快速寫的更好嗎？

**自我檢驗**：當你能解釋為何「debug this bug」比「find bugs」更強大（上下文很重要！）時，你就理解了開發工作流程。

---

## 📝 作業

### 主要挑戰：重構、測試並交付

實作範例專注於 `find_book_by_title` 和程式碼審查。現在在 `book-app-project` 的不同函式上練習相同的工作流程技能：

1. **審查**：請 Copilot CLI 審查 `books.py` 中的 `remove_book()` 是否有邊界案例和潛在問題：
   `@samples/book-app-project/books.py Review the remove_book() function. What happens if the title partially matches another book (e.g., "Dune" vs "Dune Messiah")? Are there any edge cases not handled?`
2. **重構**：請 Copilot CLI 改善 `remove_book()`，處理如大小寫不敏感比對等邊界案例，並在找不到書籍時返回有用的回饋
3. **測試**：專門為改善後的 `remove_book()` 函式生成 pytest 測試，涵蓋：
   - 移除存在的書籍
   - 大小寫不敏感的書名比對
   - 不存在的書籍返回適當的回饋
   - 從空集合中移除
4. **審查**：暫存你的變更並執行 `/review` 檢查是否有剩餘問題
5. **提交**：生成慣例提交訊息：
   `copilot -p "Generate a conventional commit message for: $(git diff --staged)"`

<details markdown="1">
<summary>💡 提示（點擊展開）</summary>

**每個步驟的範例提示：**

```bash
copilot

# 步驟一：審查
> @samples/book-app-project/books.py Review the remove_book() function. What edge cases are not handled?

# 步驟二：重構
> Improve remove_book() to use case-insensitive matching and return a clear message when the book isn't found. Show me the before and after code.

# 步驟三：測試
> Generate pytest tests for the improved remove_book() function, including:
> - Removing a book that exists
> - Case-insensitive matching ("dune" should remove "Dune")
> - Book not found returns appropriate response
> - Removing from an empty collection

# 步驟四：審查
> /review

# 步驟五：提交
> Generate a conventional commit message for this refactor
```

**提示：** 改善 `remove_book()` 後，試著問 Copilot CLI：「Are there any other functions in this file that could benefit from the same improvements?」。它可能會建議對 `find_book_by_title()` 或 `find_by_author()` 做類似的改動。

</details>

### 加分挑戰：用 Copilot CLI 建立應用程式

> 💡 **備註**：這個 GitHub Skills 練習使用 **Node.js** 而非 Python。你將練習的 GitHub Copilot CLI 技術——建立 issue、生成程式碼和在終端機中協作——適用於任何語言。

這個練習向開發者展示如何使用 GitHub Copilot CLI 在建立 Node.js 計算機應用程式的過程中，從終端機建立 issue、生成程式碼並進行協作。你將安裝 CLI、使用範本和 agent，並練習迭代式、命令列驅動的開發。

##### <img src="../images/github-skills-logo.png" width="28" align="center" /> [開始「使用 Copilot CLI 建立應用程式」Skills 練習](https://github.com/skills/create-applications-with-the-copilot-cli)

---

<details markdown="1">
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生的事 | 解決方式 |
|------|---------|---------|
| 使用模糊的提示如「Review this code」 | 回饋籠統，遺漏具體問題 | 更精確：「Review for SQL injection, XSS, and auth issues」 |
| 不使用 `/review` 進行程式碼審查 | 錯過最佳化的程式碼審查 agent | 使用 `/review`，它專門調整為高訊噪比輸出 |
| 沒有上下文地請求「find bugs」 | Copilot CLI 不知道你遇到了什麼 bug | 描述症狀：「Users report X happens when Y」 |
| 生成測試時不指定框架 | 測試可能使用錯誤的語法或斷言函式庫 | 指定：「Generate tests using Jest」或「using pytest」 |

### 疑難排解

**審查似乎不完整** - 更具體地說明要找什麼：

```bash
copilot

# 不要這樣：
> Review @samples/book-app-project/book_app.py

# 改成這樣：
> Review @samples/book-app-project/book_app.py for input validation, error handling, and edge cases
```

**測試不符合我的框架** - 指定框架：

```bash
copilot

> @samples/book-app-project/books.py Generate tests using pytest (not unittest)
```

**重構後行為改變** - 請 Copilot CLI 保留行為：

```bash
copilot

> @samples/book-app-project/book_app.py Refactor command handling to use dictionary dispatch. IMPORTANT: Maintain identical external behavior - no breaking changes
```

</details>

---

# 摘要

## 🔑 重點整理

<img src="images/specialized-workflows.png" alt="Specialized Workflows for Every Task: Code Review, Refactoring, Debugging, Testing, and Git Integration" width="800"/>

1. **程式碼審查**透過具體的提示變得全面
2. **重構**在先生成測試後更安全
3. **除錯**在同時向 Copilot CLI 展示錯誤訊息和程式碼時更有效
4. **測試生成**應該包含邊界案例和錯誤情境
5. **Git 整合**自動化提交訊息和 PR 描述

> 📋 **快速參考**：查看 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference) 以取得完整指令與快捷鍵列表。

---

## ✅ 檢查點：你已掌握核心技能

**恭喜！** 你現在具備了使用 GitHub Copilot CLI 高效工作所需的所有核心技能：

| 技能 | 章節 | 你現在能夠… |
|------|------|------------|
| 基本指令 | 第 01 章 | 使用互動模式、計畫模式、程式化模式（-p）和斜線指令 |
| 上下文 | 第 02 章 | 以 `@` 參照檔案、管理工作階段、理解上下文視窗 |
| 工作流程 | 第 03 章 | 審查程式碼、重構、除錯、生成測試、整合 git |

第 04-06 章涵蓋更多附加功能，同樣值得學習。

---

## 🛠️ 建立你的個人工作流程

使用 GitHub Copilot CLI 沒有單一「正確」的方式。以下是你發展自己模式時的一些建議：

> 📚 **官方文件**：[Copilot CLI 最佳實踐](https://docs.github.com/copilot/how-tos/copilot-cli/cli-best-practices) — 來自 GitHub 的推薦工作流程與技巧。

- **對任何非瑣碎的事情先用 `/plan`**。在執行前細化計畫——好的計畫帶來更好的結果。
- **儲存效果好的提示。** 當 Copilot CLI 出錯時，記下哪裡出了問題。隨著時間累積，這會成為你的個人操作手冊。
- **自由實驗。** 有些開發者喜歡長而詳細的提示，有些則喜歡簡短提示搭配後續追問。嘗試不同的方式，注意哪種感覺最自然。

> 💡 **即將到來**：在第 04 和 05 章中，你將學習如何將最佳實踐編碼成自訂指示和 skill，讓 Copilot CLI 自動載入。

---

## ➡️ 接下來

其餘章節涵蓋擴展 Copilot CLI 能力的附加功能：

| 章節 | 涵蓋內容 | 適合情境 |
|------|---------|---------|
| 第 04 章：Agent | 建立專屬的 AI 角色 | 當你需要領域專家（前端、安全性）時 |
| 第 05 章：Skill | 自動載入任務指示 | 當你重複使用相同的提示時 |
| 第 06 章：MCP | 連接外部服務 | 當你需要來自 GitHub、資料庫的即時資料時 |

**建議**：先將核心工作流程使用一週，然後在有特定需求時回來學習第 04-06 章。

---

## 繼續學習進階主題

在**[第 04 章：Agent 與自訂指示](../04-agents-custom-instructions/README.md)**中，你將學習：

- 使用內建 agent（`/plan`、`/review`）
- 以 `.agent.md` 檔案建立專屬 agent（前端專家、安全稽核員）
- 多 agent 協作模式
- 專案標準的自訂指示檔案

---

**[← 回到第 02 章](../02-context-conversations/README.md)** | **[繼續前往第 04 章 →](../04-agents-custom-instructions/README.md)**
