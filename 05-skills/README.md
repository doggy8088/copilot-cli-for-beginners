![Chapter 05: Skills System](images/chapter-header.png)

> **如果 Copilot 能自動套用您團隊的最佳實踐，而您無需每次都重新說明，那會如何？**

在本章中，您將學習代理程式技能（Agent Skills）：這些資料夾包含指令，Copilot 會在與您任務相關時自動載入。代理程式改變的是 Copilot *如何*思考，而技能則教導 Copilot *以特定方式完成任務*。您將建立一個安全性稽核技能，讓 Copilot 在您詢問安全性問題時自動套用；建立符合團隊標準的審查標準，確保一致的程式碼品質；並了解技能如何在 Copilot CLI、VS Code 和 Copilot 程式碼代理程式之間運作。


## 🎯 學習目標

完成本章後，您將能夠：

- 了解代理程式技能的運作方式及使用時機
- 使用 SKILL.md 檔案建立自訂技能
- 使用共享程式庫中的社群技能
- 了解技能、代理程式與 MCP 各自的使用時機

> ⏱️ **預估時間**：約 55 分鐘（閱讀 20 分鐘 + 實作 35 分鐘）

---

## 🧩 真實世界類比：電動工具

通用電鑽雖然好用，但專用配件才能讓它如虎添翼。
<img src="images/power-tools-analogy.png" alt="Power Tools - Skills Extend Copilot's Capabilities" width="800"/>


技能的運作方式相同。就像為不同工作更換鑽頭，您可以為不同任務為 Copilot 添加技能：

| 技能配件 | 用途 |
|------------|---------|
| `commit` | 產生一致的提交訊息 |
| `security-audit` | 檢查 OWASP 漏洞 |
| `generate-tests` | 建立完整的 pytest 測試 |
| `code-checklist` | 套用團隊程式碼品質標準 |



*技能是擴展 Copilot 功能的專用配件*

---

# 技能的運作方式

<img src="images/how-skills-work.png" alt="Glowing RPG-style skill icons connected by light trails on a starfield background representing Copilot skills" width="800"/>

了解技能是什麼、為何重要，以及它們與代理程式和 MCP 有何不同。

---

## *初次使用技能？* 從這裡開始！

1. **查看已有哪些技能可用：**
   ```bash
   copilot
   > /skills list
   ```
   這會顯示 Copilot 在您的專案和個人資料夾中找到的所有技能。

2. **查看真實的技能檔案：** 看看我們提供的 [code-checklist SKILL.md](../.github/skills/code-checklist/SKILL.md)，了解其格式。它只是 YAML 前置資料加上 Markdown 指令。

3. **理解核心概念：** 技能是任務特定的指令，當您的提示詞符合技能的描述時，Copilot 會*自動*載入。您無需主動啟用，只要自然地提問即可。


## 了解技能

代理程式技能是包含指令、腳本和資源的資料夾，Copilot 在**與您的任務相關時自動載入**。Copilot 讀取您的提示詞，檢查是否有符合的技能，然後自動套用相關指令。

```bash
copilot

> Check books.py against our quality checklist
# Copilot detects this matches your "code-checklist" skill
# and automatically applies its Python quality checklist

> Generate tests for the BookCollection class
# Copilot loads your "pytest-gen" skill
# and applies your preferred test structure

> What are the code quality issues in this file?
# Copilot loads your "code-checklist" skill
# and checks against your team's standards
```

> 💡 **核心洞察**：技能根據您的提示詞與技能描述的匹配程度**自動觸發**。只要自然地提問，Copilot 就會在幕後套用相關技能。您也可以直接呼叫技能，這將在下一節介紹。

> 🧰 **隨取即用的範本**：請查看 [.github/skills](../.github/skills/) 資料夾，取得可直接複製使用的技能。

### 直接使用斜線指令呼叫

雖然自動觸發是技能的主要運作方式，您也可以使用技能名稱作為斜線指令來**直接呼叫技能**：

```bash
> /generate-tests Create tests for the user authentication module

> /code-checklist Check books.py for code quality issues

> /security-audit Check the API endpoints for vulnerabilities
```

當您想確保使用特定技能時，這能給您明確的控制權。

> 📝 **技能 vs. 代理程式的呼叫方式**：請勿混淆技能與代理程式的呼叫方式：
> - **技能**：`/技能名稱 <提示詞>`，例如 `/code-checklist Check this file`
> - **代理程式**：`/agent`（從清單選擇）或 `copilot --agent <名稱>`（命令列）
>
> 如果您同時有同名的技能和代理程式（例如「code-reviewer」），輸入 `/code-reviewer` 會呼叫**技能**，而非代理程式。

