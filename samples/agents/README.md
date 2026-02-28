# Agent 定義範例

此資料夾包含數個簡單的 agent 範本，專為 GitHub Copilot CLI 設計，幫助你快速上手使用 agents。

## 快速開始

```bash
# Copy an agent to your personal agents folder
cp hello-world.agent.md ~/.copilot/agents/

# Or copy to your project for team sharing
cp python-reviewer.agent.md .github/agents/
```

## 本資料夾的範例檔案

| 檔案 | 說明 | 適用情境 |
|------|------|----------|
| `hello-world.agent.md` | 最簡範例（11 行） | 學習格式 |
| `python-reviewer.agent.md` | Python 程式碼品質審查員 | 程式碼審查、PEP 8、型別提示 |
| `pytest-helper.agent.md` | Pytest 測試專家 | 生成測試、fixtures、邊界案例 |

## 探索更多 Agents

- **[github/awesome-copilot](https://github.com/github/awesome-copilot)** - GitHub 官方資源，收錄社群 agents 與使用說明

---

## Agent 檔案格式

每個 agent 檔案需要包含 YAML 前置區塊，至少須有 `description` 欄位：

```markdown
---
name: my-agent
description: Brief description of what this agent does
tools: ["read", "edit", "search"]  # Optional: limit available tools
---

# Agent Name

Agent instructions go here...
```

**可用的 YAML 屬性：**

| 屬性 | 必填 | 說明 |
|------|------|------|
| `description` | **是** | Agent 的功能描述 |
| `name` | 否 | 顯示名稱（預設為檔案名稱） |
| `tools` | 否 | 允許使用的工具清單（省略則允許全部）。請參閱下方別名說明。 |
| `target` | 否 | 限制僅適用於 `vscode` 或 `github-copilot` |

**工具別名**：`read`、`edit`、`search`、`execute`（shell）、`web`、`agent`

> 💡 **注意**：`model` 屬性在 VS Code 中可用，但目前尚未在 Copilot CLI 中支援。
>
> 📖 **官方文件**：[Custom agents configuration](https://docs.github.com/copilot/reference/custom-agents-configuration)

## Agent 檔案存放位置

Agents 可存放於以下位置：
- `~/.copilot/agents/` - 全域 agents，適用於所有專案
- `.github/agents/` - 專案專屬 agents
- `.agent.md` 檔案 - 相容 VS Code 的格式

每個 agent 各為一個獨立檔案，副檔名為 `.agent.md`。

---

## 使用範例

```bash
# Start with a specific agent
copilot --agent python-reviewer

# Or select an agent interactively during a session
copilot
> /agent
# Select "python-reviewer" from the list

# The agent's expertise applies to your prompts
> @samples/book-app-project/books.py Review this code for quality issues

# Switch to a different agent
> /agent
# Select "pytest-helper"

> @samples/book-app-project/tests/test_books.py What additional tests should we add?
```

---

## 建立你自己的 Agent

1. 在 `~/.copilot/agents/` 中建立一個副檔名為 `.agent.md` 的新檔案
2. 加入 YAML 前置區塊，至少須包含 `description` 欄位
3. 加入描述性標題（例如 `# Security Agent`）
4. 定義 agent 的專業領域、規範與行為準則
5. 使用 `/agent` 或 `--agent <name>` 來啟用該 agent

**打造高效 agent 的小訣竅：**
- 明確定義專業領域
- 納入程式碼規範與模式
- 說明 agent 的審查重點
- 指定輸出格式的偏好設定
