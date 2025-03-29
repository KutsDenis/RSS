import json
import hashlib
import os
from datetime import datetime, timedelta

JSON_FILE = "data.json"
EXPIRATION_DAYS = 3  # Сколько храним записи


def load_data():
    """Загружаем JSON-хранилище или создаем пустое"""
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"articles": []}


def save_data(data):
    """Сохраняем JSON-хранилище"""
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def generate_id(title, link):
    """Генерируем уникальный ID на основе заголовка и ссылки"""
    return hashlib.md5(f"{title}{link}".encode()).hexdigest()


def clean_old_articles(data):
    """Удаляем устаревшие записи"""
    now = datetime.now()
    data["articles"] = [a for a in data["articles"] if datetime.fromisoformat(a["expires"]) > now]
    save_data(data)


def add_article(title, link):
    """Добавляем новую статью, если её ещё нет"""
    data = load_data()
    article_id = generate_id(title, link)

    if any(a["id"] == article_id for a in data["articles"]):
        return False  # Уже есть

    expires = (datetime.now() + timedelta(days=EXPIRATION_DAYS)).isoformat()
    data["articles"].append({"id": article_id, "title": title, "link": link, "expires": expires})

    save_data(data)
    return True  # Новая статья добавлена
