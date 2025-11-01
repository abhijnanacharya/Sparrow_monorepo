import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
  timeout: 15000,
});

export async function analyzeUrl(url, method = "tfidf", top_k = 50) {
  const { data } = await api.post("/analyze", { url, method, top_k });
  return data;
}
