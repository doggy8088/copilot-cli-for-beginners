<!--
---
id: CopilotCLI-05
title: 自動化重複性工作
description: 建立並使用 Agent 技能，讓 GitHub Copilot CLI 能自動套用特定任務指令與團隊最佳實踐。
audience: Developers / Students / Terminal users
slug: automate-repetitive-tasks
weight: 6
---
-->

![第 05 章：技能系統](assets/chapter-header.png)

> **如果 Copilot 能自動套用你們團隊的最佳實踐，而不需要你每次都解釋，會怎樣？**

在本章中，你將學習 Agent 技能：Copilot 會在與你的任務相關時自動載入的指令資料夾。Agent 會改變 Copilot *思考的方式*，而技能則教 Copilot *完成任務的具體方法*。你將建立一個安全性稽核技能，讓 Copilot 在你詢問安全性時自動套用，打造團隊標準的審查準則，確保程式碼品質一致，並學習技能如何在 Copilot CLI、VS Code 及 GitHub Copilot 雲端 agent 中運作。

## 🎯 學習目標

完成本章後，你將能夠：

- 了解 Agent 技能的運作方式及使用時機
- 以 SKILL.md 檔案建立自訂技能
- 使用來自共用儲存庫的社群技能
- 知道何時該用技能、Agent 或 MCP

> ⏱️ **預估時間**：約 55 分鐘（閱讀 20 分鐘 + 實作 35 分鐘）

---

## 🧩 真實世界類比：電動工具

一般的電鑽很有用，但專用的配件讓它更強大。
<img src="assets/power-tools-analogy.png" alt="電動工具 - 技能擴充 Copilot 能力" width="800"/>

技能的運作方式也是如此。就像根據不同工作更換鑽頭一樣，你可以為 Copilot 加入不同任務的技能：

| 技能配件 | 用途 |
|------------|---------|
| `commit` | 產生一致的提交訊息 |
| `security-audit` | 檢查 OWASP 漏洞 |
| `generate-tests` | 建立完整的 pytest 測試 |
| `code-checklist` | 套用團隊程式碼品質標準 |

*技能是專用配件，能擴展 Copilot 的能力*

---

# 技能的運作方式

<img src="assets/how-skills-work.png" alt="發光的 RPG 風格技能圖示，彼此以光軌連結，背景為星空，象徵 Copilot 技能" width="800"/>

了解什麼是技能、為什麼重要，以及它們與 Agent 和 MCP 的差異。

---

## *第一次接觸技能？* 從這裡開始！

1. **查看現有技能：**
   ```bash
   copilot
   > /skills list
   ```
   這會顯示 Copilot 能找到的所有技能，包括 CLI 內建的**內建技能**，以及來自你專案和個人資料夾的技能。

   > 💡 **內建技能**：Copilot CLI 隨附預先安裝的技能。例如，`customizing-copilot-cloud-agents-environment` 技能提供自訂 Copilot 雲端 agent 環境的指南。你不需要建立或安裝即可使用這些技能。執行 `/skills list` 來查看有哪些可用技能。

2. **查看實際的技能檔案：** 參考我們提供的 [code-checklist SKILL.md](../.github/skills/code-checklist/SKILL.md) 來了解格式。它只是 YAML frontmatter 加上 markdown 指令。

3. **理解核心概念：** 技能是針對任務的指令，當你的提示詞符合技能描述時，Copilot 會*自動*載入。你不需要手動啟用，只要自然地提問即可。

## 理解技能

Agent 技能是包含指令、腳本和資源的資料夾，當與你的任務相關時，Copilot 會**自動載入**。Copilot 會讀取你的提示詞，檢查是否有技能符合，並自動套用相關指令。

```bash
copilot

> Check books.py against our quality checklist
# Copilot 偵測到這符合你的 "code-checklist" 技能
# 並自動套用 Python 品質檢查清單

> Generate tests for the BookCollection class
# Copilot 載入你的 "pytest-gen" 技能
# 並套用你偏好的測試結構

> What are the code quality issues in this file?
# Copilot 載入你的 "code-checklist" 技能
# 並依據團隊標準檢查
```

