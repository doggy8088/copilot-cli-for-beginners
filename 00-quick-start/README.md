![Chapter 00: Quick Start](images/chapter-header.png)

歡迎！在本章中，你將安裝 GitHub Copilot CLI（命令列介面），使用你的 GitHub 帳號登入，並驗證一切運作正常。這是一個快速設定章節。當你完成安裝並開始使用後，真正的示範會在第 01 章開始！

## 🎯 學習目標

在本章結束時，你將能夠：

- 安裝 GitHub Copilot CLI
- 使用你的 GitHub 帳號登入
- 透過簡單測試驗證功能正常

> ⏱️ **預估時間**：約 10 分鐘（5 分鐘閱讀 + 5 分鐘實作）

---

## ✅ 先備條件

- **GitHub 帳號**，且具備 Copilot 存取權。[查看訂閱方案](https://github.com/features/copilot/plans)。學生／教師可透過 [GitHub Education 免費取得 Copilot Pro](https://education.github.com/pack)。
- **終端機基礎**：熟悉 `cd` 和 `ls` 等指令

### 什麼是「Copilot 存取權」

GitHub Copilot CLI 需要有效的 Copilot 訂閱。你可以在 [github.com/settings/copilot](https://github.com/settings/copilot) 檢查你的狀態。你應該會看到以下其中一種：

- **Copilot Individual** - 個人訂閱
- **Copilot Business** - 由你的組織提供
- **Copilot Enterprise** - 由你的企業提供
- **GitHub Education** - 經驗證的學生／教師免費使用

如果你看到「You don't have access to GitHub Copilot」，你需要使用免費方案、訂閱付費方案，或加入有提供存取權的組織。

---

## 安裝

> ⏱️ **時間預估**：安裝約需 2-5 分鐘。驗證身分再多 1-2 分鐘。

### GitHub Codespaces（零設定）

如果你不想安裝任何先備軟體，可以使用 GitHub Codespaces，它已經內建 GitHub Copilot CLI（你只需登入），並預先安裝 Python 和 pytest。

1. [Fork 這個儲存庫](https://github.com/github/copilot-cli-for-beginners/fork) 到你的 GitHub 帳號
2. 選擇 **Code** > **Codespaces** > **Create codespace on main**
3. 等待幾分鐘讓容器建置完成
4. 一切就緒！終端機會自動在 Codespace 環境中開啟。

> 💡 **在 Codespace 驗證**：執行 `cd samples/book-app-project && python book_app.py help` 來確認 Python 和範例應用程式可正常運作。

### 本機安裝

如果你想在本機執行 Copilot CLI 並搭配課程範例，請依下列步驟操作。

1. 將課程範例複製到你的電腦：

    ```bash
    git clone https://github.com/github/copilot-cli-for-beginners
    cd copilot-cli-for-beginners
    ```

2. 使用下列其中一種方式安裝 Copilot CLI。

    > 💡 **不確定選哪個？** 如果你已安裝 Node.js，建議使用 `npm`。否則請選擇符合你系統的方式。

    ### 所有平台（npm）

    ```bash
    # 如果你已安裝 Node.js，這是快速取得 CLI 的方法
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

<details>
<summary>選用：啟用 Shell Tab 補全</summary>

Shell Tab 補全可讓你按下 **Tab** 自動補齊 `copilot` 子指令、指令選項及部分選項值。這是選用功能，但熟悉 CLI 後會很方便。

Copilot CLI 目前支援 Bash、Zsh 和 Fish 的補全腳本：

```shell
# Bash，僅限目前 session
source <(copilot completion bash)

# Bash，Linux 永久啟用
copilot completion bash | sudo tee /etc/bash_completion.d/copilot

# Zsh
copilot completion zsh > "${fpath[1]}/_copilot"

# Fish
copilot completion fish > ~/.config/fish/completions/copilot.fish
```

新增永久補全後請重新啟動 shell。PowerShell 可在 Windows 執行 Copilot CLI，但 `copilot completion` 目前僅支援 Bash、Zsh 和 Fish。

</details>

---

## 驗證身分

在 `copilot-cli-for-beginners` 儲存庫根目錄開啟終端機，啟動 CLI 並允許存取該資料夾。

```bash
copilot
```

你會被要求信任包含此儲存庫的資料夾（如果尚未信任）。你可以選擇僅信任一次，或永久信任。

<img src="images/copilot-trust.png" alt="Trusting files in a folder with the Copilot CLI" width="800"/>

信任資料夾後，你可以使用 GitHub 帳號登入。

```
> /login
```

**接下來會發生什麼：**

1. Copilot CLI 會顯示一次性代碼（例如 `ABCD-1234`）
2. 瀏覽器會開啟 GitHub 的裝置授權頁面。若尚未登入 GitHub，請先登入。
3. 按指示輸入該代碼
4. 選擇「Authorize」授權 GitHub Copilot CLI 存取
5. 回到終端機——你已成功登入！

<img src="images/auth-device-flow.png" alt="Device Authorization Flow - showing the 5-step process from terminal login to signed-in confirmation" width="800"/>

*裝置授權流程：終端機產生代碼，你在瀏覽器驗證，Copilot CLI 完成驗證。*

**提示**：登入狀態會跨 session 保留。除非 token 失效或你手動登出，只需做一次。

---

## 驗證功能正常

### 步驟 1：測試 Copilot CLI

現在你已登入，讓我們驗證 Copilot CLI 是否可正常運作。在終端機啟動 CLI（如果尚未啟動）：

```bash
> Say hello and tell me what you can help with
```

收到回應後，你可以離開 CLI：

```bash
> /exit
```

---

<details>
<summary>🎬 實際操作影片</summary>

![Hello Demo](images/hello-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡展示的不同。*

</details>

---

**預期輸出**：一個友善的回應，列出 Copilot CLI 的功能。

### 步驟 2：執行範例書籍應用程式

本課程提供一個範例應用程式，你將在課程中用 CLI 探索並改進它（你可以在 /samples/book-app-project 看到程式碼）。請先確認 *Python 書籍收藏終端機應用程式* 可正常運作。根據你的系統，請執行 `python` 或 `python3`。

> **注意：** 本課程主要範例使用 Python（`samples/book-app-project`），如果你選擇本機安裝，請確保你的電腦有 [Python 3.10+](https://www.python.org/downloads/)。如果你偏好，也可使用 JavaScript（`samples/book-app-project-js`）或 C#（`samples/book-app-project-cs`）版本。每個範例資料夾都有 README 說明如何執行該語言的應用程式。

```bash
cd samples/book-app-project
python book_app.py list
```

**預期輸出**：5 本書的清單，包括 "The Hobbit"、"1984" 和 "Dune"。

### 步驟 3：搭配書籍應用程式試用 Copilot CLI

（如果你剛執行完步驟 2）請先回到儲存庫根目錄：

```bash
cd ../..   # 如有需要，回到儲存庫根目錄
copilot 
> What does @samples/book-app-project/book_app.py do?
```

**預期輸出**：書籍應用程式主要功能和指令的摘要。

如果出現錯誤，請參考下方的 [疑難排解區段](#troubleshooting)。

完成後你可以離開 Copilot CLI：

```bash
> /exit
```

---

## ✅ 你已準備就緒！

安裝就到這裡。真正的樂趣從第 01 章開始，你將會：

- 觀看 AI 審查書籍應用程式並即時找出程式碼品質問題
- 學會三種不同的 Copilot CLI 使用方式
- 以純英文產生可運作的程式碼

**[繼續前往第 01 章：First Steps →](../01-setup-and-first-steps/README.md)**

---

## 疑難排解

### "copilot: command not found"

CLI 尚未安裝。請嘗試其他安裝方式：

```bash
# 如果 brew 失敗，請嘗試 npm：
npm install -g @github/copilot

# 或安裝腳本：
curl -fsSL https://gh.io/copilot-install | bash
```

### "You don't have access to GitHub Copilot"

1. 請在 [github.com/settings/copilot](https://github.com/settings/copilot) 確認你有 Copilot 訂閱
2. 如果你用的是工作帳號，請確認你的組織允許 CLI 存取

### "Authentication failed"

請重新驗證身分：

```bash
copilot
> /login
```

### 瀏覽器未自動開啟

請手動前往 [github.com/login/device](https://github.com/login/device) 並輸入終端機顯示的代碼。

### Token 過期

只需再次執行 `/login`：

```bash
copilot
> /login
```

### 還是卡住了？

- 查看 [GitHub Copilot CLI 文件](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)
- 搜尋 [GitHub Issues](https://github.com/github/copilot-cli/issues)

---

## 🔑 重點整理

1. **GitHub Codespace 是快速入門的好選擇**——Python、pytest 和 GitHub Copilot CLI 都已預先安裝，你可以直接開始實作
2. **多種安裝方式**——可依你的系統選擇（Homebrew、WinGet、npm 或安裝腳本）
3. **一次性驗證身分**——登入狀態會保留直到 token 失效
4. **書籍應用程式可正常運作**——你會在整個課程中使用 `samples/book-app-project`

> 📚 **官方文件**：[安裝 Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli/cli-getting-started) 以取得安裝選項與需求。

> 📋 **快速參考**：完整指令與捷徑請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

**[繼續前往第 01 章：First Steps →](../01-setup-and-first-steps/README.md)**
