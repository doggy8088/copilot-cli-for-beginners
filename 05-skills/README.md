![Chapter 05: Skills System](images/chapter-header.png)

> **如果 Copilot 能自動套用你們團隊的最佳實踐，而你不必每次都解釋，會怎麼樣？**

在本章中，你將學習 Agent 技能：Copilot 會在與你的任務相關時自動載入的指令資料夾。Agent 會改變 Copilot「思考的方式」，而技能則教 Copilot「完成任務的具體方法」。你將建立一個安全稽核技能，讓 Copilot 在你詢問安全性時自動套用，打造團隊標準的審查規範，確保程式碼品質一致，並學習技能如何在 Copilot CLI、VS Code 及 GitHub Copilot 雲端代理人中運作。

## 🎯 學習目標

完成本章後，你將能夠：

- 了解 Agent 技能的運作方式及使用時機
- 以 SKILL.md 檔案建立自訂技能
- 使用來自社群的技能（共用儲存庫）
- 知道何時該用技能、Agent 或 MCP

> ⏱️ **預估時間**：~55 分鐘（20 分鐘閱讀 + 35 分鐘實作）

---

## 🧩 真實世界比喻：電動工具

一般的電鑽很實用，但專用配件讓它更強大。
<img src="images/power-tools-analogy.png" alt="Power Tools - Skills Extend Copilot's Capabilities" width="800"/>

技能的運作方式也一樣。就像根據不同工作更換鑽頭，你可以為 Copilot 加入不同任務的技能：

| 技能配件 | 目的 |
|------------|---------|
| `commit` | 產生一致的提交訊息 |
| `security-audit` | 檢查 OWASP 漏洞 |
| `generate-tests` | 建立完整的 pytest 測試 |
| `code-checklist` | 套用團隊程式碼品質標準 |

*技能是專用配件，能擴充 Copilot 的能力*

---

# 技能的運作方式

<img src="images/how-skills-work.png" alt="Glowing RPG-style skill icons connected by light trails on a starfield background representing Copilot skills" width="800"/>

了解什麼是技能、為什麼重要，以及它們與 Agent 和 MCP 的差異。

---

## *第一次接觸技能？* 從這裡開始！

1. **查看目前有哪些技能可用：**
   ```bash
   copilot
   > /skills list
   ```
   這會顯示 Copilot 能找到的所有技能，包括 CLI 內建的**內建技能**，以及來自你專案和個人資料夾的技能。

   > 💡 **內建技能**：Copilot CLI 預設就有內建技能。例如，`customizing-copilot-cloud-agents-environment` 技能提供自訂 Copilot 雲端代理人環境的指南。你不需要建立或安裝就能使用。執行 `/skills list` 查看有哪些技能可用。

2. **看看實際的技能檔案：** 參考我們提供的 [code-checklist SKILL.md](../.github/skills/code-checklist/SKILL.md) 來了解範例格式。它就是 YAML frontmatter 加上 markdown 指令。

3. **理解核心概念：** 技能是針對任務的指令，只要你的提示詞符合技能描述，Copilot 就會*自動*載入。你不需要手動啟用，只要自然提問即可。

## 認識技能

Agent 技能是一個資料夾，內含指令、腳本和資源，Copilot 會在**與你的任務相關時自動載入**。Copilot 會讀取你的提示詞，檢查是否有技能符合，並自動套用相關指令。

```bash
copilot

> Check books.py against our quality checklist
# Copilot 偵測到這符合你的 "code-checklist" 技能
# 並自動套用 Python 品質檢查表

> Generate tests for the BookCollection class
# Copilot 載入你的 "pytest-gen" 技能
# 並套用你偏好的測試結構

> What are the code quality issues in this file?
# Copilot 載入你的 "code-checklist" 技能
# 並依團隊標準檢查
```

> 💡 **關鍵洞見**：技能會根據你的提示詞是否符合技能描述**自動觸發**。只要自然提問，Copilot 就會在背後自動套用相關技能。你也可以直接呼叫技能，接下來會介紹。

> 🧰 **現成範本**：參考 [.github/skills](../.github/skills/) 資料夾，有許多可直接複製貼上的技能範例。

### 直接斜線指令呼叫

雖然自動觸發是技能的主要運作方式，你也可以用技能名稱作為斜線指令**直接呼叫技能**：

