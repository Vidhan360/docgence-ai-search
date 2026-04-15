import os
import sys
import numpy as np
import faiss

# Django setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "backend"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django
django.setup()

from books.models import Book
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')


# 🔹 BUILD INDEX
def build_index():
    books = Book.objects.all()

    embeddings = []
    metadata = []

    for book in books:
        text = f"{book.title} {book.description}"
        vector = model.encode(text)

        embeddings.append(vector)

        metadata.append({
            "title": book.title,
            "description": book.description
        })

    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index, metadata


# 🔹 SEARCH + BETTER XAI
def retrieve(query, index, metadata, k=3):
    query_vector = model.encode([query]).astype("float32")

    distances, indices = index.search(query_vector, k)

    results = []

    for i, idx in enumerate(indices[0]):
        book = metadata[idx]
        score = float(distances[0][i])

        # 🔥 IMPROVED XAI
        if score < 0.8:
            explanation = "Highly relevant: Strong semantic similarity with your query."
        elif score < 1.4:
            explanation = "Good match: Context closely aligns with your search intent."
        elif score < 2.2:
            explanation = "Moderate match: Some overlap in meaning but not exact."
        else:
            explanation = "Weak match: Only loosely related content."

        results.append({
            "title": book["title"],
            "description": book["description"],
            "score": round(score, 3),
            "reason": explanation
        })

    return results


# 🔹 PIPELINE
def rag_pipeline(query):
    index, metadata = build_index()
    results = retrieve(query, index, metadata)
    return results


# 🔹 TEST
if __name__ == "__main__":
    query = input("Enter query: ")
    results = rag_pipeline(query)

    print("\n📖 Results:\n")
    for r in results:
        print(f"👉 {r['title']}")
        print(f"⭐ Score: {r['score']}")
        print(f"💡 {r['reason']}\n")