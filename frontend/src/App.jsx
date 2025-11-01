import React, { useState } from "react";
import WordCloud3D from "./components/WordCloud3D/WordCloud3D.jsx";
import { analyzeUrl } from "./api.js";

const samples = [
  "https://www.bbc.com/news",
  "https://www.reuters.com/world/",
  "https://www.theverge.com/",
];

export default function App() {
  const [url, setUrl] = useState(samples[0]);
  const [method, setMethod] = useState("tfidf");
  const [topK, setTopK] = useState(50);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [topics, setTopics] = useState([]);
  const [tokens, setTokens] = useState(0);

  async function handleAnalyze(e) {
    e.preventDefault();
    setLoading(true);
    setError("");
    try {
      const res = await analyzeUrl(url, method, topK);
      setTopics(res.topics || []);
      setTokens(res.tokens || 0);
    } catch (err) {
      setError(
        err?.response?.data?.detail || err.message || "Failed to analyze."
      );
      setTopics([]);
      setTokens(0);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div
      style={{
        fontFamily: "Inter, system-ui, Avenir, Helvetica, Arial, sans-serif",
        color: "#e8ecff",
        background: "linear-gradient(180deg,#0b1020,#0b0f1a)",
        height: "100vh",
        overflow: "hidden",
      }}
    >
      <header style={{ padding: "24px 16px", maxWidth: 980, margin: "0 auto" }}>
        <h1 style={{ margin: 0, fontSize: 32 }}>Word Cloud Visualizer</h1>
        <p style={{ opacity: 0.8, marginTop: 8 }}>
          Enter an article URL, analyze the text, and explore a 3D word cloud.
        </p>

        <form
          onSubmit={handleAnalyze}
          style={{
            display: "grid",
            gridTemplateColumns: "1fr auto",
            gap: 8,
            marginTop: 16,
          }}
        >
          <input
            type="url"
            placeholder="https://example.com/article"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            required
            style={{
              padding: "12px 14px",
              borderRadius: 10,
              border: "1px solid #2a3358",
              background: "#0f1630",
              color: "#e8ecff",
            }}
          />
          <button
            type="submit"
            disabled={loading}
            style={{
              padding: "12px 16px",
              borderRadius: 10,
              border: loading ? "1px solid white" : "1px solid #2a3358",
              background: "#20306b",
              color: "#fff",
              cursor: "pointer",
              boxShadow: loading
                ? "0 0 10px rgba(255,255,255,0.9), 0 0 20px rgba(255,255,255,0.6)"
                : "0 0 0 rgba(0,0,0,0)",
              transition: "box-shadow 0.3s ease, border 0.3s ease",
            }}
          >
            {loading ? "Analyzing…" : "Analyze"}
          </button>
        </form>

        <div
          style={{
            display: "flex",
            gap: 8,
            alignItems: "center",
            marginTop: 10,
            flexWrap: "wrap",
          }}
        >
          <label style={{ fontSize: 13, opacity: 0.9 }}>
            Method:&nbsp;
            <select
              value={method}
              onChange={(e) => setMethod(e.target.value)}
              style={{
                background: "#10183a",
                color: "#c7d2ff",
                border: "1px solid #2a3358",
                borderRadius: 6,
                padding: "4px 8px",
              }}
            >
              <option value="tfidf">TF-IDF</option>
              <option value="freq">Frequency</option>
            </select>
          </label>
          <label style={{ fontSize: 13, opacity: 0.9 }}>
            Top K:&nbsp;
            <input
              type="number"
              min={1}
              max={120}
              value={topK}
              onChange={(e) => setTopK(Number(e.target.value))}
              style={{
                width: 70,
                background: "#10183a",
                color: "#c7d2ff",
                border: "1px solid #2a3358",
                borderRadius: 6,
                padding: "4px 8px",
              }}
            />
          </label>
          <div style={{ display: "flex", gap: 6 }}>
            {samples.map((s) => (
              <button
                key={s}
                onClick={() => setUrl(s)}
                type="button"
                style={{
                  padding: "6px 10px",
                  borderRadius: 8,
                  border: "1px solid #2a3358",
                  background: "#10183a",
                  color: "#c7d2ff",
                  cursor: "pointer",
                  fontSize: 12,
                }}
              >
                Sample
              </button>
            ))}
          </div>
        </div>

        {error && (
          <div style={{ marginTop: 10, color: "#ff96a6" }}>
            <strong>Error:</strong> {error}
          </div>
        )}
        {!loading && tokens > 0 && (
          <div style={{ marginTop: 6, opacity: 0.8, fontSize: 13 }}>
            Processed ~{tokens.toLocaleString()} tokens
          </div>
        )}
      </header>

      <main style={{ paddingBottom: 90 }}>
        <section
          style={{
            position: "relative",
            width: "100%",
            height: "calc(100dvh - 280px)",
          }}
        >
          <WordCloud3D topics={topics} limit={topK} />
        </section>

        <p
          style={{
            opacity: 0.7,
            fontSize: 12,
            marginTop: 12,
            textAlign: "center",
          }}
        >
          Tip: drag to orbit, zoom with wheel. Larger/brighter words = more
          relevant.
        </p>
      </main>
    </div>
  );
}
