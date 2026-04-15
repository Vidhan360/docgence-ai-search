import { useState } from "react";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [expanded, setExpanded] = useState({}); // 🔥 track read more

  // 🔥 FETCH BOOK COVER
  const getBookCover = async (title) => {
    try {
      const res = await fetch(
        `https://www.googleapis.com/books/v1/volumes?q=intitle:${title}`
      );
      const data = await res.json();

      return (
        data.items?.[0]?.volumeInfo?.imageLinks?.thumbnail ||
        "https://via.placeholder.com/200x300?text=No+Cover"
      );
    } catch {
      return "https://via.placeholder.com/200x300?text=No+Cover";
    }
  };

  const handleSearch = async () => {
    if (!query) return;

    setLoading(true);
    setResults([]);

    try {
      const res = await fetch(
        `http://127.0.0.1:8000/api/books/search/?q=${query}`
      );
      const data = await res.json();

      const updated = await Promise.all(
        (data.results || []).map(async (book) => {
          const cover = await getBookCover(book.title);
          return { ...book, cover };
        })
      );

      setResults(updated);
    } catch (err) {
      alert("Error fetching results");
      console.error(err);
    }

    setLoading(false);
  };

  // 🔥 TOGGLE READ MORE
  const toggleReadMore = (index) => {
    setExpanded((prev) => ({
      ...prev,
      [index]: !prev[index],
    }));
  };

  return (
    <div className="app">
      <h1 className="title">DOCGENCE</h1>

      <div className="search-box">
        <input
          type="text"
          placeholder="Search books..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
      </div>

      {/* LOADING */}
      {loading && (
        <div className="grid">
          {[...Array(6)].map((_, i) => (
            <div className="card skeleton" key={i}></div>
          ))}
        </div>
      )}

      {/* RESULTS */}
      <div className="grid">
        {results.map((book, index) => {
          const isExpanded = expanded[index];

          return (
            <div className="card glass" key={index}>
              <img src={book.cover} alt="book" />

              <div className="card-content">
                <h3>#{index + 1} {book.title}</h3>

                {/* 🔥 DESCRIPTION WITH TOGGLE */}
                <p>
                  {isExpanded
                    ? book.description
                    : book.description.slice(0, 120) + "..."}
                </p>

                <button
                  onClick={() => toggleReadMore(index)}
                  style={{
                    border: "none",
                    background: "none",
                    color: "#8e2de2",
                    cursor: "pointer",
                    fontWeight: "bold",
                    marginTop: "5px"
                  }}
                >
                  {isExpanded ? "Show Less" : "Read More"}
                </button>

                <div className="score">⭐ {book.score.toFixed(3)}</div>

                <div className="reason">{book.reason}</div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default App;