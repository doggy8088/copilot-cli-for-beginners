# 書籍收藏應用程式

*(此 README 刻意寫得較為粗略，供你使用 GitHub Copilot CLI 加以改善)*

一個用於管理你已擁有或想閱讀的書籍的 Python 應用程式。
支援新增、刪除與列出書籍，也可以將書籍標記為已讀。

---

## 目前功能

* 從 JSON 檔案讀取書籍資料（作為資料庫使用）
* 部分區域的輸入驗證較為薄弱
* 已有部分測試，但可能尚不充足

---

## 檔案說明

* `book_app.py` - CLI 主程式進入點
* `books.py` - 含資料邏輯的 BookCollection 類別
* `utils.py` - UI 與輸入的輔助函式
* `data.json` - 書籍範例資料
* `tests/test_books.py` - pytest 入門測試

---

## 執行應用程式

```bash
python book_app.py list
python book_app.py add
python book_app.py find
python book_app.py remove
python book_app.py help
```

## 執行測試

```bash
python -m pytest tests/
```

---

## 備註

* 尚未達到正式上線的品質（顯而易見）
* 部分程式碼仍有改善空間
* 未來可考慮新增更多指令
