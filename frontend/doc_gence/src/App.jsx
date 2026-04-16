import { useState } from "react";
import "./App.css";

const covers = [
  "https://images.unsplash.com/photo-1512820790803-83ca734da794",
  "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f",
  "https://images.unsplash.com/photo-1495446815901-a7297e633e8d",
  "https://images.unsplash.com/photo-1519681393784-d120267933ba",
  "https://images.unsplash.com/photo-1507842217343-583bb7270b66",
  "https://images.unsplash.com/photo-1476275466078-4007374efbbe",
  "https://images.unsplash.com/photo-1455885666463-9757b5a7a56a",
  "https://images.unsplash.com/photo-1516979187457-637abb4f9353",
  "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
  "https://images.unsplash.com/photo-1528207776546-365bb710ee93",
];

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [expanded, setExpanded] = useState({}); 

  const getRandomCover = (index) => {
    return covers[index % covers.length] + "?w=200&h=300&fit=crop";
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

      const updated = (data.results || []).map((book, index) => ({
        ...book,
        cover: getRandomCover(index),
      }));

      setResults(updated);
    } catch (err) {
      alert("Error fetching results");
      console.error(err);
    }

    setLoading(false);
  };

  // 🔥 TOGGLE FUNCTION
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

      {loading && (
        <div className="grid">
          {[...Array(6)].map((_, i) => (
            <div className="card skeleton" key={i}></div>
          ))}
        </div>
      )}

      <div className="grid">
        {results.map((book, index) => {
          const isExpanded = expanded[index];

          return (
            <div className="card glass" key={index}>
              <img src={book.cover} alt="book" />

              <div className="card-content">
                <h3>
                  #{index + 1} {book.title}
                </h3>

                {/* 🔥 DESCRIPTION */}
                <p>
                  {isExpanded
                    ? book.description
                    : book.description?.slice(0, 120) + "..."}
                </p>

                {/* 🔥 READ MORE BUTTON */}
                {book.description && book.description.length > 120 && (
                  <button
                    onClick={() => toggleReadMore(index)}
                    style={{
                      border: "none",
                      background: "none",
                      color: "#8e2de2",
                      cursor: "pointer",
                      fontWeight: "bold",
                      marginTop: "5px",
                    }}
                  >
                    {isExpanded ? "Show Less" : "Read More"}
                  </button>
                )}

                <div className="score">
                  ⭐ {book.score?.toFixed(3)}
                </div>

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
