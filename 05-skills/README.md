![Chapter 05: Skills System](images/chapter-header.png)

> **如果 Copilot 能自動套用你們團隊的最佳實踐，而你不必每次都重新說明，會怎麼樣？**

在本章，你將學習 Agent 技能：Copilot 會在與你的任務相關時自動載入的指令資料夾。Agent 會改變 Copilot 的「思考方式」，而技能則教 Copilot「完成任務的具體方法」。你將建立一個安全性稽核技能，讓 Copilot 在你詢問安全性時自動套用，打造團隊標準的審查準則，確保程式碼品質一致，並學習技能如何在 Copilot CLI、VS Code 和 GitHub Copilot 雲端 Agent 中運作。

## 🎯 學習目標

完成本章後，你將能夠：

- 理解 Agent 技能的運作方式及適用時機
- 使用 SKILL.md 檔案建立自訂技能
- 使用來自共享儲存庫的社群技能
- 知道何時該用技能、Agent 或 MCP

> ⏱️ **預估時間**：約 55 分鐘（20 分鐘閱讀 + 35 分鐘實作）

---

## 🧩 真實世界比喻：電動工具

一般用途的電鑽很有用，但專用配件讓它更強大。
<img src="images/power-tools-analogy.png" alt="Power Tools - Skills Extend Copilot's Capabilities" width="800"/>

技能的運作方式也一樣。就像更換不同的鑽頭來處理不同工作，你可以為 Copilot 加上不同技能來完成不同任務：

| 技能配件 | 用途 |
|------------|---------|
| `commit` | 產生一致的提交訊息 |
| `security-audit` | 檢查 OWASP 漏洞 |
| `generate-tests` | 建立完整的 pytest 測試 |
| `code-checklist` | 套用團隊程式碼品質標準 |

*技能是專用配件，能擴展 Copilot 的能力*

---

# 技能的運作方式

<img src="images/how-skills-work.png" alt="Glowing RPG-style skill icons connected by light trails on a starfield background representing Copilot skills" width="800"/>

了解什麼是技能、為什麼重要，以及它們與 Agent 和 MCP 的差異。

---

## *第一次接觸技能？* 從這裡開始！

1. **查看現有技能：**
   ```bash
   copilot
   > /skills list
   ```
   這會顯示 Copilot 能找到的所有技能，包括 CLI 內建技能，以及你的專案和個人資料夾中的技能。

   > 💡 **內建技能**：Copilot CLI 隨附預先安裝的技能。例如，`customizing-copilot-cloud-agents-environment` 技能提供自訂 Copilot 雲端 Agent 環境的指南。你不需要建立或安裝任何東西即可使用這些技能。執行 `/skills list` 查看可用技能。

2. **查看實際技能檔案：** 請參考我們提供的 [code-checklist SKILL.md](../.github/skills/code-checklist/SKILL.md) 來了解格式。它只包含 YAML frontmatter 和 Markdown 指令。

3. **理解核心概念：** 技能是針對任務的指令，當你的提示詞符合技能描述時，Copilot 會*自動*載入。你不需要啟用它們，只要自然提問即可。

## 技能的理解

Agent 技能是包含指令、腳本和資源的資料夾，Copilot 會在與你的任務相關時**自動載入**。Copilot 會讀取你的提示詞，檢查是否有技能符合，並自動套用相關指令。

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
# 並依團隊標準檢查
```

> 💡 **關鍵洞見**：技能會根據你的提示詞是否符合技能描述而**自動觸發**。只要自然提問，Copilot 就會在背後套用相關技能。你也可以直接呼叫技能，接下來會學到。

> 🧰 **現成範本**：請參考 [.github/skills](../.github/skills/) 資料夾，裡面有可直接複製使用的技能範例。

### 直接斜線指令呼叫

雖然自動觸發是技能主要運作方式，你也可以用技能名稱作為斜線指令**直接呼叫技能**：

```bash
> /generate-tests Create tests for the user authentication module

