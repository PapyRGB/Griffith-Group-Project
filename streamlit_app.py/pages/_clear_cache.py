# clear_cache.py
import streamlit as st
import time

st.set_page_config(page_title="Clearing Cache...", page_icon="🧹")

st.title("🧹 Clearing Cache")
st.write("Please wait while we reset the cache and restart the assistant...")

with st.spinner("Clearing..."):
    st.cache_data.clear()
    st.session_state.clear()
    time.sleep(2)  # Just to show a delay for UX

# Redirect back to main app
st.success("Cache cleared. Redirecting...")
time.sleep(1)
st.switch_page("app.py")
