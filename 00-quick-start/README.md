![Chapter 00: Quick Start](images/chapter-header.png)

歡迎！本章將帶你完成 GitHub Copilot CLI（命令列介面）的安裝、GitHub 帳號登入，並確認一切正常運作。這是一章快速設定指南，等你準備就緒，精彩的示範就從第 01 章正式展開！

## 🎯 學習目標

完成本章後，你將：

- 安裝好 GitHub Copilot CLI
- 以 GitHub 帳號完成登入
- 透過簡單測試驗證功能正常

> ⏱️ **預估時間**：約 10 分鐘（閱讀 5 分鐘 + 實作 5 分鐘）

---

## ✅ 前置需求

- 具備 Copilot 存取權限的 **GitHub 帳號**。[查看訂閱方案](https://github.com/features/copilot/plans)。學生與教師可透過 [GitHub Education](https://education.github.com/pack) 免費取得 Copilot Pro。
- **終端機基礎操作**：熟悉 `cd`、`ls` 等基本指令

### 「Copilot 存取權限」的意思

GitHub Copilot CLI 需要有效的 Copilot 訂閱。你可以前往 [github.com/settings/copilot](https://github.com/settings/copilot) 確認狀態，應會看到以下其中一項：

- **Copilot Individual** - 個人訂閱
- **Copilot Business** - 透過組織提供
- **Copilot Enterprise** - 透過企業提供
- **GitHub Education** - 已驗證學生／教師免費使用

若顯示「You don't have access to GitHub Copilot」，你需要選用免費方案、訂閱付費方案，或加入已提供存取權限的組織。

---

## 安裝

> ⏱️ **時間預估**：安裝約需 2-5 分鐘，驗證步驟再加 1-2 分鐘。

### 推薦方式：GitHub Codespaces（零設定）

若不想在本機安裝任何前置套件，可以使用 GitHub Codespaces——它已預先備妥 GitHub Copilot CLI（需登入）、Python 3.13、pytest 以及 GitHub CLI。

1. 將此儲存庫 [Fork 到你的 GitHub 帳號](https://github.com/github/copilot-cli-for-beginners/fork)
2. 選擇 **Code** > **Codespaces** > **Create codespace on main**
3. 等待容器建置（需要幾分鐘）
4. 準備完成！終端機會在 Codespace 環境中自動開啟。

> 💡 **在 Codespace 中驗證**：執行 `cd samples/book-app-project && python book_app.py help`，確認 Python 與範例應用程式正常運作。

### 替代方案：本機安裝

> 💡 **不確定該選哪個？** 若已安裝 Node.js，請使用 `npm`；否則選擇適合你系統的方式。

> 💡 **示範需要 Python**：本課程使用 Python 範例應用程式。若在本機操作，請在開始示範前先安裝 [Python 3.10+](https://www.python.org/downloads/)。

> **備註：** 課程主要範例使用 Python（`samples/book-app-project`），但 JavaScript（`samples/book-app-project-js`）和 C#（`samples/book-app-project-cs`）版本也同樣提供，可依個人偏好選用。每個範例目錄均附有說明如何執行該語言版本的 README。

請選擇適合你系統的安裝方式：

### 所有平台（npm）

```bash
# 若已安裝 Node.js，這是最快的安裝方式
npm install -g @github/copilot
```

### macOS/Linux（Homebrew）

```bash
brew install copilot-cli
```

### Windows（WinGet）

```bash
winget install GitHub.Copilot
```

### macOS/Linux（安裝腳本）

```bash
curl -fsSL https://gh.io/copilot-install | bash
```

---

## 驗證身份

在 `copilot-cli-for-beginners` 儲存庫根目錄開啟終端機視窗，啟動 CLI 並允許存取該資料夾。

```bash
copilot
```

系統會詢問你是否信任包含此儲存庫的資料夾（若尚未信任）。你可以選擇單次信任，或對所有未來的工作階段永久信任。

<img src="images/copilot-trust.png" alt="Trusting files in a folder with the Copilot CLI" width="800"/>

信任資料夾後，即可以 GitHub 帳號登入。

```
> /login
```

**接下來會發生的事：**

1. Copilot CLI 顯示一組一次性代碼（例如 `ABCD-1234`）
2. 瀏覽器自動開啟 GitHub 的裝置授權頁面。若尚未登入 GitHub，請先登入。
3. 在提示處輸入代碼
4. 選擇「Authorize」授權 GitHub Copilot CLI 存取
5. 返回終端機——你已成功登入！

<img src="images/auth-device-flow.png" alt="Device Authorization Flow - showing the 5-step process from terminal login to signed-in confirmation" width="800"/>

*裝置授權流程：終端機產生代碼，你在瀏覽器中確認，Copilot CLI 即完成驗證。*

**提示**：登入狀態會跨工作階段保留，除非 token 過期或你主動登出，否則只需登入一次。

---

## 驗證是否正常運作

### 步驟一：測試 Copilot CLI

登入後，讓我們確認 Copilot CLI 運作正常。在終端機中啟動 CLI（若尚未啟動）：

```bash
> Say hello and tell me what you can help with
```

收到回應後，即可離開 CLI：

```bash
> /exit
```

---

<details>
<summary>🎬 看看實際效果！</summary>

<img src="images/hello-demo.gif" alt="Hello Demo">

<em>示範輸出僅供參考，你的模型、工具與回應內容可能與此不同。</em>

</details>

---

**預期輸出**：一段友善的回應，列出 Copilot CLI 的能力。

### 步驟二：執行範例書籍應用程式

本課程提供一個範例應用程式，你將在整個課程中使用 CLI 來探索並改善它 *（程式碼位於 /samples/book-app-project）*。在正式開始前，請先確認這個 *Python 書籍收藏終端機應用程式* 能正常運作。依你的系統環境，執行 `python` 或 `python3`。

> **備註：** 課程主要範例使用 Python（`samples/book-app-project`），但 JavaScript（`samples/book-app-project-js`）和 C#（`samples/book-app-project-cs`）版本也同樣提供，可依個人偏好選用。每個範例目錄均附有說明如何執行該語言版本的 README。

```bash
cd samples/book-app-project
python book_app.py list
```

**預期輸出**：包含「The Hobbit」、「1984」和「Dune」在內的 5 本書清單。

### 步驟三：以 Copilot CLI 搭配書籍應用程式

若已執行步驟二，請先返回儲存庫根目錄：

```bash
cd ../..   # 回到儲存庫根目錄（若有需要）
copilot 
> What does @samples/book-app-project/book_app.py do?
```

**預期輸出**：書籍應用程式主要功能與指令的摘要說明。

若看到錯誤訊息，請參閱下方的[疑難排解](#troubleshooting)章節。

完成後即可離開 Copilot CLI：

```bash
> /exit
```

---

## ✅ 準備就緒！

安裝部分到此完成。真正有趣的內容從第 01 章開始，你將：

- 看著 AI 審查書籍應用程式，即時找出程式碼品質問題
- 學習使用 Copilot CLI 的三種不同方式
- 用白話英文生成可執行的程式碼

**[繼續前往第 01 章：第一步 →](../01-setup-and-first-steps/README.md)**

---

## 疑難排解 {#troubleshooting}

### 「copilot: command not found」

CLI 尚未安裝，請嘗試其他安裝方式：

```bash
# 若 brew 失敗，改用 npm：
npm install -g @github/copilot

# 或使用安裝腳本：
curl -fsSL https://gh.io/copilot-install | bash
```

### 「You don't have access to GitHub Copilot」

1. 前往 [github.com/settings/copilot](https://github.com/settings/copilot) 確認是否具有 Copilot 訂閱
2. 若使用工作帳號，請確認組織是否允許 CLI 存取

### 「Authentication failed」

重新驗證身份：

```bash
copilot
> /login
```

### 瀏覽器未自動開啟

手動前往 [github.com/login/device](https://github.com/login/device)，輸入終端機上顯示的代碼。

### Token 已過期

重新執行 `/login`：

```bash
copilot
> /login
```

### 仍然卡關？

- 查看 [GitHub Copilot CLI 官方文件](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)
- 搜尋 [GitHub Issues](https://github.com/github/copilot-cli/issues)

---

## 🔑 重點整理

1. **GitHub Codespace 是快速上手的好方法** - Python、pytest 與 GitHub Copilot CLI 皆已預先安裝，可直接跳入示範
2. **多種安裝方式** - 依系統選擇適合的方案（Homebrew、WinGet、npm 或安裝腳本）
3. **一次性驗證** - 登入狀態保留至 token 過期為止
4. **書籍應用程式可正常運行** - 整個課程都會使用 `samples/book-app-project`

> 📚 **官方文件**：[安裝 Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli/cli-getting-started) — 查看安裝選項與需求說明。

> 📋 **快速參考**：查看 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference) 以取得完整指令與快捷鍵列表。

---

**[繼續前往第 01 章：第一步 →](../01-setup-and-first-steps/README.md)**