```bash
> /generate-tests Create tests for the user authentication module

> /code-checklist Check books.py for code quality issues

> /security-audit Check the API endpoints for vulnerabilities
```

這讓你在需要時能明確指定要用哪個技能。

> 📝 **技能 vs Agent 呼叫**：不要混淆技能呼叫和 Agent 呼叫：
> - **技能**：`/skill-name <prompt>`，例如 `/code-checklist Check this file`
> - **Agent**：`/agent`（從清單選擇）或 `copilot --agent <name>`（命令列）
>
> 如果你同時有同名的技能和 Agent（例如 "code-reviewer"），輸入 `/code-reviewer` 會呼叫**技能**，而不是 Agent。

### 如何知道 Copilot 用了哪些技能？

你可以直接問 Copilot：

```bash
> What skills did you use for that response?

> What skills do you have available for security reviews?
```

### 技能 vs Agent vs MCP

技能只是 GitHub Copilot 擴充模型的一部分。以下是它們與 Agent 和 MCP 伺服器的比較。

> *不用現在擔心 MCP。我們會在[第六章](../06-mcp-servers/)介紹。這裡先讓你了解技能在整體架構中的定位。*

<img src="images/skills-agents-mcp-comparison.png" alt="Comparison diagram showing the differences between Agents, Skills, and MCP Servers and how they combine into your workflow" width="800"/>

| 功能 | 作用 | 使用時機 |
|---------|--------------|-------------|
| **Agent** | 改變 AI 的思考方式 | 需要跨多任務的專業知識 |
| **技能** | 提供任務專屬指令 | 具體、可重複的細部任務 |
| **MCP** | 連接外部服務 | 需要即時 API 資料 |

廣泛專業用 Agent，具體任務指令用技能，外部資料用 MCP。Agent 在對話中可以用一個或多個技能。例如，當你請 Agent 檢查程式碼時，它可能會自動套用 `security-audit` 技能和 `code-checklist` 技能。

> 📚 **深入了解**：參考官方 [About Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills) 文件，完整說明技能格式與最佳實踐。

---

## 從手動提示到自動專業

在學習如何建立技能之前，先看看*為什麼*值得學。當你看到一致性的提升，學「怎麼做」會更有感。

### 沒有技能時：審查品質不一

每次程式碼審查，你可能都會漏掉某些項目：

```bash
copilot

> Review this code for issues
# 一般審查——可能漏掉你們團隊特有的重點
```

或是每次都要寫很長的提示：

```bash
> Review this code checking for bare except clauses, missing type hints,
> mutable default arguments, missing context managers for file I/O,
> functions over 50 lines, print statements in production code...
```

花費時間：**30+ 秒**。一致性：**靠記憶，品質不一**。

### 有技能後：自動套用最佳實踐

安裝 `code-checklist` 技能後，只要自然提問：

```bash
copilot

> Check the book collection code for quality issues
```

**背後發生的事**：
1. Copilot 偵測你的提示詞有「code quality」、「issues」
2. 檢查技能描述，發現 `code-checklist` 技能符合
3. 自動載入團隊品質檢查表
4. 全部檢查自動執行，你不用一條條列出

<img src="images/skill-auto-discovery-flow.png" alt="How Skills Auto-Trigger - 4-step flow showing how Copilot automatically matches your prompt to the right skill" width="800"/>

*只要自然提問，Copilot 會自動比對並套用正確的技能。*

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

**差異**：團隊標準每次都自動套用，不用每次手動輸入。

---

<details>
<summary>🎬 實際操作影片</summary>

![Skill Trigger Demo](images/skill-trigger-demo.gif)

*Demo 輸出會有差異。你的模型、工具和回應可能與此不同。*

</details>

---

## 一致性擴展：團隊 PR 審查技能

假設你們團隊有 10 點 PR 檢查表。沒有技能時，每個開發者都得記住全部 10 點，總有人會漏掉。有了 `pr-review` 技能，全團隊都能一致審查：

```bash
copilot

> Can you review this PR?
```

Copilot 會自動載入團隊的 `pr-review` 技能，檢查全部 10 點：

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

**威力**：每位團隊成員都自動套用相同標準。新進人員不用背檢查表，技能會自動處理。

---

# 建立自訂技能

<img src="images/creating-managing-skills.png" alt="Human and robotic hands building a wall of glowing LEGO-like blocks representing skill creation and management" width="800"/>

