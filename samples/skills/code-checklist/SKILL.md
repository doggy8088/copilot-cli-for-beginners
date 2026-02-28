---
name: code-checklist
description: Team code quality checklist - use for checking Python code quality, bugs, security issues, and best practices
---

# 程式碼檢查清單技能

檢查 Python 程式碼時，請套用此清單。

## 程式碼品質檢查清單

- [ ] 所有函式均已加上型別提示
- [ ] 未使用裸露的 except 子句
- [ ] 未使用可變的預設引數
- [ ] 檔案 I/O 使用 context manager
- [ ] 函式長度不超過 50 行
- [ ] 變數與函式命名符合 PEP 8（snake_case）

## 輸入驗證檢查清單

- [ ] 使用者輸入在處理前已驗證
- [ ] 已處理邊界情境（空字串、None、超出範圍的值）
- [ ] 錯誤訊息清晰易懂

## 測試檢查清單

- [ ] 新程式碼有對應的 pytest 測試
- [ ] 已涵蓋邊界情境
- [ ] 測試名稱具有描述性

## 輸出格式

以下列格式呈現結果：

```
## Code Checklist: [filename]

### Code Quality
- [PASS/FAIL] Description of finding

### Input Validation
- [PASS/FAIL] Description of finding

### Testing
- [PASS/FAIL] Description of finding

### Summary
[X] items need attention before merge
```
