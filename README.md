# 🚀 DOCGENCE — AI Book Search Engine

DOCGENCE is an AI-powered semantic book search engine that uses embeddings, FAISS, and Explainable AI (XAI) to retrieve and rank relevant books based on meaning, not just keywords.

---

## 🔥 Features

* 🔍 Semantic Search (not keyword-based)
* ⚡ Fast similarity search using FAISS
* 🧠 Explainable AI (XAI) insights for each result
* 🎨 Modern UI with React (glassmorphism + animations)
* 📊 Ranking system with similarity scores
* 📖 Expandable descriptions (Read More / Less)

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **AI Engine:** Sentence Transformers, FAISS
* **Frontend:** React (Vite)
* **Database:** SQLite

---

## 📂 Project Structure

```
docgence-ai-search/
│
├── backend/        # Django backend
├── frontend/       # React frontend
├── ai_engine/      # RAG + FAISS logic
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Vidhan360/docgence-ai-search.git
cd docgence-ai-search
```

---

## 🔧 Backend Setup (Django)

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate     # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r ../requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
```

---

## 🎨 Frontend Setup (React)

```bash
cd frontend

# Install dependencies
npm install

# Run frontend
npm run dev
```

---

## 🌐 Open Application

```text
http://localhost:5173
```

---

## 🔌 API Endpoint

```
GET /api/books/search/?q=your_query
```

Example:

```
http://127.0.0.1:8000/api/books/search/?q=science
```

---

## 🧪 Sample Queries

- science books
- emotional novels
- history of humans

The system returns semantically relevant books with similarity scores and explanations.

## 🧠 How It Works

1. User enters a query
2. Query is converted into embeddings
3. FAISS searches for closest matches
4. Top results are returned
5. XAI explains relevance of each result

---

## Screenshots are added in the Repo

---

## 🚀 Future Improvements

* 📚 Real book cover API integration
* 🤖 LLM-based explanations
* 🌐 Deployment (Vercel + Render)
* 📈 Advanced ranking & filtering

---

## 👨‍💻 Author

**Vidhan Mishra**

---

## ⭐ Note

This project demonstrates practical implementation of:

* Retrieval-Augmented Search (RAG)
* Vector Databases (FAISS)
* Explainable AI (XAI)
* Full-stack integration (Django + React)

---