> 💡 **關鍵洞見**：技能會根據你的提示詞是否符合技能描述**自動觸發**。只要自然提問，Copilot 就會在背後自動套用相關技能。你也可以直接呼叫技能，接下來會學到怎麼做。

> 🧰 **現成範本**：參考 [.github/skills](../.github/skills/) 資料夾，裡面有可直接複製貼上的簡易技能範例。

### 直接以 Slash 指令呼叫

雖然自動觸發是技能的主要運作方式，你也可以用技能名稱作為 slash 指令**直接呼叫技能**：

```bash
> /generate-tests Create tests for the user authentication module

> /code-checklist Check books.py for code quality issues

> /security-audit Check the API endpoints for vulnerabilities
```

這讓你在需要確保使用特定技能時有明確的控制權。

#### 一則訊息中結合多個技能

你可以在**同一則訊息中呼叫多個技能**，而且技能的 slash 指令可以出現在提示詞的任何地方——不一定要在開頭。這在你想一次完成兩種不同檢查時很方便：

```bash
> Check @samples/book-app-project/book_app.py with /code-checklist and also run /generate-tests for it

> Review the auth module /security-audit then /code-checklist the result
```

Copilot 會在同一回應中套用每個指定的技能，省去你多次分開提問的麻煩。

> 💡 **小技巧**：把技能 slash 指令放在句子中你覺得最自然的位置。可以放在開頭、中間或結尾。

> 📝 **技能與 Agent 呼叫方式差異**：不要混淆技能呼叫與 Agent 呼叫：
> - **技能**：`/skill-name <prompt>`，例如 `/code-checklist Check this file`
> - **Agent**：`/agent`（從清單選擇）或 `copilot --agent <name>`（命令列）
>
> 如果你同時有同名的技能和 Agent（例如 "code-reviewer"），輸入 `/code-reviewer` 會呼叫**技能**，而不是 Agent。

### 如何知道技能是否被使用？

你可以直接問 Copilot：

```bash
> What skills did you use for that response?

> What skills do you have available for security reviews?
```

### 技能 vs Agent vs MCP

技能只是 GitHub Copilot 擴充模型的一部分。以下是它們與 Agent 和 MCP 伺服器的比較。

> *不用急著了解 MCP。我們會在[第 06 章](../06-mcp-servers/)介紹。這裡先讓你了解技能在整體架構中的定位。*

<img src="assets/skills-agents-mcp-comparison.png" alt="比較圖，顯示 Agent、技能與 MCP 伺服器的差異，以及它們如何結合進你的工作流程" width="800"/>

| 功能 | 作用 | 適用時機 |
|---------|--------------|-------------|
| **Agent** | 改變 AI 的思考方式 | 需要跨多種任務的專業知識 |
| **技能** | 提供特定任務指令 | 具體、可重複、步驟明確的任務 |
| **MCP** | 連接外部服務 | 需要從 API 取得即時資料 |

Agent 適合廣泛專業知識，技能適合特定任務指令，MCP 則用於外部資料。Agent 在對話中可以同時使用一個或多個技能。例如，當你請 Agent 檢查程式碼時，它可能會自動套用 `security-audit` 技能和 `code-checklist` 技能。

> 📚 **深入了解**：參考官方文件 [About Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills) 取得技能格式與最佳實踐完整說明。

---

## 從手動提示到自動專業

在深入技能建立方法前，先看看*為什麼*值得學習技能。當你看到一致性的提升後，"怎麼做" 就會更有意義。

### 沒有技能前：審查標準不一致

每次程式碼審查，你可能都會漏掉某些項目：

```bash
copilot

> Review this code for issues
# 一般性審查——可能漏掉你們團隊特別關注的問題
```

或者你每次都要寫一長串提示：

```bash
> Review this code checking for bare except clauses, missing type hints,
> mutable default arguments, missing context managers for file I/O,
> functions over 50 lines, print statements in production code...
```

