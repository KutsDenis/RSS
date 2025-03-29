from src.rss_fetcher import fetch_rss
import storage
#from src.translator import translate_text

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

    for item in articles:
        title = item["title"]
        link = item["link"]
        description = item["description"]

        if storage.add_article(title, link):
            print(f"🔹 Новая статья: {title}")

            #translated_title = translate_text(title, "ru")
            #translated_description = translate_text(description, "ru")

            #print(f"✅ Переведено: {translated_title}")

        else:
            print(f"🔸 Уже было: {title}")

    # Удаляем старые записи
    storage.clean_old_articles(storage.load_data())
