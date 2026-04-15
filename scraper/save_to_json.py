import json
from scraper import scrape_books

def save_books():
    books = scrape_books()

    with open("data/books.json", "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

    print("✅ Data saved to data/books.json")


if __name__ == "__main__":
    save_books()