耗時：**30 秒以上**。一致性：**取決於記憶力**。

### 有技能後：自動套用最佳實踐

安裝 `code-checklist` 技能後，只要自然提問即可：

```bash
copilot

> Check the book collection code for quality issues
```

**幕後發生的事**：
1. Copilot 在你的提示詞中看到 "code quality" 和 "issues"
2. 檢查技能描述，發現 `code-checklist` 技能符合
3. 自動載入你們團隊的品質檢查清單
4. 套用所有檢查項目，無需你逐條列出

<img src="assets/skill-auto-discovery-flow.png" alt="技能自動觸發流程圖 - 4 步驟說明 Copilot 如何自動將你的提示詞對應到正確技能" width="800"/>

*只要自然提問，Copilot 會自動對應並套用正確技能。*

**輸出範例**：
```
## Code Checklist: books.py

### Code Quality
- [PASS] All functions have type hints
- [PASS] No bare except clauses
- [PASS] No mutable default arguments
- [PASS] Context managers used for file I/O
- [PASS] Functions are under 50 lines
- [PASS] Variable and function names follow PEP 8

### Input Validation
- [FAIL] User input is not validated - add_book() accepts any year value
- [FAIL] Edge cases not fully handled - empty strings accepted for title/author
- [PASS] Error messages are clear and helpful

### Testing
- [FAIL] No corresponding pytest tests found

### Summary
3 items need attention before merge
```

**差異**：你們團隊的標準每次都會自動套用，無需手動輸入。

---

<details>
<summary>🎬 實際操作影片！</summary>

![Skill Trigger Demo](assets/skill-trigger-demo.gif)

*Demo 輸出會有所不同。你的模型、工具與回應可能與此不同。*

</details>

---

## 一致性規模化：團隊 PR 審查技能

假設你們團隊有 10 點 PR 檢查清單。沒有技能時，每個開發者都要記住這 10 點，總有人會漏掉。使用 `pr-review` 技能後，全團隊都能獲得一致的審查：

```bash
copilot

> Can you review this PR?
```

Copilot 會自動載入你們團隊的 `pr-review` 技能並檢查所有 10 點：

```
PR Review: feature/user-auth

## Security ✅
- No hardcoded secrets
- Input validation present
- No bare except clauses

## Code Quality ⚠️
- [WARN] print statement on line 45 - remove before merge
- [WARN] TODO on line 78 missing issue reference
- [WARN] Missing type hints on public functions

## Testing ✅
- New tests added
- Edge cases covered

## Documentation ❌
- [FAIL] Breaking change not documented in CHANGELOG
- [FAIL] API changes need OpenAPI spec update
```

**威力**：每位團隊成員都能自動套用相同標準。新進人員無需死背檢查清單，技能會自動處理。

---

# 建立自訂技能

<img src="assets/creating-managing-skills.png" alt="人類與機器手共同堆疊發光的樂高積木，象徵技能建立與管理" width="800"/>

從 SKILL.md 檔案打造你自己的技能。

---

## 技能存放位置

技能儲存在 `.github/skills/`（專案專屬）或 `~/.copilot/skills/`（使用者層級）。

### Copilot 如何尋找技能

Copilot 會自動掃描這些位置尋找技能：

| 位置 | 範圍 |
|----------|-------|
| `.github/skills/` | 專案專屬（透過 git 與團隊共用） |
| `~/.copilot/skills/` | 使用者專屬（你個人的技能） |

### 技能結構

每個技能都放在自己的資料夾，裡面有一個 `SKILL.md` 檔案。你也可以選擇加入腳本、範例或其他資源：

```
.github/skills/
└── my-skill/
    ├── SKILL.md           # 必要：技能定義與指令
    ├── examples/          # 選用：Copilot 可參考的範例檔案
    │   └── sample.py
    └── scripts/           # 選用：技能可用的腳本
        └── validate.sh
```

> 💡 **小技巧**：資料夾名稱應與 SKILL.md frontmatter 的 `name` 欄位一致（小寫並用連字號）。

### SKILL.md 格式