### 如何確認技能已被使用？

您可以直接詢問 Copilot：

```bash
> What skills did you use for that response?

> What skills do you have available for security reviews?
```

### 技能 vs. 代理程式 vs. MCP

技能只是 GitHub Copilot 擴充模型的一個環節。以下是它們與代理程式和 MCP 伺服器的比較。

> *暫時不用擔心 MCP。我們將在[第 06 章](../06-mcp-servers/)中介紹。這裡提及是為了讓您了解技能在整體架構中的定位。*

<img src="images/skills-agents-mcp-comparison.png" alt="Comparison diagram showing the differences between Agents, Skills, and MCP Servers and how they combine into your workflow" width="800"/>

| 功能 | 作用 | 使用時機 |
|---------|--------------|-------------|
| **代理程式** | 改變 AI 的思考方式 | 需要跨多項任務的專業知識 |
| **技能** | 提供任務特定的指令 | 具有詳細步驟的特定、可重複任務 |
| **MCP** | 連接外部服務 | 需要 API 的即時資料 |

代理程式用於廣泛的專業知識，技能用於特定任務指令，MCP 用於外部資料。在對話過程中，代理程式可以使用一個或多個技能。例如，當您要求代理程式檢查程式碼時，它可能會自動同時套用 `security-audit` 技能和 `code-checklist` 技能。

> 📚 **深入了解**：請參閱官方的 [About Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills) 文件，取得技能格式和最佳實踐的完整參考。

---

## 從手動提示詞到自動專業知識

在深入了解如何建立技能之前，讓我們先看看*為何*值得學習技能。一旦您看到一致性帶來的好處，「如何做」就會更容易理解。

### 沒有技能：審查結果參差不齊

每次程式碼審查，您可能都會忘記某些事項：

```bash
copilot

> Review this code for issues
# Generic review - might miss your team's specific concerns
```

或者每次都要輸入一長串提示詞：

```bash
> Review this code checking for bare except clauses, missing type hints,
> mutable default arguments, missing context managers for file I/O,
> functions over 50 lines, print statements in production code...
```

所需時間：輸入需 **30 秒以上**。一致性：**因記憶而異**。

### 有了技能：自動套用最佳實踐

安裝 `code-checklist` 技能後，只需自然地提問：

```bash
copilot

> Check the book collection code for quality issues
```

**幕後發生的事情**：
1. Copilot 在您的提示詞中看到「code quality」和「issues」
2. 檢查技能描述，發現您的 `code-checklist` 技能符合
3. 自動載入您團隊的品質清單
4. 套用所有檢查項目，無需您一一列舉

<img src="images/skill-auto-discovery-flow.png" alt="How Skills Auto-Trigger - 4-step flow showing how Copilot automatically matches your prompt to the right skill" width="800"/>

*只需自然地提問。Copilot 會將您的提示詞與適合的技能匹配並自動套用。*

**輸出結果**：
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

**差異所在**：您的團隊標準每次都會自動套用，無需再手動輸入。

---

<details>
<summary>🎬 看看實際效果！</summary>

![Skill Trigger Demo](images/skill-trigger-demo.gif)

*示範輸出因人而異。您的模型、工具和回應結果可能與這裡顯示的有所不同。*

</details>

---

## 規模化的一致性：團隊 PR 審查技能

試想您的團隊有一份 10 點 PR 清單。沒有技能時，每位開發者都必須記住所有 10 個要點，而總是有人會漏掉其中一點。有了 `pr-review` 技能，整個團隊的審查都能保持一致：

```bash
copilot

> Can you review this PR?
```

Copilot 自動載入您團隊的 `pr-review` 技能，並檢查所有 10 個要點：

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

**技能的威力**：每位團隊成員自動套用相同的標準。新人無需記住清單，因為技能已幫他們處理好了。

---

# 建立自訂技能

<img src="images/creating-managing-skills.png" alt="Human and robotic hands building a wall of glowing LEGO-like blocks representing skill creation and management" width="800"/>

使用 SKILL.md 檔案建立您自己的技能。

---

## 技能的存放位置

技能存放於 `.github/skills/`（專案特定）或 `~/.copilot/skills/`（使用者層級）。

### Copilot 如何找到技能

