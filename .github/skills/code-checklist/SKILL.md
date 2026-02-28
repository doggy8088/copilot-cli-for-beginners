---
name: code-checklist
description: 團隊程式碼品質清單 - 適用於檢查 Python 程式碼品質、錯誤、安全性問題及最佳實踐
---

# 程式碼檢查清單技能

檢查 Python 程式碼時，請套用此清單。

## 程式碼品質清單

- [ ] 所有函式均具備型別提示
- [ ] 沒有裸露的 except 子句
- [ ] 沒有可變的預設引數
- [ ] 檔案 I/O 使用情境管理器
- [ ] 函式不超過 50 行
- [ ] 變數與函式命名遵循 PEP 8（snake_case）

## 輸入驗證清單

- [ ] 使用者輸入在處理前已驗證
- [ ] 已處理邊界情況（空字串、None、超出範圍的值）
- [ ] 錯誤訊息清晰且具指引性

## 測試清單

- [ ] 新程式碼具有對應的 pytest 測試
- [ ] 邊界情況已涵蓋
- [ ] 測試使用描述性名稱

## 輸出格式

呈現結果如下：

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
