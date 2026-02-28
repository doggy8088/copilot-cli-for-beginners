# 範例原始碼（舊版 — 選讀參考資料）

> **注意**：本課程的主要範例為 `../book-app-project/` 中的 **Python 書籍收藏應用程式**。這些 JS/React 檔案來自課程的早期版本，保留作為想參考 JS 範例的學員之選讀資料。

此資料夾包含範例原始檔。這些僅為示範用途，並非完整可執行的應用程式。

## 結構

```
src/
├── api/           # API route handlers
│   ├── auth.js    # Authentication endpoints
│   └── users.js   # User CRUD endpoints
├── auth/          # Client-side auth handlers
│   ├── login.js   # Login form logic
│   └── register.js # Registration form logic
├── components/    # React components
│   ├── Button.jsx # Reusable button
│   └── Header.jsx # App header with nav
├── models/        # Data models
│   └── User.js    # User model
├── services/      # Business logic
│   ├── productService.js
│   └── userService.js
├── utils/         # Helper functions
│   └── helpers.js
├── index.js       # App entry point
└── refactor-me.js # Beginner refactoring practice (Chapter 03)
```

## 使用方式

這些檔案在課程範例中以 `@` 語法引用：

```bash
copilot

> Explain what @samples/src/utils/helpers.js does
> Review @samples/src/api/ for security issues
> Compare @samples/src/auth/login.js and @samples/src/auth/register.js
```

## 重構練習

`refactor-me.js` 檔案專門為第 03 章的重構練習設計：

```bash
copilot

> @samples/src/refactor-me.js Rename the variable 'x' to something more descriptive
> @samples/src/refactor-me.js This function is too long. Split it into smaller functions.
> @samples/src/refactor-me.js Remove any unused variables
```

## 注意事項

- 檔案中刻意包含 TODOs 與小問題，供 Copilot 在審查時發現
- 這是示範程式碼，並非設計為實際可執行的應用，**不適合用於正式環境**
- 用於學習 `@` 檔案引用語法
