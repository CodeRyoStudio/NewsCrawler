# Architecture

## Modules

- `news_crawler.crawler`
  - 負責網頁請求、HTML 解析、檔案輸出。
  - 主要函式：`crawl_business_news(output_dir: str) -> int`
- `news_crawler.cli`
  - 命令列介面，解析參數並呼叫 crawler。

## Data flow

1. 抓取 CNN Business 首頁 HTML。
2. 解析每則新聞卡片 `div.cd__content`。
3. 取得文章連結後抓內文頁。
4. 解析 `section#body-text`。
5. 產生日期資料夾，並寫入 `.txt` 檔案。

## Design decisions

- 使用 `pathlib` 取代字串拼路徑。
- 將 URL 抓取、欄位清洗、文章解析拆成小函式。
- 保留舊入口檔 (`News/`, `News Dynamic webpages/`) 以免既有使用者腳本壞掉。
