![GitHub Copilot CLI for Beginners](./assets/copilot-banner.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)&ensp;
[![Open project in GitHub Codespaces](https://img.shields.io/badge/Codespaces-Open-blue?style=flat-square&logo=github)](https://codespaces.new/github/copilot-cli-for-beginners?hide_repo_select=true&ref=main&quickstart=true)&ensp;
[![Official Copilot CLI documentation](https://img.shields.io/badge/GitHub-CLI_Documentation-00a3ee?style=flat-square&logo=github)](https://docs.github.com/en/copilot/how-tos/copilot-cli)&ensp;
[![Join AI Foundry Discord](https://img.shields.io/badge/Discord-AI_Community-blue?style=flat-square&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

🎯 [你將學到什麼](#what-youll-learn) &ensp; ✅ [先備知識](#prerequisites) &ensp; 🤖 [Copilot 家族介紹](#understanding-the-github-copilot-family) &ensp; 📚 [課程架構](#course-structure) &ensp; 📋 [指令參考](#-github-copilot-cli-command-reference)

# GitHub Copilot CLI 新手入門

> **✨ 學習如何用 AI 強化你的開發流程，讓命令列工作更高效。**

GitHub Copilot CLI 將 AI 助手直接帶進你的終端機。你不必切換到瀏覽器或程式碼編輯器，就能在命令列中提問、產生完整應用程式、審查程式碼、產生測試、除錯問題。

你可以把它想像成一位隨時待命、知識豐富的同事，能閱讀你的程式碼、解釋難懂的模式，並幫助你更快完成工作！

> 📘 **想要網頁版體驗？** 你可以直接在 GitHub 上學習本課程，或前往 [Awesome Copilot](https://awesome-copilot.github.com/learning-hub/cli-for-beginners/) 享受更傳統的瀏覽體驗。

本課程適合：

- **軟體開發者**：希望從命令列使用 AI
- **終端機使用者**：偏好鍵盤導向工作流程而非 IDE 整合
- **團隊**：希望標準化 AI 協助的程式碼審查與開發實踐

## 🎯 你將學到什麼

這是一門實作導向課程，帶你從零開始熟練使用 GitHub Copilot CLI。全程以一個 Python 書籍收藏應用程式為例，逐步用 AI 協作方式優化它。課程結束時，你將能自信地用 AI 審查程式碼、產生測試、除錯問題、並自動化工作流程——全部在終端機內完成。

**不需要任何 AI 經驗。** 只要你會用終端機，就能學會這些技能。

**非常適合：** 開發者、學生，以及有軟體開發經驗的任何人。

## ✅ 先備知識

開始前，請確認你已具備：

- **GitHub 帳號**：[免費註冊](https://github.com/signup)<br>
- **GitHub Copilot 存取權**：[免費方案](https://github.com/features/copilot/plans)、[月費訂閱](https://github.com/features/copilot/plans)、或[學生／教師免費](https://education.github.com/pack)<br>
- **終端機基礎**：熟悉 `cd`、`ls`、執行指令

## 🤖 Copilot 家族介紹

GitHub Copilot 已發展成一系列 AI 工具。以下是各自的定位：

| 產品 | 執行位置 | 說明 |
|---------|---------------|----------|
| [**GitHub Copilot CLI**](https://docs.github.com/copilot/how-tos/copilot-cli/cli-getting-started)<br>(本課程) | 你的終端機 |  原生於終端機的 AI 程式碼助手  |
| [**GitHub Copilot**](https://docs.github.com/copilot) | VS Code、Visual Studio、JetBrains 等 | Agent 模式、聊天、即時建議  |
| [**Copilot on GitHub.com**](https://github.com/copilot) | GitHub | 深入你的儲存庫聊天、建立 Agent 等 |
| [**GitHub Copilot cloud agent**](https://docs.github.com/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks) | GitHub  | 指派議題給 Agent，取得 PR 回覆 |

本課程聚焦於 **GitHub Copilot CLI**，讓 AI 助手直接進駐你的終端機。

## 📚 課程架構

![GitHub Copilot CLI Learning Path](assets/learning-path.png)

| 章節 | 標題 | 你將完成的內容 |
|:-------:|-------|-------------------|
| 00 | 🚀 [快速開始](./00-quick-start/README.md) | 安裝與驗證 |
| 01 | 👋 [第一步](./01-setup-and-first-steps/README.md) | 現場示範＋三種互動模式 |
| 02 | 🔍 [情境與對話](./02-context-conversations/README.md) | 多檔案專案分析 |
| 03 | ⚡ [開發工作流程](./03-development-workflows/README.md) | 程式碼審查、除錯、產生測試 |
| 04 | 🤖 [打造專屬 AI 助手](./04-agents-custom-instructions/README.md) | 為你的工作流程自訂 Agent |
| 05 | 🛠️ [自動化重複性工作](./05-skills/README.md) | 自動載入的 Skills |
| 06 | 🔌 [連接 GitHub、資料庫與 API](./06-mcp-servers/README.md) | MCP 伺服器整合 |
| 07 | 🎯 [整合應用](./07-putting-it-together/README.md) | 完整功能工作流程 |

## 📖 課程進行方式

每個章節都遵循相同結構：

1. **真實世界比喻**：用熟悉的例子理解概念
2. **核心觀念**：學習必要知識
3. **實作範例**：實際執行指令並觀察結果
4. **練習題**：動手練習所學內容
5. **預告下一章**：簡介下一章節重點

**程式碼範例皆可執行。** 本課程中的 copilot 文字區塊都能直接複製到終端機執行。

## 📋 GitHub Copilot CLI 指令參考

**[GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)** 可協助你快速查詢指令與快捷鍵，讓你更有效率地使用 Copilot CLI。

## 🙋 尋求協助

- 🐛 **發現錯誤？** [回報 Issue](https://github.com/github/copilot-cli-for-beginners/issues)
- 📚 **官方文件：** [GitHub Copilot CLI 文件](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)

## 貢獻指南

> **注意**：本課程的程式碼設計為在審查、說明與除錯時產生特定輸出，因此無法接受會更動現有程式碼的 PR。

**如何貢獻：**

1. Fork 本儲存庫並將其 clone 到你的電腦
2. 建立功能分支（`git checkout -b my-improvement`）
3. 進行修改
4. 提交 Pull Request

## 授權

本專案採用 MIT 開源授權。完整條款請參閱 [LICENSE](./LICENSE) 檔案。
