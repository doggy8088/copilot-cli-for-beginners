---
name: commit-message
description: 生成慣例式提交訊息 - 適用於建立提交、撰寫提交訊息或尋求 git commit 協助
---

# Commit Message 技能

依照 Conventional Commits 規範生成提交訊息。

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
| `fix` | 錯誤修復 |
| `docs` | 僅文件變更 |
| `style` | 格式調整（無程式碼變更） |
| `refactor` | 既未修復問題也未新增功能的程式碼變更 |
| `perf` | 效能改善 |
| `test` | 新增或更新測試 |
| `chore` | 維護任務 |

## 規則

1. 標題行最多 72 個字元
2. 使用祈使語氣（「add」而非「added」或「adds」）
3. 標題行結尾不加句點
4. 標題與內文之間以空白行分隔
5. 內文說明**做了什麼**與**為何這樣做**，而非如何做

## 範例

Simple:
```
fix(auth): prevent redirect loop on expired sessions
```

With body:
```
feat(api): add rate limiting to public endpoints

- Limits requests to 100/minute per IP
- Returns 429 status with retry-after header
- Configurable via RATE_LIMIT_MAX env variable

Closes #234
```
