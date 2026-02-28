# AGENTS.md

適合初學者的 GitHub Copilot CLI 課程。內容為教學材料，非軟體程式。

## 結構

| 路徑 | 用途 |
|------|---------|
| `00-07/` | 章節：類比 → 概念 → 實作 → 作業 → 下一步 |
| `samples/book-app-project/` | **主要範例**：Python CLI 書籍收藏應用程式，貫穿所有章節使用 |
| `samples/book-app-project-cs/` | C# 版書籍收藏應用程式 |
| `samples/book-app-project-js/` | JavaScript 版書籍收藏應用程式 |
| `samples/book-app-buggy/` | **刻意埋入的錯誤**，用於除錯練習（第 03 章） |
| `samples/agents/` | Agent 範本範例（python-reviewer、pytest-helper、hello-world） |
| `samples/skills/` | Skill 範本範例（code-checklist、pytest-gen、commit-message、hello-world） |
| `samples/mcp-configs/` | MCP Server 設定範例 |
| `samples/buggy-code/` | **選讀延伸**：以安全性為主題的含錯程式碼（JS 與 Python） |
| `samples/src/` | **選讀延伸**：舊版課程遺留的 JS/React 範例 |
| `appendices/` | 補充參考資料 |

## 應做

- 保持說明對初學者友善；使用 AI/ML 術語時請加以解釋
- 確保 bash 範例可直接複製貼上執行
- 語氣：親切、鼓勵、實用
- 所有主要範例均使用 `samples/book-app-project/` 路徑
- 程式碼範例使用 Python/pytest 情境

## 不應做

- 不要修正 `samples/book-app-buggy/` 或 `samples/buggy-code/` 中的錯誤——這些是刻意為之
- 不要在未更新 README.md 課程目錄的情況下新增章節
- 不要假設讀者熟悉 AI/ML 術語

## 建置

```bash
npm install && npm run release
```
