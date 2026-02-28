# 術語表

本課程使用的技術術語快速參考。現在不需要背起來——有需要時再回來查閱即可。

---

## A

### Agent

具有特定領域專業知識的 AI 角色（例如：前端、安全性）。定義於 `.agent.md` 檔案中，以 YAML frontmatter 表示，至少須包含 `description` 欄位。

### API

應用程式介面（Application Programming Interface）。程式之間互相溝通的方式。

---

## C

### CI/CD

持續整合／持續部署（Continuous Integration/Continuous Deployment）。自動化測試與部署流程。

### CLI

命令列介面（Command Line Interface）。以文字為基礎的軟體操作方式（就像這個工具！）。

### Context Window

AI 一次可考量的文字量。就像一張只能放有限東西的桌子。當你加入檔案、對話記錄和系統提示時，這些內容都會佔用此窗口的空間。

### Context Manager

Python 中使用 `with` 陳述式的結構，可自動處理初始化與清理作業（例如開啟和關閉檔案）。範例：`with open("file.txt") as f:` 確保即使發生錯誤，檔案也一定會被關閉。

### Conventional Commit

遵循標準化格式的提交訊息：`type(scope): description`。常見類型包括 `feat`（新功能）、`fix`（錯誤修正）、`docs`（文件）、`refactor` 和 `test`。範例：`feat(auth): add password reset flow`。

### Dataclass

Python 裝飾器（`@dataclass`），可為主要用於儲存資料的類別自動生成 `__init__`、`__repr__` 等方法。在書籍應用程式中，用於定義具有 `title`、`author`、`year` 和 `read` 欄位的 `Book` 類別。

---

## F

### Frontmatter

位於 Markdown 檔案頂部、以 `---` 分隔符包圍的元資料。用於 Agent 和 Skill 檔案中，以 YAML 格式定義 `description`、`name` 等屬性。

---

## G

### Glob Pattern

使用萬用字元來比對檔案路徑的模式（例如：`*.py` 比對所有 Python 檔案，`*.js` 比對所有 JavaScript 檔案）。

---

## J

### JWT

JSON Web Token。一種在系統之間安全傳遞身分驗證資訊的方式。

---

## M

### MCP

模型情境協定（Model Context Protocol）。一種將 AI 助手與外部資料來源連接的標準。

---

## N

### npx

Node.js 工具，無需全域安裝即可執行 npm 套件。用於 MCP Server 設定中啟動伺服器（例如：`npx @modelcontextprotocol/server-filesystem`）。

---

## O

### OWASP

開放網路應用程式安全專案（Open Web Application Security Project）。一個發布安全最佳實踐並維護「OWASP Top 10」（最關鍵網路應用程式安全風險清單）的組織。

---

## P

### PEP 8

Python 增強提案 8（Python Enhancement Proposal 8）。Python 程式碼的官方風格指南，涵蓋命名慣例（函式用 snake_case，類別用 PascalCase）、縮排（4 個空格）和程式碼版面配置。遵循 PEP 8 可讓 Python 程式碼保持一致且易於閱讀。

### Pre-commit Hook

在每次 `git commit` 前自動執行的腳本。可用於在提交程式碼前執行 Copilot 安全審查或程式碼品質檢查。

### pytest

廣受歡迎的 Python 測試框架，以簡潔的語法、強大的 Fixture 機制和豐富的外掛生態系統著稱。本課程全程使用它來測試書籍應用程式。執行方式：`python -m pytest tests/`。

### Programmatic Mode

使用 `-p` 旗標執行 Copilot，以非互動方式執行單一指令。

---

## R

### Rate Limiting

在特定時間內對 API 請求數量的限制。若你超出方案的使用配額，Copilot 可能會暫時限制回應。

---

## S

### Session

與 Copilot 的對話，可保留情境並於稍後繼續。

### Skill

包含指令的資料夾，當提示詞與其相關時，Copilot 會自動載入。定義於具有 YAML frontmatter 的 `SKILL.md` 檔案中。

### Slash Command

以 `/` 開頭的指令，用於控制 Copilot（例如：`/help`、`/clear`、`/model`）。

---

## T

### Token

AI 模型處理文字的基本單位。大約等於 4 個字元或 0.75 個英文單字。用於衡量輸入（你的提示詞與情境）和輸出（AI 的回應）。

### Type Hints

Python 標註，用於說明函式參數和回傳值的預期型別（例如：`def add_book(title: str, year: int) -> Book:`）。它們不會在執行期強制型別，但有助於提升程式碼可讀性、IDE 支援，以及 mypy 等靜態分析工具的效果。

---

## W

### WCAG

網路內容無障礙指引（Web Content Accessibility Guidelines）。由 W3C 發布的標準，旨在讓殘障人士能無障礙地使用網路內容。WCAG 2.1 AA 是常見的合規目標。

---

## Y

### YAML

YAML 不是標記語言（YAML Ain't Markup Language）。一種人類可讀的資料格式，用於設定檔。在本課程中，YAML 出現於 Agent 和 Skill 的 frontmatter（即 `.agent.md` 和 `SKILL.md` 檔案頂部以 `---` 分隔的區塊）中。
