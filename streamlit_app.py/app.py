# streamlit_app.py
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.retriever import retrieve
from src.hf_model import query_huggingface

st.title("📚 Griffith College Document Assistant")

# Cache backend resources (e.g., index loading, embedding model)
@st.cache_data(show_spinner="Loading backend...")
def load_resources():
    _ = retrieve("test")  # warm-up call to build FAISS/retriever once
    return "Backend ready"

# Load resources once (cached)
st.success(load_resources())

# Initialize Q&A history
if "history" not in st.session_state:
    st.session_state.history = []

# User query input
query = st.text_input("Enter your question:")

if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        top_chunks = retrieve(query)
        context = "\n".join(top_chunks)
        prompt = f"Use this context to answer:\n{context}\n\nQuestion: {query}"
        answer = query_huggingface(prompt)

        # Store Q&A in session history
        st.session_state.history.append((query, answer))

        st.markdown("### Answer")
        st.write(answer)

# Show previous Q&A
if st.session_state.history:
    st.markdown("---")
    st.markdown("### 🧠 Conversation History")
    for i, (q, a) in enumerate(reversed(st.session_state.history), 1):
        st.markdown(f"**Q{i}:** {q}")
        st.markdown(f"**A{i}:** {a}")
