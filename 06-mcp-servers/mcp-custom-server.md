# 建立自訂 MCP 伺服器

> ⚠️ **本內容完全為選修。** 你只需使用預先建置的 MCP 伺服器（GitHub、filesystem、Context7），就能高效使用 Copilot CLI。本指南適合想要將 Copilot 連接到自訂內部 API 的開發者。更多細節請參考 [MCP for Beginners 課程](https://github.com/microsoft/mcp-for-beginners)。
>
> **先備知識：**
> - 熟悉 Python
> - 理解 `async`/`await` 模式
> - 系統已安裝 `pip`（本開發容器已內建）
>
> **[← 回到第 06 章：MCP 伺服器](README.md)**

---

想要將 Copilot 連接到你自己的 API 嗎？以下將示範如何用 Python 建立一個簡單的 MCP 伺服器，查詢書籍資訊，並與本課程一直使用的書籍應用程式專案相結合。

## 專案設定

```bash
mkdir book-lookup-mcp-server
cd book-lookup-mcp-server
pip install mcp
```

> 💡 **什麼是 `mcp` 套件？** 它是官方的 Python SDK，用於建立 MCP 伺服器。它會處理協定細節，讓你專注於開發自己的工具。

## 伺服器實作

建立一個名為 `server.py` 的檔案：

```python
# server.py
import json
from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("book-lookup")

# Sample book database (in a real server, this could query an API or database)
BOOKS_DB = {
    "978-0-547-92822-7": {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "genre": "Fantasy",
    },
    "978-0-451-52493-5": {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genre": "Dystopian Fiction",
    },
    "978-0-441-17271-9": {
        "title": "Dune",
        "author": "Frank Herbert",
        "year": 1965,
        "genre": "Science Fiction",
    },
}


@mcp.tool()
def lookup_book(isbn: str) -> str:
    """Look up a book by its ISBN and return title, author, year, and genre."""
    book = BOOKS_DB.get(isbn)
    if book:
        return json.dumps(book, indent=2)
    return f"No book found with ISBN: {isbn}"


@mcp.tool()
def search_books(query: str) -> str:
    """Search for books by title or author. Returns all matching results."""
    query_lower = query.lower()
    results = [
        {**book, "isbn": isbn}
        for isbn, book in BOOKS_DB.items()
        if query_lower in book["title"].lower()
        or query_lower in book["author"].lower()
    ]
    if results:
        return json.dumps(results, indent=2)
    return f"No books found matching: {query}"


@mcp.tool()
def list_all_books() -> str:
    """List all books in the database with their ISBNs."""
    books_list = [
        {"isbn": isbn, "title": book["title"], "author": book["author"]}
        for isbn, book in BOOKS_DB.items()
    ]
    return json.dumps(books_list, indent=2)


if __name__ == "__main__":
    mcp.run()
```

**這裡發生了什麼事：**

| 部分 | 功能說明 |
|------|-------------|
| `FastMCP("book-lookup")` | 建立一個名為 "book-lookup" 的伺服器 |
| `@mcp.tool()` | 註冊一個 Copilot 可呼叫的工具函式 |
| 型別提示 + 文件字串 | 告訴 Copilot 每個工具的用途及所需參數 |
| `mcp.run()` | 啟動伺服器並監聽請求 |

> 💡 **為什麼要用裝飾器？** 只需 `@mcp.tool()` 這個裝飾器即可。MCP SDK 會自動讀取你的函式名稱、型別提示和文件字串來產生工具結構描述。無需手動撰寫 JSON schema！

## 設定

在你的 `~/.copilot/mcp-config.json` 中加入：

```json
{
  "mcpServers": {
    "book-lookup": {
      "type": "local",
      "command": "python3",
      "args": ["./book-lookup-mcp-server/server.py"],
      "tools": ["*"]
    }
  }
}
```

## 使用方式

```bash
copilot

> 查詢 ISBN 為 978-0-547-92822-7 的書籍

{
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "year": 1937,
  "genre": "Fantasy"
}

> 搜尋作者為 Orwell 的書籍

[
  {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "genre": "Dystopian Fiction",
    "isbn": "978-0-451-52493-5"
  }
]

> 列出所有可用書籍

[顯示資料庫中所有書籍及其 ISBN]
```

## 下一步

當你完成基本伺服器後，可以：

1. **新增更多工具** - 每個 `@mcp.tool()` 函式都會成為 Copilot 可呼叫的工具
2. **串接真實 API** - 將模擬的 `BOOKS_DB` 換成實際的 API 呼叫或資料庫查詢
3. **加入驗證機制** - 安全地處理 API 金鑰與權杖
4. **分享你的伺服器** - 發布到 PyPI，讓其他人可以用 `pip` 安裝

## 相關資源

- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [MCP 伺服器範例](https://github.com/modelcontextprotocol/servers)
- [MCP for Beginners 課程](https://github.com/microsoft/mcp-for-beginners)

---

**[← 回到第 06 章：MCP 伺服器](README.md)**