技能採用簡單的 markdown 格式，搭配 YAML frontmatter：

```markdown
---
name: code-checklist
description: Comprehensive code quality checklist with security, performance, and maintainability checks
license: MIT
---

# Code Checklist

When checking code, look for:

## Security
- SQL injection vulnerabilities
- XSS vulnerabilities
- Authentication/authorization issues
- Sensitive data exposure

## Performance
- N+1 query problems (running one query per item instead of one query for all items)
- Unnecessary loops or computations
- Memory leaks
- Blocking operations

## Maintainability
- Function length (flag functions > 50 lines)
- Code duplication
- Missing error handling
- Unclear naming

## Output Format
Provide issues as a numbered list with severity:
- [CRITICAL] - Must fix before merge
- [HIGH] - Should fix before merge
- [MEDIUM] - Should address soon
- [LOW] - Nice to have
```

**YAML 屬性說明：**

| 屬性 | 必填 | 說明 |
|----------|----------|-------------|
| `name` | **是** | 唯一識別名稱（小寫、空格用連字號） |
| `description` | **是** | 技能的用途，以及 Copilot 何時應該使用 |
| `license` | 否 | 技能適用的授權條款 |
| `argument-hint` | 否 | 顯示給使用者的簡短提示，說明技能預期的參數（例如："file path or code snippet"） |

> 💡 **什麼是 `argument-hint`？** 當使用者直接呼叫技能（如 `/security-audit`）時，`argument-hint` 會作為佔位提示，告訴使用者接下來要輸入什麼——就像迷你說明。例如設為 `argument-hint: "file path to review"`，就會提示使用者在技能名稱後輸入檔案路徑。

> 📖 **官方文件**：[About Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills)

### 建立你的第一個技能

我們來建立一個檢查 OWASP Top 10 漏洞的安全性稽核技能：

```bash
# 建立技能資料夾
mkdir -p .github/skills/security-audit

# 建立 SKILL.md 檔案
cat > .github/skills/security-audit/SKILL.md << 'EOF'
---
name: security-audit
description: Security-focused code review checking OWASP (Open Web Application Security Project) Top 10 vulnerabilities
---

# Security Audit

Perform a security audit checking for:

## Injection Vulnerabilities
- SQL injection (string concatenation in queries)
- Command injection (unsanitized shell commands)
- LDAP injection
- XPath injection

## Authentication Issues
- Hardcoded credentials
- Weak password requirements
- Missing rate limiting
- Session management flaws

## Sensitive Data
- Plaintext passwords
- API keys in code
- Logging sensitive information
- Missing encryption

## Access Control
- Missing authorization checks
- Insecure direct object references
- Path traversal vulnerabilities

## Output
For each issue found, provide:
1. File and line number
2. Vulnerability type
3. Severity (CRITICAL/HIGH/MEDIUM/LOW)
4. Recommended fix
EOF

# 測試你的技能（技能會根據提示自動載入）
copilot

> @samples/book-app-project/ Check this code for security vulnerabilities
# Copilot 偵測到 "security vulnerabilities" 符合你的技能
# 並自動套用 OWASP 檢查清單
```

**預期輸出**（實際結果會有所不同）：

```
Security Audit: book-app-project

[HIGH] Hardcoded file path (book_app.py, line 12)
  File path is hardcoded rather than configurable
  Fix: Use environment variable or config file

[MEDIUM] No input validation (book_app.py, line 34)
  User input passed directly to function without sanitization
  Fix: Add input validation before processing

✅ No SQL injection found
✅ No hardcoded credentials found
```

---

## 撰寫良好的技能描述

SKILL.md 中的 `description` 欄位非常重要！Copilot 會根據它決定是否載入你的技能：

```markdown
---
name: security-audit
description: Use for security reviews, vulnerability scanning,
  checking for SQL injection, XSS, authentication issues,
  OWASP Top 10 vulnerabilities, and security best practices
---
```

> 💡 **小技巧**：包含你平常提問時會用到的關鍵字。如果你會說 "security review"，就把 "security review" 寫進 description。

