<!--
---
id: CopilotCLI-02
title: !translate 情境與對話
description: !translate 使用檔案與目錄情境、繼續先前會話，並學會用 GitHub Copilot CLI 撰寫有效的多輪對話。
audience: Developers / Students / Terminal users
slug: context-and-conversations
weight: 3
---
-->

![第 02 章：情境與對話](assets/chapter-header.png)

> **如果 AI 能看見你整個程式碼庫，而不只是單一檔案，會怎樣？**

在本章中，你將解鎖 GitHub Copilot CLI 的真正威力：情境。你會學會用 `@` 語法來引用檔案和目錄，讓 Copilot CLI 能深入理解你的程式碼庫。你將發現如何在多個會話間維持對話、如何在數天後精確地從上次中斷處繼續工作，並看到跨檔案分析如何發現單檔案審查完全忽略的錯誤。

## 🎯 學習目標

完成本章後，你將能夠：

- 使用 `@` 語法引用檔案、目錄和圖片
- 用 `--resume` 和 `--continue` 繼續先前的會話
- 了解 [情境窗口](../GLOSSARY.md#context-window) 的運作方式
- 撰寫有效的多輪對話
- 管理多專案工作流程下的目錄權限

> ⏱️ **預估時間**：約 50 分鐘（閱讀 20 分鐘 + 實作 30 分鐘）

---

## 🧩 真實世界類比：與同事協作

<img src="assets/colleague-context-analogy.png" alt="情境帶來差異－無情境 vs 有情境" width="800"/>

*就像你的同事一樣，Copilot CLI 不是讀心術專家。提供更多資訊能幫助人類與 Copilot 都給出更精準的協助！*

想像你要向同事解釋一個 bug：

> **沒有情境**：「書籍應用程式壞掉了。」

> **有情境**：「請看 `books.py`，特別是 `find_book_by_title` 函式。它沒有做不分大小寫比對。」

要給 Copilot CLI 提供情境，請用 *`@` 語法* 指定特定檔案。

---

# 必備：基本情境

<img src="assets/essential-basic-context.png" alt="發光的程式碼區塊由光軌連結，象徵情境如何在 Copilot CLI 對話中流動" width="800"/>

本節涵蓋你有效運用情境所需的一切。先掌握這些基礎。

---

## @ 語法

`@` 符號用於在提示中引用檔案和目錄。這就是你告訴 Copilot CLI「請看這個檔案」的方式。

> 💡 **注意**：本課程所有範例都使用本儲存庫內的 `samples/` 資料夾，你可以直接嘗試每個指令。

### 立即試試看（無需設定）

你可以用你電腦上的任何檔案來試試看：

```bash
copilot

# 指定你有的任何檔案
> Explain what @package.json does
> Summarize @README.md
> What's in @.gitignore and why?
```

> 💡 **沒有現成專案嗎？** 快速建立一個測試檔案：
> ```bash
> echo "def greet(name): return 'Hello ' + name" > test.py
> copilot
> > What does @test.py do?
> ```

### 基本 @ 模式

| 模式 | 作用 | 範例用途 |
|------|------|----------|
| `@file.py` | 引用單一檔案 | `Review @samples/book-app-project/books.py` |
| `@folder/` | 引用目錄下所有檔案 | `Review @samples/book-app-project/` |
| `@file1.py @file2.py` | 引用多個檔案 | `Compare @samples/book-app-project/book_app.py @samples/book-app-project/books.py` |

### 引用單一檔案

```bash
copilot

> Explain what @samples/book-app-project/utils.py does
```

---

<details>
<summary>🎬 實際操作影片！</summary>

![檔案情境示範](assets/file-context-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

---

### 引用多個檔案

```bash
copilot

> Compare @samples/book-app-project/book_app.py and @samples/book-app-project/books.py for consistency
```

### 引用整個目錄

```bash
copilot

> Review all files in @samples/book-app-project/ for error handling
```

---

## 跨檔案智慧

這就是情境變成超能力的地方。單檔案分析很有用，跨檔案分析則能徹底改變你的開發方式。

<img src="assets/cross-file-intelligence.png" alt="跨檔案智慧－比較單檔案與跨檔案分析，顯示一起分析檔案能揭露單獨時看不到的錯誤、資料流與模式" width="800"/>

### 示範：找出跨多檔案的錯誤

```bash
copilot

> @samples/book-app-project/book_app.py @samples/book-app-project/books.py
>
> How do these files work together? What's the data flow?
```

> 💡 **進階選項**：想做安全性導向的跨檔案分析，請試試 Python 安全性範例：
> ```bash
> > @samples/buggy-code/python/user_service.py @samples/buggy-code/python/payment_processor.py
> > Find security vulnerabilities that span BOTH files
> ```

---

<details>
<summary>🎬 實際操作影片！</summary>

![多檔案示範](assets/multi-file-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

---

**Copilot CLI 發現的內容**：

```
跨模組分析
=====================

1. 資料流模式
   book_app.py 建立 BookCollection 實例並呼叫方法
   books.py 定義 BookCollection 類別並管理資料持久化

   流程：book_app.py（UI）→ books.py（商業邏輯）→ data.json（儲存）

2. 重複的顯示函式
   book_app.py:9-21    show_books() 函式
   utils.py:28-36      print_books() 函式

   影響：兩個幾乎一樣的函式做同樣的事。如果你修改其中一個（例如格式），必須記得也要改另一個。

3. 不一致的錯誤處理
   book_app.py 處理 year 轉換時的 ValueError
   books.py 發生錯誤時靜默回傳 None/False

   模式：各模組間沒有統一的錯誤處理方式
```

**為什麼這很重要**：單檔案審查會錯過大局。只有跨檔案分析才能發現：
- **重複程式碼** 應該整併
- **資料流模式** 顯示元件如何互動
- **架構問題** 影響可維護性

---

### 示範：60 秒內理解一個程式碼庫

<img src="assets/codebase-understanding.png" alt="分割畫面比較，手動審查需 1 小時，AI 協助分析僅需 10 秒" width="800" />

新加入專案？用 Copilot CLI 快速了解它。

```bash
copilot

> @samples/book-app-project/
>
> In one paragraph, what does this app do and what are its biggest quality issues?
```

**你會得到**：
```
這是一個 CLI 書籍收藏管理器，讓使用者能新增、列出、移除和搜尋儲存在 JSON 檔案中的書籍。主要品質問題如下：

1. 重複的顯示邏輯－show_books() 和 print_books() 做一樣的事
2. 錯誤處理不一致－有些錯誤會丟出例外，有些只回傳 False
3. 沒有輸入驗證－year 可以是 0，title/author 可以是空字串
4. 缺少測試－關鍵函式如 find_book_by_title 沒有測試覆蓋

優先修正：整併重複的顯示函式並加入輸入驗證。
```

**結果**：原本需一小時閱讀的程式碼，壓縮成 10 秒。你能立刻知道該聚焦在哪裡。

---

## 實用範例

### 範例 1：帶情境的程式碼審查

```bash
copilot

> @samples/book-app-project/books.py Review this file for potential bugs

# Copilot CLI 現在有完整檔案內容，能給出具體回饋：
# "Line 49: Case-sensitive comparison may miss books..."
# "Line 29: JSON decode errors are caught but data corruption isn't logged..."

> What about @samples/book-app-project/book_app.py?

# 現在審查 book_app.py，但仍記得 books.py 的情境
```

### 範例 2：理解一個程式碼庫

```bash
copilot

> @samples/book-app-project/books.py What does this module do?

# Copilot CLI 讀取 books.py，理解 BookCollection 類別

> @samples/book-app-project/ Give me an overview of the code structure

# Copilot CLI 掃描目錄並摘要

> How does the app save and load books?

# Copilot CLI 能追蹤已讀過的程式碼
```

<details>
<summary>🎬 看多輪對話實際操作！</summary>

![多輪對話示範](assets/multi-turn-demo.gif)

*示範輸出會有所不同。你的模型、工具和回應可能與這裡顯示的不同。*

</details>

### 範例 3：多檔案重構

```bash
copilot

> @samples/book-app-project/book_app.py @samples/book-app-project/utils.py
> I see duplicate display functions: show_books() and print_books(). Help me consolidate these.

# Copilot CLI 同時看到兩個檔案，能建議如何合併重複程式碼
```

---

## 會話管理

會話會自動儲存。你可以隨時繼續先前的會話，從中斷處繼續。

### 會話自動儲存

每次對話都會自動儲存。只要正常結束即可：

```bash
copilot

> @samples/book-app-project/ Let's improve error handling across all modules

[... 進行一些工作 ...]

> /exit
```

### 繼續最近的會話

```bash
# 從上次中斷處繼續
copilot --continue
```

### 繼續特定會話

```bash
# 互動式選擇會話清單
copilot --resume

# -r 是 --resume 的簡寫（省點打字！）
copilot -r

# 或用 ID 繼續特定會話
copilot --resume=abc123

# 或用你給會話取的名字繼續
copilot --resume="my book app review"
```

> 💡 **怎麼找到會話 ID？** 你不用記住它們。執行 `copilot --resume` 不帶 ID 會顯示互動式清單，列出你所有先前會話、名稱、ID 和上次活動時間。直接選你要的即可。
>
> **多個終端機怎麼辦？** 每個終端機視窗都是獨立會話，有自己的情境。如果你同時開三個 Copilot CLI，就是三個獨立會話。從任一終端機執行 `--resume` 都能瀏覽全部。`--continue` 旗標會優先抓取目前工作目錄的會話；若無則選最近活動的會話。
>
> **可以不用重啟就切換會話嗎？** 可以。在啟動中的會話內用 `/resume` slash 指令：
> ```
> > /resume
> # 顯示可切換的會話清單
> ```

### 組織你的會話

給會話取有意義的名字，方便日後查找。你可以在啟動時命名，也可隨時在會話內重新命名：

```bash
# 啟動時直接命名會話
copilot --name book-app-review

# 或在會話內重新命名
copilot

> /rename book-app-review
# 會話已重新命名，方便辨識
```

會話命名後，你可以直接用名字繼續，不用瀏覽清單：

```bash
copilot --resume=book-app-review
```

要清理不需要的會話，可在會話內用 `/session delete`：

```bash
copilot

> /session delete            # 刪除目前會話
> /session delete abc123     # 刪除指定 ID 的會話
> /session delete-all        # 刪除所有會話（請小心使用！）
```

### 跨會話持久記憶

會話會儲存你的對話歷史，但 **記憶** 更進一步，讓 Copilot CLI 能在*所有會話*間記住偏好與事實，而不只限於單一會話。

```bash
copilot

> /memory show
# 顯示 Copilot CLI 目前記得你和專案的哪些資訊

> /memory on
# 啟用記憶（若你的帳號支援，預設為開啟）

> /memory off
# 關閉記憶（若你每次都想全新開始很有用）
```

例如，你告訴 Copilot CLI「我偏好用 pytest 做 Python 測試」，它就能記住這個偏好，未來自動套用。你不用每次重複說明。

> 💡 **記憶 vs. 會話**：會話儲存對話歷史，方便你繼續特定任務。記憶則儲存可重複使用的儲存庫事實與使用者偏好，Copilot 能在未來自動應用。把會話想成任務筆記本，記憶則是 Copilot 可延續帶著走的 reusable context。

### 檢查與管理情境

隨著你加入檔案和對話，Copilot CLI 的 [情境窗口](../GLOSSARY.md#context-window) 會逐漸填滿。有多種指令可協助你掌控：

```bash
copilot

> /context
Context usage: 62k/200k tokens (31%)

> /clear
# 放棄目前會話（不儲存歷史），開始全新對話

> /new
# 結束目前會話（會儲存到歷史以便搜尋/繼續），開始全新對話

> /rewind
# 開啟時間軸選擇器，讓你回溯到對話中的較早階段
```

> 💡 **何時用 `/clear` 或 `/new`**：如果你剛審查完 books.py，想切換討論 utils.py，請先執行 /new（或 /clear 若你不需要會話歷史）。否則舊主題的情境可能會干擾回應。

> 💡 **操作錯誤或想嘗試不同做法？** 用 `/rewind`（或連按兩下 Esc）開啟**時間軸選擇器**，可回到對話中任一早期點，而不只最近一次。回溯時，Copilot CLI 會問你要只還原對話，還是連 Copilot 修改過的檔案也一起還原——不需要 git 儲存庫。這很適合走錯路想回頭但又不想全部重來時。

---

### 從中斷處繼續

<img src="assets/session-persistence-timeline.png" alt="時間軸顯示 GitHub Copilot CLI 會話如何跨天持續－週一開始，週三繼續，完整情境被還原" width="800"/>

*會話在你離開時自動儲存。數天後繼續，完整情境（檔案、問題、進度）都被記住。*

想像這樣的多天工作流程：

```bash
# 週一：一開始就用名字啟動書籍應用程式審查
copilot --name book-app-review

> @samples/book-app-project/books.py
> Review and number all code quality issues

發現的品質問題：
1. 重複的顯示函式（book_app.py & utils.py）－中
2. 沒有空字串輸入驗證－中
3. 年份可為 0 或負數－低
4. 所有函式缺少型別提示－低
5. 缺少錯誤日誌－低

> Fix issue #1 (duplicate functions)
# 著手修正...

> /exit
```

```bash
# 週三：用名字精確從上次中斷處繼續
copilot --resume=book-app-review

> What issues remain unfixed from our book app review?

book-app-review 會話剩餘未修正問題：
2. 沒有空字串輸入驗證－中
3. 年份可為 0 或負數－低
4. 所有函式缺少型別提示－低
5. 缺少錯誤日誌－低

第 1 項（重複函式）已於週一修正。

> Let's tackle issue #2 next
```

**這有多強大**：數天後，Copilot CLI 仍記得：
- 你正在處理的檔案
- 編號的問題清單
- 哪些已經處理過
- 你的對話情境

不用重複解釋、不用重讀檔案，直接繼續工作。

---

**🎉 你已掌握所有必備技巧！** `@` 語法、會話管理（`--name`/`--continue`/`--resume`/`/rename`）、情境指令（`/context`/`/clear`）已足夠讓你高效工作。以下內容為進階選讀，等你準備好再回來。

---

# 進階選讀：更深入的情境運用

<img src="assets/optional-going-deeper.png" alt="藍紫色調的抽象水晶洞穴，象徵更深入探索情境概念" width="800"/>

這些主題建立在前述基礎之上。**挑你有興趣的看，或直接跳到[實作練習](#practice)。**

| 我想學... | 跳到 |
|---|---|
| 萬用字元模式與進階會話指令 | [進階 @ 模式與會話指令](#additional-patterns) |
| 跨多個提示累積情境 | [情境感知對話](#context-aware-conversations) |
| Token 限制與 `/compact` | [理解情境窗口](#understanding-context-windows) |
| 如何挑選要引用的檔案 | [選擇要引用的內容](#choosing-what-to-reference) |
| 分析截圖與設計稿 | [處理圖片](#working-with-images) |

<details>
<summary><strong>進階 @ 模式與會話指令</strong></summary>
<a id="additional-patterns"></a>

### 進階 @ 模式

進階用戶可用萬用字元模式與圖片引用：

| 模式 | 作用 |
|------|------|
| `@folder/*.py` | 資料夾下所有 .py 檔案 |
| `@**/test_*.py` | 遞迴萬用字元：尋找所有測試檔 |
| `@image.png` | 圖片檔，用於 UI 審查 |

```bash
copilot

> Find all TODO comments in @samples/book-app-project/**/*.py
```

### 檢視會話資訊

```bash
copilot

> /session
# 顯示目前會話細節與工作區摘要

> /usage
# 顯示會話指標與統計
```

### 分享你的會話

```bash
copilot

> /share file ./my-session.md
# 匯出會話為 markdown 檔案

> /share gist
# 建立 GitHub gist，分享會話

> /share html
# 匯出會話為自包含互動式 HTML 檔
# 適合與團隊分享精美報告或存檔參考
```

</details>

<details>
<summary><strong>情境感知對話</strong></summary>
<a id="context-aware-conversations"></a>

### 情境感知對話

多輪對話逐步累積成果時，魔法就發生了。

#### 範例：漸進式強化

```bash
copilot

> @samples/book-app-project/books.py Review the BookCollection class

Copilot CLI：「這個類別功能齊全，但我注意到：
1. 有些方法缺少型別提示
2. 沒有檢查 title/author 是否為空
3. 錯誤處理可再加強」

> Add type hints to all methods

Copilot CLI：「這是加上完整型別提示的類別...」
[顯示加註型別的版本]

> Now improve error handling

Copilot CLI：「在加上型別提示的基礎上，這是加強錯誤處理的版本...」
[加入驗證與正確例外處理]

> Generate tests for this final version

Copilot CLI：「根據這個有型別與錯誤處理的類別...」
[產生完整測試]
```

注意每個提示都建立在前一次的成果上。這就是情境的威力。

</details>

<details>
<summary><strong>理解情境窗口</strong></summary>
<a id="understanding-context-windows"></a>

### 理解情境窗口

你已從基礎學過 `/context` 和 `/clear`。這裡更深入說明情境窗口的運作。

每個 AI 都有一個「情境窗口」，即它一次能考慮的文字量。

<img src="assets/context-window-visualization.png" alt="情境窗口視覺化" width="800"/>

*情境窗口就像一張桌子：一次只能放有限的東西。檔案、對話歷史與系統提示都會佔用空間。*

#### 達到上限時會發生什麼

```bash
copilot

> /context

Context usage: 45,000 / 128,000 tokens (35%)

# 加入更多檔案與對話時，這個數字會增加

> @large-codebase/

Context usage: 120,000 / 128,000 tokens (94%)

# 警告：接近情境上限

> @another-large-file.py

Context limit reached. Older context will be summarized.
```

#### `/compact` 指令

當你的情境快滿了又不想丟失對話時，`/compact` 會將歷史摘要，釋放 token 空間：

```bash
copilot

> /compact
# 摘要對話歷史，釋放情境空間
# 你的重點發現與決策會被保留
```

你也可以給 `/compact` 加上聚焦指示，決定摘要時優先保留哪些內容：

```bash
copilot

> /compact focus on the list of bugs we found and decisions made
# 摘要歷史，讓 bug 清單與決策更明顯
```

> 💡 **何時用聚焦指示**：如果你的對話涵蓋很多主題，聚焦指示能讓 `/compact` 優先保留對你下一步最重要的部分，避免斷線。

#### 情境效率小技巧

| 情境 | 行動 | 原因 |
|------|------|------|
| 開新主題 | `/clear` | 移除無關情境 |
| 走錯路 | `/rewind` | 回溯對話（可選擇還原檔案） |
| 對話過長 | `/compact` | 摘要歷史，釋放 token |
| 只需特定檔案 | `@file.py` 而非 `@folder/` | 只載入所需內容 |
| 達到上限 | `/new` 或 `/clear` | 全新情境 |
| 多主題 | 每主題用 `/rename` | 容易繼續正確會話 |

#### 大型程式碼庫最佳實踐

1. **具體明確**：用 `@samples/book-app-project/books.py` 取代 `@samples/book-app-project/`
2. **主題切換時清空情境**：切換焦點時用 `/new` 或 `/clear`
3. **善用 `/compact`**：摘要對話，釋放情境
4. **多開會話**：每個功能或主題用一個會話

</details>

<details>
<summary><strong>選擇要引用的內容</strong></summary>
<a id="choosing-what-to-reference"></a>

### 選擇要引用的內容

不是所有檔案都同等重要。以下是明智選擇的方式：

#### 檔案大小考量

| 檔案大小 | 約略 [Token 數](../GLOSSARY.md#token) | 策略 |
|----------|-------------------|------|
| 小（<100 行） | ~500-1,500 tokens | 可自由引用 |
| 中（100-500 行） | ~1,500-7,500 tokens | 引用特定檔案 |
| 大（500+ 行） | 7,500+ tokens | 謹慎選擇，聚焦特定檔案 |
| 超大（1000+ 行） | 15,000+ tokens | 考慮拆分或只針對區段 |

**具體例子：**
- 書籍應用的 4 個 Python 檔合計 ≈ 2,000-3,000 tokens
- 典型 Python 模組（200 行）≈ 3,000 tokens
- Flask API 檔（400 行）≈ 6,000 tokens
- 你的 package.json ≈ 200-500 tokens
- 一個簡短提示＋回應 ≈ 500-1,500 tokens

> 💡 **程式碼 token 粗估法：** 行數 × 15 ≈ token 數。僅供參考。

#### 包含與排除的選擇

**高價值**（建議包含）：
- 進入點（`book_app.py`、`main.py`、`app.py`）
- 你要詢問的特定檔案
- 目標檔案直接 import 的檔案
- 設定檔（`requirements.txt`、`pyproject.toml`）
- 資料模型或 dataclass

**低價值**（可考慮排除）：
- 產生的檔案（編譯輸出、打包資產）
- node modules 或 vendor 目錄
- 大型資料檔或測試資料
- 與問題無關的檔案

#### 具體性光譜

```
較不具體 ────────────────────────► 較具體
@samples/book-app-project/                      @samples/book-app-project/books.py:47-52
     │                                       │
     └─ 掃描全部（佔較多情境）                 └─ 只載入所需（節省情境）
```

**何時用廣泛引用**（`@samples/book-app-project/`）：
- 初步探索程式碼庫
- 尋找跨多檔案的模式
- 架構審查

**何時用具體引用**（`@samples/book-app-project/books.py`）：
- 偵錯特定問題
- 審查特定檔案
- 詢問單一函式

#### 實用範例：分階段載入情境

```bash
copilot

# 步驟 1：先看結構
> @package.json What frameworks does this project use?

# 步驟 2：根據回答縮小範圍
> @samples/book-app-project/ Show me the project structure

# 步驟 3：聚焦重點
> @samples/book-app-project/books.py Review the BookCollection class

# 步驟 4：只在需要時加入相關檔案
> @samples/book-app-project/book_app.py @samples/book-app-project/books.py How does the CLI use the BookCollection?
```

這種分階段方式能讓情境聚焦且高效。

</details>

<details>
<summary><strong>處理圖片</strong></summary>
<a id="working-with-images"></a>

### 處理圖片

你可以使用 `@` 語法在對話中插入圖片，或直接**從剪貼簿貼上**（Cmd+V / Ctrl+V）。Copilot CLI 能夠分析螢幕截圖、設計稿和圖表，協助 UI 除錯、設計實作與錯誤分析。

```bash
copilot

> @assets/screenshot.png 這張圖片發生了什麼事？

> @assets/mockup.png 請撰寫符合此設計的 HTML 和 CSS。將 HTML 放在新檔案 index.html，CSS 放在 styles.css。
```

> 📖 **深入了解**：請參閱[進階情境功能](../appendices/additional-context.md#working-with-images)，瞭解支援的格式、實用案例，以及圖片與程式碼結合的小技巧。

</details>

---

# 練習

<img src="../assets/practice.png" alt="溫馨書桌擺設，螢幕顯示程式碼，檯燈、咖啡杯與耳機，準備好動手練習" width="800"/>

是時候運用你的情境與會話管理技巧了。

---

## ▶️ 自己動手試試

### 專案完整審查

本課程提供範例檔案可供你直接審查。啟動 copilot 並執行下方的提示：

```bash
copilot

> @samples/book-app-project/ 請幫我進行這個專案的程式碼品質審查

# Copilot CLI 會找出像是：
# - 重複的顯示函式
# - 缺少輸入驗證
# - 不一致的錯誤處理
```

> 💡 **想用自己的檔案試試嗎？** 建立一個小型 Python 專案（`mkdir -p my-project/src`），新增一些 .py 檔案，然後用 `@my-project/src/` 來審查它們。如果你想，也可以請 copilot 幫你產生範例程式碼！

### 會話工作流程

```bash
copilot

> /rename book-app-review
> @samples/book-app-project/books.py 我們來為空白書名加入輸入驗證

[Copilot CLI 建議驗證做法]

> 實作這個修正
> 現在整合 @samples/book-app-project/ 中重複的顯示函式
> /exit

# 稍後 - 從上次進度繼續
copilot --continue

> 為我們做的變更產生測試
```

---

完成示範後，試試這些變化題：

1. **跨檔案挑戰**：分析 book_app.py 和 books.py 如何協作：
   ```bash
   copilot
   > @samples/book-app-project/book_app.py @samples/book-app-project/books.py
   > 這兩個檔案有什麼關聯？有沒有任何程式碼異味？
   ```

2. **會話挑戰**：啟動一個會話，用 `/rename my-first-session` 命名，做些事情後用 `/exit` 離開，再用 `copilot --continue`。它還記得你在做什麼嗎？

3. **情境挑戰**：在會話中執行 `/context`。你用了多少 token？試試 `/compact` 再檢查一次。（更多 `/compact` 用法請見 Going Deeper 的 [理解情境窗口](#understanding-context-windows)。）

**自我檢查**：當你能解釋為什麼 `@folder/` 比逐一開啟每個檔案更強大時，就代表你已經理解情境了。

---

## 📝 作業

### 主要挑戰：追蹤資料流

前面的實作範例著重於程式碼品質審查與輸入驗證。現在請用相同的情境技巧，練習追蹤資料在應用程式中的流動：

1. 啟動互動式會話：`copilot`
2. 同時引用 `books.py` 和 `book_app.py`：
   `@samples/book-app-project/books.py @samples/book-app-project/book_app.py 追蹤一本書如何從使用者輸入被儲存到 data.json。每個步驟涉及哪些函式？`
3. 加入資料檔案以提供更多情境：
   `@samples/book-app-project/data.json 如果這個 JSON 檔案遺失或損毀會發生什麼事？哪些函式會失敗？`
4. 請求跨檔案的改進建議：
   `@samples/book-app-project/books.py @samples/book-app-project/utils.py 建議一個能在兩個檔案都適用的一致性錯誤處理策略。`
5. 重新命名會話：`/rename data-flow-analysis`
6. 用 `/exit` 離開，然後用 `copilot --continue` 回到會話，追問資料流相關問題

**成功標準**：你能跨多個檔案追蹤資料流、恢復命名會話，並獲得跨檔案建議。

<details>
<summary>💡 提示（點擊展開）</summary>

**開始步驟：**
```bash
cd /path/to/copilot-cli-for-beginners
copilot
> @samples/book-app-project/books.py @samples/book-app-project/book_app.py 追蹤一本書如何從使用者輸入被儲存到 data.json。
> @samples/book-app-project/data.json 如果這個檔案遺失或損毀會發生什麼事？
> /rename data-flow-analysis
> /exit
```

然後用：`copilot --continue` 恢復

**實用指令：**
- `@file.py` - 引用單一檔案
- `@folder/` - 引用資料夾內所有檔案（注意結尾的 `/`）
- `/context` - 檢查你用了多少情境
- `/rename <name>` - 幫會話命名，方便日後繼續

</details>

### 加分挑戰：情境上限

1. 用 `@samples/book-app-project/` 一次引用所有書籍應用程式檔案
2. 針對不同檔案（`books.py`、`utils.py`、`book_app.py`、`data.json`）提出多個詳細問題
3. 執行 `/context` 查看使用量。填滿得有多快？
4. 練習用 `/compact` 回收空間，然後繼續對話
5. 嘗試更精確地引用檔案（例如用 `@samples/book-app-project/books.py` 取代整個資料夾），觀察對情境用量的影響

---

<details>
<summary>🔧 <strong>常見錯誤與疑難排解</strong>（點擊展開）</summary>

### 常見錯誤

| 錯誤 | 會發生什麼事 | 修正方式 |
|------|--------------|----------|
| 忘記在檔名前加 `@` | Copilot CLI 會把 "books.py" 當成純文字 | 用 `@samples/book-app-project/books.py` 來引用檔案 |
| 以為會話會自動保存 | 重新啟動 `copilot` 會失去所有先前情境 | 用 `--continue`（上次會話）或 `--resume`（選擇會話） |
| 引用當前目錄外的檔案 | 出現 "Permission denied" 或 "File not found" 錯誤 | 用 `/add-dir /path/to/directory` 開放存取權限 |
| 換主題沒用 `/clear` | 舊情境會干擾新主題的回應 | 換任務前先執行 `/clear` |

### 疑難排解

**"File not found" 錯誤** - 確認你在正確的目錄下：

```bash
pwd  # 檢查目前目錄
ls   # 列出檔案

# 然後啟動 copilot 並用相對路徑
copilot

> Review @samples/book-app-project/books.py
```

**"Permission denied"** - 將目錄加入允許清單：

```bash
copilot --add-dir /path/to/directory

# 或在會話中：
> /add-dir /path/to/directory
```

**情境太快填滿**：
- 更精確地引用檔案
- 不同主題間用 `/clear`
- 將工作分散到多個會話

</details>

---

# 小結

## 🔑 重點整理

1. **`@` 語法** 讓 Copilot CLI 取得檔案、資料夾與圖片的情境
2. **多輪對話** 會隨著情境累積而更深入
3. **會話自動儲存**：啟動時用 `--name` 命名，之後用 `--resume=<name>` 恢復，或用 `--continue` 接續最近的會話
4. **情境窗口有限**：用 `/clear`、`/compact`、`/context`、`/new`、`/rewind` 管理。用 `/compact focus on <topic>` 決定摘要保留重點
5. **持久記憶**（`/memory`）讓 Copilot CLI 能跨*所有*會話記住偏好與事實——不只限於當前會話
6. **權限旗標**（`--add-dir`、`--allow-all`）控管多目錄存取。請謹慎使用！
7. **圖片引用**（`@screenshot.png`）可視覺化協助 UI 除錯

> 📚 **官方文件**：[使用 Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli) 取得完整的情境、會話與檔案操作參考。

> 📋 **快速參考**：請見 [GitHub Copilot CLI 指令參考](https://docs.github.com/en/copilot/reference/cli-command-reference) 取得完整指令與快捷鍵列表。

---

## ➡️ 接下來

現在你已經會給 Copilot CLI 提供情境，接下來讓我們把這些技巧用在實際開發任務上。你剛學到的情境技巧（檔案引用、跨檔案分析、會話管理）正是下一章強大工作流程的基礎。

在 **[第 03 章：開發工作流程](../03-development-workflows/README.md)**，你將學到：

- 程式碼審查工作流程
- 重構模式
- 除錯協助
- 測試產生
- Git 整合

---

**[← 回到第 01 章](../01-setup-and-first-steps/README.md)** | **[繼續前往第 03 章 →](../03-development-workflows/README.md)**