> /code-checklist Check books.py for code quality issues

> /security-audit Check the API endpoints for vulnerabilities
```

這讓你在需要時能明確控制要使用哪個技能。

> 📝 **技能與 Agent 呼叫差異**：不要混淆技能呼叫與 Agent 呼叫：
> - **技能**：`/skill-name <prompt>`，例如 `/code-checklist Check this file`
> - **Agent**：`/agent`（從清單選擇）或 `copilot --agent <name>`（命令列）
>
> 如果你同時有同名的技能和 Agent（例如 "code-reviewer"），輸入 `/code-reviewer` 會呼叫**技能**，而不是 Agent。

### 如何知道技能有被使用？

你可以直接問 Copilot：

```bash
> What skills did you use for that response?

> What skills do you have available for security reviews?
```

### 技能 vs Agent vs MCP

技能只是 GitHub Copilot 擴充模型的一部分。以下是它們與 Agent 和 MCP 伺服器的比較。

> *暫時不用擔心 MCP。我們會在[第六章](../06-mcp-servers/)介紹。這裡先讓你了解技能在整體架構中的定位。*

<img src="images/skills-agents-mcp-comparison.png" alt="Comparison diagram showing the differences between Agents, Skills, and MCP Servers and how they combine into your workflow" width="800"/>

| 功能 | 作用 | 適用時機 |
|---------|--------------|-------------|
| **Agent** | 改變 AI 的思考方式 | 需要跨多任務的專業知識 |
| **技能** | 提供針對任務的指令 | 具體、可重複的任務及詳細步驟 |
| **MCP** | 連接外部服務 | 需要 API 即時資料 |

Agent 適合廣泛專業知識，技能適合具體任務指令，MCP 適合外部資料。Agent 在對話中可以套用一個或多個技能。例如，當你請 Agent 檢查程式碼時，它可能會自動套用 `security-audit` 技能和 `code-checklist` 技能。

> 📚 **深入了解**：請參考官方 [About Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills) 文件，獲得完整技能格式與最佳實踐說明。

---

## 從手動提示到自動專業

在學習如何建立技能之前，先看看*為什麼*值得學。當你看到一致性的提升後，「如何做」就更容易理解。

### 沒有技能時：審查不一致

每次程式碼審查，你可能會漏掉某些項目：

```bash
copilot

> Review this code for issues
# 一般審查——可能漏掉團隊特定關注點
```

或者每次都要寫很長的提示詞：

```bash
> Review this code checking for bare except clauses, missing type hints,
> mutable default arguments, missing context managers for file I/O,
> functions over 50 lines, print statements in production code...
```

時間：**30+ 秒**打字。審查一致性：**取決於記憶力**。

### 有技能後：自動最佳實踐

安裝 `code-checklist` 技能後，只要自然提問：

```bash
copilot

> Check the book collection code for quality issues
```

**背後發生的事**：
1. Copilot 在你的提示詞中看到「code quality」和「issues」
2. 檢查技能描述，找到符合的 `code-checklist` 技能
3. 自動載入團隊品質檢查清單
4. 套用所有檢查項目，不需你逐一列出

<img src="images/skill-auto-discovery-flow.png" alt="How Skills Auto-Trigger - 4-step flow showing how Copilot automatically matches your prompt to the right skill" width="800"/>

*只要自然提問。Copilot 會自動比對提示詞並套用正確技能。*

**輸出**：
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

**差異**：團隊標準每次都自動套用，不需手動輸入。

---

<details>
<summary>🎬 實際操作展示！</summary>

![Skill Trigger Demo](images/skill-trigger-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與此不同。*

</details>

---

## 大規模一致性：團隊 PR 審查技能

假設你的團隊有 10 點 PR 檢查清單。沒有技能時，每位開發者都必須記住全部 10 點，總有人會漏掉。安裝 `pr-review` 技能後，全團隊都能一致審查：

```bash
copilot

