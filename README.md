![GitHub Copilot CLI for Beginners](./images/copilot-banner.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)&ensp;
[![Open project in GitHub Codespaces](https://img.shields.io/badge/Codespaces-Open-blue?style=flat-square&logo=github)](https://codespaces.new/github/copilot-cli-for-beginners?hide_repo_select=true&ref=main&quickstart=true)&ensp;
[![Official Copilot CLI documentation](https://img.shields.io/badge/GitHub-CLI_Documentation-00a3ee?style=flat-square&logo=github)](https://docs.github.com/en/copilot/how-tos/copilot-cli)&ensp;
[![Join AI Foundry Discord](https://img.shields.io/badge/Discord-AI_Community-blue?style=flat-square&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

🎯 [你將學到什麼](#what-youll-learn) &ensp; ✅ [先決條件](#prerequisites) &ensp; 🤖 [Copilot 家族介紹](#understanding-the-github-copilot-family) &ensp; 📚 [課程架構](#course-structure) &ensp; 📋 [指令參考](#-github-copilot-cli-command-reference)

# GitHub Copilot CLI 新手入門

> **✨ 學習如何用 AI 強化你的開發流程，享受命令列智慧助理。**

GitHub Copilot CLI 將 AI 助理直接帶到你的終端機。你不必切換到瀏覽器或程式編輯器，就能提問、產生完整應用程式、審查程式碼、生成測試、偵錯問題——全部都在命令列完成。

想像你有一位隨時待命的專業同事，可以閱讀你的程式碼、解釋難懂的模式，並協助你更快完成工作！

> 📘 **想要網頁體驗嗎？** 你可以直接在 GitHub 上學習本課程，或前往 [Awesome Copilot](https://awesome-copilot.github.com/learning-hub/cli-for-beginners/) 享受更傳統的瀏覽體驗。

本課程適合：

- **軟體開發者**：想從命令列使用 AI
- **終端機使用者**：偏好鍵盤操作流程而非 IDE 整合
- **團隊**：希望標準化 AI 協助的程式碼審查與開發流程

## 🎯 你將學到什麼

這門實作課程將帶你從零開始，學會 GitHub Copilot CLI 的高效應用。你會在每個章節操作同一個 Python 書籍收藏應用程式，並透過 AI 協助逐步優化它。課程結束時，你將能自信地用 AI 審查程式碼、生成測試、偵錯問題、並自動化工作流程——全部都在終端機完成。

**不需要任何 AI 經驗。** 只要會用終端機，你就能學會這些技能。

**非常適合：** 開發者、學生，以及任何有軟體開發經驗的人。

## ✅ 先決條件

開始前，請確認你已具備：

- **GitHub 帳號**：[免費註冊](https://github.com/signup)<br>
- **GitHub Copilot 使用權限**：[免費方案](https://github.com/features/copilot/plans)、[月費訂閱](https://github.com/features/copilot/plans)、或 [學生／教師免費](https://education.github.com/pack)<br>
- **終端機基礎操作**：熟悉 `cd`、`ls`、執行指令

## 🤖 Copilot 家族介紹

GitHub Copilot 已發展成一系列 AI 工具。以下是各工具的運作位置：

| 產品 | 執行位置 | 說明 |
|---------|---------------|----------|
| [**GitHub Copilot CLI**](https://docs.github.com/copilot/how-tos/copilot-cli/cli-getting-started)<br>(本課程主角) | 你的終端機 |  原生命令列 AI 程式碼助理  |
| [**GitHub Copilot**](https://docs.github.com/copilot) | VS Code、Visual Studio、JetBrains 等 | Agent 模式、聊天、即時建議  |
| [**Copilot on GitHub.com**](https://github.com/copilot) | GitHub | 關於你的儲存庫的沉浸式聊天、建立 Agent 等功能 |
| [**GitHub Copilot cloud agent**](https://docs.github.com/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks) | GitHub  | 指派議題給 Agent、取得 PR 回覆 |

本課程專注於 **GitHub Copilot CLI**，將 AI 助理直接帶到你的終端機。

## 📚 課程架構

![GitHub Copilot CLI Learning Path](images/learning-path.png)

| 章節 | 標題 | 你將完成的內容 |
|:-------:|-------|-------------------|
| 00 | 🚀 [快速開始](./00-quick-start/README.md) | 安裝與驗證 |
| 01 | 👋 [第一步](./01-setup-and-first-steps/README.md) | 現場示範＋三種互動模式 |
| 02 | 🔍 [情境與對話](./02-context-conversations/README.md) | 多檔案專案分析 |
| 03 | ⚡ [開發流程](./03-development-workflows/README.md) | 程式碼審查、偵錯、測試產生 |
| 04 | 🤖 [打造專屬 AI 助理](./04-agents-custom-instructions/README.md) | 為你的工作流程建立自訂 Agent |
| 05 | 🛠️ [自動化重複性工作](./05-skills/README.md) | 自動載入的 Skills |
| 06 | 🔌 [連接 GitHub、資料庫與 API](./06-mcp-servers/README.md) | MCP Server 整合 |
| 07 | 🎯 [整合所有技能](./07-putting-it-together/README.md) | 完整功能工作流程 |

## 📖 課程運作方式

每個章節都遵循相同流程：

1. **生活比喻**：用熟悉的例子理解概念
2. **核心知識**：學習必要的重點
3. **實作範例**：實際執行指令並觀察結果
4. **練習題**：動手練習所學內容
5. **下一步預告**：預覽下一章節內容

**程式碼範例皆可執行。** 本課程所有 Copilot 文字區塊都能直接複製到終端機運行。

## 📋 GitHub Copilot CLI 指令參考

**[GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)** 可協助你查找指令與快捷鍵，讓你更有效率地使用 Copilot CLI。

## 🙋 求助管道

- 🐛 **發現錯誤？** [提出 Issue](https://github.com/github/copilot-cli-for-beginners/issues)
- 📚 **官方文件：** [GitHub Copilot CLI 文件](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)

## 貢獻方式

> **注意**：本課程使用的程式碼設計為在審查、解釋與偵錯時產生特定輸出，因此我們無法接受會更動現有程式碼的 PR。

**貢獻流程：**

1. Fork 本儲存庫並將其 clone 到你的電腦
2. 建立功能分支（`git checkout -b my-improvement`）
3. 進行修改
4. 提交 pull request

## 授權條款

本專案採用 MIT 開源授權。完整條款請參閱 [LICENSE](./LICENSE) 檔案。
