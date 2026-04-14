![Chapter 06: MCP Servers](images/chapter-header.png)

> **如果 Copilot 能直接從終端機讀取你的 GitHub issue、檢查資料庫、建立 PR……會怎樣？**

到目前為止，Copilot 只能處理你直接給它的東西：你用 `@` 指定的檔案、對話記錄，以及它自己的訓練資料。但如果它能主動連到 GitHub 儲存庫、瀏覽你的專案檔案，或查詢某個函式庫的最新文件呢？

這就是 MCP（模型情境協定）的功能。它是一種讓 Copilot 連接外部服務的方式，讓它能存取即時、真實世界的資料。Copilot 連接的每個服務都稱為一個「MCP 伺服器」。本章你將設定幾個這樣的連線，看看它們如何大幅提升 Copilot 的實用性。

> 💡 **已經熟悉 MCP？** [直接跳到快速開始](#-use-the-built-in-github-mcp) 確認功能正常並開始設定伺服器。

## 🎯 學習目標

完成本章後，你將能夠：

- 了解 MCP 是什麼，以及它的重要性
- 使用 `/mcp` 指令管理 MCP 伺服器
- 設定 GitHub、檔案系統與文件的 MCP 伺服器
- 在書籍應用程式專案中運用 MCP 強化的工作流程
- 知道何時以及如何打造自訂 MCP 伺服器（選用）

> ⏱️ **預估時間**：約 50 分鐘（閱讀 15 分鐘 + 實作 35 分鐘）

---

## 🧩 真實世界比喻：瀏覽器擴充功能

<img src="images/browser-extensions-analogy.png" alt="MCP Servers are like Browser Extensions" width="800"/>

把 MCP 伺服器想像成瀏覽器的擴充功能。你的瀏覽器本身能顯示網頁，但擴充功能能讓它連接更多服務：

| 瀏覽器擴充功能 | 連接對象 | MCP 對應 |
|-------------------|---------------------|----------------|
| 密碼管理器 | 你的密碼保險箱 | **GitHub MCP** → 你的 repo、issue、PR |
| Grammarly | 寫作分析服務 | **Context7 MCP** → 函式庫文件 |
| 檔案管理器 | 雲端儲存空間 | **Filesystem MCP** → 本機專案檔案 |

沒有擴充功能，瀏覽器還是有用，但加上它們就變成超強工具。MCP 伺服器對 Copilot 也是如此。它們讓 Copilot 連接到真實、即時的資料來源，能讀取你的 GitHub issue、瀏覽檔案系統、抓取最新文件，還有更多。

***MCP 伺服器讓 Copilot 連接外部世界：GitHub、儲存庫、文件等等***

> 💡 **關鍵洞見**：沒有 MCP，Copilot 只能看到你用 `@` 明確分享的檔案。有了 MCP，它能主動探索專案、檢查 GitHub repo、查詢文件，全部自動完成。

---

<img src="images/quick-start-mcp.png" alt="Power cable connecting with bright electrical spark surrounded by floating tech icons representing MCP server connections" width="800"/>

# 快速開始：30 秒體驗 MCP

## 立即體驗內建的 GitHub MCP 伺服器
讓我們馬上來看看 MCP 的威力，還不用設定任何東西。
GitHub MCP 伺服器預設就有。試試看：

```bash
copilot
> List the recent commits in this repository
```

如果 Copilot 回傳了真實的 commit 資料，你已經親眼見識 MCP 的效果。這就是 GitHub MCP 伺服器代表你連到 GitHub。但 GitHub 只是其中 *一個* 伺服器。本章會教你如何加入更多（檔案系統存取、即時文件等），讓 Copilot 能做的事更多。

---

## `/mcp show` 指令

使用 `/mcp show` 查看目前有哪些 MCP 伺服器已設定，以及它們是否啟用：

```bash
copilot

> /mcp show

MCP Servers:
✓ github (enabled) - GitHub integration
✓ filesystem (enabled) - File system access
```

> 💡 **只看到 GitHub 伺服器？** 這是正常的！如果你還沒加其他 MCP 伺服器，預設只有 GitHub。下一節你會學會如何新增。

> 📚 **想看所有 MCP 管理指令？** 你可以在聊天裡用 `/mcp` 斜線指令管理伺服器，或直接在終端機用 `copilot mcp`。完整指令請見本章最後的 [指令參考](#-additional-mcp-commands)。

<details>
<summary>🎬 實際操作示範！</summary>

![MCP Status Demo](images/mcp-status-demo.gif)

*示範輸出會因模型、工具、回應而異。你的結果可能不同。*

</details>

---

## MCP 帶來哪些改變？

以下是 MCP 實際帶來的差異：

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

MCP 讓 Copilot 能感知你的實際開發環境。

> 📚 **官方文件**：[關於 MCP](https://docs.github.com/copilot/concepts/context/mcp) 深入了解 MCP 如何與 GitHub Copilot 配合。

---

# 設定 MCP 伺服器

<img src="images/configuring-mcp-servers.png" alt="Hands adjusting knobs and sliders on a professional audio mixing board representing MCP server configuration" width="800"/>

既然你已經見識 MCP 的效果，現在來設定更多伺服器。本節會介紹設定檔格式，以及如何新增伺服器。

---

## MCP 設定檔

MCP 伺服器可在 `~/.copilot/mcp-config.json`（使用者層級，所有專案適用）或 `.mcp.json`（專案層級，放在專案根目錄）中設定。

> ⚠️ **注意**：`.vscode/mcp.json` 已不再支援作為 MCP 設定來源。如果你有舊的 `.vscode/mcp.json`，請移到專案根目錄的 `.mcp.json`。CLI 偵測到舊檔案時會顯示遷移提示。

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

*大多數 MCP 伺服器都是以 npm 套件形式發佈，並透過 `npx` 執行。*

<details>
<summary>💡 <strong>不熟 JSON？</strong> 點此了解各欄位意義</summary>

| 欄位 | 意義 |
|-------|---------------|
| `"mcpServers"` | 所有 MCP 伺服器設定的容器 |
| `"server-name"` | 你自訂的名稱（如 "github"、"filesystem"） |
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

GitHub MCP 伺服器是內建的，不需額外設定。以下是你可以新增的其他伺服器。**選你有興趣的，或依序練習。**

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

> 💡 **`.` 路徑**：`.` 代表「目前目錄」。Copilot 可存取你啟動時所在目錄的檔案。在 Codespace 裡，這就是你的 workspace 根目錄。你也可以用絕對路徑（如 `/workspaces/copilot-cli-for-beginners`）指定。

將這段加入 `~/.copilot/mcp-config.json`，然後重啟 Copilot。

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
- ✅ **你的程式碼只在本機**

將這段加入 `~/.copilot/mcp-config.json`，然後重啟 Copilot。

</details>

<details>
<summary><strong>Beyond the Basics</strong> - 進階：自訂伺服器與網頁存取（選用）</summary>
<a id="beyond-the-basics"></a>

這些是進階選項，適合你已熟悉上面核心伺服器後再嘗試。

### Microsoft Learn MCP Server

前述所有 MCP 伺服器（filesystem、Context7）都是在本機執行。但 MCP 伺服器也能遠端執行，只要 Copilot CLI 指向一個 URL，其他都自動搞定。不需 `npx`、不需 python、不需本機安裝任何相依。

[Microsoft Learn MCP Server](https://github.com/microsoftdocs/mcp) 就是好例子。它讓 Copilot CLI 直接存取官方 Microsoft 文件（Azure、Microsoft Foundry 與其他 AI 主題、.NET、Microsoft 365 等），能搜尋文件、抓取完整頁面、查找官方程式碼範例，不再只靠模型訓練資料。

- ✅ **不需 API 金鑰** 
- ✅ **不需註冊帳號** 
- ✅ **不需本機安裝**

**用 `/plugin install` 一鍵安裝：**

不用手動編輯 JSON 設定檔，只要一行指令：

```bash
copilot

> /plugin install microsoftdocs/mcp
```

這會自動加入伺服器及相關 agent 技能。安裝的技能包含：

- **microsoft-docs**：概念、教學、事實查詢
- **microsoft-code-reference**：API 查詢、程式碼範例、疑難排解
- **microsoft-skill-creator**：產生 Microsoft 技術自訂技能的 meta-skill

**用法：**
```bash
copilot

> What's the recommended way to deploy a Python app to Azure App Service? Search Microsoft Learn.
```

📚 進一步了解：[Microsoft Learn MCP Server 簡介](https://learn.microsoft.com/training/support/mcp-get-started)

### 用 `web_fetch` 存取網頁

Copilot CLI 內建 `web_fetch` 工具，可抓取任意 URL 的內容。這對於拉取 README、API 文件或發行說明很方便，無需離開終端機。不需 MCP 伺服器。

你可在 `~/.copilot/config.json`（Copilot 一般設定，與 `~/.copilot/mcp-config.json` 分開）控制哪些 URL 可存取。

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

**用法：**
```bash
copilot

> Fetch and summarize the README from https://github.com/facebook/react
```

### 建立自訂 MCP 伺服器

想讓 Copilot 連接你自己的 API、資料庫或內部工具嗎？你可以用 Python 打造自訂 MCP 伺服器。這完全選用，因為預設的伺服器（GitHub、filesystem、Context7）已涵蓋大多數需求。

📖 參見 [自訂 MCP 伺服器指南](mcp-custom-server.md)，以書籍應用程式為例完整教學。

📚 更多背景知識，參見 [MCP for Beginners 課程](https://github.com/microsoft/mcp-for-beginners)。

</details>

<a id="complete-configuration-file"></a>

### 完整設定檔範例

以下是同時設定 filesystem 與 Context7 伺服器的 `mcp-config.json` 範例：

> 💡 **注意：** GitHub MCP 是內建的，不需寫進設定檔。

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

將此檔案存為 `~/.copilot/mcp-config.json`（全域），或專案根目錄的 `.mcp.json`（專案專用）。

---

# 使用 MCP 伺服器

現在你已設定好 MCP 伺服器，來看看它們能做什麼。

<img src="images/using-mcp-servers.png" alt="Using MCP Servers - Hub-and-spoke diagram showing a Developer CLI connected to GitHub, Filesystem, Context7, and Custom/Web Fetch servers" width="800" />

---

## 伺服器使用範例

**選一個伺服器來探索，或依序練習。**

| 我想嘗試…… | 跳到 |
|---|---|
| GitHub repo、issue、PR | [GitHub Server](#github-server-built-in) |
| 瀏覽專案檔案 | [Filesystem Server Usage](#filesystem-server-usage) |
| 查詢函式庫文件 | [Context7 Server Usage](#context7-server-usage) |
| 自訂伺服器、Microsoft Learn MCP 與 web_fetch 用法 | [Beyond the Basics Usage](#beyond-the-basics-usage) |

<details>
<summary><strong>GitHub Server（內建）</strong> - 存取 repo、issue、PR 等</summary>
<a id="github-server-built-in"></a>

### GitHub Server（內建）

GitHub MCP 伺服器是**內建**的。只要你已登入 Copilot（安裝時已做過），就能直接用，無需設定！

> 💡 **無法使用？** 執行 `/login` 重新驗證 GitHub。

<details>
<summary><strong>Dev Container 認證說明</strong></summary>

- **GitHub Codespaces**（推薦）：認證自動完成。`gh` CLI 會繼承你的 Codespace token，無需手動操作。
- **本機 dev container（Docker）**：容器啟動後執行 `gh auth login`，再重啟 Copilot。

**認證疑難排解：**
```bash
# 檢查是否已認證
gh auth status

# 若未認證，請登入
gh auth login

# 確認 GitHub MCP 已連線
copilot
> /mcp show
```

</details>

| 功能 | 範例 |
|---------|----------|
| **儲存庫資訊** | 查看 commit、分支、貢獻者 |
| **Issue** | 列出、建立、搜尋、留言 |
| **Pull request** | 查看 PR、diff、建立 PR、查詢狀態 |
| **程式碼搜尋** | 跨 repo 搜尋程式碼 |
| **Actions** | 查詢 workflow 執行與狀態 |

```bash
copilot

# 查看本 repo 近期活動
> List the last 5 commits in this repository

Recent commits:
1. abc1234 - Update chapter 05 skills examples (2 days ago)
2. def5678 - Add book app test fixtures (3 days ago)
3. ghi9012 - Fix typo in chapter 03 README (4 days ago)
...

# 探索 repo 結構
> What branches exist in this repository?

Branches:
- main (default)
- chapter6 (current)

# 跨 repo 搜尋程式碼模式
> Search this repository for files that import pytest

Found 1 file:
- samples/book-app-project/tests/test_books.py
```

> 💡 **在自己 fork 上練習？** 如果你 fork 了本課程 repo，也可嘗試建立 issue、PR 等寫入操作。下方練習會實作。

> ⚠️ **沒看到結果？** GitHub MCP 操作的是 repo 的遠端（github.com），不只是本地檔案。請確認 repo 有 remote：執行 `git remote -v` 檢查。

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

# Copilot 現在知道 pytest 官方模式
# 並能應用於 samples/book-app-project/tests/test_books.py
```

</details>

<details>
<summary><strong>Beyond the Basics</strong> - 進階：自訂伺服器與 web_fetch 用法</summary>
<a id="beyond-the-basics-usage"></a>

### Beyond the Basics

**自訂 MCP 伺服器**：如果你依 [自訂 MCP 伺服器指南](mcp-custom-server.md) 建立了 book-lookup server，可直接查詢你的書籍收藏：

```bash
copilot

> Look up information about "1984" using the book lookup server. Search for books by George Orwell
```

**Microsoft Learn MCP**：如果你安裝了 [Microsoft Learn MCP server](#microsoft-learn-mcp-server)，可直接查詢官方 Microsoft 文件：

```bash
copilot

> How do I configure managed identity for an Azure Function? Search Microsoft Learn.
```

**Web Fetch**：用內建 `web_fetch` 工具拉取任意 URL 內容：

```bash
copilot

> Fetch and summarize the README from https://github.com/facebook/react
```

</details>

---

## 多伺服器工作流程

這些工作流程展現為什麼開發者會說「用了就回不去了」。每個範例都在同一工作階段結合多個 MCP 伺服器。

<img src="images/issue-to-pr-workflow.png" alt="Issue to PR Workflow using MCP - Shows the complete flow from getting a GitHub issue through creating a pull request" width="800"/>

*完整 MCP 工作流程：GitHub MCP 取得 repo 資料、Filesystem MCP 找程式碼、Context7 MCP 查詢最佳實務，Copilot 負責分析*

下方每個範例都是獨立的。**選你有興趣的，或全部閱讀。**

| 我想看…… | 跳到 |
|---|---|
| 多個伺服器協作 | [Multi-Server Exploration](#multi-server-exploration) |
| 一次從 issue 到 PR | [Issue-to-PR Workflow](#issue-to-pr-workflow) |
| 快速專案健檢 | [Health Dashboard](#health-dashboard) |

<details>
<summary><strong>Multi-Server Exploration</strong> - 同時用 filesystem、GitHub、Context7</summary>
<a id="multi-server-exploration"></a>

#### 用多個 MCP 伺服器探索書籍應用程式

```bash
copilot

# 步驟 1：用 filesystem MCP 探索書籍應用程式
> List all Python files in samples/book-app-project/ and summarize
> what each file does

Found 3 Python files:
- book_app.py: CLI entry point with command routing (list, add, remove, find)
- books.py: BookCollection class with data persistence via JSON
- utils.py: Helper functions for user input and display

# 步驟 2：用 GitHub MCP 查詢近期異動
> What were the last 3 commits that touched files in samples/book-app-project/?

Recent commits affecting book app:
1. abc1234 - Add test fixtures for BookCollection (2 days ago)
2. def5678 - Add find_by_author method (5 days ago)
3. ghi9012 - Initial book app setup (1 week ago)

# 步驟 3：用 Context7 MCP 查詢最佳實務
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
<summary>🎬 MCP 工作流程實際操作！</summary>

![MCP Workflow Demo](images/mcp-workflow-demo.gif)

*示範輸出會因模型、工具、回應而異。你的結果可能不同。*

</details>

**成果**：程式碼探索 → 歷史檢視 → 最佳實務查詢 → 改進建議。**全部在同一終端機工作階段、三個 MCP 伺服器協作完成。**

</details>

<details>
<summary><strong>Issue-to-PR Workflow</strong> - 從 GitHub issue 到 PR，全程不離開終端機</summary>
<a id="issue-to-pr-workflow"></a>

#### Issue-to-PR 工作流程（適用於你自己的 repo）

這在你有寫入權限的 fork 或 repo 上效果最佳：

> 💡 **現在無法實作也沒關係。** 如果你用的是唯讀 clone，之後作業會練習。現在先閱讀流程即可。

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

**零複製貼上。零情境切換。只用一個終端機工作階段。**

</details>

<details>
<summary><strong>Health Dashboard</strong> - 用多個伺服器快速檢查專案健康狀態</summary>
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

**成果**：多個資料來源幾秒內彙整。手動做這些要跑 grep、數行數、查 git log、瀏覽測試檔，至少 15 分鐘起跳。

</details>

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

**🎉 你已掌握重點！** 你了解 MCP，學會設定伺服器，也看過實際工作流程。現在輪到你親自動手。

---

## ▶️ 自己試試看

現在換你練習！完成下列練習，體驗 MCP 伺服器在書籍應用程式專案的實戰應用。

### 練習 1：檢查你的 MCP 狀態

先查看有哪些 MCP 伺服器可用：

```bash
copilot

> /mcp show
```

你應該會看到 GitHub 伺服器已啟用。如果沒有，請執行 `/login` 進行驗證。

---

### 練習 2：使用 Filesystem MCP 探索書籍應用程式

如果你已設定 filesystem 伺服器，請用它來探索書籍應用程式：

```bash
copilot

> How many Python files are in samples/book-app-project/?
> What functions are defined in each file?
```

**預期結果**：Copilot 會列出 `book_app.py`、`books.py` 和 `utils.py` 及其函式。

> 💡 **還沒設定 filesystem MCP？** 請參考上方 [完整設定檔](#complete-configuration-file) 區段建立設定檔，然後重新啟動 Copilot。

---

### 練習 3：使用 GitHub MCP 查詢版本庫歷史

使用內建的 GitHub MCP 探索本課程的版本庫：

```bash
copilot

> List the last 5 commits in this repository

> What branches exist in this repository?
```

**預期結果**：Copilot 會顯示 GitHub 遠端的近期提交訊息與分支名稱。

> ⚠️ **在 Codespace 中？** 這會自動運作，驗證會繼承。如果你在本機複製的版本，請確認 `gh auth status` 顯示你已登入。

---

### 練習 4：結合多個 MCP 伺服器

現在在同一個 session 中結合 filesystem 和 GitHub MCP：

```bash
copilot

> Read samples/book-app-project/data.json and tell me what books are
> in the collection. Then check the recent commits to see when this
> file was last modified.
```

**預期結果**：Copilot 會讀取 JSON 檔案（filesystem MCP），列出 5 本書，包括 "The Hobbit"、"1984"、"Dune"、"To Kill a Mockingbird" 和 "Mysterious Book"，然後查詢 GitHub 的提交歷史。

**自我檢查**：當你能解釋為什麼「Check my repo's commit history」比手動執行 `git log` 並將輸出貼到提示詞中更好時，代表你已理解 MCP。

---

## 📝 作業

### 主要挑戰：書籍應用程式 MCP 探索

練習在書籍應用程式專案中同時使用 MCP 伺服器。請在單一 Copilot session 內完成以下步驟：

1. **確認 MCP 正常運作**：執行 `/mcp show` 並確認至少有啟用 GitHub 伺服器
2. **設定 filesystem MCP**（若尚未完成）：建立 `~/.copilot/mcp-config.json` 並加入 filesystem 伺服器設定
3. **探索程式碼**：請 Copilot 使用 filesystem 伺服器來：
   - 列出 `samples/book-app-project/books.py` 中所有函式
   - 檢查 `samples/book-app-project/utils.py` 中哪些函式缺少型別註記
   - 讀取 `samples/book-app-project/data.json` 並找出任何資料品質問題（提示：查看最後一筆資料）
4. **檢查版本庫活動**：請 Copilot 使用 GitHub MCP 來：
   - 列出最近有修改 `samples/book-app-project/` 目錄檔案的提交
   - 檢查是否有任何未關閉的 issue 或 pull request
5. **結合伺服器**：在單一提示中請 Copilot：
   - 讀取 `samples/book-app-project/tests/test_books.py` 測試檔
   - 比較測試過的函式與 `books.py` 中所有函式
   - 摘要說明哪些測試覆蓋尚未涵蓋

**成功標準**：你能在單一 Copilot session 中無縫結合 filesystem 與 GitHub MCP 的資料，並能解釋每個 MCP 伺服器對回應的貢獻。

<details>
<summary>💡 提示（點擊展開）</summary>

**步驟 1：確認 MCP**
```bash
copilot
> /mcp show
# 應顯示 "github" 為啟用狀態
# 若無，執行：/login
```

**步驟 2：建立設定檔**

請使用上方 [完整設定檔](#complete-configuration-file) 區段的 JSON，並儲存為 `~/.copilot/mcp-config.json`。

**步驟 3：資料品質問題提示**

`data.json` 最後一本書為：
```json
{
  "title": "Mysterious Book",
  "author": "",
  "year": 0,
  "read": false
}
```
作者為空且年份為 0。這就是資料品質問題！

**步驟 5：測試覆蓋比較**

`test_books.py` 測試了：`add_book`、`mark_as_read`、`remove_book`、`get_unread_books` 和 `find_book_by_title`。像是 `load_books`、`save_books`、`list_books` 沒有直接測試。`book_app.py` 的 CLI 函式和 `utils.py` 的輔助函式則完全沒有測試。

**若 MCP 無法運作：** 編輯設定檔後請重新啟動 Copilot。

</details>

### 進階挑戰：打造自訂 MCP 伺服器

想要更進階嗎？請參考 [自訂 MCP 伺服器指南](mcp-custom-server.md)，用 Python 打造連接任意 API 的 MCP 伺服器。

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 會發生什麼事 | 修正方式 |
|------|--------------|----------|
| 不知道 GitHub MCP 是內建的 | 嘗試手動安裝／設定 | GitHub MCP 預設已包含。直接嘗試：「List the recent commits in this repo」即可 |
| 設定檔放錯位置 | 找不到或無法編輯 MCP 設定 | 使用者層級設定在 `~/.copilot/mcp-config.json`，專案層級在專案根目錄的 `.mcp.json` |
| 設定檔 JSON 無效 | MCP 伺服器載入失敗 | 使用 `/mcp show` 檢查設定，並驗證 JSON 語法 |
| 忘記驗證 MCP 伺服器 | 出現 "Authentication failed" 錯誤 | 有些 MCP 需要額外驗證。請檢查每個伺服器的需求 |

### 疑難排解

**"MCP server not found"** - 請檢查：
1. npm 套件是否存在：`npm view @modelcontextprotocol/server-github`
2. 你的設定檔是否為有效的 JSON
3. 伺服器名稱是否與設定檔一致

使用 `/mcp show` 查看目前設定。

**"GitHub authentication failed"** - 內建 GitHub MCP 使用你的 `/login` 憑證。請嘗試：

```bash
copilot
> /login
```

這會重新驗證你的 GitHub 帳號。如果問題持續，請確認你的 GitHub 帳號對該版本庫有必要權限。

**"MCP server failed to start"** - 請檢查伺服器日誌：
```bash
# 手動執行伺服器指令以查看錯誤
npx -y @modelcontextprotocol/server-github
```

**MCP 工具無法使用** - 請確認伺服器已啟用：
```bash
copilot

> /mcp show
# 檢查伺服器是否已列出並啟用
```

若伺服器為停用狀態，請參考下方 [更多 `/mcp` 指令](#-additional-mcp-commands) 以重新啟用。

</details>

---

<details>
<summary>📚 <strong>更多 MCP 指令</strong>（點擊展開）</summary>
<a id="-additional-mcp-commands"></a>

你可以用兩種方式管理 MCP 伺服器：**在聊天 session 內使用斜線指令**，或直接在終端機使用 **`copilot mcp` 指令**（不需進入聊天）。

### 方式一：斜線指令（於聊天 session 內）

這些指令適用於你已在 `copilot` 內時：

| 指令 | 功能說明 |
|------|----------|
| `/mcp show` | 顯示所有已設定的 MCP 伺服器及其狀態 |
| `/mcp add` | 互動式新增新伺服器 |
| `/mcp edit <server-name>` | 編輯現有伺服器設定 |
| `/mcp enable <server-name>` | 啟用已停用的伺服器（設定會永久保存） |
| `/mcp disable <server-name>` | 停用伺服器（設定會永久保存） |
| `/mcp delete <server-name>` | 永久移除伺服器 |
| `/mcp auth <server-name>` | 重新驗證使用 OAuth 的 MCP 伺服器（例如切換帳號後） |

### 方式二：`copilot mcp` 指令（於終端機）

你也可以直接在終端機管理 MCP 伺服器，無需先啟動聊天 session：

```bash
# 列出所有已設定的 MCP 伺服器
copilot mcp list

# 啟用伺服器
copilot mcp enable filesystem

# 停用伺服器
copilot mcp disable context7
```

> 💡 **何時用哪一種？** 已在聊天 session 時請用 `/mcp` 斜線指令。想在啟動 session 前快速檢查或變更伺服器設定，請用終端機的 `copilot mcp`。

本課程大多時候只需 `/mcp show`。隨著你管理更多伺服器，其他指令會越來越實用。

</details>

---

# 摘要

## 🔑 重點整理

1. **MCP** 讓 Copilot 能連接外部服務（GitHub、檔案系統、文件）
2. **GitHub MCP 內建** —— 無需設定，只要 `/login` 即可
3. **Filesystem 與 Context7** 透過 `~/.copilot/mcp-config.json` 設定
4. **多伺服器工作流程** 可在單一 session 結合多來源資料
5. **伺服器管理有兩種方式**：聊天內用 `/mcp` 斜線指令，或在終端機用 `copilot mcp`
6. **自訂伺服器** 可連接任意 API（選用，詳見附錄指南）

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 接下來

你現在已具備所有基礎：模式、情境、工作流程、Agent、Skill 及 MCP。是時候把它們整合起來了。

在 **[第 07 章：整合應用](../07-putting-it-together/README.md)**，你將學到：

- 結合 Agent、Skill 與 MCP 的整合式工作流程
- 從構想到合併 PR 的完整功能開發
- 使用 hook 進行自動化
- 團隊協作最佳實踐

---

**[← 回到第 05 章](../05-skills/README.md)** | **[繼續前往第 07 章 →](../07-putting-it-together/README.md)**