> Can you review this PR?
```

Copilot 會自動載入團隊的 `pr-review` 技能並檢查所有 10 點：

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

**威力**：每位團隊成員都能自動套用相同標準。新進人員不用背檢查清單，技能會自動處理。

---

# 建立自訂技能

<img src="images/creating-managing-skills.png" alt="Human and robotic hands building a wall of glowing LEGO-like blocks representing skill creation and management" width="800"/>

從 SKILL.md 檔案打造自己的技能。

---

## 技能存放位置

技能儲存在 `.github/skills/`（專案專屬）或 `~/.copilot/skills/`（使用者層級）。

### Copilot 如何尋找技能

Copilot 會自動掃描以下位置尋找技能：

| 位置 | 範圍 |
|----------|-------|
| `.github/skills/` | 專案專屬（透過 git 與團隊共享） |
| `~/.copilot/skills/` | 使用者專屬（個人技能） |

### 技能結構

每個技能都在自己的資料夾內，並有一個 `SKILL.md` 檔案。你可以選擇性加入腳本、範例或其他資源：

```
.github/skills/
└── my-skill/
    ├── SKILL.md           # 必須：技能定義與指令
    ├── examples/          # 選擇性：Copilot 可參考的範例檔案
    │   └── sample.py
    └── scripts/           # 選擇性：技能可用的腳本
        └── validate.sh
```

> 💡 **提示**：資料夾名稱應與 SKILL.md frontmatter 的 `name` 相同（小寫並用連字號）。

### SKILL.md 格式

技能採用簡單的 Markdown 格式，搭配 YAML frontmatter：

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

| 屬性 | 必須 | 說明 |
|----------|----------|-------------|
| `name` | **是** | 唯一識別名稱（小寫、空格用連字號） |
| `description` | **是** | 技能用途及 Copilot 何時應該使用 |
| `license` | 否 | 技能適用的授權條款 |

> 📖 **官方文件**：[About Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills)

### 建立你的第一個技能

來建立一個安全性稽核技能，檢查 OWASP Top 10 漏洞：

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

# 測試你的技能（技能會根據提示詞自動載入）
copilot

> @samples/book-app-project/ Check this code for security vulnerabilities
# Copilot 偵測到 "security vulnerabilities" 符合你的技能
# 並自動套用 OWASP 檢查清單
```

**預期輸出**（結果會有所不同）：

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

SKILL.md 的 `description` 欄位非常重要！Copilot 就是靠它判斷是否要載入你的技能：

```markdown
---
name: security-audit
description: Use for security reviews, vulnerability scanning,
  checking for SQL injection, XSS, authentication issues,
  OWASP Top 10 vulnerabilities, and security best practices
---
```

> 💡 **提示**：加入你平常提問時會用到的關鍵字。如果你會說「security review」，請在描述中包含「security review」。

### 技能與 Agent 結合運用

技能與 Agent 可協同運作。Agent 提供專業知識，技能提供具體指令：

```bash
# 使用 code-reviewer Agent
copilot --agent code-reviewer

> Check the book app for quality issues
# code-reviewer Agent 的專業結合
# code-checklist 技能的檢查清單
```

---

# 管理與分享技能

探索已安裝技能、尋找社群技能、並分享自己的技能。

<img src="images/managing-sharing-skills.png" alt="Managing and Sharing Skills - showing the discover, use, create, and share cycle for CLI skills" width="800" />

---

## 使用 `/skills` 指令管理技能

用 `/skills` 指令管理已安裝技能：

| 指令 | 功能說明 |
|---------|--------------|
| `/skills list` | 顯示所有已安裝技能 |
| `/skills info <name>` | 查看特定技能詳細資訊 |
| `/skills add <name>` | 啟用技能（從儲存庫或市集） |
| `/skills remove <name>` | 停用或解除安裝技能 |
| `/skills reload` | 編輯 SKILL.md 後重新載入技能 |

