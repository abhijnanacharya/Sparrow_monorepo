# 🌐 Word Cloud Visualizer

A modern web application that **analyzes articles from URLs** and visualizes the most relevant topics using an **interactive 3D word cloud**.

---

## Features

- **URL Analysis** – Extract and analyze content from any article link
- **3D Visualization** – Immersive word cloud powered by React Three Fiber
- **Multiple Methods** – Choose between _TF-IDF_ and _Frequency-based_ extraction
- **Customizable Display** – Adjust top-K topic count

---

## 🛠 Tech Stack

**Frontend**

- React 19 + Vite
- Three.js
- Axios for API requests

**Backend**

- FastAPI + Uvicorn
- BeautifulSoup + Scikit-learn (TF-IDF)

---

## ⚙️ Quick Setup

### Prerequisites

- Python 3.8+
- Node.js 16+

### One-Command Setup

```bash
chmod +x setup.sh
./setup.sh
```

This installs dependencies for both backend and frontend automatically.

---

## 🚀 Run Locally

### Start Backend

```bash
cd backend
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uvicorn main:app --reload
```

Backend → **http://localhost:8000**

### Start Frontend

```bash
cd frontend
npm run dev
```

Frontend → **http://localhost:5173**

---

## 📖 Usage Guide

1. Open the app in your browser
2. Paste a news/article URL
3. Select analysis method (`tfidf` or `frequency`)
4. Adjust number of words (Top-K)
5. Click **Analyze**
6. Interact with the 3D visualization
   - **Drag:** Orbit view
   - **Scroll:** Zoom
   - **Larger words:** Higher importance

---

## 🧩 API Reference

### `POST /analyze`

Analyze content from a given URL.

**Request**

```json
{
  "url": "https://example.com/article",
  "method": "tfidf",
  "top_k": 50
}
```

**Response**

```json
{
  "topics": [
    { "word": "technology", "weight": 0.95 },
    { "word": "innovation", "weight": 0.87 }
  ],
  "tokens": 5234,
  "method": "tfidf"
}
```

Swagger Docs available at → `http://localhost:8000/docs`

---

## 🧱 Project Structure

```
wordcloud-visualizer/
├── backend/
│   ├── main.py
│   ├── utils/ (analyzer, fetcher, cleaner)
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/WordCloud3D/
│   │   ├── App.jsx
│   │   └── api.js
│   └── package.json
├── setup.sh
└── README.md
```

---

Built with ❤️ by [**Abhijnan Acharya**](https://www.linkedin.com/in/abhijnanacharya)
