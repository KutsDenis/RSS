from src.rss_fetcher import fetch_rss

RSS_FEEDS = [
    "https://www.exploit-db.com/rss.xml",
    "https://googleprojectzero.blogspot.com/feeds/posts/default",
    "https://portswigger.net/blog/rss",
    "https://krebsonsecurity.com/feed",
    "https://www.darkreading.com/rss.xml",
    "https://threatpost.com/feed",
    "https://www.securityweek.com/feed",
]

if __name__ == "__main__":
    articles = fetch_rss(RSS_FEEDS)
    print(f"Загружено {len(articles)} статей.")