> 💡 **提醒**：你不需要每次提示都「啟用」技能。安裝後，技能會在提示詞符合描述時**自動觸發**。這些指令是用來管理技能是否可用，不是用來使用技能。

### 範例：查看你的技能

```bash
copilot

> /skills list

Available skills:
- security-audit: Security-focused code review checking OWASP Top 10
- generate-tests: Generate comprehensive unit tests with edge cases
- code-checklist: Team code quality checklist
...

> /skills info security-audit

Skill: security-audit
Source: Project
Location: .github/skills/security-audit/SKILL.md
Description: Security-focused code review checking OWASP Top 10 vulnerabilities
```

---

<details>
<summary>實際操作展示！</summary>

![List Skills Demo](images/list-skills-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與此不同。*

</details>

---

### 何時使用 `/skills reload`

建立或編輯技能的 SKILL.md 檔案後，執行 `/skills reload` 以載入變更，無需重啟 Copilot：

```bash
# 編輯技能檔案
# 然後在 Copilot 中：
> /skills reload
Skills reloaded successfully.
```

> 💡 **補充說明**：即使使用 `/compact` 來摘要對話紀錄，技能仍然有效。壓縮後不需重新載入技能。

---

## 尋找與使用社群技能

### 使用插件安裝技能

> 💡 **什麼是插件？** 插件是可安裝的套件，可以同時包含技能、Agent 和 MCP 伺服器設定。就像 Copilot CLI 的「應用程式商店」擴充功能。

使用 `/plugin` 指令瀏覽並安裝這些套件：

```bash
copilot

> /plugin list
# 顯示已安裝插件

> /plugin marketplace
# 瀏覽可用插件

> /plugin install <plugin-name>
# 從市集安裝插件
```

要保持本地插件目錄最新，請執行：

```bash
copilot plugin marketplace update
```

插件可以同時包含多種功能。一個插件可能包含相關技能、Agent 和 MCP 伺服器設定，協同運作。

### 社群技能儲存庫

也有現成技能可從社群儲存庫取得：

- **[Awesome Copilot](https://github.com/github/awesome-copilot)** - 官方 GitHub Copilot 資源，包括技能文件與範例

### 手動安裝社群技能

如果你在 GitHub 儲存庫找到技能，將其資料夾複製到你的技能目錄：

```bash
# 下載 awesome-copilot 儲存庫
git clone https://github.com/github/awesome-copilot.git /tmp/awesome-copilot

# 將特定技能複製到專案
cp -r /tmp/awesome-copilot/skills/code-checklist .github/skills/

# 或個人用途（所有專案都能用）
cp -r /tmp/awesome-copilot/skills/code-checklist ~/.copilot/skills/
```

> ⚠️ **安裝前請檢查**：安裝技能前務必閱讀其 `SKILL.md`。技能會控制 Copilot 行為，惡意技能可能指示 Copilot 執行危險命令或意外修改程式碼。

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

實作你所學，打造並測試自己的技能。

---

## ▶️ 自己動手試試看

### 建立更多技能

這裡有兩個不同模式的技能範例。請依照「建立你的第一個技能」的 `mkdir` + `cat` 流程操作，或直接複製貼到正確位置。更多範例可見於 [.github/skills](../.github/skills)。

### pytest 測試產生技能

一個確保全程式碼庫 pytest 結構一致的技能：

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

一個強制團隊 PR 審查標準一致的技能：

```bash
mkdir -p .github/skills/pr-review

cat > .github/skills/pr-review/SKILL.md << 'EOF'
---
name: pr-review
description: Team-standard PR review checklist
---

# PR Review

Review code changes against team standards:

## Security Checklist
- [ ] No hardcoded secrets or API keys
- [ ] Input validation on all user data
- [ ] No bare except clauses
- [ ] No sensitive data in logs

## Code Quality
- [ ] Functions under 50 lines
- [ ] No print statements in production code
- [ ] Type hints on public functions
- [ ] Context managers for file I/O
- [ ] No TODOs without issue references

## Testing
- [ ] New code has tests
- [ ] Edge cases covered
- [ ] No skipped tests without explanation

## Documentation
- [ ] API changes documented
- [ ] Breaking changes noted
- [ ] README updated if needed

## Output Format
Provide results as:
- ✅ PASS: Items that look good
- ⚠️ WARN: Items that could be improved
- ❌ FAIL: Items that must be fixed before merge
EOF
```

### 更進一步

1. **技能創建挑戰**：建立一個 `quick-review` 技能，檢查三點：
   - bare except 子句
   - 缺少型別提示
   - 不明確的變數名稱

   測試時請提問：「Do a quick review of books.py」

2. **技能比較**：計時你手動撰寫詳細安全審查提示詞的時間。然後只問「Check for security issues in this file」，讓 security-audit 技能自動載入。技能為你省下多少時間？

3. **團隊技能挑戰**：思考你們團隊的程式碼審查清單。能否將它編碼成技能？寫下技能應該永遠檢查的三項內容。

**自我檢查**：你能解釋為什麼 `description` 欄位重要（Copilot 就是靠它判斷是否要載入技能），就表示你理解技能了。

---

## 📝 作業

### 主要挑戰：建立書籍摘要技能

上述範例建立了 `pytest-gen` 和 `pr-review` 技能。現在請練習建立完全不同類型的技能：用來根據資料產生格式化輸出。

1. 列出你目前的技能：執行 Copilot 並輸入 `/skills list`。也可用 `ls .github/skills/` 查看專案技能，或 `ls ~/.copilot/skills/` 查看個人技能。
2. 建立一個 `book-summary` 技能於 `.github/skills/book-summary/SKILL.md`，能產生書籍收藏的格式化 Markdown 摘要
3. 技能內容需包含：
   - 清楚的名稱與描述（描述很重要，決定是否能匹配！）
   - 明確的格式規則（例如：用 Markdown 表格列出書名、作者、年份、閱讀狀態）
   - 輸出慣例（例如：閱讀狀態用 ✅/❌ 表示，依年份排序）
4. 測試技能：`@samples/book-app-project/data.json Summarize the books in this collection`
5. 確認技能自動觸發，可用 `/skills list` 檢查
6. 嘗試用 `/book-summary Summarize the books in this collection` 直接呼叫

**成功標準**：你有一個可用的 `book-summary` 技能，Copilot 能在你詢問書籍收藏時自動套用。

<details>
<summary>💡 提示（點擊展開）</summary>

**起始範本**：建立 `.github/skills/book-summary/SKILL.md`：

```markdown
---
name: book-summary
description: Generate a formatted markdown summary of a book collection
---

# Book Summary Generator

根據以下規則產生書籍收藏的摘要：

1. 輸出一個包含以下欄位的 Markdown 表格：Title、Author、Year、Status
2. 已閱讀的書籍使用 ✅，未閱讀的書籍使用 ❌
3. 依年份排序（由最舊到最新）
4. 在底部加入總數統計
5. 標示任何資料問題（如缺少作者、年份無效）

範例：
| Title | Author | Year | Status |
|-------|--------|------|--------|
| 1984 | George Orwell | 1949 | ✅ |
| Dune | Frank Herbert | 1965 | ❌ |

**總計：2 本書（1 已讀，1 未讀）**
```

**測試方法：**
```bash
copilot
> @samples/book-app-project/data.json Summarize the books in this collection
# 技能應該會根據描述自動觸發
```

**如果沒有觸發：** 請嘗試 `/skills reload`，然後再詢問一次。

</details>

### 加分挑戰：提交訊息技能

1. 建立一個 `commit-message` 技能，能以一致格式產生 conventional commit 訊息
2. 透過暫存變更並詢問：「Generate a commit message for my staged changes」來測試
3. 撰寫技能文件並在 GitHub 上以 `copilot-skill` 標籤分享

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生狀況 | 解決方式 |
|------|----------|----------|
| 檔案命名不是 `SKILL.md` | 技能無法被辨識 | 檔案必須正確命名為 `SKILL.md` |
| `description` 欄位過於模糊 | 技能永遠不會自動載入 | 描述是主要的觸發機制，請使用具體的關鍵字 |
| frontmatter 缺少 `name` 或 `description` | 技能載入失敗 | 在 YAML frontmatter 中加入這兩個欄位 |
| 資料夾位置錯誤 | 技能找不到 | 使用 `.github/skills/skill-name/`（專案）或 `~/.copilot/skills/skill-name/`（個人） |

### 疑難排解

**技能未被使用**－如果 Copilot 沒有在預期時使用你的技能：

1. **檢查描述內容**：是否與你的詢問方式相符？
   ```markdown
   # 不佳：太模糊
   description: Reviews code

   # 良好：包含觸發關鍵字
   description: Use for code reviews, checking code quality,
     finding bugs, security issues, and best practice violations
   ```

2. **確認檔案位置**：
   ```bash
   # 專案技能
   ls .github/skills/

   # 個人技能
   ls ~/.copilot/skills/
   ```

3. **檢查 SKILL.md 格式**：必須有 frontmatter：
   ```markdown
   ---
   name: skill-name
   description: What the skill does and when to use it
   ---

   # 指令說明寫在這裡
   ```

**技能未出現**－確認資料夾結構：
```
.github/skills/
└── my-skill/           # 資料夾名稱
    └── SKILL.md        # 必須正確命名為 SKILL.md（區分大小寫）
```

建立或編輯技能後，請執行 `/skills reload` 以確保變更被載入。

**測試技能是否載入**－直接詢問 Copilot：
```bash
> What skills do you have available for checking code quality?
# Copilot 會描述找到的相關技能
```

**如何確認技能真的有作用？**

1. **檢查輸出格式**：如果技能指定了輸出格式（如 `[CRITICAL]` 標籤），請在回應中尋找這些標記
2. **直接詢問**：取得回應後，問「Did you use any skills for that?」
3. **比較有無技能**：用 `--no-custom-instructions` 重複同一提示，觀察差異：
   ```bash
   # 有技能
   copilot --allow-all -p "Review @file.py for security issues"

   # 無技能（基準比較）
   copilot --allow-all -p "Review @file.py for security issues" --no-custom-instructions
   ```
4. **尋找特定檢查**：如果技能包含特定檢查（如「函式超過 50 行」），請確認這些內容是否出現在輸出中

</details>

---

# 摘要

## 🔑 重點整理

1. **技能自動載入**：Copilot 會在你的提示詞符合技能描述時自動載入技能
2. **直接呼叫**：也可以用 `/skill-name` 斜線指令直接呼叫技能
3. **SKILL.md 格式**：YAML frontmatter（name、description、可選 license）加上 Markdown 指令說明
4. **位置很重要**：專案／團隊共用用 `.github/skills/`，個人用 `~/.copilot/skills/`
5. **描述是關鍵**：撰寫描述時要符合你自然詢問問題的方式

> 📋 **快速參考**：完整指令與捷徑請參見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

技能能自動載入指令，擴展 Copilot 的能力。但如果要連接外部服務呢？這就是 MCP 的用途。

在 **[第 06 章：MCP 伺服器](../06-mcp-servers/README.md)**，你將學到：

- MCP（模型情境協定）是什麼
- 如何連接 GitHub、檔案系統與文件服務
- MCP 伺服器設定方式
- 多伺服器工作流程

---

**[← 回到第 04 章](../04-agents-custom-instructions/README.md)** | **[繼續前往第 06 章 →](../06-mcp-servers/README.md)**