### 技能與 Agent 結合運作

技能與 Agent 可以協同運作。Agent 提供專業知識，技能則給予具體指令：

```bash
# 以 code-reviewer agent 開始
copilot --agent code-reviewer

> Check the book app for quality issues
# code-reviewer agent 的專業知識會結合
# 你的 code-checklist 技能檢查清單
```

---

# 管理與分享技能

探索已安裝技能、尋找社群技能，並分享你自己的技能。

<img src="assets/managing-sharing-skills.png" alt="技能管理與分享 - 展示 CLI 技能的探索、使用、建立與分享循環" width="800" />

---

## 用 `copilot skill` 指令與 `/skills` 管理技能

Copilot CLI 提供兩種技能管理方式。你可以在啟動 Copilot 前直接在終端機操作，也可以在 Copilot 互動會話中操作。

### 選項 1：`copilot skill`（終端機指令）

`copilot skill` 子指令讓你直接在終端機管理技能，無需開啟互動式 Copilot 會話。這對於腳本自動化、快速檢查或事前新增技能很方便。

```bash
# 查看所有已安裝技能
copilot skill list

# 從本地檔案、URL 或目錄新增技能
copilot skill add .github/skills/my-skill/SKILL.md
copilot skill add https://example.com/skills/security-audit/SKILL.md

# 依名稱移除技能
copilot skill remove security-audit
```

### 選項 2：`/skills`（Copilot 會話中）

進入互動式 Copilot 會話後，使用 `/skills`（或快捷 `/skill`）即可管理技能，無需離開會話：

| 指令 | 作用 |
|---------|--------------|
| `/skills list` | 顯示所有已安裝技能 |
| `/skills info <name>` | 查看特定技能詳細資訊 |
| `/skills add <name>` | 啟用技能（來自儲存庫或市集） |
| `/skills remove <name>` | 停用或解除安裝技能 |
| `/skills reload` | 編輯 SKILL.md 後重新載入技能 |

> 💡 **`/skill` 快捷指令**：你可以輸入 `/skill` 取代 `/skills`——兩者等效。例如 `/skill list` 與 `/skills list` 效果相同。

> 💡 **請記住**：你不需要每次提示都「啟用」技能。安裝後，只要提示詞符合描述，技能就會**自動觸發**。這些指令是用來管理可用技能，而不是用來使用技能。

### 範例：查看你的技能

```bash
# 在終端機（無需互動會話）：
copilot skill list

Project skills:
- security-audit: Security-focused code review checking OWASP Top 10
- generate-tests: Generate comprehensive unit tests with edge cases
- code-checklist: Team code quality checklist (disabled)
...

# 或在 Copilot 會話中：
copilot

> /skills list

Project skills:
- security-audit: Security-focused code review checking OWASP Top 10
- generate-tests: Generate comprehensive unit tests with edge cases
- code-checklist: Team code quality checklist (disabled)
...

> /skills info security-audit

Skill: security-audit
Source: Project
Location: .github/skills/security-audit/SKILL.md
Description: Security-focused code review checking OWASP Top 10 vulnerabilities
```

> 💡 **已停用技能**：標記為 `(disabled)` 的技能已安裝但目前未啟用。它們不會被提示詞觸發，直到重新啟用。這可能是因為 SKILL.md 設定有誤，或技能被明確停用。你可以透過 `/skills` 啟用/停用技能。

---

<details>
<summary>實際操作影片！</summary>

![List Skills Demo](assets/list-skills-demo.gif)

*Demo 輸出會有所不同。你的模型、工具與回應可能與此不同。*

</details>

---

### 什麼時候要用 `/skills reload`

建立或編輯技能的 SKILL.md 檔案後，執行 `/skills reload` 即可在不重啟 Copilot 的情況下套用變更：

```bash
# 編輯你的技能檔案
# 然後在 Copilot 中：
> /skills reload
Skills reloaded successfully.
```

> 💡 **小知識**：即使你用 `/compact` 指令壓縮對話歷史，技能依然有效。壓縮後無需重新載入。

---

