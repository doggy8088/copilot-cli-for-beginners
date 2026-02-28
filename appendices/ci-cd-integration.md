# CI/CD 整合

> 📖 **先備條件**：請先完成[第 07 章：融會貫通](../07-putting-it-together/README.md)後再閱讀本附錄。
>
> ⚠️ **本附錄適用於已有 CI/CD 流水線的團隊。** 若您剛接觸 GitHub Actions 或 CI/CD 概念，建議先從第 07 章[程式碼審查自動化](../07-putting-it-together/README.md#workflow-3-code-review-automation-optional)章節中較簡單的 pre-commit hook 方式入手。

本附錄示範如何將 GitHub Copilot CLI 整合至 CI/CD 流水線，以便在 pull request 上自動進行程式碼審查。

---

## GitHub Actions 工作流程

以下工作流程會在 pull request 開啟或更新時，自動審查已變更的檔案：

```yaml
# .github/workflows/copilot-review.yml
name: Copilot Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Needed to compare with main branch

      - name: Install Copilot CLI
        run: npm install -g @github/copilot

      - name: Review Changed Files
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Get list of changed JS/TS files
          FILES=$(git diff --name-only origin/main...HEAD | grep -E '\.(js|ts|jsx|tsx)$' || true)
          
          if [ -z "$FILES" ]; then
            echo "No JavaScript/TypeScript files changed"
            exit 0
          fi
          
          echo "# Copilot Code Review" > review.md
          echo "" >> review.md
          
          for file in $FILES; do
            echo "Reviewing $file..."
            echo "## $file" >> review.md
            echo "" >> review.md
            
            # Use --silent to suppress progress output
            copilot --allow-all -p "Quick security and quality review of @$file. List only critical issues." --silent >> review.md 2>/dev/null || echo "Review skipped" >> review.md
            echo "" >> review.md
          done

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = fs.readFileSync('review.md', 'utf8');
            
            // Only post if there's meaningful content
            if (review.includes('CRITICAL') || review.includes('HIGH')) {
              github.rest.issues.createComment({
                issue_number: context.issue.number,
                owner: context.repo.owner,
                repo: context.repo.repo,
                body: review
              });
            } else {
              console.log('No critical issues found, skipping comment');
            }
```

---

## 設定選項

### 縮限審查範圍

您可以將審查聚焦於特定類型的問題：

```yaml
# Security-only review
copilot --allow-all -p "Security review of @$file. Check for: SQL injection, XSS, hardcoded secrets, authentication issues." --silent

# Performance-only review
copilot --allow-all -p "Performance review of @$file. Check for: N+1 queries, memory leaks, blocking operations." --silent
```

### 處理大型 PR

對於包含大量檔案的 PR，可考慮分批處理或加以限制：

```yaml
# Limit to first 10 files
FILES=$(git diff --name-only origin/main...HEAD | grep -E '\.(js|ts)$' | head -10)

# Or set a timeout per file
timeout 60 copilot --allow-all -p "Review @$file" --silent || echo "Review timed out"
```

### 團隊設定

若要在整個團隊中維持一致的審查標準，可建立共用設定檔：

```json
// .copilot/config.json (committed to repo)
{
  "model": "claude-sonnet-4.5",
  "permissions": {
    "allowedPaths": ["src/**/*", "tests/**/*"],
    "deniedPaths": [".env*", "secrets/**/*", "*.min.js"]
  }
}
```

---

## 替代方案：PR 審查機器人

若需要更完善的審查工作流程，可考慮使用 Copilot 編程代理：

```yaml
# .github/workflows/copilot-agent-review.yml
name: Request Copilot Review

on:
  pull_request:
    types: [opened, ready_for_review]

jobs:
  request-review:
    runs-on: ubuntu-latest
    steps:
      - name: Request Copilot Review
        uses: actions/github-script@v7
        with:
          script: |
            await github.rest.pulls.requestReviewers({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.issue.number,
              reviewers: ['copilot[bot]']
            });
```

---

## CI/CD 整合最佳實踐

1. **使用 `--silent` 旗標** — 抑制進度輸出，讓日誌更整潔
2. **設定逾時時間** — 避免卡住的審查任務阻塞流水線
3. **篩選檔案類型** — 只審查相關檔案（跳過自動生成的程式碼與依賴套件）
4. **注意 API 頻率限制** — 對大型 PR 的審查請求適當分散
5. **優雅地處理失敗** — 不應因審查失敗而阻擋合併；記錄錯誤後繼續執行

---

## 疑難排解

### CI 環境中出現「Authentication failed（驗證失敗）」

請確認工作流程具備正確的權限設定：

```yaml
permissions:
  contents: read
  pull-requests: write
  issues: write
```

### 審查任務逾時

增加逾時時間或縮減審查範圍：

```bash
timeout 120 copilot --allow-all -p "Quick review of @$file - critical issues only" --silent
```

### 大型檔案超出 token 限制

跳過過大的檔案：

```bash
if [ $(wc -l < "$file") -lt 500 ]; then
  copilot --allow-all -p "Review @$file" --silent
else
  echo "Skipping $file (too large)"
fi
```

---

**[← 返回第 07 章](../07-putting-it-together/README.md)** | **[返回附錄](README.md)**
