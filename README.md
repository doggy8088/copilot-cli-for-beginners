![GitHub Copilot CLI for Beginners](./images/copilot-banner.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)&ensp;
[![Open project in GitHub Codespaces](https://img.shields.io/badge/Codespaces-Open-blue?style=flat-square&logo=github)](https://codespaces.new/github/copilot-cli-for-beginners?hide_repo_select=true&ref=main&quickstart=true)&ensp;
[![Official Copilot CLI documentation](https://img.shields.io/badge/GitHub-CLI_Documentation-00a3ee?style=flat-square&logo=github)](https://docs.github.com/en/copilot/how-tos/copilot-cli)&ensp;
[![Join AI Foundry Discord](https://img.shields.io/badge/Discord-AI_Community-blue?style=flat-square&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

🎯 [你將學到什麼](#what-youll-learn) &ensp; ✅ [先決條件](#prerequisites) &ensp; 🤖 [Copilot 家族介紹](#understanding-the-github-copilot-family) &ensp; 📚 [課程架構](#course-structure) &ensp; 📋 [指令參考](#-github-copilot-cli-command-reference)

# GitHub Copilot CLI 新手入門

> **✨ 學習如何用 AI 強化你的開發流程，享受命令列智慧助手。**

GitHub Copilot CLI 將 AI 助手直接帶到你的終端機。你無需切換到瀏覽器或程式編輯器，就能在命令列上提問、產生完整應用程式、審查程式碼、生成測試、除錯問題。

想像你有一位隨時待命的專業同事，能閱讀你的程式碼、解釋難懂的模式，並協助你更快完成工作！

> 📘 **偏好網頁體驗嗎？** 你可以直接在 GitHub 上學習本課程，或前往 [Awesome Copilot](https://awesome-copilot.github.com/learning-hub/cli-for-beginners/) 享受更傳統的瀏覽體驗。

本課程適合：

- **軟體開發者**：希望在命令列上使用 AI
- **終端機使用者**：偏好鍵盤操作流程而非 IDE 整合
- **團隊**：希望標準化 AI 協助的程式碼審查與開發流程

<a href="https://aka.ms/githubcopilotdevdays" target="_blank">
  <picture>
    <img src="./images/copilot-dev-days.png" alt="GitHub Copilot Dev Days - Find or host an event" width="100%" />
  </picture>
</a>

## 🎯 你將學到什麼

這是一門實作導向課程，從零開始帶你熟悉 GitHub Copilot CLI。你將以一個 Python 書籍收藏應用程式為例，逐步用 AI 協助的流程優化它。課程結束時，你將能自信地用 AI 審查程式碼、生成測試、除錯問題、並自動化工作流程——全部在終端機完成。

**不需任何 AI 經驗。** 只要你會用終端機，就能學會這門課。

**非常適合：** 開發者、學生，以及任何有軟體開發經驗的人。

## ✅ 先決條件

開始前，請確認你已具備：

- **GitHub 帳號**：[免費註冊](https://github.com/signup)<br>
- **GitHub Copilot 存取權**：[免費方案](https://github.com/features/copilot/plans)、[月費訂閱](https://github.com/features/copilot/plans)、或[學生／教師免費](https://education.github.com/pack)<br>
- **終端機基礎操作**：熟悉 `cd`、`ls`、執行指令

## 🤖 Copilot 家族介紹

GitHub Copilot 已發展成一系列 AI 工具。各工具運作位置如下：

| 產品 | 執行位置 | 說明 |
|---------|---------------|----------|
| [**GitHub Copilot CLI**](https://docs.github.com/copilot/how-tos/copilot-cli/cli-getting-started)<br>(本課程) | 你的終端機 |  原生命令列 AI 程式碼助手  |
| [**GitHub Copilot**](https://docs.github.com/copilot) | VS Code、Visual Studio、JetBrains 等 | Agent 模式、聊天、即時建議  |
| [**Copilot on GitHub.com**](https://github.com/copilot) | GitHub | 深度聊天你的儲存庫、建立 Agent 等功能 |
| [**GitHub Copilot cloud agent**](https://docs.github.com/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks) | GitHub  | 指派議題給 Agent，取得 PR 回覆 |

本課程專注於 **GitHub Copilot CLI**，將 AI 助手直接帶到你的終端機。

## 📚 課程架構

![GitHub Copilot CLI Learning Path](images/learning-path.png)

| 章節 | 標題 | 你將完成的內容 |
|:-------:|-------|-------------------|
| 00 | 🚀 [快速開始](./00-quick-start/README.md) | 安裝與驗證 |
| 01 | 👋 [第一步](./01-setup-and-first-steps/README.md) | 現場示範＋三種互動模式 |
| 02 | 🔍 [情境與對話](./02-context-conversations/README.md) | 多檔案專案分析 |
| 03 | ⚡ [開發流程](./03-development-workflows/README.md) | 程式碼審查、除錯、測試生成 |
| 04 | 🤖 [打造專屬 AI 助手](./04-agents-custom-instructions/README.md) | 為你的流程建立自訂 Agent |
| 05 | 🛠️ [自動化重複性工作](./05-skills/README.md) | 自動載入的 Skill |
| 06 | 🔌 [連接 GitHub、資料庫與 API](./06-mcp-servers/README.md) | MCP Server 整合 |
| 07 | 🎯 [總結與實作](./07-putting-it-together/README.md) | 完整功能流程 |

## 📖 課程進行方式

每個章節都遵循相同流程：

1. **生活比喻**：用熟悉的例子理解概念
2. **核心知識**：學習必要重點
3. **實作範例**：實際執行指令並觀察結果
4. **練習題**：動手練習所學內容
5. **下一步預告**：預覽下個章節內容

**所有程式碼範例都可執行。** 本課程中的 copilot 文字區塊都能直接複製到終端機運行。

## 📋 GitHub Copilot CLI 指令參考

**[GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)** 可協助你查找指令與快捷鍵，提升 Copilot CLI 使用效率。

## 🙋 求助管道

- 🐛 **發現錯誤？** [提出 Issue](https://github.com/github/copilot-cli-for-beginners/issues)
- 🤝 **想貢獻？** 歡迎 PR！
- 📚 **官方文件：** [GitHub Copilot CLI Documentation](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)

## 授權條款

本專案採用 MIT 開源授權。完整條款請參閱 [LICENSE](./LICENSE) 檔案。
