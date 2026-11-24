# 進階情境功能

> 📖 **前置需求**：請先完成[第 02 章：情境與對話](../02-context-conversations/README.md)再閱讀本附錄。

本附錄介紹兩項進階情境功能：處理圖片與跨多個目錄的權限管理。

---

## 處理圖片

你可以使用 `@` 語法在對話中加入圖片。Copilot 能分析螢幕截圖、設計稿、圖表及其他視覺內容。

### 基本圖片引用

```bash
copilot

> @screenshot.png 這個 UI 發生了什麼事？

# Copilot 會分析圖片並回應

> @mockup.png @current-design.png 比較這兩個設計

# 你也可以拖曳圖片或從剪貼簿貼上
```

### 支援的圖片格式

| 格式 | 最適用於 |
|--------|----------|
| PNG | 螢幕截圖、UI 設計稿、圖表 |
| JPG/JPEG | 照片、複雜圖片 |
| GIF | 簡單圖表（僅第一幀） |
| WebP | 網頁截圖 |

### 圖片實用案例

**1. UI 除錯**
```
> @bug-screenshot.png 按鈕沒有正確對齊。可能是哪些 CSS 造成的？
```

**2. 設計實作**
```
> @figma-export.png 寫出符合這個設計的 HTML 和 Tailwind CSS
```

**3. 錯誤分析**
```
> @error-screenshot.png 這個錯誤是什麼意思？我要怎麼修正？
```

**4. 架構審查**
```
> @whiteboard-diagram.png 把這個架構圖轉成我可以放在文件裡的 Mermaid 圖
```

**5. 前後比較**
```
> @before.png @after.png 這兩個 UI 版本有什麼變化？
```

### 圖片與程式碼結合

將圖片與程式碼情境結合，能發揮更大威力：

```bash
copilot

> @screenshot-of-bug.png @src/components/Header.jsx
> 截圖中的 header 看起來有問題。程式碼裡是什麼原因？
```

### 圖片使用小技巧

- **裁切截圖**，只保留相關區域（節省情境 token）
- **提高對比度**，讓要分析的 UI 元素更明顯
- **必要時加註記**——上傳前可圈選或標記問題區域
- **一張圖片一個重點**——可多張，但建議聚焦

---

## 權限模式

預設情況下，Copilot 只能存取你目前目錄下的檔案。若要存取其他位置的檔案，需額外授權。

### 新增目錄

```bash
# 將目錄加入允許清單
copilot --add-dir /path/to/other/project

# 一次加入多個目錄
copilot --add-dir ~/workspace --add-dir /tmp
```

### 允許所有路徑

```bash
# 完全停用路徑限制（請小心使用）
copilot --allow-all-paths
```

### 會話中操作

```bash
copilot

> /add-dir /path/to/other/project
# 現在你可以引用該目錄下的檔案

> /list-dirs
# 查看所有已允許的目錄

> /yolo
# /allow-all 的快速別名——自動同意所有權限提示
```

### 自動化用途

```bash
# 非互動腳本允許所有權限
copilot -p "Review @src/" --allow-all

# 或使用好記的別名
copilot -p "Review @src/" --yolo
```

### 需要多目錄存取的情境

常見需要這些權限的情境：

1. **Monorepo 作業**——跨多個套件比較程式碼
2. **跨專案重構**——更新共用函式庫
3. **文件專案**——引用多個程式碼庫
4. **遷移作業**——比較新舊實作

---

**[← 回到第 02 章](../02-context-conversations/README.md)** | **[返回附錄列表](README.md)**
