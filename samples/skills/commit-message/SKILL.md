---
name: commit-message
description: Generate conventional commit messages - use when creating commits, writing commit messages, or asking for git commit help
---

# Commit Message 技能

依照 Conventional Commits 規範產生 commit 訊息。

## 格式

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

## 類型

| 類型 | 使用時機 |
|------|-------------|
| `feat` | 新功能 |
| `fix` | 錯誤修正 |
| `docs` | 僅修改文件 |
| `style` | 格式調整（不影響程式邏輯） |
| `refactor` | 既非修正錯誤也非新增功能的程式碼重構 |
| `perf` | 效能改善 |
| `test` | 新增或更新測試 |
| `chore` | 維護性工作 |

## 規則

1. 標題行最多 72 個字元
2. 使用祈使語氣（用「add」而非「added」或「adds」）
3. 標題行結尾不加句點
4. 標題與內文之間以空行分隔
5. 內文說明**做了什麼**以及**為什麼**，而非如何做

## 範例

簡單格式：
```
fix(auth): prevent redirect loop on expired sessions
```

含內文格式：
```
feat(api): add rate limiting to public endpoints

- Limits requests to 100/minute per IP
- Returns 429 status with retry-after header
- Configurable via RATE_LIMIT_MAX env variable

Closes #234
```
