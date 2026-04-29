# NewsCrawler

一個用 Python 撰寫的 CNN Business 新聞爬蟲專案。

## 專案整理後結構

```text
NewsCrawler/
├─ docs/
│  └─ ARCHITECTURE.md
├─ src/
│  └─ news_crawler/
│     ├─ __init__.py
│     ├─ cli.py
│     └─ crawler.py
├─ News/
│  └─ crawler.py                  # 舊路徑相容入口
├─ News Dynamic webpages/
│  ├─ crawler.py                  # 舊路徑相容入口
│  └─ chromedriver.exe            # 舊檔案保留
├─ requirements.txt
└─ README.md
```

## 功能

- 抓取 `https://edition.cnn.com/business` 文章列表
- 解析文章標題、連結、日期
- 進一步抓每篇文章正文
- 以 `output/<YYYYMMDD>/YYYYMMDD title.txt` 輸出

## 安裝

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 使用方式

```bash
PYTHONPATH=src python -m news_crawler.cli --output-dir output
```

若你仍使用舊入口：

```bash
python News/crawler.py
python "News Dynamic webpages/crawler.py"
```

兩者都會轉呼叫新的 `news_crawler.cli`。

## 注意事項

- CNN 頁面結構可能變動，若 selector 失效需調整 `src/news_crawler/crawler.py`。
- 請遵守目標網站使用條款與 robots 規範。
