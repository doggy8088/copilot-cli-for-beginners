# 進階情境功能

> 📖 **先備知識**：請先完成 [第 02 章：情境與對話](../02-context-conversations/README.md) 再閱讀本附錄。

本附錄介紹兩項進階情境功能：圖片處理，以及跨多個目錄的權限管理。

---

## 圖片處理

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

### 圖片實用情境範例

**1. UI 除錯**
```bash
> @bug-screenshot.png 按鈕沒有正確對齊。可能是哪個 CSS 造成的？
```

**2. 設計實作**
```bash
> @figma-export.png 寫出符合這個設計的 HTML 和 Tailwind CSS
```

**3. 錯誤分析**
```bash
> @error-screenshot.png 這個錯誤是什麼意思？要怎麼修正？
```

**4. 架構審查**
```bash
> @whiteboard-diagram.png 把這個架構圖轉成可以放在文件裡的 Mermaid 圖
```

**5. 前後版本比較**
```bash
> @before.png @after.png 這兩個 UI 版本之間有什麼變化？
```

### 圖片與程式碼結合

圖片搭配程式碼情境會更強大：

```bash
copilot

> @screenshot-of-bug.png @src/components/Header.jsx
> 標頭在截圖裡看起來不對。程式碼中是什麼原因？
```

### 圖片使用小技巧

- **裁切截圖**，只保留相關區域（節省情境 token）
- **使用高對比**，讓要分析的 UI 元素更明顯
- **必要時加註解**——上傳前圈出或標示問題區域
- **一個概念一張圖**——多張圖片可以，但要聚焦

---

## 權限模式

預設情況下，Copilot 只能存取你目前目錄的檔案。若要存取其他地方的檔案，需手動授權。

### 新增目錄

```bash
# 將目錄加入允許清單
copilot --add-dir /path/to/other/project

# 一次新增多個目錄
copilot --add-dir ~/workspace --add-dir /tmp
```

### 全路徑允許

```bash
# 完全解除路徑限制（請謹慎使用）
copilot --allow-all-paths
```

### 在對話中操作

```bash
copilot

> /add-dir /path/to/other/project
# 現在可以引用該目錄的檔案

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

### 多目錄存取需求情境

常見需要這些權限的情境：

1. **單一儲存庫作業**——跨套件比較程式碼
2. **跨專案重構**——更新共用函式庫
3. **文件專案**——引用多個程式碼庫
4. **移植作業**——比較舊版與新版實作

---

**[← 回到第 02 章](../02-context-conversations/README.md)** | **[返回附錄目錄](README.md)**
