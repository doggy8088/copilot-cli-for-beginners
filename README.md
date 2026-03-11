![GitHub Copilot CLI for Beginners](./images/copilot-banner.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)&ensp;
[![Open project in GitHub Codespaces](https://img.shields.io/badge/Codespaces-Open-blue?style=flat-square&logo=github)](https://codespaces.new/github/copilot-cli-for-beginners?hide_repo_select=true&ref=main&quickstart=true)&ensp;
[![Official Copilot CLI documentation](https://img.shields.io/badge/GitHub-CLI_Documentation-00a3ee?style=flat-square&logo=github)](https://docs.github.com/en/copilot/how-tos/copilot-cli)&ensp;
[![Join AI Foundry Discord](https://img.shields.io/badge/Discord-AI_Community-blue?style=flat-square&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

🎯 [你將學到什麼](#what-youll-learn) &ensp; ✅ [先決條件](#prerequisites) &ensp; 🤖 [Copilot 家族介紹](#understanding-the-github-copilot-family) &ensp; 📚 [課程結構](#course-structure) &ensp; 📋 [指令參考](#-github-copilot-cli-command-reference)

# GitHub Copilot CLI 新手入門

> **✨ 學習如何用 AI 強化你的開發流程，讓命令列工作更高效。**

GitHub Copilot CLI 讓 AI 協助直接進入你的終端機。你無需切換到瀏覽器或程式碼編輯器，就能提問、產生完整應用程式、審查程式碼、產生測試、除錯問題——全都在命令列中完成。

你可以把它想像成一位 24 小時待命、知識豐富的同事，能閱讀你的程式碼、解釋難懂的寫法，並協助你更快完成工作！

本課程適合：

- **想在命令列使用 AI 的軟體開發者**
- **偏好鍵盤操作流程而非 IDE 整合的終端機使用者**
- **希望團隊標準化 AI 協助程式碼審查與開發流程的團隊**

<a href="https://aka.ms/githubcopilotdevdays" target="_blank">
  <img src="./images/copilot-dev-days.png" alt="GitHub Copilot Dev Days - Find or host an event" width="100%" />
</a>

## 🎯 你將學到什麼

這門實作課程會帶你從零開始，熟練使用 GitHub Copilot CLI。你將在所有章節中持續改進一個 Python 書籍收藏應用程式，逐步利用 AI 協作優化它。課程結束時，你將能自信地用 AI 進行程式碼審查、產生測試、除錯問題、並自動化工作流程——全部都在終端機完成。

**不需要任何 AI 經驗。** 只要你會用終端機，就能學會這門課。

**非常適合：** 開發者、學生，以及有軟體開發經驗的任何人。

## ✅ 先決條件

開始前，請確保你已具備：

- **GitHub 帳號**：[免費註冊](https://github.com/signup)<br>
- **GitHub Copilot 存取權**：[免費方案](https://github.com/features/copilot/plans)、[月費訂閱](https://github.com/features/copilot/plans)、或 [學生/教師免費](https://education.github.com/pack)<br>
- **終端機基礎**：熟悉 `cd`、`ls`、執行指令

## 🤖 Copilot 家族介紹

GitHub Copilot 已經發展成一系列 AI 工具。以下是各工具的定位：

| 產品 | 執行位置 | 說明 |
|---------|---------------|----------|
| [**GitHub Copilot CLI**](https://docs.github.com/copilot/how-tos/copilot-cli/cli-getting-started)<br>(本課程主角) | 你的終端機 |  原生於命令列的 AI 程式碼助理  |
| [**GitHub Copilot**](https://docs.github.com/copilot) | VS Code、Visual Studio、JetBrains 等 | Agent 模式、聊天、即時建議  |
| [**Copilot on GitHub.com**](https://github.com/copilot) | GitHub | 深度聊天你的儲存庫、建立 Agent 等 |
| [**GitHub Copilot coding agent**](https://docs.github.com/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks) | GitHub  | 指派議題給 Agent，取得 PR 回饋 |

本課程聚焦於 **GitHub Copilot CLI**，讓 AI 協助直接進入你的終端機。

## 📚 課程結構

![GitHub Copilot CLI Learning Path](images/learning-path.png)

| 章節 | 標題 | 你將實作內容 |
|:-------:|-------|-------------------|
| 00 | 🚀 [快速開始](./00-quick-start/README.md) | 安裝與驗證 |
| 01 | 👋 [第一步](./01-setup-and-first-steps/README.md) | 現場示範＋三種互動模式 |
| 02 | 🔍 [情境與對話](./02-context-conversations/README.md) | 多檔案專案分析 |
| 03 | ⚡ [開發工作流程](./03-development-workflows/README.md) | 程式碼審查、除錯、測試產生 |
| 04 | 🤖 [打造專屬 AI 助理](./04-agents-custom-instructions/README.md) | 客製化 Agent 強化工作流程 |
| 05 | 🛠️ [自動化重複性工作](./05-skills/README.md) | 自動載入的 Skill |
| 06 | 🔌 [連接 GitHub、資料庫與 API](./06-mcp-servers/README.md) | MCP 伺服器整合 |
| 07 | 🎯 [整合應用](./07-putting-it-together/README.md) | 完整功能工作流程 |

## 📖 課程進行方式

每個章節都遵循相同架構：

1. **生活化比喻**：用熟悉的例子理解新概念
2. **核心觀念**：學習必要知識
3. **實作範例**：實際執行指令並觀察結果
4. **練習題**：動手練習剛學到的內容
5. **下一步**：預告下個章節內容

**所有程式碼範例都可執行。** 課程中的 copilot 指令區塊都能直接複製到終端機運行。

## 📋 GitHub Copilot CLI 指令參考

**[GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)** 可協助你查詢指令與快捷鍵，讓你更有效率地使用 Copilot CLI。

## 🙋 取得協助

- 🐛 **發現錯誤？** [提出 Issue](https://github.com/github/copilot-cli-for-beginners/issues)
- 🤝 **想要貢獻？** 歡迎 PR！
- 📚 **官方文件：** [GitHub Copilot CLI 文件](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)

## 授權

本專案採用 MIT 開源授權條款。完整條款請參閱 [LICENSE](./LICENSE) 檔案。
