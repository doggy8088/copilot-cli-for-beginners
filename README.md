![GitHub Copilot CLI for Beginners](./images/copilot-banner.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)&ensp;
[![Open project in GitHub Codespaces](https://img.shields.io/badge/Codespaces-Open-blue?style=flat-square&logo=github)](https://codespaces.new/github/copilot-cli-for-beginners?hide_repo_select=true&ref=main&quickstart=true)&ensp;
[![Official Copilot CLI documentation](https://img.shields.io/badge/GitHub-CLI_Documentation-00a3ee?style=flat-square&logo=github)](https://docs.github.com/en/copilot/how-tos/copilot-cli)&ensp;
[![Join AI Foundry Discord](https://img.shields.io/badge/Discord-AI_Community-blue?style=flat-square&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

🎯 [學習目標](#學習目標) &ensp; ✅ [前置需求](#前置需求) &ensp; 🤖 [Copilot 家族](#瞭解-github-copilot-家族) &ensp; 📚 [課程架構](#課程架構) &ensp; 📋 [指令參考](#-github-copilot-cli-指令參考)

# GitHub Copilot CLI for Beginners

> **✨ 學習如何以 AI 驅動的命令列助手為你的開發工作流程加速。**

GitHub Copilot CLI 將 AI 助手直接帶到你的終端機。你不再需要切換到瀏覽器或程式碼編輯器，就能提問、生成完整應用程式、審查程式碼、產生測試，以及除錯——一切盡在命令列完成。

把它想像成一位全天候待命的博學同事，能閱讀你的程式碼、解釋令人困惑的模式，並幫助你更有效率地工作！

本課程適合以下對象：

- **軟體開發者**：希望從命令列使用 AI
- **終端機愛好者**：偏好鍵盤驅動的工作流程，而非 IDE 整合
- **希望統一規範的團隊**：推動 AI 輔助的程式碼審查與開發實踐

## 🎯 學習目標

本實作課程帶你從零開始，逐步掌握 GitHub Copilot CLI。你將在所有章節中持續改進同一個 Python 書籍收藏應用程式，透過 AI 輔助的工作流程逐步提升它的品質。課程結束後，你將能自信地使用 AI 審查程式碼、生成測試、除錯，以及自動化工作流程——全部在終端機中完成。

**不需要 AI 相關經驗。** 只要你會使用終端機，就能學會。

**適合對象：** 開發者、學生，以及任何具備軟體開發基礎的人。

## ✅ 前置需求

開始之前，請確認你已備妥：

- **GitHub 帳號**：[免費申請](https://github.com/signup)<br>
- **GitHub Copilot 使用權限**：[免費方案](https://github.com/features/copilot/plans)、[月費訂閱](https://github.com/features/copilot/plans)，或[學生／教師免費方案](https://education.github.com/pack)<br>
- **終端機基礎操作**：熟悉 `cd`、`ls` 及執行指令

## 🤖 瞭解 GitHub Copilot 家族

GitHub Copilot 已演進為一系列 AI 工具。以下說明各工具的使用場景：

| 產品 | 執行環境 | 說明 |
|---------|---------------|----------|
| [**GitHub Copilot CLI**](https://docs.github.com/copilot/how-tos/copilot-cli/cli-getting-started)<br>（本課程） | 終端機 | 原生終端機 AI 程式開發助手 |
| [**GitHub Copilot**](https://docs.github.com/copilot) | VS Code、Visual Studio、JetBrains 等 | Agent 模式、對話、行內建議 |
| [**Copilot on GitHub.com**](https://github.com/copilot) | GitHub | 深度對話你的程式庫、建立 Agent 等更多功能 |
| [**GitHub Copilot coding agent**](https://docs.github.com/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks) | GitHub | 將 Issue 指派給 Agent，自動取得 PR |

本課程專注於 **GitHub Copilot CLI**，將 AI 助手直接帶入你的終端機。

## 📚 課程架構

![GitHub Copilot CLI Learning Path](images/learning-path.png)

| 章節 | 標題 | 你將完成的內容 |
|:-------:|-------|-------------------|
| 00 | 🚀 [快速入門](./00-quick-start/README.md) | 安裝與驗證 |
| 01 | 👋 [第一步](./01-setup-and-first-steps/README.md) | 即時示範 + 三種互動模式 |
| 02 | 🔍 [情境與對話](./02-context-conversations/README.md) | 多檔案專案分析 |
| 03 | ⚡ [開發工作流程](./03-development-workflows/README.md) | 程式碼審查、除錯、測試生成 |
| 04 | 🤖 [建立專屬 AI 助手](./04-agents-custom-instructions/README.md) | 為你的工作流程打造自訂 Agent |
| 05 | 🛠️ [自動化重複任務](./05-skills/README.md) | 自動載入的 Skill |
| 06 | 🔌 [連接 GitHub、資料庫與 API](./06-mcp-servers/README.md) | MCP Server 整合 |
| 07 | 🎯 [整合應用](./07-putting-it-together/README.md) | 完整功能開發流程 |

## 📖 課程學習方式

每個章節均遵循相同的學習流程：

1. **生活化類比**：透過熟悉的比喻理解概念
2. **核心概念**：學習必要的知識
3. **實作範例**：執行實際指令並觀察結果
4. **作業練習**：實踐所學
5. **預告下一章**：預覽下一章節的內容

**所有程式碼範例皆可直接執行。** 本課程中每個 copilot 文字區塊都可以複製並在終端機中執行。

## 📋 GitHub Copilot CLI 指令參考

**[GitHub Copilot CLI 指令參考文件](https://docs.github.com/en/copilot/reference/cli-command-reference)** 可協助你查找指令和鍵盤快捷鍵，讓你更有效率地使用 Copilot CLI。

## 🙋 取得協助

- 🐛 **發現錯誤？** [開啟 Issue](https://github.com/github/copilot-cli-for-beginners/issues)
- 🤝 **想要貢獻？** 歡迎提交 PR！
- 📚 **官方文件：** [GitHub Copilot CLI 說明文件](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)

## 授權條款

本專案採用 MIT 開源授權條款。完整條款請參閱 [LICENSE](./LICENSE) 檔案。

