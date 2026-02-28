# 有缺陷的程式碼範例

此資料夾包含刻意埋入 bugs 的程式碼，用於搭配 GitHub Copilot CLI 練習程式碼審查與除錯。

## 資料夾結構

```
buggy-code/
├── js/                    # JavaScript examples
│   ├── userService.js     # User management with 8 bugs
│   └── paymentProcessor.js # Payment handling with 8 bugs
└── python/                # Python examples
    ├── user_service.py    # User management with 10 bugs
    └── payment_processor.py # Payment handling with 12 bugs
```

## 快速開始

### JavaScript

```bash
copilot

# Security audit
> Review @samples/buggy-code/js/userService.js for security issues

# Find all bugs
> Find all bugs in @samples/buggy-code/js/paymentProcessor.js
```

### Python

```bash
copilot

# Security audit
> Review @samples/buggy-code/python/user_service.py for security issues

# Find all bugs
> Find all bugs in @samples/buggy-code/python/payment_processor.py
```

## Bug 類別

### 兩種語言共同的問題

| Bug 類型 | 說明 |
|----------|------|
| SQL Injection | 使用者輸入直接拼接進 SQL 查詢 |
| Hardcoded Secrets | API 金鑰與密碼寫死在原始碼中 |
| Race Conditions | 共用狀態缺乏適當的同步機制 |
| Sensitive Data Logging | 密碼與卡號被寫入日誌 |
| Missing Input Validation | 未對使用者提供的資料進行檢查 |
| No Error Handling | 缺少 try/catch 或 try/except 區塊 |
| Weak Password Comparison | 使用明文比對或存在計時攻擊漏洞的比對方式 |
| Missing Auth Checks | 操作前未驗證授權 |

### Python 特有的 Bugs

| Bug 類型 | 說明 |
|----------|------|
| Pickle Deserialization | 對不可信資料使用 `pickle.loads()` |
| eval() Injection | 將使用者輸入傳入 `eval()` |
| Unsafe YAML Loading | 未使用安全載入器呼叫 `yaml.load()` |
| Shell Injection | 在 `os.system()` 呼叫中使用使用者輸入 |
| Weak Hashing | 使用 MD5 進行密碼雜湊 |
| Insecure Random | 將 `random` 模組用於安全用途 |

## 練習題

1. **安全性審計**：執行全面的安全審查，依嚴重程度列出所有漏洞
2. **修復單一 Bug**：挑選一個關鍵 bug，透過 Copilot 取得修復方案，並理解其原理
3. **生成測試**：建立能在部署前捕捉這些 bugs 的測試案例
4. **安全重構**：在維持功能不變的前提下，修復 SQL injection 漏洞
