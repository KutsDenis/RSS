import feedparser
from typing import List, Dict

def fetch_rss(feed_urls: List[str]) -> List[Dict[str, str]]:
    """
    Загружает RSS-каналы и возвращает их содержимое.
    :param feed_urls: cписок URL-адресов RSS-каналов
    :return: cписок статей
    """
    articles = []

    for url in feed_urls:
        feed = feedparser.parse(url)

        if not feed_urls:
            print(f"[WARN] No feed in {url}")
            continue

        for entry in feed.entries:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "description": entry.get("description", ""),
                "published": entry.get("published", ""),
                "source": feed.feed.get("title", "Unknown Source"),
            })

    return articles