Copilot 會自動掃描以下位置尋找技能：

| 位置 | 適用範圍 |
|----------|-------|
| `.github/skills/` | 專案特定（透過 git 與團隊共用） |
| `~/.copilot/skills/` | 使用者特定（您的個人技能） |

### 技能結構

每個技能都存放在自己的資料夾中，包含一個 `SKILL.md` 檔案。您可以選擇性地加入腳本、範例或其他資源：

```
.github/skills/
└── my-skill/
    ├── SKILL.md           # Required: Skill definition and instructions
    ├── examples/          # Optional: Example files Copilot can reference
    │   └── sample.py
    └── scripts/           # Optional: Scripts the skill can use
        └── validate.sh
```

> 💡 **提示**：資料夾名稱應與 SKILL.md 前置資料中的 `name` 相符（小寫加連字號）。

### SKILL.md 格式

技能使用帶有 YAML 前置資料的簡單 Markdown 格式：

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

| 屬性 | 必填 | 說明 |
|----------|----------|-------------|
| `name` | **是** | 唯一識別碼（小寫，空格以連字號替代） |
| `description` | **是** | 技能的功能以及 Copilot 應何時使用它 |
| `license` | 否 | 適用於此技能的授權條款 |

> 📖 **官方文件**：[About Agent Skills](https://docs.github.com/copilot/concepts/agents/about-agent-skills)

### 建立您的第一個技能

讓我們建立一個用於檢查 OWASP Top 10 漏洞的安全性稽核技能：

```bash
# Create skill directory
mkdir -p .github/skills/security-audit

# Create the SKILL.md file
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

# Test your skill (skills load automatically based on your prompt)
copilot

> @samples/book-app-project/ Check this code for security vulnerabilities
# Copilot detects "security vulnerabilities" matches your skill
# and automatically applies its OWASP checklist
```

**預期輸出**（您的結果可能有所不同）：

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

SKILL.md 中的 `description` 欄位至關重要！它是 Copilot 決定是否載入您的技能的依據：

```markdown
---
name: security-audit
description: Use for security reviews, vulnerability scanning,
  checking for SQL injection, XSS, authentication issues,
  OWASP Top 10 vulnerabilities, and security best practices
---
```

> 💡 **提示**：加入符合您自然提問方式的關鍵字。如果您會說「security review」，請在描述中加入「security review」。

### 結合技能與代理程式

技能和代理程式可以協同運作。代理程式提供專業知識，技能提供具體指令：

```bash
# Start with a code-reviewer agent
copilot --agent code-reviewer

> Check the book app for quality issues
# code-reviewer agent's expertise combines
# with your code-checklist skill's checklist
```

---

# 管理與分享技能

探索已安裝的技能，尋找社群技能，並分享您自己的技能。

<img src="images/managing-sharing-skills.png" alt="Managing and Sharing Skills - showing the discover, use, create, and share cycle for CLI skills" width="800" />

---

## 使用 `/skills` 指令管理技能

使用 `/skills` 指令來管理您已安裝的技能：

| 指令 | 功能說明 |
|---------|--------------|
| `/skills list` | 顯示所有已安裝的技能 |
| `/skills info <name>` | 取得特定技能的詳細資訊 |
| `/skills add <name>` | 啟用技能（來自程式庫或市集） |
| `/skills remove <name>` | 停用或解除安裝技能 |
| `/skills reload` | 編輯 SKILL.md 檔案後重新載入技能 |

> 💡 **記住**：您無需為每個提示詞「啟用」技能。技能一經安裝，當您的提示詞符合其描述時便會**自動觸發**。這些指令用於管理哪些技能可用，而非用於使用技能。

### 範例：查看您的技能

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
<summary>看看實際效果！</summary>

![List Skills Demo](images/list-skills-demo.gif)

*示範輸出因人而異。您的模型、工具和回應結果可能與這裡顯示的有所不同。*

</details>

---

### 何時使用 `/skills reload`

建立或編輯技能的 SKILL.md 檔案後，執行 `/skills reload` 以套用變更，無需重新啟動 Copilot：

```bash
# Edit your skill file
# Then in Copilot:
> /skills reload
Skills reloaded successfully.
```

> 💡 **補充知識**：使用 `/compact` 壓縮對話歷程後，技能仍然有效，無需重新載入。

---

## 尋找和使用社群技能

### 使用外掛安裝技能

> 💡 **什麼是外掛？** 外掛是可安裝的套件，可將技能、代理程式和 MCP 伺服器設定打包在一起。可以把它們想像成 Copilot CLI 的「應用程式商店」擴充功能。

`/plugin` 指令讓您能夠瀏覽和安裝這些套件：

```bash
copilot

> /plugin list
# Shows installed plugins

> /plugin marketplace
# Browse available plugins

> /plugin install <plugin-name>
# Install a plugin from the marketplace
```

外掛可以將多種功能捆綁在一起——單一外掛可能包含相互配合的相關技能、代理程式和 MCP 伺服器設定。

### 社群技能程式庫

現成的技能也可從社群程式庫取得：

- **[Awesome Copilot](https://github.com/github/awesome-copilot)** - 官方 GitHub Copilot 資源，包含技能文件和範例

### 手動安裝社群技能

如果您在 GitHub 程式庫中找到技能，請將其資料夾複製到您的技能目錄：

```bash
# Clone the awesome-copilot repository
git clone https://github.com/github/awesome-copilot.git /tmp/awesome-copilot

# Copy a specific skill to your project
cp -r /tmp/awesome-copilot/skills/code-checklist .github/skills/

# Or for personal use across all projects
cp -r /tmp/awesome-copilot/skills/code-checklist ~/.copilot/skills/
```

> ⚠️ **安裝前請先審查**：在將技能複製到您的專案之前，務必先閱讀其 `SKILL.md`。技能控制 Copilot 的行為，惡意技能可能會指示它執行有害指令或以意外方式修改程式碼。

---

# 練習

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

透過建立和測試您自己的技能，將所學付諸實踐。

---

## ▶️ 親自試試看

### 建立更多技能

以下是兩個展示不同模式的技能。按照上方「建立您的第一個技能」中的 `mkdir` + `cat` 工作流程操作，或直接複製貼上技能到適當位置。更多範例請參閱 [.github/skills](../.github/skills)。

### pytest 測試生成技能

一個確保整個程式碼庫具有一致 pytest 結構的技能：

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

一個在整個團隊中強制執行一致 PR 審查標準的技能：

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

1. **技能建立挑戰**：建立一個執行 3 點清單的 `quick-review` 技能：
   - bare except 子句
   - 缺少型別提示
   - 不清晰的變數名稱

   透過提問來測試：「Do a quick review of books.py」

2. **技能比較**：計時手動輸入詳細安全性審查提示詞所需的時間。然後只需問「Check for security issues in this file」，讓您的 security-audit 技能自動載入。技能節省了多少時間？

3. **團隊技能挑戰**：思考您團隊的程式碼審查清單。能否將其編碼為技能？寫下技能應始終檢查的 3 件事。

**自我檢核**：當您能解釋為何 `description` 欄位很重要時（它是 Copilot 決定是否載入您的技能的依據），代表您已理解技能的概念。

---

## 📝 作業

### 主要挑戰：建立書籍摘要技能

上述範例建立了 `pytest-gen` 和 `pr-review` 技能。現在練習建立一種完全不同類型的技能：用於從資料產生格式化輸出的技能。

1. 列出您目前的技能：執行 Copilot 並輸入 `/skills list`。您也可以使用 `ls .github/skills/` 查看專案技能，或使用 `ls ~/.copilot/skills/` 查看個人技能。
2. 在 `.github/skills/book-summary/SKILL.md` 建立一個 `book-summary` 技能，用於產生書籍集合的格式化 Markdown 摘要
3. 您的技能應具備：
   - 清晰的名稱和描述（描述對匹配至關重要！）
   - 具體的格式規則（例如：包含書名、作者、年份、閱讀狀態的 Markdown 表格）
   - 輸出慣例（例如：用 ✅/❌ 表示閱讀狀態，依年份排序）
4. 測試技能：`@samples/book-app-project/data.json Summarize the books in this collection`
5. 透過 `/skills list` 確認技能已自動觸發
6. 嘗試直接呼叫：`/book-summary Summarize the books in this collection`

**成功標準**：您有一個可運作的 `book-summary` 技能，當您詢問書籍集合時，Copilot 會自動套用它。

<details>
<summary>💡 提示（點擊展開）</summary>

**起始範本**：建立 `.github/skills/book-summary/SKILL.md`：

```markdown
---
name: book-summary
description: Generate a formatted markdown summary of a book collection
---

# Book Summary Generator

Generate a summary of the book collection following these rules:

1. Output a markdown table with columns: Title, Author, Year, Status
2. Use ✅ for read books and ❌ for unread books
3. Sort by year (oldest first)
4. Include a total count at the bottom
5. Flag any data issues (missing authors, invalid years)

Example:
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
# The skill should auto-trigger based on the description match
```

**如果未觸發：** 嘗試 `/skills reload`，然後再次提問。

</details>

### 加分挑戰：提交訊息技能

1. 建立一個 `commit-message` 技能，以一致的格式產生慣例提交訊息
2. 暫存一項變更，透過提問來測試：「Generate a commit message for my staged changes」
3. 記錄您的技能，並在 GitHub 上以 `copilot-skill` 主題標籤分享

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 發生情況 | 修正方式 |
|---------|--------------|-----|
| 將檔案命名為非 `SKILL.md` 的名稱 | 技能無法被識別 | 檔案必須準確命名為 `SKILL.md` |
| `description` 欄位過於模糊 | 技能永遠無法自動載入 | 描述是主要的發現機制，請使用具體的觸發關鍵字 |
| 前置資料中缺少 `name` 或 `description` | 技能載入失敗 | 在 YAML 前置資料中加入這兩個欄位 |
| 資料夾位置錯誤 | 找不到技能 | 使用 `.github/skills/技能名稱/`（專案）或 `~/.copilot/skills/技能名稱/`（個人） |

### 疑難排解

**技能未被使用** - 如果 Copilot 在預期時未使用您的技能：

1. **檢查描述**：它是否符合您的提問方式？
   ```markdown
   # Bad: Too vague
   description: Reviews code

   # Good: Includes trigger words
   description: Use for code reviews, checking code quality,
     finding bugs, security issues, and best practice violations
   ```

2. **確認檔案位置**：
   ```bash
   # Project skills
   ls .github/skills/

   # User skills
   ls ~/.copilot/skills/
   ```

3. **檢查 SKILL.md 格式**：前置資料是必要的：
   ```markdown
   ---
   name: skill-name
   description: What the skill does and when to use it
   ---

   # Instructions here
   ```

**技能未出現** - 確認資料夾結構：
```
.github/skills/
└── my-skill/           # Folder name
    └── SKILL.md        # Must be exactly SKILL.md (case-sensitive)
```

建立或編輯技能後執行 `/skills reload`，確保變更已套用。

**測試技能是否載入** - 直接詢問 Copilot：
```bash
> What skills do you have available for checking code quality?
# Copilot will describe relevant skills it found
```

**如何確認我的技能真的在運作？**

1. **檢查輸出格式**：如果您的技能指定了輸出格式（如 `[CRITICAL]` 標籤），請在回應中尋找這些標籤
2. **直接詢問**：收到回應後，問「Did you use any skills for that?」
3. **有無對比**：使用 `--no-custom-instructions` 嘗試相同提示詞，觀察差異：
   ```bash
   # With skills
   copilot --allow-all -p "Review @file.py for security issues"

   # Without skills (baseline comparison)
   copilot --allow-all -p "Review @file.py for security issues" --no-custom-instructions
   ```
4. **檢查特定項目**：如果您的技能包含特定檢查（如「超過 50 行的函式」），確認這些項目是否出現在輸出中

</details>

---

# 總結

## 🔑 重點摘要

1. **技能是自動的**：當您的提示詞符合技能的描述時，Copilot 便會載入
2. **直接呼叫**：您也可以使用 `/技能名稱` 斜線指令直接呼叫技能
3. **SKILL.md 格式**：YAML 前置資料（name、description、選填的 license）加上 Markdown 指令
4. **位置很重要**：`.github/skills/` 用於專案/團隊共用，`~/.copilot/skills/` 用於個人使用
5. **描述是關鍵**：撰寫符合您自然提問方式的描述

> 📋 **快速參考**：請參閱 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)，取得完整的指令和快捷鍵清單。

---

## ➡️ 接下來

技能透過自動載入指令來擴展 Copilot 的功能。但如何連接到外部服務呢？這正是 MCP 的用武之地。

在**[第 06 章：MCP 伺服器](../06-mcp-servers/README.md)**中，您將學習：

- 什麼是 MCP（模型情境協定）
- 連接到 GitHub、檔案系統和文件服務
- 設定 MCP 伺服器
- 多伺服器工作流程

---

**[← 返回第 04 章](../04-agents-custom-instructions/README.md)** | **[繼續前往第 06 章 →](../06-mcp-servers/README.md)**
