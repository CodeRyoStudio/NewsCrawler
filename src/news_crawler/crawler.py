from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable
import urllib.request as req

from bs4 import BeautifulSoup

BASE_URL = "https://edition.cnn.com"
BUSINESS_URL = f"{BASE_URL}/business"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    )
}


@dataclass(frozen=True)
class NewsItem:
    date: str
    title: str
    link: str


def _fetch_html(url: str) -> str:
    request = req.Request(url, headers=HEADERS)
    with req.urlopen(request) as response:
        return response.read().decode("utf-8")


def _sanitize_filename(name: str) -> str:
    cleaned = re.sub(r'[\\/:*?"<>|]+', "", name).strip()
    return cleaned or "untitled"


def _parse_date_from_path(path: str) -> str:
    digits = "".join(ch for ch in path if ch.isdigit())
    return digits[:8] if len(digits) >= 8 else "unknown-date"


def _extract_news_items(html: str) -> Iterable[NewsItem]:
    soup = BeautifulSoup(html, "html.parser")
    for content in soup.select("div.cd__content"):
        anchor = content.find("a")
        if anchor is None or not anchor.get("href"):
            continue

        relative_link = anchor.get("href")
        title = _sanitize_filename(content.get_text(strip=True))
        date = _parse_date_from_path(relative_link)
        link = f"{BASE_URL}{relative_link}"
        yield NewsItem(date=date, title=title, link=link)


def _extract_article_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("section", id="body-text")
    if article is None:
        return "None"
    return article.get_text("\n", strip=True)


def crawl_business_news(output_dir: str = "output") -> int:
    out_root = Path(output_dir)
    out_root.mkdir(parents=True, exist_ok=True)

    homepage = _fetch_html(BUSINESS_URL)
    count = 0

    for item in _extract_news_items(homepage):
        article_html = _fetch_html(item.link)
        article_text = _extract_article_text(article_html)

        target_dir = out_root / item.date
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / f"{item.date} {item.title}.txt"

        target_file.write_text(
            f"{item.title}\n{item.link}\n\n{article_text}\n",
            encoding="utf-8",
        )
        count += 1

    return count
