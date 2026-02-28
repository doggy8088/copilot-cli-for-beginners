# 額外情境功能

> 📖 **先備條件**：請先完成[第 02 章：情境與對話](../02-context-conversations/README.md)後再閱讀本附錄。

本附錄介紹兩項額外的情境功能：使用圖片，以及跨多個目錄的權限管理。

---

## 使用圖片

您可以在對話中使用 `@` 語法引用圖片。Copilot 能分析螢幕截圖、設計稿、架構圖及其他視覺內容。

### 基本圖片引用

```bash
copilot

> @screenshot.png What's happening in this UI?

# Copilot analyzes the image and responds

> @mockup.png @current-design.png Compare these two designs

# You can also drag and drop images or paste from clipboard
```

### 支援的圖片格式

| 格式 | 最適用於 |
|------|---------|
| PNG | 螢幕截圖、UI 設計稿、架構圖 |
| JPG/JPEG | 照片、複雜影像 |
| GIF | 簡單示意圖（僅分析第一幀） |
| WebP | 網頁截圖 |

### 圖片實用情境

**1. UI 除錯**
```bash
> @bug-screenshot.png The button doesn't align properly. What CSS might cause this?
```

**2. 設計實作**
```bash
> @figma-export.png Write the HTML and Tailwind CSS to match this design
```

**3. 錯誤分析**
```bash
> @error-screenshot.png What does this error mean and how do I fix it?
```

**4. 架構審查**
```bash
> @whiteboard-diagram.png Convert this architecture diagram to a Mermaid diagram I can put in docs
```

**5. 前後對比**
```bash
> @before.png @after.png What changed between these two versions of the UI?
```

### 圖片與程式碼的結合應用

將圖片與程式碼情境搭配使用，效果更為強大：

```bash
copilot

> @screenshot-of-bug.png @src/components/Header.jsx
> The header looks wrong in the screenshot. What's causing it in the code?
```

### 圖片使用技巧

- **裁切截圖**，只保留相關區域（節省情境 token）
- **提高對比度**，使欲分析的 UI 元素更清晰
- **必要時加上標註**——上傳前圈出或標示問題區域
- **一圖一概念**——雖可使用多張圖片，但保持焦點更有效率

---

## 權限設定模式

預設情況下，Copilot 僅能存取您當前目錄中的檔案。若需存取其他位置的檔案，則須授予對應的存取權限。

### 新增目錄

```bash
# Add a directory to the allowed list
copilot --add-dir /path/to/other/project

# Add multiple directories
copilot --add-dir ~/workspace --add-dir /tmp
```

### 開放所有路徑

```bash
# Disable path restrictions entirely (use with caution)
copilot --allow-all-paths
```

### 在對話中管理權限

```bash
copilot

> /add-dir /path/to/other/project
# Now you can reference files from that directory

> /list-dirs
# See all allowed directories
```

### 用於自動化腳本

```bash
# Allow all permissions for non-interactive scripts
copilot -p "Review @src/" --allow-all

# Or use the memorable alias
copilot -p "Review @src/" --yolo
```

### 需要多目錄存取的常見情境

以下是常見的使用場景：

1. **Monorepo 開發** — 跨套件比較程式碼
2. **跨專案重構** — 更新共用函式庫
3. **文件編寫專案** — 同時參照多個程式碼庫
4. **遷移作業** — 比對新舊實作

---

**[← 返回第 02 章](../02-context-conversations/README.md)** | **[返回附錄](README.md)**
