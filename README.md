# 📚 DOCGENCE – AI Book Search with Explainable AI

DOCGENCE is an AI-powered semantic book search system that uses vector embeddings and explainable AI to return meaningful search results.

---

## 🚀 Features

- 🔍 Semantic Search (not keyword-based)
- 🧠 Explainable AI insights (why results matched)
- ⚡ Fast retrieval using FAISS
- 🎨 Modern React UI with glassmorphism
- 📖 Real book covers via Google Books API
- 📊 Ranking system based on similarity score

---

## 🏗️ Tech Stack

### Backend
- Django REST Framework
- Sentence Transformers (`all-MiniLM-L6-v2`)
- FAISS (Vector Search)

### Frontend
- React (Vite)
- CSS (Glassmorphism UI)

---

## 🧠 How It Works

1. Books are converted into vector embeddings
2. User query is also converted into embedding
3. FAISS finds nearest vectors (similar books)
4. Results are ranked by similarity score
5. Explainable AI provides reasoning for matches (USP)

---

## 📸 Screenshots

- Semantic Search Results
- Ranking + Score
- Explainable AI Insights
- Real Book Covers

---

## ⚙️ Setup Instructions

### Backend

```bash
cd backend
pip install -r requirements.txt
python manage.py runserver
