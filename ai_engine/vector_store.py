import os
import sys
import numpy as np
import faiss


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "backend"))

# ✅ DJANGO SETUP
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django
django.setup()

from books.models import Book
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')


def build_index():
    books = Book.objects.all()

    if not books:
        print("❌ No books found")
        return None, None

    embeddings = []
    metadata = []

    print(f"📚 Building index for {books.count()} books...\n")

    for book in books:
        text = f"{book.title} {book.description}"

        vector = model.encode(text)
        embeddings.append(vector)

        metadata.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })

        print(f"✅ Indexed: {book.title}")

    embeddings = np.array(embeddings).astype("float32")

    # FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    print("\n🎉 Index built successfully!")

    return index, metadata


def search_books(query, index, metadata, k=5):
    print(f"\n🔍 Searching for: {query}")

    query_vector = model.encode([query]).astype("float32")

    distances, indices = index.search(query_vector, k)

    results = []

    for idx in indices[0]:
        results.append(metadata[idx])

    return results


if __name__ == "__main__":
    index, metadata = build_index()

    if index:
        query = input("\nEnter search query: ")
        results = search_books(query, index, metadata)

        print("\n📖 Top Results:\n")
        for r in results:
            print(f"👉 {r['title']}")