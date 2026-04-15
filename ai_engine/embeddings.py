import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "backend"))

# ✅ DJANGO SETUP
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django
django.setup()


from books.models import Book

# ✅ EMBEDDING MODEL
from sentence_transformers import SentenceTransformer
import numpy as np

# Load model (lightweight + fast)
model = SentenceTransformer('all-MiniLM-L6-v2')


def create_embeddings():
    books = Book.objects.all()

    if not books:
        print("❌ No books found in DB")
        return

    embeddings = []

    print(f"📚 Found {books.count()} books\n")

    for book in books:
        text = f"{book.title} {book.description}"

        vector = model.encode(text)

        embeddings.append({
            "id": book.id,
            "title": book.title,
            "embedding": vector.tolist()
        })

        print(f"✅ Embedded: {book.title}")

    print("\n🎉 All embeddings created!")
    print(f"Total embeddings: {len(embeddings)}")

    return embeddings


if __name__ == "__main__":
    create_embeddings()