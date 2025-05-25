import streamlit as st

# Cached function: Simulate loading FAISS index or model
@st.cache_data
def load_backend():
    # Simulate expensive backend load
    return "🔁 Backend ready"

# Function to process user query (replace with real logic)
def process_query(query):
    # Replace with actual call to HF inference or FAISS-based retrieval
    return f"📘 Processed answer for: {query}"

def main():
    st.title('Griffith RAG Assistant')

    # Load backend (cached)
    backend_status = load_backend()
    st.success(backend_status)

    # Initialize session state for Q&A history
    if "history" not in st.session_state:
        st.session_state.history = []

    # User query input
    user_query = st.text_input('Enter your query:')
    
    if st.button('Submit'):
        if user_query:
            response = process_query(user_query)
            st.session_state.history.append((user_query, response))  # Add to history

    # Display history
    if st.session_state.history:
        st.subheader("🧠 Conversation History")
        for i, (q, a) in enumerate(reversed(st.session_state.history), 1):
            st.markdown(f"**Q{i}:** {q}")
            st.markdown(f"**A{i}:** {a}")

if __name__ == '__main__':
    main()
