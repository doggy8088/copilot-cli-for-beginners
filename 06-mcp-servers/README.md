![Chapter 06: MCP Servers](images/chapter-header.png)

> **如果 Copilot 能從終端機直接讀取您的 GitHub 議題、查詢資料庫並建立 PR，那會如何？**

目前為止，Copilot 只能處理您直接提供的內容：以 `@` 引用的檔案、對話歷程，以及它自身的訓練資料。但如果它能自行查詢您的 GitHub 程式庫、瀏覽您的專案檔案，或查閱某個套件庫的最新文件呢？

這正是 MCP（模型情境協定，Model Context Protocol）的作用。它是一種將 Copilot 連接到外部服務的方式，讓它能存取即時的真實世界資料。每個 Copilot 連接的服務稱為「MCP 伺服器」。在本章中，您將設定幾個這樣的連線，並親眼見證它們如何讓 Copilot 大幅提升實用性。

> 💡 **已熟悉 MCP？** [跳至快速入門](#-use-the-built-in-github-mcp)，確認運作正常並開始設定伺服器。

## 🎯 學習目標

完成本章後，您將能夠：

- 了解 MCP 是什麼以及為何重要
- 使用 `/mcp` 指令管理 MCP 伺服器
- 設定 GitHub、檔案系統和文件的 MCP 伺服器
- 使用 MCP 驅動的工作流程搭配書籍應用程式專案
- 了解何時以及如何建立自訂 MCP 伺服器（選讀）

> ⏱️ **預估時間**：約 50 分鐘（閱讀 15 分鐘 + 實作 35 分鐘）

---

## 🧩 真實世界類比：瀏覽器擴充功能

<img src="images/browser-extensions-analogy.png" alt="MCP Servers are like Browser Extensions" width="800"/>

將 MCP 伺服器想像成瀏覽器擴充功能。您的瀏覽器本身可以顯示網頁，但擴充功能將其連接到額外的服務：

| 瀏覽器擴充功能 | 連接對象 | MCP 對應項目 |
|-------------------|---------------------|----------------|
| 密碼管理員 | 您的密碼庫 | **GitHub MCP** → 您的程式庫、議題、PR |
| Grammarly | 寫作分析服務 | **Context7 MCP** → 套件庫文件 |
| 檔案管理員 | 雲端儲存 | **Filesystem MCP** → 本地專案檔案 |

沒有擴充功能，您的瀏覽器仍然好用，但有了擴充功能，它就變成了強大的工具。MCP 伺服器對 Copilot 的作用相同。它們將 Copilot 連接到真實的即時資料來源，讓它能讀取您的 GitHub 議題、探索您的檔案系統、擷取最新文件等等。

***MCP 伺服器將 Copilot 與外部世界連接：GitHub、程式庫、文件等等***

> 💡 **核心洞察**：沒有 MCP，Copilot 只能看到您透過 `@` 明確分享的檔案。有了 MCP，它可以主動探索您的專案、查詢您的 GitHub 程式庫，並查閱文件，全部自動完成。

---

<img src="images/quick-start-mcp.png" alt="Power cable connecting with bright electrical spark surrounded by floating tech icons representing MCP server connections" width="800"/>

# 快速入門：30 秒了解 MCP

## 開始使用內建 GitHub MCP 伺服器
讓我們立即看看 MCP 的實際效果，無需任何設定。
GitHub MCP 伺服器預設已包含在內。試試這個：

```bash
copilot
> List the recent commits in this repository
```

如果 Copilot 回傳了真實的提交資料，您剛才就看到了 MCP 的實際運作。那就是 GitHub MCP 伺服器代表您向 GitHub 發出請求。但 GitHub 只是*其中一個*伺服器。本章將向您展示如何新增更多伺服器（檔案系統存取、最新文件等），讓 Copilot 能做更多事情。

---

## `/mcp show` 指令

使用 `/mcp show` 查看已設定的 MCP 伺服器及其啟用狀態：

```bash
copilot

> /mcp show

MCP Servers:
✓ github (enabled) - GitHub integration
✓ filesystem (enabled) - File system access
```

> 💡 **只看到 GitHub 伺服器？** 這是正常的！如果您尚未新增任何額外的 MCP 伺服器，GitHub 是唯一列出的伺服器。您將在下一節新增更多。

> 📚 **想查看所有 `/mcp` 指令？** 還有更多用於新增、編輯、啟用和刪除伺服器的指令。請參閱本章末尾的[完整指令參考](#-additional-mcp-commands)。

<details>
<summary>🎬 看看實際效果！</summary>

<img src="images/mcp-status-demo.gif" alt="MCP Status Demo">

<em>示範輸出因人而異。您的模型、工具和回應結果可能與這裡顯示的有所不同。</em>

</details>

---

## MCP 帶來了什麼改變？

以下是 MCP 在實際使用中的差異：

**沒有 MCP：**
```bash
> What's in GitHub issue #42?

"I don't have access to GitHub. You'll need to copy and paste the issue content."
```

**有了 MCP：**
```bash
> What's in GitHub issue #42 of this repository?

Issue #42: Login fails with special characters
Status: Open
Labels: bug, priority-high
Description: Users report that passwords containing...
```

MCP 讓 Copilot 了解您真實的開發環境。

> 📚 **官方文件**：[About MCP](https://docs.github.com/copilot/concepts/context/mcp)，深入了解 MCP 如何與 GitHub Copilot 協作。

---

# 設定 MCP 伺服器

<img src="images/configuring-mcp-servers.png" alt="Hands adjusting knobs and sliders on a professional audio mixing board representing MCP server configuration" width="800"/>

既然您已看過 MCP 的實際運作，讓我們設定額外的伺服器。本節涵蓋設定檔格式以及如何新增新伺服器。

---

## MCP 設定檔

MCP 伺服器設定於 `~/.copilot/mcp-config.json`（全域）或 `.copilot/mcp-config.json`（專案）。

```json
{
  "mcpServers": {
    "server-name": {
      "type": "local",
      "command": "npx",
      "args": ["@package/server-name"],
      "tools": ["*"]
    }
  }
}
```

*大多數 MCP 伺服器以 npm 套件的形式發布，並透過 `npx` 指令執行。*

<details>
<summary>💡 <strong>初次接觸 JSON？</strong> 點擊了解各欄位含義</summary>

| 欄位 | 含義 |
|-------|---------------|
| `"mcpServers"` | 所有 MCP 伺服器設定的容器 |
| `"server-name"` | 您自訂的名稱（例如「github」、「filesystem」） |
| `"type": "local"` | 伺服器在您的電腦上執行 |
| `"command": "npx"` | 要執行的程式（npx 用於執行 npm 套件） |
| `"args": [...]` | 傳遞給指令的參數 |
| `"tools": ["*"]` | 允許此伺服器的所有工具 |

**重要的 JSON 規則：**
- 字串使用雙引號 `"`（不是單引號）
- 最後一個項目後不加尾部逗號
- 檔案必須是有效的 JSON（不確定時可使用 [JSON 驗證器](https://jsonlint.com/)）

</details>

---

## 新增 MCP 伺服器

GitHub MCP 伺服器已內建，無需設定。以下是您可以新增的其他伺服器。**選擇您感興趣的，或依序操作。**

| 我想要... | 跳至 |
|---|---|
| 讓 Copilot 瀏覽我的專案檔案 | [Filesystem 伺服器](#filesystem-server) |
| 取得最新的套件庫文件 | [Context7 伺服器](#context7-server-documentation) |
| 探索選讀內容（自訂伺服器、web_fetch） | [進階主題](#beyond-the-basics) |

<details>
<summary><strong>Filesystem 伺服器</strong> - 讓 Copilot 探索您的專案檔案</summary>
<a id="filesystem-server"></a>

### Filesystem 伺服器

```json
{
  "mcpServers": {
    "filesystem": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."],
      "tools": ["*"]
    }
  }
}
```

> 💡 **`.` 路徑的含義**：`.` 表示「目前目錄」。Copilot 可以存取相對於啟動位置的檔案。在 Codespace 中，這是您的工作區根目錄。您也可以使用絕對路徑，例如 `/workspaces/copilot-cli-for-beginners`。

將此設定加入您的 `~/.copilot/mcp-config.json` 並重新啟動 Copilot。

</details>

<details>
<summary><strong>Context7 伺服器</strong> - 取得最新的套件庫文件</summary>
<a id="context7-server-documentation"></a>

### Context7 伺服器（文件）

Context7 讓 Copilot 能存取熱門框架和套件庫的最新文件。不依賴可能已過時的訓練資料，而是擷取實際的當前文件。

```json
{
  "mcpServers": {
    "context7": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"],
      "tools": ["*"]
    }
  }
}
```

✅ **無需 API 金鑰** · ✅ **無需帳號** · ✅ **您的程式碼保留在本地**

將此設定加入您的 `~/.copilot/mcp-config.json` 並重新啟動 Copilot。

</details>

<details>
<summary><strong>進階主題</strong> - 自訂伺服器和網頁存取（選讀）</summary>
<a id="beyond-the-basics"></a>

這些是選讀的進階內容，適合您熟悉上述核心伺服器後再探索。

### 建立自訂 MCP 伺服器

想將 Copilot 連接到您自己的 API、資料庫或內部工具？您可以用 Python 建立自訂 MCP 伺服器。由於預建的伺服器（GitHub、filesystem、Context7）已涵蓋大多數使用案例，這完全是選讀內容。

📖 請參閱[自訂 MCP 伺服器指南](mcp-custom-server.md)，取得以書籍應用程式為範例的完整教學。

📚 如需更多背景知識，請參閱 [MCP for Beginners 課程](https://github.com/microsoft/mcp-for-beginners)。

### 使用 `web_fetch` 存取網頁

Copilot CLI 內建 `web_fetch` 工具，可以從任何 URL 擷取內容。這對於在不離開終端機的情況下引入 README、API 文件或發行說明非常有用。無需 MCP 伺服器。

您可以透過 `~/.copilot/config.json`（一般 Copilot 設定）控制哪些 URL 可以存取，此檔案與 `~/.copilot/mcp-config.json`（MCP 伺服器定義）是分開的。

```json
{
  "permissions": {
    "allowedUrls": [
      "https://api.github.com/**",
      "https://docs.github.com/**",
      "https://*.npmjs.org/**"
    ],
    "blockedUrls": [
      "http://**"
    ]
  }
}
```

**使用方式：**
```bash
copilot

> Fetch and summarize the README from https://github.com/facebook/react
```

</details>

<a id="complete-configuration-file"></a>

### 完整設定檔

以下是包含 filesystem 和 Context7 伺服器的完整 `mcp-config.json`：

> 💡 **注意：** GitHub MCP 已內建，無需加入設定檔。

```json
{
  "mcpServers": {
    "filesystem": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."],
      "tools": ["*"]
    },
    "context7": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"],
      "tools": ["*"]
    }
  }
}
```

將此儲存為 `~/.copilot/mcp-config.json`（全域存取）或 `.copilot/mcp-config.json`（專案特定設定）。

---

# 使用 MCP 伺服器

設定好 MCP 伺服器後，讓我們看看它們能做什麼。

<img src="images/using-mcp-servers.png" alt="Using MCP Servers - Hub-and-spoke diagram showing a Developer CLI connected to GitHub, Filesystem, Context7, and Custom/Web Fetch servers" width="800" />

---

## 伺服器使用範例

**選擇您想探索的伺服器，或依序操作。**

| 我想嘗試... | 跳至 |
|---|---|
| GitHub 程式庫、議題和 PR | [GitHub 伺服器](#github-server-built-in) |
| 瀏覽專案檔案 | [Filesystem 伺服器用法](#filesystem-server-usage) |
| 查詢套件庫文件 | [Context7 伺服器用法](#context7-server-usage) |
| 自訂伺服器和 web_fetch 用法 | [進階主題用法](#beyond-the-basics-usage) |

<details>
<summary><strong>GitHub 伺服器（內建）</strong> - 存取程式庫、議題、PR 等</summary>
<a id="github-server-built-in"></a>

### GitHub 伺服器（內建）

GitHub MCP 伺服器已**內建**。如果您已登入 Copilot（在初始設定時完成），它即可直接使用，無需任何設定！

> 💡 **無法使用？** 執行 `/login` 重新向 GitHub 驗證。

<details>
<summary><strong>Dev Container 中的驗證</strong></summary>

- **GitHub Codespaces**（推薦）：驗證是自動的。`gh` CLI 繼承您的 Codespace token，無需任何操作。
- **本地 dev container（Docker）**：容器啟動後執行 `gh auth login`，然後重新啟動 Copilot。

**驗證疑難排解：**
```bash
# Check if you're authenticated
gh auth status

# If not, log in
gh auth login

# Verify GitHub MCP is connected
copilot
> /mcp show
```

</details>

| 功能 | 範例 |
|---------|----------|
| **程式庫資訊** | 查看提交、分支、貢獻者 |
| **議題** | 列出、建立、搜尋議題並留言 |
| **PR** | 查看 PR、差異，建立 PR，檢查狀態 |
| **程式碼搜尋** | 跨程式庫搜尋程式碼 |
| **Actions** | 查詢工作流程執行和狀態 |

```bash
copilot

# See recent activity in this repo
> List the last 5 commits in this repository

Recent commits:
1. abc1234 - Update chapter 05 skills examples (2 days ago)
2. def5678 - Add book app test fixtures (3 days ago)
3. ghi9012 - Fix typo in chapter 03 README (4 days ago)
...

# Explore the repo structure
> What branches exist in this repository?

Branches:
- main (default)
- chapter6 (current)

# Search for code patterns across the repo
> Search this repository for files that import pytest

Found 1 file:
- samples/book-app-project/tests/test_books.py
```

> 💡 **在您自己的 fork 上操作？** 如果您 fork 了本課程程式庫，還可以嘗試寫入操作，例如建立議題和 PR。我們將在下方的練習中實作。

> ⚠️ **看不到結果？** GitHub MCP 操作的是程式庫的遠端（github.com 上的），而非僅限本地檔案。請確認您的程式庫有遠端：執行 `git remote -v` 來確認。

</details>

<details>
<summary><strong>Filesystem 伺服器</strong> - 瀏覽和分析專案檔案</summary>
<a id="filesystem-server-usage"></a>

### Filesystem 伺服器

設定完成後，filesystem MCP 提供 Copilot 可自動使用的工具：

```bash
copilot

> How many Python files are in the book-app-project directory?

Found 3 Python files in samples/book-app-project/:
- book_app.py
- books.py
- utils.py

> What's the total size of the data.json file?

samples/book-app-project/data.json: 2.4 KB

> Find all functions that don't have type hints in the book app

Found 2 functions without type hints:
- samples/book-app-project/utils.py:10 - get_user_choice()
- samples/book-app-project/utils.py:14 - get_book_details()
```

</details>

<details>
<summary><strong>Context7 伺服器</strong> - 查詢套件庫文件</summary>
<a id="context7-server-usage"></a>

### Context7 伺服器

```bash
copilot

> What are the best practices for using pytest fixtures?

From pytest Documentation:

Fixtures - Use fixtures to provide a fixed baseline for tests:

    import pytest

    @pytest.fixture
    def sample_books():
        return [
            {"title": "1984", "author": "George Orwell", "year": 1949},
            {"title": "Dune", "author": "Frank Herbert", "year": 1965},
        ]

    def test_find_by_author(sample_books):
        # fixture is automatically passed as argument
        results = [b for b in sample_books if "Orwell" in b["author"]]
        assert len(results) == 1

Best practices:
- Use fixtures instead of setup/teardown methods
- Use tmp_path fixture for temporary files
- Use monkeypatch for modifying environment
- Scope fixtures appropriately (function, class, module, session)

> How can I apply this to the book app's test file?

# Copilot now knows the official pytest patterns
# and can apply them to samples/book-app-project/tests/test_books.py
```

</details>

<details>
<summary><strong>進階主題</strong> - 自訂伺服器和 web_fetch 用法</summary>
<a id="beyond-the-basics-usage"></a>

### 進階主題

**自訂 MCP 伺服器**：如果您按照[自訂 MCP 伺服器指南](mcp-custom-server.md)建立了書籍查詢伺服器，可以直接查詢您的書籍集合：

```bash
copilot

> Look up information about "1984" using the book lookup server
> Search for books by George Orwell
```

**Web Fetch**：使用內建的 `web_fetch` 工具從任何 URL 擷取內容：

```bash
copilot

> Fetch and summarize the README from https://github.com/facebook/react
```

</details>

---

## 多伺服器工作流程

這些工作流程展示了為何開發者會說「我再也不想沒有這個工具了」。每個範例在單一工作階段中結合多個 MCP 伺服器。

<img src="images/issue-to-pr-workflow.png" alt="Issue to PR Workflow using MCP - Shows the complete flow from getting a GitHub issue through creating a pull request" width="800"/>

*完整的 MCP 工作流程：GitHub MCP 擷取程式庫資料、Filesystem MCP 找到程式碼、Context7 MCP 提供最佳實踐，Copilot 負責分析*

以下每個範例均可獨立使用。**選擇您感興趣的，或全部閱讀。**

| 我想看... | 跳至 |
|---|---|
| 多個伺服器協同運作 | [多伺服器探索](#multi-server-exploration) |
| 在單一工作階段從議題到 PR | [議題轉 PR 工作流程](#issue-to-pr-workflow) |
| 快速專案健康檢查 | [健康儀表板](#health-dashboard) |

<details>
<summary><strong>多伺服器探索</strong> - 在單一工作階段中結合 filesystem、GitHub 和 Context7</summary>
<a id="multi-server-exploration"></a>

#### 使用多個 MCP 伺服器探索書籍應用程式

```bash
copilot

# Step 1: Use filesystem MCP to explore the book app
> List all Python files in samples/book-app-project/ and summarize
> what each file does

Found 3 Python files:
- book_app.py: CLI entry point with command routing (list, add, remove, find)
- books.py: BookCollection class with data persistence via JSON
- utils.py: Helper functions for user input and display

# Step 2: Use GitHub MCP to check recent changes
> What were the last 3 commits that touched files in samples/book-app-project/?

Recent commits affecting book app:
1. abc1234 - Add test fixtures for BookCollection (2 days ago)
2. def5678 - Add find_by_author method (5 days ago)
3. ghi9012 - Initial book app setup (1 week ago)

# Step 3: Use Context7 MCP for best practices
> What are Python best practices for JSON data persistence?

From Python Documentation:
- Use context managers (with statements) for file I/O
- Handle JSONDecodeError for corrupted files
- Use dataclasses for structured data
- Consider atomic writes to prevent data corruption

# Step 4: Synthesize a recommendation
> Based on the book app code and these best practices,
> what improvements would you suggest?

Suggestions:
1. Add input validation in add_book() for empty strings and invalid years
2. Consider atomic writes in save_books() to prevent data corruption
3. Add type hints to utils.py functions (get_user_choice, get_book_details)
```

<details>
<summary>🎬 看看 MCP 工作流程的實際效果！</summary>

<img src="images/mcp-workflow-demo.gif" alt="MCP Workflow Demo">

<em>示範輸出因人而異。您的模型、工具和回應結果可能與這裡顯示的有所不同。</em>

</details>

**最終成果**：程式碼探索 → 歷程審查 → 最佳實踐查詢 → 改進計畫。**全程在單一終端機工作階段中完成，同時使用三個 MCP 伺服器。**

</details>

<details>
<summary><strong>議題轉 PR 工作流程</strong> - 不離開終端機，從 GitHub 議題直接建立 PR</summary>
<a id="issue-to-pr-workflow"></a>

#### 議題轉 PR 工作流程（在您自己的程式庫上）

這在您有寫入權限的 fork 或程式庫上效果最佳：

> 💡 **現在無法嘗試也沒關係。** 如果您在唯讀的 clone 上，可以在作業中實作。現在只需閱讀以了解流程。

```bash
copilot

> Get the details of GitHub issue #1

Issue #1: Add input validation for book year
Status: Open
Description: The add_book function accepts any year value...

> @samples/book-app-project/books.py Fix the issue described in issue #1

[Copilot implements year validation in add_book()]

> Run the tests to make sure the fix works

All 8 tests passed ✓

> Create a pull request titled "Add year validation to book app"

✓ Created PR #2: Add year validation to book app
```

**無需複製貼上。無需切換情境。一個終端機工作階段搞定。**

</details>

<details>
<summary><strong>健康儀表板</strong> - 使用多個伺服器進行快速專案健康檢查</summary>
<a id="health-dashboard"></a>

#### 書籍應用程式健康儀表板

```bash
copilot

> Give me a health report for the book app project:
> 1. List all functions across the Python files in samples/book-app-project/
> 2. Check which functions have type hints and which don't
> 3. Show what tests exist in samples/book-app-project/tests/
> 4. Check the recent commit history for this directory

Book App Health Report
======================

📊 Functions Found:
- books.py: 8 methods in BookCollection (all have type hints ✓)
- book_app.py: 6 functions (4 have type hints, 2 missing)
- utils.py: 3 functions (1 has type hints, 2 missing)

🧪 Test Coverage:
- test_books.py: 8 test functions covering BookCollection
- Missing: no tests for book_app.py CLI functions
- Missing: no tests for utils.py helper functions

📝 Recent Activity:
- 3 commits in the last week
- Most recent: added test fixtures

Recommendations:
- Add type hints to utils.py functions
- Add tests for book_app.py CLI handlers
- All files well-sized (<100 lines) - good structure!
```

**最終成果**：多個資料來源在數秒內彙總完成。手動操作的話，需要執行 grep、計算行數、查看 git log 以及瀏覽測試檔案，輕鬆耗費 15 分鐘以上。

</details>

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

**🎉 您已掌握基本知識！** 您了解了 MCP，看過如何設定伺服器，也見過真實工作流程的示範。現在是親自動手的時候了。

---

## ▶️ 親自試試看

現在輪到您了！完成以下練習，練習使用 MCP 伺服器搭配書籍應用程式專案。

### 練習 1：確認您的 MCP 狀態

首先確認哪些 MCP 伺服器可用：

```bash
copilot

> /mcp show
```

您應該看到 GitHub 伺服器列為已啟用。如果沒有，執行 `/login` 進行驗證。

---

### 練習 2：使用 Filesystem MCP 探索書籍應用程式

如果您已設定 filesystem 伺服器，請用它探索書籍應用程式：

```bash
copilot

> How many Python files are in samples/book-app-project/?
> What functions are defined in each file?
```

**預期結果**：Copilot 列出 `book_app.py`、`books.py` 和 `utils.py` 及其函式。

> 💡 **尚未設定 filesystem MCP？** 使用上方[完整設定](#complete-configuration-file)章節的設定建立設定檔，然後重新啟動 Copilot。

---

### 練習 3：使用 GitHub MCP 查詢程式庫歷程

使用內建的 GitHub MCP 探索本課程程式庫：

```bash
copilot

> List the last 5 commits in this repository

> What branches exist in this repository?
```

**預期結果**：Copilot 顯示來自 GitHub 遠端的最新提交訊息和分支名稱。

> ⚠️ **在 Codespace 中？** 這會自動運作，驗證已繼承。如果您在本地 clone 上，請確認 `gh auth status` 顯示您已登入。

---

### 練習 4：結合多個 MCP 伺服器

現在在單一工作階段中結合 filesystem 和 GitHub MCP：

```bash
copilot

> Read samples/book-app-project/data.json and tell me what books are
> in the collection. Then check the recent commits to see when this
> file was last modified.
```

**預期結果**：Copilot 讀取 JSON 檔案（filesystem MCP），列出 5 本書包括《哈比人》、《1984》、《沙丘》、《梅岡城故事》和《神秘之書》，然後查詢 GitHub 的提交歷程。

**自我檢核**：當您能解釋為何「Check my repo's commit history」比手動執行 `git log` 並貼上輸出到提示詞更好時，代表您已理解 MCP。

---

## 📝 作業

### 主要挑戰：書籍應用程式 MCP 探索

練習在書籍應用程式專案上結合使用 MCP 伺服器。在單一 Copilot 工作階段中完成以下步驟：

1. **確認 MCP 運作**：執行 `/mcp show`，確認至少 GitHub 伺服器已啟用
2. **設定 filesystem MCP**（若尚未完成）：使用 filesystem 伺服器設定建立 `~/.copilot/mcp-config.json`
3. **探索程式碼**：要求 Copilot 使用 filesystem 伺服器：
   - 列出 `samples/book-app-project/books.py` 中的所有函式
   - 檢查 `samples/book-app-project/utils.py` 中哪些函式缺少型別提示
   - 讀取 `samples/book-app-project/data.json` 並找出任何資料品質問題（提示：看看最後一筆條目）
4. **查詢程式庫活動**：要求 Copilot 使用 GitHub MCP：
   - 列出最近觸及 `samples/book-app-project/` 中檔案的提交
   - 確認是否有任何開放的議題或 PR
5. **結合伺服器**：在單一提示詞中，要求 Copilot：
   - 讀取 `samples/book-app-project/tests/test_books.py` 的測試檔案
   - 將已測試的函式與 `books.py` 中的所有函式進行比對
   - 摘要缺少哪些測試覆蓋率

**成功標準**：您能在單一 Copilot 工作階段中無縫結合 filesystem 和 GitHub MCP 資料，並能解釋每個 MCP 伺服器對回應的貢獻。

<details>
<summary>💡 提示（點擊展開）</summary>

**步驟 1：確認 MCP**
```bash
copilot
> /mcp show
# Should show "github" as enabled
# If not, run: /login
```

**步驟 2：建立設定檔**

使用上方[完整設定](#complete-configuration-file)章節的 JSON，儲存為 `~/.copilot/mcp-config.json`。

**步驟 3：需要尋找的資料品質問題**

`data.json` 中的最後一本書是：
```json
{
  "title": "Mysterious Book",
  "author": "",
  "year": 0,
  "read": false
}
```
空白的作者和年份為 0，這就是資料品質問題！

**步驟 5：測試覆蓋率比較**

`test_books.py` 中的測試涵蓋：`add_book`、`mark_as_read`、`remove_book`、`get_unread_books` 和 `find_book_by_title`。`load_books`、`save_books` 和 `list_books` 等函式沒有直接測試。`book_app.py` 中的 CLI 函式和 `utils.py` 中的輔助函式完全沒有測試。

**如果 MCP 無法運作：** 編輯設定檔後重新啟動 Copilot。

</details>

### 加分挑戰：建立自訂 MCP 伺服器

準備好深入了解了嗎？按照[自訂 MCP 伺服器指南](mcp-custom-server.md)，用 Python 建立您自己的 MCP 伺服器，連接任何 API。

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生情況 | 修正方式 |
|---------|--------------|-----|
| 不知道 GitHub MCP 已內建 | 嘗試手動安裝/設定 | GitHub MCP 預設已包含。直接嘗試：「List the recent commits in this repo」 |
| 在錯誤位置尋找設定 | 找不到或無法編輯 MCP 設定 | 設定在 `~/.copilot/mcp-config.json` |
| 設定檔中的 JSON 無效 | MCP 伺服器無法載入 | 使用 `/mcp show` 確認設定；驗證 JSON 語法 |
| 忘記驗證 MCP 伺服器 | 出現「Authentication failed」錯誤 | 部分 MCP 需要單獨驗證，請確認每個伺服器的需求 |

### 疑難排解

**「MCP server not found」** - 確認：
1. npm 套件存在：`npm view @modelcontextprotocol/server-github`
2. 您的設定是有效的 JSON
3. 伺服器名稱與設定相符

使用 `/mcp show` 查看目前的設定。

**「GitHub authentication failed」** - 內建的 GitHub MCP 使用您的 `/login` 憑證。請嘗試：

```bash
copilot
> /login
```

這會重新向 GitHub 驗證。如果問題持續，請確認您的 GitHub 帳號對所存取的程式庫具有必要的權限。

**「MCP server failed to start」** - 手動執行伺服器指令以查看錯誤：
```bash
# Run the server command manually to see errors
npx -y @modelcontextprotocol/server-github
```

**MCP 工具不可用** - 確認伺服器已啟用：
```bash
copilot

> /mcp show
# Check if server is listed and enabled
```

如果伺服器已停用，請參閱下方的[額外 `/mcp` 指令](#-additional-mcp-commands)以了解如何重新啟用。

</details>

---

<details>
<summary>📚 <strong>額外的 <code>/mcp</code> 指令</strong>（點擊展開）</summary>
<a id="-additional-mcp-commands"></a>

除了 `/mcp show` 之外，還有幾個管理 MCP 伺服器的指令：

| 指令 | 功能說明 |
|---------|--------------|
| `/mcp show` | 顯示所有已設定的 MCP 伺服器及其狀態 |
| `/mcp add` | 互動式新增伺服器設定 |
| `/mcp edit <server-name>` | 編輯現有的伺服器設定 |
| `/mcp enable <server-name>` | 啟用已停用的伺服器 |
| `/mcp disable <server-name>` | 暫時停用伺服器 |
| `/mcp delete <server-name>` | 永久移除伺服器 |

在本課程大部分情況下，`/mcp show` 就足夠了。隨著您管理越來越多的伺服器，其他指令也會變得實用。

</details>

---

# 總結

## 🔑 重點摘要

1. **MCP** 將 Copilot 連接到外部服務（GitHub、檔案系統、文件）
2. **GitHub MCP 已內建** - 無需設定，只需 `/login`
3. **Filesystem 和 Context7** 透過 `~/.copilot/mcp-config.json` 設定
4. **多伺服器工作流程**在單一工作階段中結合來自多個來源的資料
5. **使用 `/mcp show` 確認伺服器狀態**（還有更多管理指令可供使用）
6. **自訂伺服器**讓您能連接任何 API（選讀，附錄指南中有說明）

> 📋 **快速參考**：請參閱 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)，取得完整的指令和快捷鍵清單。

---

## ➡️ 接下來

您現在擁有了所有基礎：模式、情境、工作流程、代理程式、技能和 MCP。是時候將它們整合在一起了。

在**[第 07 章：整合所有知識](../07-putting-it-together/README.md)**中，您將學習：

- 在統一工作流程中結合代理程式、技能和 MCP
- 從構想到合併 PR 的完整功能開發
- 使用鉤子（hooks）進行自動化
- 團隊環境的最佳實踐

---

**[← 返回第 05 章](../05-skills/README.md)** | **[繼續前往第 07 章 →](../07-putting-it-together/README.md)**
