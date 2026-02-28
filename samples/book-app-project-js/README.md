# 書籍收藏應用程式

*(此 README 刻意寫得較為粗略，供你使用 GitHub Copilot CLI 加以改善)*

一個用於管理你已擁有或想閱讀的書籍的 JavaScript 應用程式。
支援新增、刪除與列出書籍，也可以將書籍標記為已讀。

---

## 目前功能

* 從 JSON 檔案讀取書籍資料（作為資料庫使用）
* 部分區域的輸入驗證較為薄弱
* 已有部分測試，但可能尚不充足

---

## 檔案說明

* `book_app.js` - CLI 主程式進入點
* `books.js` - 含資料邏輯的 BookCollection 類別
* `utils.js` - UI 與輸入的輔助函式
* `data.json` - 書籍範例資料
* `tests/test_books.js` - 使用 Node 內建測試執行器的入門測試

---

## 執行應用程式

```bash
node book_app.js list
node book_app.js add
node book_app.js find
node book_app.js remove
node book_app.js help
```

## 執行測試

```bash
npm test
```

---

## 備註

* 尚未達到正式上線的品質（顯而易見）
* 部分程式碼仍有改善空間
* 未來可考慮新增更多指令
