# 🧭 Vertexa Systems Onboarding Navigator

An AI-powered onboarding chatbot built with Retrieval-Augmented Generation (RAG). It answers new-employee questions using Vertexa Systems' internal onboarding documents — IT setup, leave policy, reimbursements, communication flow, and more.

## 🚀 Live Demo
👉 **[Try the chatbot here](PASTE_YOUR_STREAMLIT_LINK_HERE)**

## 🛠️ Tech Stack
- **Embeddings:** sentence-transformers (all-MiniLM-L6-v2)
- **Vector Store:** FAISS
- **LLM:** Groq API (Llama 3.3 70B)
- **Interface:** Streamlit
- **Language:** Python

## 📂 Project Structure
- `app.py` — Streamlit chat interface
- `chatbot.py` — RAG pipeline (retrieval + LLM response)
- `search.py` — vector search logic
- `build_index.py` — builds the FAISS index from knowledge_base documents
- `knowledge_base/` — company onboarding documents (8 topics)

## ▶️ Run Locally
```bash
pip install -r requirements.txt
python build_index.py
streamlit run app.py
```

## 👥 Team
- Awantika Kholia — 065060
- Parv — 065040
- Mayank Jha — 065036
- Akshit Kansal — 065008
- Aditi Agarwal — 065006

Built for the AI Integration Group Project — AI for Managers.
