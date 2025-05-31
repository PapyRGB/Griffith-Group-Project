# streamlit_app.py
import os, sys
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.retriever import retrieve
from src.hf_model import query_huggingface_chat

# Set page configuration
st.set_page_config(page_title="Griffith College Assistant", page_icon="📚")
st.title("📚 Griffith College Document Assistant")

# Hide pages menu
@st.cache_resource()
def hide_pages_menu():
    # Final CSS: hide sidebar, nav, toggle control, and spacer
    hide_sidebar_completely = """
        <style>
            /* Hide sidebar entirely */
            [data-testid="stSidebar"] {
                display: none !important;
            }

            /* Hide sidebar toggle/collapse control */
            [data-testid="stSidebarCollapsedControl"] {
                display: none !important;
            }

            /* Optional: reset main padding if needed */
            [data-testid="stAppViewContainer"] > div:first-child {
                padding-left: 0rem !important;
            }
        </style>
    """

    st.markdown(hide_sidebar_completely, unsafe_allow_html=True)

hide_pages_menu()

# Backend loader
@st.cache_resource(show_spinner="Loading backend...")
def load_resources():
    _ = retrieve("test")
    return "Backend ready"

backend_status = load_resources()
st.success(backend_status)

# Confirm clear cache → route to clear_cache.py
if "history" not in st.session_state:
    st.session_state.history = []

with st.expander("⚙️ Maintenance Actions"):
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🧹 Clear Cache"):
            st.session_state.confirm_clear_cache = True

    with col2:
        if st.button("♻️ Reset Backend Resources"):
            st.session_state.confirm_reset_resources = True

# Confirm dialogs
if st.session_state.get("confirm_clear_cache"):
    st.warning("This will fully clear the cache and restart the app.")
    if st.button("✅ Yes, clear cache now"):
        st.switch_page("pages/_clear_cache.py")  # Go to the clear_cache route
    if st.button("❌ Cancel", key="cancel_clear"):
        del st.session_state["confirm_clear_cache"]
        st.rerun()

if st.session_state.get("confirm_reset_resources"):
    st.warning("This will clear backend resources and reload them.")
    if st.button("✅ Yes, reset backend"):
        st.switch_page("pages/_clear_resource.py")  # Go to the clear_resource route
    if st.button("❌ Cancel", key="cancel_reset"):
        del st.session_state["confirm_reset_resources"]
        st.rerun()

# Chat history
for role, content in st.session_state.history:
    with st.chat_message(role):
        st.markdown(content)

if user_query := st.chat_input("Ask a question about Griffith College documentation..."):
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.spinner("Thinking..."):
        top_chunks = retrieve(user_query)
        context = "\n".join(top_chunks)
        prompt = f"Use this context to answer:\n{context}\n\nQuestion: {user_query}"
        answer = query_huggingface_chat(prompt)

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.history.append(("user", user_query))
    st.session_state.history.append(("assistant", answer))
