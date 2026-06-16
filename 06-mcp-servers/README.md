<!--
---
id: CopilotCLI-06
title: !translate 連接 GitHub、資料庫與 API
description: !translate 設定 MCP 伺服器，讓 GitHub Copilot CLI 能連接 GitHub、本機檔案、文件、資料庫及其他即時資料來源。
audience: Developers / Students / Terminal users
slug: connect-to-github-databases-and-apis
weight: 7
---
-->

![第 06 章：MCP 伺服器](assets/chapter-header.png)

> **如果 Copilot 能從終端機讀取你的 GitHub 問題、查詢資料庫、建立 PR……會怎樣？**

到目前為止，Copilot 只能處理你直接給它的內容：你用 `@` 引用的檔案、對話記錄，以及它自己的訓練資料。但如果它能主動查詢你的 GitHub 儲存庫、瀏覽你的專案檔案，或查找某個函式庫的最新文件呢？

這就是 MCP（模型情境協定，Model Context Protocol）的用途。它是一種讓 Copilot 能連接外部服務、取得即時真實資料的方式。Copilot 連接的每個服務都稱為「MCP 伺服器」。本章你將設定幾個這樣的連線，並體驗它如何大幅提升 Copilot 的實用性。

> 💡 **已經熟悉 MCP？** [直接跳到快速開始](#-use-the-built-in-github-mcp) 確認運作正常並開始設定伺服器。

## 🎯 學習目標

完成本章後，你將能夠：

- 了解 MCP 是什麼，以及它的重要性
- 使用 `/mcp` 指令管理 MCP 伺服器
- 設定 GitHub、檔案系統與文件的 MCP 伺服器
- 在書籍應用程式專案中體驗 MCP 強化的工作流程
- 知道何時、如何打造自訂 MCP 伺服器（選用）

> ⏱️ **預估時間**：約 50 分鐘（閱讀 15 分鐘 + 實作 35 分鐘）

---

## 🧩 真實世界類比：瀏覽器擴充功能

<img src="assets/browser-extensions-analogy.png" alt="MCP 伺服器就像瀏覽器擴充功能" width="800"/>

把 MCP 伺服器想像成瀏覽器擴充功能。你的瀏覽器本身能顯示網頁，但擴充功能能讓它連接更多服務：

| 瀏覽器擴充功能 | 連接對象 | MCP 對應 |
|-------------------|---------------------|----------------|
| 密碼管理員 | 你的密碼保險箱 | **GitHub MCP** → 你的儲存庫、問題、PR |
| Grammarly | 寫作分析服務 | **Context7 MCP** → 函式庫文件 |
| 檔案管理員 | 雲端儲存 | **Filesystem MCP** → 本機專案檔案 |

沒有擴充功能，瀏覽器還是有用，但加上它們就變得超強大。MCP 伺服器對 Copilot 來說也是如此。它們讓 Copilot 能連接真實、即時的資料來源，讀取 GitHub 問題、探索檔案系統、取得最新文件等等。

***MCP 伺服器讓 Copilot 連接外部世界：GitHub、儲存庫、文件等***

> 💡 **關鍵洞見**：沒有 MCP，Copilot 只能看到你用 `@` 明確分享的檔案。有了 MCP，它能主動探索你的專案、查詢 GitHub 儲存庫、查找文件，全部自動完成。

---

<img src="assets/quick-start-mcp.png" alt="電源線連接時閃爍著明亮電火花，周圍漂浮著代表 MCP 伺服器連線的科技圖示" width="800"/>

# 快速開始：30 秒體驗 MCP

## 立即體驗內建的 GitHub MCP 伺服器
在還沒設定任何東西前，先來看看 MCP 的威力。
GitHub MCP 伺服器預設已包含。試試看：

```bash
copilot
> List the recent commits in this repository
```

如果 Copilot 回傳了真實的提交資料，你就親眼見到 MCP 的運作了。這就是 GitHub MCP 伺服器代表你連線到 GitHub。不過 GitHub 只是*其中一個*伺服器。本章會教你如何加更多（檔案系統存取、最新文件等），讓 Copilot 能做得更多。

---

## `/mcp show` 指令

使用 `/mcp show` 查看目前已設定哪些 MCP 伺服器，以及它們是否啟用：

```bash
copilot

> /mcp show

MCP Servers:
✓ github (enabled) - GitHub integration
✓ filesystem (enabled) - File system access
```

> 💡 **只看到 GitHub 伺服器？** 這很正常！如果你還沒加其他 MCP 伺服器，目前只會列出 GitHub。下一節你會學會如何新增。

> 📚 **想看所有 MCP 管理指令？** 你可以在聊天中用 `/mcp` slash 指令管理伺服器，或直接在終端機用 `copilot mcp`。完整指令參考請見本章結尾的[指令總覽](#-additional-mcp-commands)。

<details>
<summary>🎬 實際操作影片</summary>

![MCP 狀態示範](assets/mcp-status-demo.gif)

*示範輸出會因模型、工具、回應而異。*

</details>

---

## MCP 帶來哪些改變？

實際上，MCP 讓 Copilot 有這樣的差異：

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

> 📚 **官方文件**：[關於 MCP](https://docs.github.com/copilot/concepts/context/mcp) 深入了解 MCP 如何與 GitHub Copilot 協作。

---

# 設定 MCP 伺服器

<img src="assets/configuring-mcp-servers.png" alt="雙手調整專業音控台上的旋鈕與推桿，象徵 MCP 伺服器設定" width="800"/>

你已經體驗過 MCP，現在來設定更多伺服器。有兩種方式可以新增伺服器：**從內建註冊表安裝**（最簡單——CLI 互動式引導），或**手動編輯設定檔**（更彈性）。如果不確定，建議先用註冊表方式。

---

## 從註冊表安裝 MCP 伺服器

CLI 內建 MCP 伺服器註冊表，讓你能用互動式引導安裝熱門伺服器——不用自己編輯 JSON。

```bash
copilot

> /mcp search
```

Copilot 會開啟一個互動式選擇器，顯示可用伺服器。選一個後，CLI 會引導你完成所需設定（API 金鑰、路徑等），並自動加入設定檔。

> 💡 **為什麼用註冊表？** 這是最簡單的入門方式——你不用知道 npm 套件名稱、指令參數或 JSON 結構，CLI 會全部幫你處理。

---

## MCP 設定檔

MCP 伺服器可在使用者層級（`~/.copilot/mcp-config.json`，全專案適用）、專案層級（`.mcp.json`），或工作區設定檔（`.github/mcp.json`）中設定。`.github/mcp.json` 會和 `.mcp.json` 一起自動載入。如果你用 `/mcp search`，CLI 會建立或更新你的使用者層級 `~/.copilot/mcp-config.json`，但了解 JSON 格式有助於自訂或分享專案層級設定。

> ⚠️ **注意**：`.vscode/mcp.json` 已不再支援作為 MCP 設定來源。如果你有舊的 `.vscode/mcp.json`，請移到專案根目錄的 `.mcp.json`。CLI 偵測到舊檔會顯示遷移提示。

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

*大多數 MCP 伺服器以 npm 套件形式發佈，並透過 `npx` 執行。*

<details>
<summary>💡 <strong>不熟 JSON？</strong> 點此看各欄位說明</summary>

| 欄位 | 說明 |
|-------|---------------|
| `"mcpServers"` | 所有 MCP 伺服器設定的容器 |
| `"server-name"` | 你自訂的名稱（如 "github"、"filesystem"） |
| `"type": "local"` | 伺服器在本機執行 |
| `"command": "npx"` | 執行的程式（npx 執行 npm 套件） |
| `"args": [...]` | 傳給指令的參數 |
| `"tools": ["*"]` | 允許此伺服器所有工具 |

**重要 JSON 規則：**
- 字串請用雙引號 `"`（不要用單引號）
- 最後一項後面不能有逗號
- 檔案必須是合法 JSON（不確定時可用 [JSON validator](https://jsonlint.com/)）

</details>

---

## 新增 MCP 伺服器

GitHub MCP 伺服器是內建的，不需額外設定。以下是你可以加裝的其他伺服器。**選你有興趣的，或依序練習。**

| 我想要…… | 跳到 |
|---|---|
| 讓 Copilot 瀏覽我的專案檔案 | [Filesystem Server](#filesystem-server) |
| 取得最新函式庫文件 | [Context7 Server](#context7-server-documentation) |
| 探索進階應用（自訂伺服器、web_fetch） | [進階應用](#beyond-the-basics) |

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

> 💡 **`.` 路徑**：`.` 代表「目前目錄」。Copilot 可存取你啟動時所在目錄的相對檔案。在 Codespace 裡，這是你的工作區根目錄。你也可以用絕對路徑（如 `/workspaces/copilot-cli-for-beginners`）。

把這段加到你的 `~/.copilot/mcp-config.json`，然後重啟 Copilot。

</details>

<details>
<summary><strong>Context7 Server</strong> - 取得最新函式庫文件</summary>
<a id="context7-server-documentation"></a>

### Context7 Server（文件）

Context7 讓 Copilot 能存取熱門框架與函式庫的最新官方文件。不再依賴可能過時的訓練資料，Copilot 會抓取真正的最新文件。

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
- ✅ **你的程式碼留在本地**

把這段加到你的 `~/.copilot/mcp-config.json`，然後重啟 Copilot。

</details>

<details>
<summary><strong>進階應用</strong> - 自訂伺服器與網頁存取（選用）</summary>
<a id="beyond-the-basics"></a>

這些是進階選項，適合你已熟悉前述核心伺服器時再嘗試。

### Microsoft Learn MCP Server

前面介紹的 MCP 伺服器（filesystem、Context7）都是在本機執行。但 MCP 伺服器也可以遠端執行，只要 Copilot CLI 指向一個 URL 即可，無需 `npx`、`python`、本地安裝。

[Microsoft Learn MCP Server](https://github.com/microsoftdocs/mcp) 就是好例子。它讓 Copilot CLI 直接存取官方 Microsoft 文件（Azure、Microsoft Foundry 與其他 AI 主題、.NET、Microsoft 365 等），能搜尋文件、抓取完整頁面、查找官方程式碼範例，不再只靠模型訓練資料。

- ✅ **不需 API 金鑰** 
- ✅ **不需註冊帳號** 
- ✅ **不需本地安裝**

**用 `/plugin install` 快速安裝：**

不用手動編輯 JSON 設定檔，只要一行指令：

```bash
copilot

> /plugin install microsoftdocs/mcp
```

這會自動加入伺服器及其相關 agent 技能。安裝的技能包含：

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

Copilot CLI 內建 `web_fetch` 工具，可從任意 URL 抓取內容。這對於拉取 README、API 文件或發行說明很方便，無需離開終端機。不需 MCP 伺服器。

你可在 `~/.copilot/config.json`（Copilot 一般設定，與 MCP 伺服器設定檔 `~/.copilot/mcp-config.json` 分開）中控制哪些 URL 可存取。

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

想讓 Copilot 連接你自己的 API、資料庫或內部工具？你可以用 Python 打造自訂 MCP 伺服器。這完全是選用功能，因為預設伺服器（GitHub、filesystem、Context7）已涵蓋大多數需求。

📖 參考 [自訂 MCP 伺服器指南](mcp-custom-server.md)，以書籍應用程式為例完整教學。

📚 更多背景知識請見 [MCP for Beginners 課程](https://github.com/microsoft/mcp-for-beginners)。

</details>

<a id="complete-configuration-file"></a>

### 完整設定檔範例

這是一份同時包含 filesystem 與 Context7 伺服器的 `mcp-config.json` 範例：

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

將此檔案儲存為 `~/.copilot/mcp-config.json`（全域設定），或專案根目錄的 `.mcp.json`（專案專用設定）。

---

# 使用 MCP 伺服器

你已設定好 MCP 伺服器，現在來看看它們能做什麼。

<img src="assets/using-mcp-servers.png" alt="使用 MCP 伺服器 - 輻射圖顯示開發者 CLI 連接 GitHub、Filesystem、Context7 及自訂/Web Fetch 伺服器" width="800" />

---

## 伺服器使用範例

**選一個伺服器體驗，或依序練習。**

| 我想嘗試…… | 跳到 |
|---|---|
| GitHub 儲存庫、問題、PR | [GitHub Server](#github-server-built-in) |
| 瀏覽專案檔案 | [Filesystem Server 用法](#filesystem-server-usage) |
| 查詢函式庫文件 | [Context7 Server 用法](#context7-server-usage) |
| 自訂伺服器、Microsoft Learn MCP 與 web_fetch 用法 | [進階應用用法](#beyond-the-basics-usage) |

<details>
<summary><strong>GitHub Server（內建）</strong> - 存取儲存庫、問題、PR 等</summary>
<a id="github-server-built-in"></a>

### GitHub Server（內建）

GitHub MCP 伺服器是**內建**的。如果你已登入 Copilot（初次設定時已做過），它就能直接用，不需額外設定！

> 💡 **無法運作？** 執行 `/login` 重新驗證 GitHub。

<details>
<summary><strong>Dev Containers 認證說明</strong></summary>

- **GitHub Codespaces**（推薦）：認證自動完成。`gh` CLI 會繼承你的 Codespace token，無需手動操作。
- **本地 dev container（Docker）**：容器啟動後執行 `gh auth login`，再重啟 Copilot。

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
| **儲存庫資訊** | 查看提交、分支、貢獻者 |
| **問題** | 列出、建立、搜尋、留言 |
| **Pull requests** | 查看 PR、diff、建立 PR、查詢狀態 |
| **程式碼搜尋** | 跨儲存庫搜尋程式碼 |
| **Actions** | 查詢 workflow 執行與狀態 |

```bash
copilot

# 查看此儲存庫近期活動
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

> 💡 **在自己的 fork 上操作？** 如果你 fork 了本課程儲存庫，也可以嘗試建立 issue、pull request 等寫入操作。下方練習會實際操作。

> ⚠️ **沒看到結果？** GitHub MCP 操作的是儲存庫的遠端（github.com 上），不只本地檔案。請確認你的 repo 有 remote：用 `git remote -v` 檢查。

</details>

<details>
<summary><strong>Filesystem Server</strong> - 瀏覽與分析專案檔案</summary>
<a id="filesystem-server-usage"></a>

### Filesystem Server

設定好後，filesystem MCP 會自動提供 Copilot 可用的工具：

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

# Copilot 現在已知道 pytest 官方模式
# 並能應用於 samples/book-app-project/tests/test_books.py
```

</details>

<details>
<summary><strong>進階應用</strong> - 自訂伺服器與 web_fetch 用法</summary>
<a id="beyond-the-basics-usage"></a>

### 進階應用

**自訂 MCP 伺服器**：如果你依照 [自訂 MCP 伺服器指南](mcp-custom-server.md) 建立了 book-lookup 伺服器，可以直接查詢你的書籍收藏：

```bash
copilot

> Look up information about "1984" using the book lookup server. Search for books by George Orwell
```

**Microsoft Learn MCP**：如果你安裝了 [Microsoft Learn MCP server](#microsoft-learn-mcp-server)，可以直接查詢官方 Microsoft 文件：

```bash
copilot

> How do I configure managed identity for an Azure Function? Search Microsoft Learn.
```

**Web Fetch**：用內建 `web_fetch` 工具從任意 URL 拉取內容：

```bash
copilot

> Fetch and summarize the README from https://github.com/facebook/react
```

</details>

---

## 多伺服器工作流程

這些工作流程展現了為什麼開發者會說「用了就回不去了」。每個範例都在同一會話中結合多個 MCP 伺服器。

<img src="assets/issue-to-pr-workflow.png" alt="使用 MCP 的 Issue 到 PR 工作流程 - 展示從取得 GitHub issue 到建立 pull request 的完整流程" width="800"/>

*完整 MCP 工作流程：GitHub MCP 取得 repo 資料、Filesystem MCP 找程式碼、Context7 MCP 提供最佳實踐，Copilot 負責分析*

以下每個範例都可獨立操作。**選你有興趣的，或全部閱讀。**

| 我想看到…… | 跳到 |
|---|---|
| 多個伺服器協作 | [多伺服器探索](#multi-server-exploration) |
| 一次會話從 issue 到 PR | [Issue-to-PR 工作流程](#issue-to-pr-workflow) |
| 快速專案健康檢查 | [健康儀表板](#health-dashboard) |

<details>
<summary><strong>多伺服器探索</strong> - 同時結合 filesystem、GitHub、Context7</summary>
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

# 步驟 2：用 GitHub MCP 查詢近期變更
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
<summary>🎬 MCP 工作流程示範影片</summary>

![MCP 工作流程示範](assets/mcp-workflow-demo.gif)

*示範輸出會因模型、工具、回應而異。*

</details>

**成果**：程式碼探索 → 歷史回顧 → 最佳實踐查詢 → 改進建議。**全部在同一終端機會話，三個 MCP 伺服器協作完成。**

</details>

<details>
<summary><strong>Issue-to-PR 工作流程</strong> - 一次會話從 GitHub issue 到 pull request</summary>
<a id="issue-to-pr-workflow"></a>

#### Issue-to-PR 工作流程（在你自己的儲存庫）

這在你有寫入權限的 fork 或儲存庫上效果最佳：

> 💡 **現在沒法操作也別擔心。** 如果你用的是唯讀 clone，之後作業會練習。現在先看流程即可。

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

**零複製貼上。零情境切換。一次終端機會話完成。**

</details>

<details>
<summary><strong>健康儀表板</strong> - 用多個伺服器快速檢查專案健康狀態</summary>
<a id="health-dashboard"></a>

#### 書籍應用程式健康儀表板

```bash
copilot

> 幫我產生書籍應用程式專案的健康報告：
> 1. 列出 samples/book-app-project/ 目錄下所有 Python 檔案中的函式
> 2. 檢查哪些函式有型別註記，哪些沒有
> 3. 顯示 samples/book-app-project/tests/ 目錄下現有的測試
> 4. 檢查這個目錄下最近的提交紀錄

書籍應用程式健康報告
======================

📊 發現的函式：
- books.py：BookCollection 中有 8 個方法（全部都有型別註記 ✓）
- book_app.py：6 個函式（4 個有型別註記，2 個缺少）
- utils.py：3 個函式（1 個有型別註記，2 個缺少）

🧪 測試涵蓋率：
- test_books.py：8 個測試函式涵蓋 BookCollection
- 缺少：沒有針對 book_app.py CLI 函式的測試
- 缺少：沒有針對 utils.py 輔助函式的測試

📝 最近活動：
- 過去一週有 3 次提交
- 最近一次：新增測試 fixture

建議事項：
- 為 utils.py 的函式補上型別註記
- 為 book_app.py 的 CLI 處理函式新增測試
- 所有檔案長度適中（皆小於 100 行）－結構良好！

```

**結果**：多個資料來源在數秒內彙整。手動操作則需執行 grep、計算行數、檢查 git log 並瀏覽測試檔案，輕鬆就要花上 15 分鐘以上。

</details>

---

# 練習

<img src="../assets/practice.png" alt="溫暖的書桌擺設，螢幕顯示程式碼、檯燈、咖啡杯與耳機，準備動手練習" width="800"/>

**🎉 你現在已經掌握了基本要素！** 你了解 MCP，看過如何設定伺服器，也見識過實際工作流程。現在輪到你親自嘗試。

---

## ▶️ 自己動手試試看

現在換你來練習！完成以下練習，熟悉如何在書籍應用程式專案中使用 MCP 伺服器。

### 練習 1：檢查你的 MCP 狀態

先查看有哪些 MCP 伺服器可用：

```bash
copilot

> /mcp show
```

你應該會看到 GitHub 伺服器已啟用。如果沒有，請執行 `/login` 進行認證。

---

### 練習 2：用檔案系統 MCP 探索書籍應用程式

如果你已經設定好檔案系統伺服器，試著用它來探索書籍應用程式：

```bash
copilot

> samples/book-app-project/ 目錄下有多少個 Python 檔案？
> 每個檔案中定義了哪些函式？
```

**預期結果**：Copilot 會列出 `book_app.py`、`books.py` 和 `utils.py` 及其各自的函式。

> 💡 **還沒設定檔案系統 MCP？** 請參考上方 [完整設定檔](#complete-configuration-file) 區段建立設定檔，然後重新啟動 Copilot。

---

### 練習 3：用 GitHub MCP 查詢儲存庫歷史

使用內建的 GitHub MCP 探索本課程儲存庫：

```bash
copilot

> 列出這個儲存庫最近 5 次提交

> 這個儲存庫有哪些分支？
```

**預期結果**：Copilot 會顯示 GitHub 遠端的最近提交訊息與分支名稱。

> ⚠️ **在 Codespace 中嗎？** 這會自動運作，認證會自動繼承。如果你在本地複製的專案，請確認 `gh auth status` 顯示你已登入。

---

### 練習 4：結合多個 MCP 伺服器

現在在同一個會話中結合檔案系統與 GitHub MCP：

```bash
copilot

> 讀取 samples/book-app-project/data.json，告訴我有哪些書在收藏中。然後檢查最近的提交，看看這個檔案上次是什麼時候被修改。
```

**預期結果**：Copilot 會讀取 JSON 檔案（檔案系統 MCP），列出 5 本書，包括 "The Hobbit"、"1984"、"Dune"、"To Kill a Mockingbird" 和 "Mysterious Book"，然後查詢 GitHub 的提交歷史。

**自我檢查**：當你能解釋為什麼「檢查我的儲存庫提交歷史」比手動執行 `git log` 再貼到提示中更好時，就代表你已經理解 MCP。

---

## 📝 作業

### 主要挑戰：書籍應用程式 MCP 探索

練習在書籍應用程式專案中同時使用 MCP 伺服器。請在單一 Copilot 會話中完成以下步驟：

1. **確認 MCP 正常運作**：執行 `/mcp show`，確認至少有 GitHub 伺服器啟用
2. **設定檔案系統 MCP**（若尚未完成）：建立 `~/.copilot/mcp-config.json`，加入檔案系統伺服器設定
3. **探索程式碼**：請 Copilot 使用檔案系統伺服器：
   - 列出 `samples/book-app-project/books.py` 中所有函式
   - 檢查 `samples/book-app-project/utils.py` 中哪些函式缺少型別註記
   - 讀取 `samples/book-app-project/data.json`，找出任何資料品質問題（提示：看最後一筆資料）
4. **檢查儲存庫活動**：請 Copilot 使用 GitHub MCP：
   - 列出最近有修改 `samples/book-app-project/` 目錄下檔案的提交
   - 檢查是否有任何開啟中的 issue 或 pull request
5. **結合伺服器**：在單一提示中請 Copilot：
   - 讀取 `samples/book-app-project/tests/test_books.py` 測試檔
   - 比較測試涵蓋的函式與 `books.py` 中所有函式
   - 總結哪些測試涵蓋尚未完善

**成功標準**：你能在單一 Copilot 會話中順利結合檔案系統與 GitHub MCP 的資料，並能解釋每個 MCP 伺服器在回應中貢獻了哪些資訊。

<details>
<summary>💡 提示（點擊展開）</summary>

**步驟 1：確認 MCP**
```bash
copilot
> /mcp show
# 應該會顯示 "github" 已啟用
# 若沒有，請執行：/login
```

**步驟 2：建立設定檔**

請將 [完整設定檔](#complete-configuration-file) 區段的 JSON 存成 `~/.copilot/mcp-config.json`。

**步驟 3：資料品質問題提示**

`data.json` 最後一本書如下：
```json
{
  "title": "Mysterious Book",
  "author": "",
  "year": 0,
  "read": false
}
```
作者為空、年份為 0。這就是資料品質問題！

**步驟 5：測試涵蓋比較**

`test_books.py` 測試涵蓋：`add_book`、`mark_as_read`、`remove_book`、`get_unread_books` 和 `find_book_by_title`。像是 `load_books`、`save_books`、`list_books` 沒有直接測試。`book_app.py` 的 CLI 函式與 `utils.py` 的輔助函式則完全沒有測試。

**如果 MCP 沒作用：** 編輯設定檔後請重新啟動 Copilot。

</details>

### 加分挑戰：打造自訂 MCP 伺服器

想更進階嗎？請參考 [自訂 MCP 伺服器指南](mcp-custom-server.md)，用 Python 打造一個能連接任意 API 的 MCP 伺服器。

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 會發生什麼事 | 解決方式 |
|------|--------------|----------|
| 不知道 GitHub MCP 是內建的 | 嘗試手動安裝／設定 | GitHub MCP 預設就有。直接試：「列出這個 repo 最近的提交」 |
| 設定檔放錯位置 | 找不到或無法編輯 MCP 設定 | 使用者層級設定在 `~/.copilot/mcp-config.json`，專案層級則是專案根目錄的 `.mcp.json` |
| 設定檔 JSON 格式錯誤 | MCP 伺服器載入失敗 | 用 `/mcp show` 檢查設定，並驗證 JSON 語法 |
| 忘記認證 MCP 伺服器 | 出現「認證失敗」錯誤 | 有些 MCP 需要額外認證。請檢查每個伺服器的需求 |

### 疑難排解

**"找不到 MCP 伺服器"**－請檢查：
1. npm 套件存在：`npm view @modelcontextprotocol/server-github`
2. 你的設定檔是有效的 JSON
3. 伺服器名稱與設定檔一致

用 `/mcp show` 查看目前設定。

**"GitHub 認證失敗"**－內建 GitHub MCP 會使用你的 `/login` 認證。請嘗試：

```bash
copilot
> /login
```

這會重新與 GitHub 認證。如果問題持續，請確認你的 GitHub 帳號對該儲存庫有必要權限。

**"MCP 伺服器啟動失敗"**－請檢查伺服器日誌：
```bash
# 手動執行伺服器指令以查看錯誤
npx -y @modelcontextprotocol/server-github
```

**MCP 工具不可用**－請確認伺服器已啟用：
```bash
copilot

> /mcp show
# 檢查伺服器是否已列出並啟用
```

如果伺服器被停用，請參考下方 [更多 /mcp 指令](#-additional-mcp-commands) 以重新啟用。

</details>

---

<details>
<summary>📚 <strong>更多 MCP 指令</strong>（點擊展開）</summary>
<a id="-additional-mcp-commands"></a>

你可以用兩種方式管理 MCP 伺服器：**在聊天會話中用 slash 指令**，或直接在終端機用 **`copilot mcp` 指令**（不需進入聊天）。

### 方式一：slash 指令（在聊天會話中）

這些指令適用於你已經在 `copilot` 互動介面時：

| 指令 | 功能說明 |
|------|----------|
| `/mcp show` | 顯示所有已設定的 MCP 伺服器及其狀態 |
| `/mcp add` | 互動式新增伺服器 |
| `/mcp edit <server-name>` | 編輯現有伺服器設定 |
| `/mcp enable <server-name>` | 啟用已停用的伺服器（設定會持續保存） |
| `/mcp disable <server-name>` | 停用伺服器（設定會持續保存） |
| `/mcp delete <server-name>` | 永久移除伺服器 |
| `/mcp auth <server-name>` | 重新認證需要 OAuth 的 MCP 伺服器（例如切換帳號後） |

### 方式二：`copilot mcp` 指令（直接在終端機）

你也可以直接在終端機管理 MCP 伺服器，無需先進入聊天會話：

```bash
# 列出所有已設定的 MCP 伺服器
copilot mcp list

# 啟用伺服器
copilot mcp enable filesystem

# 停用伺服器
copilot mcp disable context7
```

> 💡 **什麼時候用哪一種？** 已經在聊天會話中就用 `/mcp` 指令；想在開始會話前快速檢查或調整伺服器設定則用 `copilot mcp`。

本課程大多時候只需 `/mcp show`。其他指令則在你管理更多伺服器時會派上用場。

</details>

---

# 小結

## 🔑 重點整理

1. **MCP** 讓 Copilot 能連接外部服務（GitHub、檔案系統、文件）
2. **GitHub MCP 內建**－無需設定，只要 `/login` 即可
3. **檔案系統與 Context7** 透過 `~/.copilot/mcp-config.json` 設定
4. **多伺服器工作流程** 可在單一會話中結合多個資料來源
5. **伺服器管理有兩種方式**：聊天內用 `/mcp` 指令，或終端機用 `copilot mcp`
6. **自訂伺服器** 可連接任何 API（進階內容，見附錄指南）

> 📋 **快速參考**：完整指令與快捷鍵請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 接下來

你已經擁有所有基礎元件：模式、情境、工作流程、Agent、Skill 與 MCP。是時候把它們全部串連起來了。

在 **[第七章：整合實戰](../07-putting-it-together/README.md)**，你將學到：

- 如何將 Agent、Skill 與 MCP 結合成統一工作流程
- 從想法到合併 PR 的完整功能開發
- 用 hook 自動化流程
- 團隊協作最佳實踐

---

**[← 回到第五章](../05-skills/README.md)** | **[前往第七章 →](../07-putting-it-together/README.md)**
