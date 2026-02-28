# 書籍應用程式 - 含缺陷版本

此目錄包含書籍收藏應用程式的刻意含缺陷版本，供第 03 章的除錯練習使用。

**請勿直接修復這些缺陷。** 它們的存在是為了讓學習者練習使用 GitHub Copilot CLI 來找出並排除問題。

---

## 刻意埋入的缺陷

### books_buggy.py

| # | 缺陷 | 症狀 |
|---|------|------|
| 1 | `find_book_by_title()` 使用大小寫完全相符的比對 | 搜尋 "the hobbit" 時毫無結果，即使 "The Hobbit" 存在於資料中 |
| 2 | `save_books()` 未使用 context manager | 檔案句柄洩漏；對權限問題缺乏錯誤處理 |
| 3 | `add_book()` 未進行年份驗證 | 接受負數年份、西元 0 年及遙遠未來的年份 |
| 4 | `remove_book()` 使用 `in` 子字串比對 | 刪除 "Dune" 時也會誤刪 "Dune Messiah" |
| 5 | `mark_as_read()` 將所有書籍標記為已讀 | 迴圈變數缺陷——遍歷了全部書籍，而非僅限符合的那本 |
| 6 | `find_by_author()` 要求完全相符 | 搜尋 "Tolkien" 找不到 "J.R.R. Tolkien"（不支援部分比對） |

### book_app_buggy.py

| # | 缺陷 | 症狀 |
|---|------|------|
| 7 | `show_books()` 編號從 0 開始 | 書籍顯示為 "0. ..."、"1. ..."，而非 "1. ..."、"2. ..." |
| 8 | `handle_add()` 接受空白的書名／作者 | 可新增書名和作者皆為空白的書籍 |
| 9 | `handle_remove()` 永遠顯示成功訊息 | 即使書籍不存在，也會顯示「書籍已移除」 |

---

## 第 03 章使用方式

```bash
copilot

> @samples/book-app-buggy/books_buggy.py Users report that searching for
> "The Hobbit" returns no results even though it's in the data. Debug why.

> @samples/book-app-buggy/book_app_buggy.py When I remove a book that
> doesn't exist, the app says it was removed. Help me find why.
```