從 SKILL.md 檔案打造自己的技能。

---

## 技能存放位置

技能儲存在 `.github/skills/`（專案專屬）或 `~/.copilot/skills/`（使用者層級）。

### Copilot 如何尋找技能

Copilot 會自動掃描這些位置尋找技能：

| 位置 | 範圍 |
|----------|-------|
| `.github/skills/` | 專案專屬（透過 git 與團隊共用） |
| `~/.copilot/skills/` | 使用者專屬（你的個人技能） |

### 技能結構

每個技能放在自己的資料夾，內有一個 `SKILL.md` 檔案。你也可以選擇加入腳本、範例或其他資源：

```
.github/skills/
└── my-skill/
    ├── SKILL.md           # 必要：技能定義與指令
    ├── examples/          # 選用：Copilot 可參考的範例檔案
    │   └── sample.py
    └── scripts/           # 選用：技能可用的腳本
        └── validate.sh
```

> 💡 **提示**：資料夾名稱應與 SKILL.md frontmatter 的 `name` 欄位一致（小寫並用連字號）。

### SKILL.md 格式

技能使用簡單的 markdown 格式，搭配 YAML frontmatter：

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

**YAML 屬性：**

| 屬性 | 必要 | 說明 |
|----------|----------|-------------|
| `name` | **是** | 唯一識別名稱（小寫、空格用連字號） |
| `description` | **是** | 技能作用及 Copilot 何時應該載入 |
| `license` | 否 | 技能適用的授權條款 |

> 📖 **官方文件**：[About Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills)

### 建立你的第一個技能

讓我們建立一個檢查 OWASP Top 10 漏洞的安全稽核技能：

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
# 並自動套用 OWASP 檢查表
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

## 撰寫好的技能描述

你的 SKILL.md 中 `description` 欄位很重要！Copilot 會根據這欄決定是否載入你的技能：

```markdown
---
name: security-audit
description: Use for security reviews, vulnerability scanning,
  checking for SQL injection, XSS, authentication issues,
  OWASP Top 10 vulnerabilities, and security best practices
---
```

> 💡 **提示**：請包含你平常提問時會用到的關鍵字。如果你會說「security review」，就把「security review」寫進 description。

### 技能與 Agent 結合

技能和 Agent 可以搭配運作。Agent 提供專業知識，技能提供具體指令：

```bash
# 啟動 code-reviewer agent
copilot --agent code-reviewer

> Check the book app for quality issues
# code-reviewer agent 的專業知識
# 結合 code-checklist 技能的檢查表
```

---

# 管理與分享技能

發現已安裝的技能、尋找社群技能、並分享你自己的技能。

<img src="images/managing-sharing-skills.png" alt="Managing and Sharing Skills - showing the discover, use, create, and share cycle for CLI skills" width="800" />

---

## 用 `/skills` 指令管理技能

使用 `/skills` 指令管理你已安裝的技能：

| 指令 | 作用 |
|---------|--------------|
| `/skills list` | 顯示所有已安裝技能 |
| `/skills info <name>` | 取得特定技能詳細資訊 |
| `/skills add <name>` | 啟用技能（從儲存庫或市集） |
| `/skills remove <name>` | 停用或解除安裝技能 |
| `/skills reload` | 編輯 SKILL.md 後重新載入技能 |

> 💡 **記得**：你不需要每次提示都「啟用」技能。安裝後，只要提示詞符合描述，技能就會**自動觸發**。這些指令是用來管理可用技能，不是用來執行技能。

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
<summary>實際操作影片</summary>

![List Skills Demo](images/list-skills-demo.gif)

*Demo 輸出會有差異。你的模型、工具和回應可能與此不同。*

</details>

---

### 什麼時候要用 `/skills reload`

建立或編輯技能的 SKILL.md 後，執行 `/skills reload` 就能載入變更，無需重啟 Copilot：

```bash
# 編輯技能檔案
# 然後在 Copilot 輸入：
> /skills reload
Skills reloaded successfully.
```

> 💡 **補充**：即使你用 `/compact` 摘要對話紀錄，技能依然有效。不需 compact 後再 reload。

---

## 尋找與使用社群技能

### 用外掛安裝技能

> 💡 **什麼是外掛？** 外掛是可安裝的套件，可以同時包含技能、Agent 和 MCP 伺服器設定。就像 Copilot CLI 的「應用程式商店」擴充功能。

