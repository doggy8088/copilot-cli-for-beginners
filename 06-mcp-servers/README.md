![Chapter 06: MCP Servers](images/chapter-header.png)

> **如果 Copilot 能直接從終端機讀取你的 GitHub 問題、檢查資料庫、建立 PR……會怎樣？**

到目前為止，Copilot 只能處理你直接提供的內容：你用 `@` 引用的檔案、對話記錄，以及它自己的訓練資料。但如果它能主動連結到你的 GitHub 儲存庫、瀏覽你的專案檔案，或查詢某個函式庫的最新文件呢？

這正是 MCP（模型情境協定，Model Context Protocol）要解決的事。它是一種讓 Copilot 連接外部服務、取得即時真實資料的方式。Copilot 連接的每個服務都稱為一個「MCP 伺服器」。本章你會設定幾個這樣的連線，看看它們如何大幅提升 Copilot 的實用性。

> 💡 **已經熟悉 MCP？** [直接跳到快速開始](#-use-the-built-in-github-mcp) 確認功能正常並開始設定伺服器。

## 🎯 學習目標

完成本章後，你將能夠：

- 了解 MCP 是什麼，以及它為什麼重要
- 使用 `/mcp` 指令管理 MCP 伺服器
- 設定 GitHub、檔案系統與文件的 MCP 伺服器
- 在書籍應用程式專案中使用 MCP 強化的工作流程
- 知道何時、如何打造自訂 MCP 伺服器（選用）

> ⏱️ **預估時間**：約 50 分鐘（閱讀 15 分鐘 + 實作 35 分鐘）

---

## 🧩 真實世界類比：瀏覽器擴充功能

<img src="images/browser-extensions-analogy.png" alt="MCP Servers are like Browser Extensions" width="800"/>

把 MCP 伺服器想像成瀏覽器的擴充功能。你的瀏覽器本身能顯示網頁，但擴充功能能讓它連接更多服務：

| 瀏覽器擴充功能 | 連接對象 | MCP 對應 |
|-------------------|---------------------|----------------|
| 密碼管理器 | 你的密碼保險庫 | **GitHub MCP** → 你的儲存庫、問題、PR |
| Grammarly | 寫作分析服務 | **Context7 MCP** → 函式庫文件 |
| 檔案管理器 | 雲端儲存空間 | **Filesystem MCP** → 本地專案檔案 |

沒有擴充功能，瀏覽器還是有用；有了它們，功能大幅提升。MCP 伺服器對 Copilot 也一樣——它們讓 Copilot 連接到真實、即時的資料來源，能讀取你的 GitHub 問題、探索檔案系統、取得最新文件等等。

***MCP 伺服器讓 Copilot 連接外部世界：GitHub、儲存庫、文件等***

> 💡 **關鍵洞見**：沒有 MCP，Copilot 只能看到你用 `@` 明確分享的檔案。有了 MCP，它能主動探索專案、檢查 GitHub 儲存庫、查詢文件，全部自動完成。

---

<img src="images/quick-start-mcp.png" alt="Power cable connecting with bright electrical spark surrounded by floating tech icons representing MCP server connections" width="800"/>

# 快速開始：30 秒體驗 MCP

## 立即體驗內建的 GitHub MCP 伺服器
在還沒設定任何東西前，先來看看 MCP 的威力。
GitHub MCP 伺服器預設已啟用。請嘗試：

```bash
copilot
> List the recent commits in this repository
```

如果 Copilot 回傳了真實的提交資料，你已經親眼見證 MCP 在運作。這就是 GitHub MCP 伺服器代表你連線到 GitHub。但 GitHub 只是其中「一個」伺服器。本章會教你如何加入更多（檔案系統存取、即時文件等），讓 Copilot 功能更強大。

---

## `/mcp show` 指令

使用 `/mcp show` 查看目前已設定、啟用的 MCP 伺服器：

```bash
copilot

> /mcp show

MCP Servers:
✓ github (enabled) - GitHub integration
✓ filesystem (enabled) - File system access
```

> 💡 **只看到 GitHub 伺服器？** 這很正常！如果你還沒新增其他 MCP 伺服器，目前只會列出 GitHub。下一節你會學會如何加入更多。

> 📚 **想看所有 `/mcp` 指令？** 還有新增、編輯、啟用、刪除伺服器等指令。請見本章結尾的 [完整指令參考](#-additional-mcp-commands)。

<details>
<summary>🎬 實際操作影片</summary>

![MCP Status Demo](images/mcp-status-demo.gif)

*示範輸出會有所不同。你的模型、工具與回應可能和這裡展示的不一樣。*

</details>

---

## MCP 帶來哪些改變？

以下是 MCP 實際上的差異：

**沒有 MCP：**
```bash
> What's in GitHub issue #42?

"I don't have access to GitHub. You'll need to copy and paste the issue content."
```

**有 MCP：**
```bash
> What's in GitHub issue #42 of this repository?

Issue #42: Login fails with special characters
Status: Open
Labels: bug, priority-high
Description: Users report that passwords containing...
```

MCP 讓 Copilot 能夠感知你的實際開發環境。

> 📚 **官方文件**：[關於 MCP](https://docs.github.com/copilot/concepts/context/mcp) 深入了解 MCP 如何與 GitHub Copilot 搭配運作。

---

# 設定 MCP 伺服器

<img src="images/configuring-mcp-servers.png" alt="Hands adjusting knobs and sliders on a professional audio mixing board representing MCP server configuration" width="800"/>

現在你已經見識過 MCP 的威力，接下來要設定更多伺服器。本節會介紹設定檔格式，以及如何新增伺服器。

---

## MCP 設定檔

MCP 伺服器設定於 `~/.copilot/mcp-config.json`（使用者層級，所有專案適用）或 `.vscode/mcp.json`（專案層級，僅當前工作區適用）。

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

*大多數 MCP 伺服器以 npm 套件形式發佈，透過 `npx` 執行。*

<details>
<summary>💡 <strong>不熟 JSON？</strong> 點此了解各欄位意義</summary>

| 欄位 | 意義 |
|-------|---------------|
| `"mcpServers"` | 所有 MCP 伺服器設定的容器 |
| `"server-name"` | 你自訂的名稱（例如 "github"、"filesystem"） |
| `"type": "local"` | 伺服器在本機執行 |
| `"command": "npx"` | 執行的程式（npx 執行 npm 套件） |
| `"args": [...]` | 傳給指令的參數 |
| `"tools": ["*"]` | 允許此伺服器的所有工具 |

**重要 JSON 規則：**
- 字串請用雙引號 `"`（不能用單引號）
- 最後一項後面不能有逗號
- 檔案必須是有效的 JSON（不確定時可用 [JSON validator](https://jsonlint.com/) 檢查）

</details>

---

## 新增 MCP 伺服器

GitHub MCP 伺服器是內建的，無需設定。以下是你可以額外加入的伺服器。**請依興趣挑選，或依序練習。**

| 我想要…… | 跳到 |
|---|---|
| 讓 Copilot 瀏覽我的專案檔案 | [Filesystem Server](#filesystem-server) |
| 取得最新函式庫文件 | [Context7 Server](#context7-server-documentation) |
| 探索進階功能（自訂伺服器、web_fetch） | [Beyond the Basics](#beyond-the-basics) |

<details>
<summary><strong>Filesystem Server</strong> - 讓 Copilot 探索你的專案檔案</summary>
<a id="filesystem-server"></a>

### Filesystem Server

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

> 💡 **`.` 路徑**：`.` 代表「目前目錄」。Copilot 可存取你啟動時所在目錄的相對檔案。在 Codespace 中，這是你的工作區根目錄。你也可以用絕對路徑（如 `/workspaces/copilot-cli-for-beginners`）來指定。

將此內容加入 `~/.copilot/mcp-config.json` 並重啟 Copilot。

</details>

<details>
<summary><strong>Context7 Server</strong> - 取得最新函式庫文件</summary>
<a id="context7-server-documentation"></a>

### Context7 Server（文件）

Context7 讓 Copilot 能存取熱門框架與函式庫的最新官方文件。不再依賴可能過時的訓練資料，Copilot 會抓取實際的最新文件。

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

- ✅ **不需 API 金鑰**
- ✅ **不需註冊帳號**
- ✅ **你的程式碼不會離開本機**

將此內容加入 `~/.copilot/mcp-config.json` 並重啟 Copilot。

</details>

<details>
<summary><strong>進階應用</strong> - 自訂伺服器與網頁存取（選用）</summary>
<a id="beyond-the-basics"></a>

這些是進階選項，適合你已熟悉前述核心伺服器後再嘗試。

### Microsoft Learn MCP Server

前述的 MCP 伺服器（filesystem、Context7）都在本機執行。但 MCP 伺服器也能遠端執行，只要 Copilot CLI 指向一個 URL 即可，無需 `npx`、`python`、本地程序或安裝依賴。

[Microsoft Learn MCP Server](https://github.com/microsoftdocs/mcp) 就是個好例子。它讓 Copilot CLI 直接存取官方 Microsoft 文件（Azure、Microsoft Foundry 及其他 AI 主題、.NET、Microsoft 365 等），可搜尋文件、抓取完整頁面、查找官方程式碼範例，不再只靠模型訓練資料。

- ✅ **不需 API 金鑰**
- ✅ **不需註冊帳號**
- ✅ **不需本地安裝**

**用 `/plugin install` 一鍵安裝：**

不用手動編輯 JSON 設定檔，只需一行指令：

```bash
copilot

> /plugin install microsoftdocs/mcp
```

這會自動加入伺服器及相關 agent 技能。安裝的技能包括：

- **microsoft-docs**：概念、教學、事實查詢
- **microsoft-code-reference**：API 查詢、程式碼範例、疑難排解
- **microsoft-skill-creator**：產生 Microsoft 技術自訂技能的元技能

**使用方式：**
```bash
copilot

> What's the recommended way to deploy a Python app to Azure App Service? Search Microsoft Learn.
```

📚 進一步了解：[Microsoft Learn MCP Server 簡介](https://learn.microsoft.com/training/support/mcp-get-started)

### 使用 `web_fetch` 取得網頁內容

Copilot CLI 內建 `web_fetch` 工具，可從任意 URL 取得內容。這對於拉取 README、API 文件或發行說明很有用，無需離開終端機，也不用 MCP 伺服器。

你可以在 `~/.copilot/config.json`（Copilot 一般設定，與 `~/.copilot/mcp-config.json` MCP 伺服器設定分開）控制哪些 URL 可存取。

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

### 建立自訂 MCP 伺服器

想讓 Copilot 連接你的自家 API、資料庫或內部工具？你可以用 Python 建立自訂 MCP 伺服器。這完全是選用功能，因為預設伺服器（GitHub、filesystem、Context7）已涵蓋大多數需求。

📖 詳見 [自訂 MCP 伺服器指南](mcp-custom-server.md)，以書籍應用程式為例完整說明。

📚 更多背景知識，參見 [MCP for Beginners 課程](https://github.com/microsoft/mcp-for-beginners)。

</details>

<a id="complete-configuration-file"></a>

### 完整設定檔範例

以下是一份同時包含 filesystem 與 Context7 伺服器的 `mcp-config.json` 範例：

> 💡 **注意：** GitHub MCP 是內建的，不需要加入設定檔。

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

將此檔案儲存為 `~/.copilot/mcp-config.json`（全域適用）或 `.vscode/mcp.json`（專案專用）。

---

# 使用 MCP 伺服器

現在你已設定好 MCP 伺服器，來看看它們能做些什麼。

<img src="images/using-mcp-servers.png" alt="Using MCP Servers - Hub-and-spoke diagram showing a Developer CLI connected to GitHub, Filesystem, Context7, and Custom/Web Fetch servers" width="800" />

---

## 伺服器使用範例

**挑一個伺服器探索，或依序練習。**

| 我想嘗試…… | 跳到 |
|---|---|
| GitHub 儲存庫、問題、PR | [GitHub Server](#github-server-built-in) |
| 瀏覽專案檔案 | [Filesystem Server Usage](#filesystem-server-usage) |
| 查詢函式庫文件 | [Context7 Server Usage](#context7-server-usage) |
| 自訂伺服器、Microsoft Learn MCP 與 web_fetch 用法 | [Beyond the Basics Usage](#beyond-the-basics-usage) |

<details>
<summary><strong>GitHub Server（內建）</strong> - 存取儲存庫、問題、PR 等</summary>
<a id="github-server-built-in"></a>

### GitHub Server（內建）

GitHub MCP 伺服器是**內建**的。只要你已登入 Copilot（初次設定時已完成），就能直接用，無需額外設定！

> 💡 **無法使用？** 執行 `/login` 重新驗證 GitHub。

<details>
<summary><strong>Dev Containers 認證說明</strong></summary>

- **GitHub Codespaces**（推薦）：認證自動完成。`gh` CLI 會繼承你的 Codespace token，無需額外動作。
- **本地 dev container（Docker）**：容器啟動後執行 `gh auth login`，再重啟 Copilot。

**認證疑難排解：**
```bash
# 檢查是否已認證
gh auth status

# 若尚未登入，請登入
gh auth login

# 確認 GitHub MCP 已連線
copilot
> /mcp show
```

</details>

| 功能 | 範例 |
|---------|----------|
| **儲存庫資訊** | 查看提交、分支、貢獻者 |
| **問題** | 列出、新增、搜尋、留言 |
| **拉取請求** | 查看 PR、差異、新增 PR、檢查狀態 |
| **程式碼搜尋** | 跨儲存庫搜尋程式碼 |
| **Actions** | 查詢 workflow 執行與狀態 |

```bash
copilot

# 查看本儲存庫近期活動
> List the last 5 commits in this repository

Recent commits:
1. abc1234 - Update chapter 05 skills examples (2 days ago)
2. def5678 - Add book app test fixtures (3 days ago)
3. ghi9012 - Fix typo in chapter 03 README (4 days ago)
...

# 探索儲存庫結構
> What branches exist in this repository?

Branches:
- main (default)
- chapter6 (current)

# 跨儲存庫搜尋程式碼模式
> Search this repository for files that import pytest

Found 1 file:
- samples/book-app-project/tests/test_books.py
```

> 💡 **在自己的 fork 上操作？** 如果你 fork 了本課程儲存庫，也可嘗試建立問題、拉取請求等寫入操作。下方練習會實際操作。

> ⚠️ **沒看到結果？** GitHub MCP 操作的是儲存庫的遠端（github.com），不只本地檔案。請確認你的 repo 有 remote：執行 `git remote -v` 檢查。

</details>

<details>
<summary><strong>Filesystem Server</strong> - 瀏覽與分析專案檔案</summary>
<a id="filesystem-server-usage"></a>

### Filesystem Server

設定完成後，filesystem MCP 會自動提供 Copilot 可用的工具：

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
<summary><strong>Context7 Server</strong> - 查詢函式庫文件</summary>
<a id="context7-server-usage"></a>

### Context7 Server

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

# Copilot 現在已知官方 pytest 實踐方式
# 並能應用於 samples/book-app-project/tests/test_books.py
```

</details>

<details>
<summary><strong>進階應用</strong> - 自訂伺服器與 web_fetch 用法</summary>
<a id="beyond-the-basics-usage"></a>

### 進階應用

**自訂 MCP 伺服器**：如果你依 [自訂 MCP 伺服器指南](mcp-custom-server.md) 建立了 book-lookup 伺服器，可直接查詢你的書籍收藏：

```bash
copilot

> Look up information about "1984" using the book lookup server. Search for books by George Orwell
```

**Microsoft Learn MCP**：如果你安裝了 [Microsoft Learn MCP server](#microsoft-learn-mcp-server)，可直接查詢官方 Microsoft 文件：

```bash
copilot

> How do I configure managed identity for an Azure Function? Search Microsoft Learn.
```

**Web Fetch**：用內建 `web_fetch` 工具從任意 URL 取得內容：

```bash
copilot

> Fetch and summarize the README from https://github.com/facebook/react
```

</details>

---

## 多伺服器工作流程

以下工作流程展示為什麼開發者會說「用了就回不去了」。每個範例都在同一個 session 結合多個 MCP 伺服器。

<img src="images/issue-to-pr-workflow.png" alt="Issue to PR Workflow using MCP - Shows the complete flow from getting a GitHub issue through creating a pull request" width="800"/>

*完整 MCP 工作流程：GitHub MCP 取得 repo 資料、Filesystem MCP 找程式碼、Context7 MCP 查詢最佳實踐、Copilot 負責分析*

下方每個範例都是獨立的。**挑一個你有興趣的，或全部閱讀。**

| 我想看…… | 跳到 |
|---|---|
| 多個伺服器協同作業 | [Multi-Server Exploration](#multi-server-exploration) |
| 一次 session 從 issue 到 PR | [Issue-to-PR Workflow](#issue-to-pr-workflow) |
| 快速專案健康檢查 | [Health Dashboard](#health-dashboard) |

<details>
<summary><strong>多伺服器探索</strong> - 一次 session 結合 filesystem、GitHub、Context7</summary>
<a id="multi-server-exploration"></a>

#### 使用多個 MCP 伺服器探索書籍應用程式

```bash
copilot

# 步驟 1：用 filesystem MCP 探索書籍應用程式
> List all Python files in samples/book-app-project/ and summarize
> what each file does

Found 3 Python files:
- book_app.py: CLI entry point with command routing (list, add, remove, find)
- books.py: BookCollection class with data persistence via JSON
- utils.py: Helper functions for user input and display

# 步驟 2：用 GitHub MCP 檢查近期變更
> What were the last 3 commits that touched files in samples/book-app-project/?

Recent commits affecting book app:
1. abc1234 - Add test fixtures for BookCollection (2 days ago)
2. def5678 - Add find_by_author method (5 days ago)
3. ghi9012 - Initial book app setup (1 week ago)

# 步驟 3：用 Context7 MCP 查詢最佳實踐
> What are Python best practices for JSON data persistence?

From Python Documentation:
- Use context managers (with statements) for file I/O
- Handle JSONDecodeError for corrupted files
- Use dataclasses for structured data
- Consider atomic writes to prevent data corruption

# 步驟 4：綜合建議
> Based on the book app code and these best practices,
> what improvements would you suggest?

Suggestions:
1. Add input validation in add_book() for empty strings and invalid years
2. Consider atomic writes in save_books() to prevent data corruption
3. Add type hints to utils.py functions (get_user_choice, get_book_details)
```

<details>
<summary>🎬 MCP 工作流程實錄</summary>

![MCP Workflow Demo](images/mcp-workflow-demo.gif)

*示範輸出會有所不同。你的模型、工具與回應可能和這裡展示的不一樣。*

</details>

**成果**：程式碼探索 → 歷史檢視 → 最佳實踐查詢 → 改進計畫。**全部在一個終端 session，三個 MCP 伺服器協作完成。**

</details>

<details>
<summary><strong>Issue-to-PR 工作流程</strong> - 從 GitHub 問題到拉取請求，全程不離開終端機</summary>
<a id="issue-to-pr-workflow"></a>

#### Issue-to-PR 工作流程（在你自己的 repo）

這在你有寫入權限的 fork 或儲存庫上效果最佳：

> 💡 **現在無法實作也沒關係。** 如果你是唯讀 clone，之後會在作業練習。現在先閱讀流程即可。

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

**零複製貼上。零情境切換。單一終端 session 完成。**

</details>

<details>
<summary><strong>健康儀表板</strong> - 多伺服器快速檢查專案健康狀態</summary>
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

**成果**：多個資料來源數秒內整合。手動操作需 grep、行數統計、查 git log、瀏覽測試檔，至少 15 分鐘以上。

</details>

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

**🎉 你已掌握重點！** 你了解 MCP，會設定伺服器，也看過實際工作流程。現在輪到你親自操作。

---

## ▶️ 自己動手試試

現在換你來練習！完成下列練習，體驗如何在書籍應用程式專案中使用 MCP 伺服器。

### 練習 1：檢查你的 MCP 狀態

先看看有哪些 MCP 伺服器可用：

```bash
copilot

> /mcp show
```

你應該會看到 GitHub 伺服器已啟用。如果沒有，請執行 `/login` 進行認證。

---

### 練習 2：用 Filesystem MCP 探索書籍應用程式

如果你已經設定好 filesystem server，請用它來探索書籍應用程式：

```bash
copilot

> How many Python files are in samples/book-app-project/?
> What functions are defined in each file?
```

**預期結果**：Copilot 會列出 `book_app.py`、`books.py` 和 `utils.py` 及其各自的函式。

> 💡 **還沒設定 filesystem MCP？** 請參考上方 [完整設定檔](#complete-configuration-file) 章節建立設定檔，然後重新啟動 Copilot。

---

### 練習 3：用 GitHub MCP 查詢版本庫歷史

使用內建的 GitHub MCP 來探索本課程的版本庫：

```bash
copilot

> List the last 5 commits in this repository

> What branches exist in this repository?
```

**預期結果**：Copilot 會顯示 GitHub 遠端的近期提交訊息與分支名稱。

> ⚠️ **在 Codespace 中嗎？** 這會自動運作，認證會自動繼承。如果你是在本機複製的版本庫，請確認 `gh auth status` 顯示你已登入。

---

### 練習 4：結合多個 MCP 伺服器

現在在同一個 session 中結合 filesystem 和 GitHub MCP：

```bash
copilot

> Read samples/book-app-project/data.json and tell me what books are
> in the collection. Then check the recent commits to see when this
> file was last modified.
```

**預期結果**：Copilot 會讀取 JSON 檔案（filesystem MCP），列出 5 本書，包括 "The Hobbit"、"1984"、"Dune"、"To Kill a Mockingbird" 和 "Mysterious Book"，然後查詢 GitHub 取得提交歷史。

**自我檢查**：當你能解釋為什麼「查詢我的版本庫提交歷史」比手動執行 `git log` 並將輸出貼到提示詞中更好時，表示你已理解 MCP。

---

## 📝 作業

### 主要挑戰：書籍應用程式 MCP 探索

練習在書籍應用程式專案中同時使用多個 MCP 伺服器。請在同一個 Copilot session 內完成下列步驟：

1. **確認 MCP 運作正常**：執行 `/mcp show` 並確認至少有啟用 GitHub server
2. **設定 filesystem MCP**（如果尚未設定）：建立 `~/.copilot/mcp-config.json`，內容為 filesystem server 設定
3. **探索程式碼**：請 Copilot 使用 filesystem server 來：
   - 列出 `samples/book-app-project/books.py` 中所有函式
   - 檢查 `samples/book-app-project/utils.py` 中哪些函式缺少型別標註
   - 讀取 `samples/book-app-project/data.json` 並指出任何資料品質問題（提示：檢查最後一筆資料）
4. **檢查版本庫活動**：請 Copilot 使用 GitHub MCP 來：
   - 列出最近有異動 `samples/book-app-project/` 目錄檔案的提交
   - 檢查是否有任何未關閉的 issue 或 pull request
5. **結合伺服器**：在同一個提示中請 Copilot：
   - 讀取 `samples/book-app-project/tests/test_books.py` 測試檔案
   - 比較測試過的函式與 `books.py` 中所有函式
   - 摘要說明哪些測試覆蓋尚未完成

**成功標準**：你能在同一個 Copilot session 中無縫結合 filesystem 與 GitHub MCP 的資料，並能解釋每個 MCP server 在回應中扮演的角色。

<details>
<summary>💡 提示（點擊展開）</summary>

**步驟 1：確認 MCP**
```bash
copilot
> /mcp show
# 應該會顯示 "github" 已啟用
# 如果沒有，請執行：/login
```

**步驟 2：建立設定檔**

請使用上方 [完整設定檔](#complete-configuration-file) 章節的 JSON，並將其儲存為 `~/.copilot/mcp-config.json`。

**步驟 3：資料品質問題檢查**

`data.json` 最後一本書是：
```json
{
  "title": "Mysterious Book",
  "author": "",
  "year": 0,
  "read": false
}
```
作者為空字串且年份為 0。這就是資料品質問題！

**步驟 5：測試覆蓋比較**

`test_books.py` 測試了：`add_book`、`mark_as_read`、`remove_book`、`get_unread_books` 和 `find_book_by_title`。像是 `load_books`、`save_books`、`list_books` 沒有直接測試。`book_app.py` 的 CLI 函式和 `utils.py` 的輔助函式則完全沒有測試。

**如果 MCP 沒有運作**：編輯設定檔後請重新啟動 Copilot。

</details>

### 進階挑戰：打造自訂 MCP 伺服器

想更進一步嗎？請參考 [自訂 MCP 伺服器指南](mcp-custom-server.md)，用 Python 建立一個可連接任意 API 的 MCP 伺服器。

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 會發生什麼 | 解法 |
|------|------------|------|
| 不知道 GitHub MCP 是內建的 | 嘗試手動安裝／設定 | GitHub MCP 預設已包含。直接試：「列出這個 repo 的近期提交」 |
| 設定檔放錯位置 | 找不到或無法編輯 MCP 設定 | 使用者層級設定在 `~/.copilot/mcp-config.json`，專案層級在 `.vscode/mcp.json` |
| 設定檔 JSON 無效 | MCP server 載入失敗 | 用 `/mcp show` 檢查設定，並驗證 JSON 語法 |
| 忘記 MCP server 認證 | 出現「認證失敗」錯誤 | 有些 MCP 需要額外認證。請檢查各 server 的需求 |

### 疑難排解

**「找不到 MCP server」** - 請檢查：
1. npm 套件存在：`npm view @modelcontextprotocol/server-github`
2. 你的設定檔是有效的 JSON
3. server 名稱與設定一致

用 `/mcp show` 查看目前設定。

**「GitHub 認證失敗」** - 內建 GitHub MCP 會用你的 `/login` 認證。請嘗試：

```bash
copilot
> /login
```

這會重新認證你的 GitHub。如果問題持續，請確認你的 GitHub 帳號對該版本庫有必要權限。

**「MCP server 啟動失敗」** - 請檢查 server log：
```bash
# 手動執行 server 指令以檢查錯誤
npx -y @modelcontextprotocol/server-github
```

**MCP 工具不可用** - 請確認 server 已啟用：
```bash
copilot

> /mcp show
# 檢查 server 是否已列出且啟用
```

如果 server 被停用，請參考下方 [更多 `/mcp` 指令](#-additional-mcp-commands) 以重新啟用。

</details>

---

<details>
<summary>📚 <strong>更多 <code>/mcp</code> 指令</strong>（點擊展開）</summary>
<a id="-additional-mcp-commands"></a>

除了 `/mcp show`，還有其他指令可用來管理 MCP server：

| 指令 | 功能說明 |
|------|----------|
| `/mcp show` | 顯示所有已設定的 MCP server 及其狀態 |
| `/mcp add` | 互動式新增新 server |
| `/mcp edit <server-name>` | 編輯現有 server 設定 |
| `/mcp enable <server-name>` | 啟用已停用的 server |
| `/mcp disable <server-name>` | 暫時停用 server |
| `/mcp delete <server-name>` | 永久移除 server |

本課程大多時候只需 `/mcp show`。其他指令適合日後管理多個 server 時使用。

</details>

---

# 摘要

## 🔑 重點整理

1. **MCP** 讓 Copilot 能連接外部服務（GitHub、檔案系統、文件）
2. **GitHub MCP 內建** — 無需設定，只要 `/login`
3. **Filesystem 與 Context7** 透過 `~/.copilot/mcp-config.json` 設定
4. **多伺服器工作流程** 可在同一 session 結合多來源資料
5. **用 `/mcp show` 檢查 server 狀態**（還有其他管理指令）
6. **自訂 server** 可連接任何 API（選用，詳見附錄指南）

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 接下來

你現在已經具備所有基礎：模式、情境、工作流程、Agent、Skill 以及 MCP。是時候把它們全部結合起來了。

在 **[第 07 章：整合應用](../07-putting-it-together/README.md)**，你將學到：

- 結合 Agent、Skill 與 MCP，打造整合式工作流程
- 從想法到合併 PR 的完整功能開發
- 用 hook 自動化
- 團隊環境最佳實踐

---

**[← 回到第 05 章](../05-skills/README.md)** | **[繼續前往第 07 章 →](../07-putting-it-together/README.md)**
