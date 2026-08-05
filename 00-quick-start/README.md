![Chapter 00: Quick Start](assets/chapter-header.png)

歡迎！在本章中，你將安裝 GitHub Copilot CLI（命令列介面），使用你的 GitHub 帳號登入，並驗證一切運作正常。這是一個快速設定章節。當你準備就緒後，真正的示範將在第 01 章開始！

## 🎯 學習目標

完成本章後，你將能夠：

- 安裝 GitHub Copilot CLI
- 使用你的 GitHub 帳號登入
- 透過簡單測試驗證其運作

> ⏱️ **預估時間**：約 10 分鐘（5 分鐘閱讀 + 5 分鐘實作）

---

## ✅ 先備條件

- **具有 Copilot 存取權的 GitHub 帳號**。[查看訂閱方案](https://github.com/features/copilot/plans)。學生／教師可透過 [GitHub Education 免費取得 Copilot Pro](https://education.github.com/pack)。
- **終端機基本操作**：熟悉如 `cd` 和 `ls` 等指令

### 什麼是「Copilot 存取權」

GitHub Copilot CLI 需要有效的 Copilot 訂閱。你可以在 [github.com/settings/copilot](https://github.com/settings/copilot) 檢查你的狀態。你應該會看到下列其中一種：

- **Copilot Individual** - 個人訂閱
- **Copilot Business** - 透過你的組織
- **Copilot Enterprise** - 透過你的企業
- **GitHub Education** - 經驗證的學生／教師可免費使用

如果你看到「You don't have access to GitHub Copilot」，你需要使用免費方案、訂閱付費方案，或加入有提供存取權的組織。

---

## 安裝

> ⏱️ **時間預估**：安裝需 2-5 分鐘，驗證身份再多 1-2 分鐘。

### GitHub Codespaces（零設定）

如果你不想安裝任何先備套件，可以使用 GitHub Codespaces，它已經內建 GitHub Copilot CLI（你只需登入），並預先安裝了 Python 和 pytest。

1. [Fork 本教學倉庫](https://github.com/github/copilot-cli-for-beginners/fork) 到你的 GitHub 帳號
2. 選擇 **Code** > **Codespaces** > **Create codespace on main**
3. 等待幾分鐘讓容器建置完成
4. 一切就緒！終端機會自動在 Codespace 環境中開啟。

> 💡 **在 Codespace 驗證**：執行 `cd samples/book-app-project && python book_app.py help` 以確認 Python 與範例應用程式運作正常。

### 本機安裝

如果你想在本機執行 Copilot CLI 並搭配課程範例，請依下列步驟操作。

1. 將課程範例倉庫複製到你的電腦：

    ```bash
    git clone https://github.com/github/copilot-cli-for-beginners
    cd copilot-cli-for-beginners
    ```

2. 使用下列其中一種方式安裝 Copilot CLI。

    > 💡 **不確定選哪一種？** 如果你已安裝 Node.js，建議使用 `npm`。否則請選擇符合你系統的方式。

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

Shell Tab 補全可讓你按下 **Tab** 鍵自動補全 `copilot` 子指令、指令選項及部分選項值。這是選用功能，但當你熟悉 CLI 後會很方便。

Copilot CLI 目前支援 Bash、Zsh 和 Fish 的補全腳本：

```shell
# Bash，僅限目前會話
source <(copilot completion bash)

# Bash，Linux 永久啟用
copilot completion bash | sudo tee /etc/bash_completion.d/copilot

# Zsh
copilot completion zsh > "${fpath[1]}/_copilot"

# Fish
copilot completion fish > ~/.config/fish/completions/copilot.fish
```

新增永久補全後請重新啟動你的 shell。PowerShell 支援在 Windows 上執行 Copilot CLI，但 `copilot completion` 目前僅支援 Bash、Zsh 和 Fish。

</details>

---

## 驗證身份

在 `copilot-cli-for-beginners` 倉庫根目錄開啟終端機，啟動 CLI 並允許存取該資料夾。

```bash
copilot
```

你會被要求信任包含此倉庫的資料夾（如果尚未信任）。你可以選擇只信任這一次，或未來所有會話都信任。

<img src="assets/copilot-trust.png" alt="Trusting files in a folder with the Copilot CLI" width="800"/>

信任資料夾後，你可以使用 GitHub 帳號登入。

```
> /login
```

**接下來會發生什麼事（本機終端機）：**

1. 選擇登入你的 GitHub.com 帳號或企業帳號。
2. 選擇 `Sign in with your browser (recommended)`
3. 瀏覽器會自動開啟 GitHub 授權頁面。若尚未登入 GitHub，請先登入。
4. 點選「Authorize」授權 GitHub Copilot CLI 存取權。
5. 回到你的終端機——你已成功登入！

> 💡 **遠端或無頭終端機**：如果你在遠端伺服器或沒有瀏覽器的終端機（如 SSH），Copilot CLI 會自動切換為 **裝置代碼流程**。你會看到一組一次性代碼，例如 `ABCD-1234`。請在另一台機器的瀏覽器造訪 [github.com/login/device](https://github.com/login/device) 並輸入該代碼完成登入。若要強制使用特定流程，可用 `copilot login --web-flow` 觸發瀏覽器彈窗，或用 `copilot login --device-code` 使用代碼流程。你也可以在 `/login` 互動式選擇。
> 
> <img src="assets/auth-device-flow.png" alt="Device Authorization Flow - showing the 5-step process from terminal login to signed-in confirmation" width="800"/>
>
 
*瀏覽器流程：瀏覽器會自動開啟，你只需一鍵授權。遠端／無頭終端機則會顯示裝置代碼。*

**提示**：登入狀態會在多次會話間保留。除非你的 token 過期或你主動登出，否則只需登入一次。

---

## 驗證運作正常

### 步驟 1：測試 Copilot CLI

現在你已登入，讓我們驗證 Copilot CLI 是否能正常運作。在終端機啟動 CLI（如果尚未啟動）：

```bash
> Say hello and tell me what you can help with
```

收到回應後，你可以結束 CLI：

```bash
> /exit
```

---

<details>
<summary>🎬 實際操作影片！</summary>

![Hello Demo](assets/hello-demo.gif)

*示範輸出會有所不同。你的模型、工具與回應可能與此不同。*

</details>

---

**預期輸出**：一個友善的回應，列出 Copilot CLI 的功能。

### 步驟 2：執行範例書籍應用程式

本課程提供一個範例應用程式，你將在課程中使用 CLI 持續探索與改進它（你可以在 /samples/book-app-project 看到程式碼）。請先確認 *Python 書籍收藏終端機應用程式* 能正常運作。根據你的系統，請執行 `python` 或 `python3`。

> **注意：** 課程主要範例皆使用 Python（`samples/book-app-project`），因此若選擇本機安裝，需確保你的電腦有安裝 [Python 3.10+](https://www.python.org/downloads/)（Codespace 已預先安裝）。若你偏好，也有 JavaScript（`samples/book-app-project-js`）與 C#（`samples/book-app-project-cs`）版本可用。每個範例資料夾皆有 README 說明如何執行該語言的應用程式。

```bash
cd samples/book-app-project
python book_app.py list
```

**預期輸出**：包含 "The Hobbit"、"1984"、"Dune" 等 5 本書的清單。

### 步驟 3：用 Copilot CLI 試用書籍應用程式

（如果你剛執行完步驟 2，請先回到倉庫根目錄）

```bash
cd ../..   # 若需要，回到倉庫根目錄
copilot 
> What does @samples/book-app-project/book_app.py do?
```

**預期輸出**：書籍應用程式主要功能與指令的摘要說明。

如果出現錯誤，請參考下方的[疑難排解區段](#troubleshooting)。

完成後你可以結束 Copilot CLI：

```bash
> /exit
```

---

## ✅ 你已準備就緒！

安裝就到這裡。真正的精彩內容將在第 01 章展開，你將會：

- 觀看 AI 審查書籍應用程式並即時找出程式碼品質問題
- 學會三種不同的 Copilot CLI 使用方式
- 直接用英文生成可執行的程式碼

**[繼續前往第 01 章：First Steps →](../01-setup-and-first-steps/README.md)**

---

## 疑難排解

### "copilot: command not found"

CLI 尚未安裝。請嘗試其他安裝方式：

```bash
# 如果 brew 失敗，請試試 npm：
npm install -g @github/copilot

# 或安裝腳本：
curl -fsSL https://gh.io/copilot-install | bash
```

### "You don't have access to GitHub Copilot"

1. 請在 [github.com/settings/copilot](https://github.com/settings/copilot) 確認你有 Copilot 訂閱
2. 若使用公司帳號，請確認你的組織允許 CLI 存取

### "Authentication failed"

請重新驗證身份：

```bash
copilot
> /login
```

### 瀏覽器未自動開啟

在遠端或無頭終端機上，會自動使用裝置代碼流程。你的終端機會顯示一次性代碼。請造訪 [github.com/login/device](https://github.com/login/device) 並輸入該代碼，然後授權存取。

### Token 過期

只需再次執行 `/login`：

```bash
copilot
> /login
```

### 仍有問題？

- 請參考 [GitHub Copilot CLI 官方文件](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)
- 搜尋 [GitHub Issues](https://github.com/github/copilot-cli/issues)

---

## 🔑 重點整理

1. **GitHub Codespace 是快速開始的好選擇**——Python、pytest 與 GitHub Copilot CLI 都已預先安裝，可立即進入示範
2. **多種安裝方式**——可依你的系統選擇（Homebrew、WinGet、npm 或安裝腳本）
3. **一次性驗證身份**——登入狀態會持續到 token 過期
4. **書籍應用程式可正常運作**——你將在整個課程中使用 `samples/book-app-project`

> 📚 **官方文件**：[安裝 Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli/cli-getting-started) 了解安裝方式與需求。

> 📋 **快速參考**：完整指令與快捷鍵請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference)。

---

**[繼續前往第 01 章：First Steps →](../01-setup-and-first-steps/README.md)**
