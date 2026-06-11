# CI/CD 整合

> 📖 **前置作業**：請先完成[第 07 章：整合應用](../07-putting-it-together/README.md)再閱讀本附錄。
>
> ⚠️ **本附錄適用於已經有 CI/CD 流程的團隊。** 如果你是 GitHub Actions 或 CI/CD 新手，請先參考第 07 章的[程式碼審查自動化](../07-putting-it-together/README.md#workflow-3-code-review-automation-optional)章節，採用較簡單的 pre-commit hook 方式。

本附錄說明如何將 GitHub Copilot CLI 整合進你的 CI/CD 流程，實現自動化的 Pull Request 程式碼審查。

---

## GitHub Actions 工作流程

此工作流程會在 Pull Request 開啟或更新時，自動審查變更的檔案：

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
          fetch-depth: 0  # 需要與 main 分支比較

      - name: Install Copilot CLI
        run: npm install -g @github/copilot

      - name: Review Changed Files
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # 取得變更的 JS/TS 檔案清單
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
            
            # 使用 --silent 抑制進度輸出
            copilot --allow-all -p "Quick security and quality review of @$file. List only critical issues." --silent >> review.md 2>/dev/null || echo "Review skipped" >> review.md
            echo "" >> review.md
          done

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = fs.readFileSync('review.md', 'utf8');
            
            // 僅在有重要內容時發佈評論
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

### 限定審查範圍

你可以聚焦於特定類型的問題進行審查：

```yaml
# 僅進行安全性審查
copilot --allow-all -p "Security review of @$file. Check for: SQL injection, XSS, hardcoded secrets, authentication issues." --silent

# 僅進行效能審查
copilot --allow-all -p "Performance review of @$file. Check for: N+1 queries, memory leaks, blocking operations." --silent
```

### 處理大型 PR

對於包含許多檔案的 PR，可考慮分批或限制數量：

```yaml
# 只審查前 10 個檔案
FILES=$(git diff --name-only origin/main...HEAD | grep -E '\.(js|ts)$' | head -10)

# 或對每個檔案設定逾時
timeout 60 copilot --allow-all -p "Review @$file" --silent || echo "Review timed out"
```

### 團隊設定

若要讓團隊審查標準一致，可建立共用設定檔：

```json
// .copilot/config.json (提交到版本庫)
{
  "model": "claude-sonnet-4.5",
  "permissions": {
    "allowedPaths": ["src/**/*", "tests/**/*"],
    "deniedPaths": [".env*", "secrets/**/*", "*.min.js"]
  }
}
```

---

## 進階選項：PR 審查機器人

若需更進階的審查流程，可考慮使用 GitHub Copilot 雲端 Agent：

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

1. **使用 `--silent` 旗標** - 抑制進度輸出，讓日誌更乾淨
2. **設定逾時** - 避免審查卡住導致流程停擺
3. **篩選檔案類型** - 只審查相關檔案（跳過產生的程式碼、相依套件等）
4. **注意速率限制** - 大型 PR 請分批審查，避免觸發速率限制
5. **容錯處理** - 審查失敗時不要阻擋合併，記錄並繼續流程

---

## 疑難排解

### CI 中出現 "Authentication failed"

請確認 workflow 設定了正確的權限：

```yaml
permissions:
  contents: read
  pull-requests: write
  issues: write
```

### 審查逾時

請增加逾時時間或縮小審查範圍：

```bash
timeout 120 copilot --allow-all -p "Quick review of @$file - critical issues only" --silent
```

### 大型檔案超過 Token 限制

跳過過大的檔案：

```bash
if [ $(wc -l < "$file") -lt 500 ]; then
  copilot --allow-all -p "Review @$file" --silent
else
  echo "Skipping $file (too large)"
fi
```

---

**[← 回到第 07 章](../07-putting-it-together/README.md)** | **[返回附錄目錄](README.md)**
