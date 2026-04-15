import requests
import json

API_URL = "http://127.0.0.1:8000/api/books/add/"


def send_books():
    with open("data/books.json", "r", encoding="utf-8") as f:
        books = json.load(f)

    for book in books:
        try:
            response = requests.post(API_URL, json=book)

            print(f"\nSending: {book['title']}")
            print("Status:", response.status_code)
            print("Response:", response.text)

            if response.status_code == 200:
                print(f"✅ Inserted: {book['title']}")
            else:
                print(f"❌ Failed: {book['title']}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    send_books()