用 `/plugin` 指令瀏覽並安裝這些套件：

```bash
copilot

> /plugin list
# 顯示已安裝外掛

> /plugin marketplace
# 瀏覽可用外掛

> /plugin install <plugin-name>
# 從市集安裝外掛
```

要讓本地外掛清單保持最新，請執行：

```bash
copilot plugin marketplace update
```

外掛可以同時包含多種功能。一個外掛可能同時有相關技能、Agent 和 MCP 伺服器設定。

### 社群技能儲存庫

也可從社群儲存庫取得現成技能：

- **[Awesome Copilot](https://github.com/github/awesome-copilot)** - 官方 GitHub Copilot 資源，包含技能文件與範例

### 用 GitHub CLI 安裝社群技能

從 GitHub 儲存庫安裝技能最簡單的方式是用 `gh skill install` 指令（需 [GitHub CLI v2.90.0+](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/)）：

```bash
# 互動式瀏覽並選擇 awesome-copilot 技能
gh skill install github/awesome-copilot

# 或直接安裝特定技能
gh skill install github/awesome-copilot code-checklist

# 安裝到所有專案（使用者範圍）
gh skill install github/awesome-copilot code-checklist --scope user
```

> ⚠️ **安裝前請審查**：安裝前務必閱讀技能的 `SKILL.md`。技能會控制 Copilot 的行為，惡意技能可能指示 Copilot 執行有害指令或異常修改程式碼。

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

動手打造並測試自己的技能，應用所學。

---

## ▶️ 自己試試看

### 建立更多技能

這裡有兩個不同模式的技能範例。請依「建立你的第一個技能」的 `mkdir` + `cat` 流程操作，或直接複製貼上到正確位置。更多範例見 [.github/skills](../.github/skills)。

### pytest 測試產生技能

一個確保全專案 pytest 結構一致的技能：

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

1. **技能創作挑戰**：建立一個 `quick-review` 技能，檢查三點：
   - bare except 子句
   - 缺少型別註記
   - 變數命名不清楚

   測試方式：「Do a quick review of books.py」

2. **技能比較**：計時你手動寫一個詳細安全審查提示要多久。然後只輸入「Check for security issues in this file」，讓 security-audit 技能自動載入。技能幫你省下多少時間？

3. **團隊技能挑戰**：想想你們團隊的程式碼審查清單。能否把它寫成一個技能？列出技能應該永遠檢查的三件事。

**自我檢查**：你能解釋 `description` 欄位為什麼重要（Copilot 會根據它決定是否載入技能），就代表你真的懂技能了。

---

## 📝 作業

### 主要挑戰：建立書籍摘要技能

上面範例建立了 `pytest-gen` 和 `pr-review` 技能。現在請練習建立完全不同類型的技能：產生資料格式化輸出的技能。

1. 列出你目前的技能：執行 Copilot 並輸入 `/skills list`。你也可以用 `ls .github/skills/` 查看專案技能，或 `ls ~/.copilot/skills/` 查看個人技能。
2. 在 `.github/skills/book-summary/SKILL.md` 建立一個 `book-summary` 技能，能針對書籍收藏產生格式化的 markdown 摘要
3. 技能內容需包含：
   - 清楚的名稱與描述（描述對比對很關鍵！）
   - 明確的格式規則（例如：用 markdown 表格顯示書名、作者、年份、閱讀狀態）
   - 輸出規範（例如：閱讀狀態用 ✅/❌，依年份排序）
4. 測試技能：`@samples/book-app-project/data.json Summarize the books in this collection`
5. 用 `/skills list` 確認技能有自動觸發
6. 試著用 `/book-summary Summarize the books in this collection` 直接呼叫

**成功標準**：你有一個運作中的 `book-summary` 技能，Copilot 會在你詢問書籍收藏時自動套用。

<details>
<summary>💡 提示（點擊展開）</summary>

**起始範本**：建立 `.github/skills/book-summary/SKILL.md`：

```markdown
---
name: book-summary
description: 產生格式化的書籍收藏 Markdown 摘要
---

# 書籍摘要產生器

請依照以下規則產生書籍收藏的摘要：

1. 輸出一個包含下列欄位的 Markdown 表格：Title、Author、Year、Status
2. 已讀書籍使用 ✅，未讀書籍使用 ❌
3. 依年份排序（由舊到新）
4. 在底部加入總數統計
5. 標註任何資料問題（如作者缺漏、年份無效）

範例：
| Title | Author | Year | Status |
|-------|--------|------|--------|
| 1984 | George Orwell | 1949 | ✅ |
| Dune | Frank Herbert | 1965 | ❌ |

**總計：2 本書（1 本已讀，1 本未讀）**
```

**測試方式：**
```bash
copilot
> @samples/book-app-project/data.json Summarize the books in this collection
# 技能應該會根據描述自動觸發
```

**若未自動觸發：** 請嘗試 `/skills reload` 後再詢問一次。

</details>

### 額外挑戰：Commit Message 技能

1. 建立一個 `commit-message` 技能，能以一致格式產生 conventional commit 訊息
2. 透過暫存變更並詢問：「Generate a commit message for my staged changes」來測試
3. 撰寫技能文件並在 GitHub 上以 `copilot-skill` 標籤分享

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 會發生什麼 | 修正方式 |
|------|------------|----------|
| 檔案名稱不是 `SKILL.md` | 技能無法被辨識 | 檔案名稱必須完全為 `SKILL.md` |
| `description` 欄位過於模糊 | 技能永遠不會自動載入 | description 是主要的自動發現機制，請使用明確的觸發關鍵字 |
| frontmatter 缺少 `name` 或 `description` | 技能載入失敗 | 在 YAML frontmatter 中加入這兩個欄位 |
| 資料夾位置錯誤 | 找不到技能 | 請使用 `.github/skills/skill-name/`（專案）或 `~/.copilot/skills/skill-name/`（個人） |

### 疑難排解

**技能未被使用**－如果 Copilot 沒有在預期時使用你的技能：

1. **檢查 description**：描述是否與你的提問方式相符？
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

   # 使用者技能
   ls ~/.copilot/skills/
   ```

3. **檢查 SKILL.md 格式**：frontmatter 必須存在：
   ```markdown
   ---
   name: skill-name
   description: What the skill does and when to use it
   ---

   # 指令內容寫在這裡
   ```

**技能未顯示**－請確認資料夾結構：
```
.github/skills/
└── my-skill/           # 資料夾名稱
    └── SKILL.md        # 必須完全為 SKILL.md（區分大小寫）
```

建立或編輯技能後，請執行 `/skills reload` 以確保變更被載入。

**測試技能是否載入**－可直接詢問 Copilot：
```bash
> What skills do you have available for checking code quality?
# Copilot 會描述它找到的相關技能
```

**如何確認技能真的有作用？**

1. **檢查輸出格式**：如果你的技能有指定輸出格式（如 `[CRITICAL]` 標籤），請在回應中尋找這些標記
2. **直接詢問**：取得回應後，問「Did you use any skills for that?」
3. **比較有無技能差異**：用 `--no-custom-instructions` 試試同一提示，觀察差異：
   ```bash
   # 有技能
   copilot --allow-all -p "Review @file.py for security issues"

   # 無技能（基準比較）
   copilot --allow-all -p "Review @file.py for security issues" --no-custom-instructions
   ```
4. **檢查特定檢查項目**：如果你的技能包含特定檢查（如「函式超過 50 行」），請確認這些內容是否出現在輸出中

</details>

---

# 摘要

## 🔑 重點整理

1. **技能會自動載入**：當你的提示詞符合技能描述時，Copilot 會自動載入技能
2. **可直接呼叫**：也可用 `/skill-name` 斜線指令直接呼叫技能
3. **SKILL.md 格式**：YAML frontmatter（name、description、可選 license）加上 Markdown 指令內容
4. **位置很重要**：專案／團隊共用放 `.github/skills/`，個人使用放 `~/.copilot/skills/`
5. **描述是關鍵**：請用自然提問方式撰寫 description

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

## ➡️ 下一步

技能讓 Copilot 能自動載入指令擴充功能。但如果要連接外部服務呢？這就需要 MCP。

在 **[第 06 章：MCP 伺服器](../06-mcp-servers/README.md)**，你將學到：

- 什麼是 MCP（模型情境協定）
- 如何連接 GitHub、檔案系統與文件服務
- MCP 伺服器設定方式
- 多伺服器協作流程

---

**[← 回到第 04 章](../04-agents-custom-instructions/README.md)** | **[繼續前往第 06 章 →](../06-mcp-servers/README.md)**
```