## 尋找與使用社群技能

### 使用插件安裝技能

> 💡 **什麼是插件？** 插件是可安裝的套件，可以同時包含技能、Agent 及 MCP 伺服器設定。你可以把它們想像成 Copilot CLI 的「應用程式商店」擴充套件。

用 `/plugin` 指令可以瀏覽並安裝這些套件：

```bash
copilot

> /plugin list
# 顯示已安裝的插件

> /plugin marketplace
# 瀏覽可用插件

> /plugin install <plugin-name>
# 從市集安裝插件
```

要讓本地插件目錄保持最新，請執行：

```bash
copilot plugin marketplace update
```

插件可以同時包含多種功能。一個插件可能包含相關的技能、Agent 和 MCP 伺服器設定，彼此協同運作。

### 社群技能儲存庫

也有許多現成技能可從社群儲存庫取得：

- **[Awesome Copilot](https://github.com/github/awesome-copilot)** - 官方 GitHub Copilot 資源，包含技能文件與範例

### 用 GitHub CLI 安裝社群技能

從 GitHub 儲存庫安裝技能最簡單的方法是使用 `gh skill install` 指令（需 [GitHub CLI v2.90.0+](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/)）：

```bash
# 瀏覽並互動式選擇 awesome-copilot 的技能
gh skill install github/awesome-copilot

# 或直接安裝特定技能
gh skill install github/awesome-copilot ai-ready

# 安裝到所有專案皆可用（使用者層級）
gh skill install github/awesome-copilot ai-ready --scope user
```

> ⚠️ **安裝前請審查**：安裝技能前請務必閱讀其 `SKILL.md`。技能會控制 Copilot 的行為，惡意技能可能會指示 Copilot 執行有害指令或意外修改程式碼。

---

# 練習

<img src="../assets/practice.png" alt="溫馨桌面，螢幕顯示程式碼、檯燈、咖啡杯與耳機，準備實作練習" width="800"/>

動手建立並測試你自己的技能，應用所學。

---

## ▶️ 自己動手試試看

### 建立更多技能

這裡有兩個不同模式的技能範例。請依照「建立你的第一個技能」中的 `mkdir` + `cat` 步驟操作，或直接複製貼上到正確位置。更多範例可參考 [.github/skills](../.github/skills)。

### pytest 測試產生技能

這個技能可確保你的程式碼庫 pytest 結構一致：

```bash
mkdir -p .github/skills/pytest-gen

cat > .github/skills/pytest-gen/SKILL.md << 'EOF'
---
name: pytest-gen
description: Generate comprehensive pytest tests with fixtures and edge cases
---

# pytest Test Generation

Generate pytest tests that include:

## Test Structure
- Use pytest conventions (test_ prefix)
- One assertion per test when possible
- Clear test names describing expected behavior
- Use fixtures for setup/teardown

## Coverage
- Happy path scenarios
- Edge cases: None, empty strings, empty lists
- Boundary values
- Error scenarios with pytest.raises()

## Fixtures
- Use @pytest.fixture for reusable test data
- Use tmpdir/tmp_path for file operations
- Mock external dependencies with pytest-mock

## Output
Provide complete, runnable test file with proper imports.
EOF
```

### 團隊 PR 審查技能

這個技能可強制全團隊遵循一致的 PR 審查標準：

```bash
mkdir -p .github/skills/pr-review

cat > .github/skills/pr-review/SKILL.md << 'EOF'
---
name: pr-review
description: 團隊標準 PR 審查清單
---

# PR 審查

依據團隊標準審查程式碼變更：

## 安全性檢查清單
- [ ] 無硬編碼的秘密或 API 金鑰
- [ ] 所有使用者資料皆有輸入驗證
- [ ] 無裸露的 except 子句
- [ ] 日誌中無敏感資料

## 程式碼品質
- [ ] 函式少於 50 行
- [ ] 生產環境程式碼中無 print 陳述式
- [ ] 公開函式皆有型別註記
- [ ] 檔案 I/O 使用 Context Manager
- [ ] 無未附議題參考的 TODO

## 測試
- [ ] 新增程式碼皆有測試
- [ ] 邊界情境皆有涵蓋
- [ ] 無未說明原因的略過測試

## 文件
- [ ] API 變更有文件說明
- [ ] 重大變更有註記
- [ ] 如有需要已更新 README

## 輸出格式
請依下列格式提供結果：
- ✅ 通過：看起來沒問題的項目
- ⚠️ 警告：可改進的項目
- ❌ 未通過：合併前必須修正的項目
EOF
```

### 更進一步

1. **Skill 創建挑戰**：建立一個 `quick-review` skill，進行三點檢查：
   - 裸露的 except 子句
   - 缺少型別註記
   - 變數名稱不明確

   測試方式：詢問「Do a quick review of books.py」

2. **Skill 比較**：計時你手動撰寫詳細安全審查提示所需時間。然後只需詢問「Check for security issues in this file」，讓你的 security-audit skill 自動載入。這樣節省了多少時間？

3. **團隊 Skill 挑戰**：思考你們團隊的程式碼審查清單。能否將其編碼成一個 skill？寫下這個 skill 應該永遠檢查的三件事。

**自我檢查**：當你能解釋為什麼 `description` 欄位很重要時（它決定 Copilot 是否載入你的 skill），就代表你已經理解 skills 的運作。

---

## 📝 作業

### 主要挑戰：打造書籍摘要 Skill

上面的範例建立了 `pytest-gen` 和 `pr-review` 這兩個 skill。現在請練習創建一個完全不同類型的 skill：用來從資料產生格式化輸出的 skill。

1. 列出你目前的 skills：執行 Copilot 並傳入 `/skills list`。你也可以用 `ls .github/skills/` 查看專案 skills，或用 `ls ~/.copilot/skills/` 查看個人 skills。
2. 在 `.github/skills/book-summary/SKILL.md` 建立一個 `book-summary` skill，能產生書籍收藏的格式化 markdown 摘要
3. 你的 skill 應包含：
   - 清楚的名稱與描述（description 對於比對非常關鍵！）
   - 明確的格式規則（例如：以 markdown 表格顯示書名、作者、年份、閱讀狀態）
   - 輸出慣例（例如：已讀用 ✅，未讀用 ❌，依年份排序）
4. 測試 skill：`@samples/book-app-project/data.json Summarize the books in this collection`
5. 驗證 skill 是否自動觸發，可用 `/skills list` 檢查
6. 嘗試用 `/book-summary Summarize the books in this collection` 直接呼叫

**成功標準**：你有一個運作中的 `book-summary` skill，當你詢問書籍收藏時 Copilot 能自動套用。

<details>
<summary>💡 提示（點擊展開）</summary>

**起始範本**：建立 `.github/skills/book-summary/SKILL.md`：

```markdown
---
name: book-summary
description: 產生書籍收藏的格式化 markdown 摘要
---

# 書籍摘要產生器

請依下列規則產生書籍收藏摘要：

1. 輸出一個包含下列欄位的 markdown 表格：Title、Author、Year、Status
2. 已讀書籍用 ✅，未讀書籍用 ❌
3. 依年份排序（由舊到新）
4. 底部加上總數統計
5. 標記任何資料問題（如缺少作者、年份無效）

範例：
| Title | Author | Year | Status |
|-------|--------|------|--------|
| 1984 | George Orwell | 1949 | ✅ |
| Dune | Frank Herbert | 1965 | ❌ |

**Total: 2 books (1 read, 1 unread)**
```

**測試方式：**
```bash
copilot
> @samples/book-app-project/data.json Summarize the books in this collection
# 應該會根據 description 自動觸發 skill
```

**如果沒有觸發：** 請嘗試 `/skills reload` 再詢問一次。

</details>

### 加分挑戰：Commit Message Skill

1. 建立一個 `commit-message` skill，能產生格式一致的 conventional commit 訊息
2. 將變更 staged 後測試：「Generate a commit message for my staged changes」
3. 撰寫 skill 文件並在 GitHub 上以 `copilot-skill` 標籤分享

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 結果 | 修正方式 |
|------|------|----------|
| 檔名不是 `SKILL.md` | Skill 無法被辨識 | 檔案名稱必須正確為 `SKILL.md` |
| `description` 欄位太模糊 | Skill 永遠不會自動載入 | description 是主要的發現機制，請用明確的觸發關鍵字 |
| frontmatter 缺少 `name` 或 `description` | Skill 載入失敗 | YAML frontmatter 必須包含這兩個欄位 |
| 資料夾位置錯誤 | 找不到 skill | 請用 `.github/skills/skill-name/`（專案）或 `~/.copilot/skills/skill-name/`（個人） |

### 疑難排解

**Skill 沒被使用** - 如果 Copilot 沒有如預期使用你的 skill：

1. **檢查 description**：是否與你的提問方式相符？
   ```markdown
   # 錯誤：太模糊
   description: Reviews code

   # 正確：包含觸發關鍵字
   description: Use for code reviews, checking code quality,
     finding bugs, security issues, and best practice violations
   ```

2. **確認檔案位置**：
   ```bash
   # 專案 skills
   ls .github/skills/

   # 個人 skills
   ls ~/.copilot/skills/
   ```

3. **檢查 SKILL.md 格式**：必須有 frontmatter：
   ```markdown
   ---
   name: skill-name
   description: Skill 的功能與使用時機
   ---

   # 指令說明
   ```

**Skill 沒出現** - 請確認資料夾結構：
```
.github/skills/
└── my-skill/           # 資料夾名稱
    └── SKILL.md        # 必須正確命名為 SKILL.md（區分大小寫）
```

建立或編輯 skill 後請執行 `/skills reload` 以確保變更生效。

**測試 skill 是否載入** - 直接詢問 Copilot：
```bash
> What skills do you have available for checking code quality?
# Copilot 會描述它找到的相關 skills
```

**如何確認 skill 實際運作？**

1. **檢查輸出格式**：如果 skill 有指定輸出格式（如 `[CRITICAL]` 標籤），請在回應中尋找這些標記
2. **直接詢問**：取得回應後問「Did you use any skills for that?」
3. **比較有無 skill 差異**：用 `--no-custom-instructions` 做對照：
   ```bash
   # 有 skills
   copilot --allow-all -p "Review @file.py for security issues"

   # 無 skills（基準比較）
   copilot --allow-all -p "Review @file.py for security issues" --no-custom-instructions
   ```
4. **檢查特定檢查項目**：如果 skill 包含特定檢查（如「函式超過 50 行」），請確認這些內容是否出現在輸出中

</details>

---

# 摘要

## 🔑 重點整理

1. **Skills 會自動載入**：當你的提示詞符合 skill 的 description，Copilot 會自動載入
2. **可直接呼叫**：也能用 `/skill-name` slash 指令直接呼叫 skill
3. **SKILL.md 格式**：YAML frontmatter（name、description、可選 license、argument-hint）加上 markdown 指令說明
4. **位置很重要**：`.github/skills/` 適合專案／團隊共用，`~/.copilot/skills/` 適合個人使用
5. **Description 是關鍵**：請用自然問法會用到的描述來寫 description
6. **管理 skills 有兩種方式**：可在終端機用 `copilot skill`，或在會話內用 `/skills`（快捷指令：`/skill`）

> 📋 **快速參考**：完整指令與快捷鍵請見 [GitHub Copilot CLI command reference](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

Skills 讓 Copilot 能自動載入指令擴充功能。但如果要連接外部服務呢？這時就需要 MCP。

在 **[第 06 章：MCP 伺服器](../06-mcp-servers/README.md)**，你將學到：

- 什麼是 MCP（模型情境協定）
- 如何連接 GitHub、檔案系統與文件服務
- MCP 伺服器設定方式
- 多伺服器協作流程

---

**[← 回到第 04 章](../04-agents-custom-instructions/README.md)** | **[繼續前往第 06 章 →](../06-mcp-servers/README.md)**
