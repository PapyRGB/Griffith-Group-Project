# clear_cache.py
import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="Clearing Resources...", page_icon="🧹")

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

st.title("🧹 Clearing Resources")
st.write("Please wait while we reset the resources and restart the assistant...")

with st.spinner("Clearing..."):
    st.cache_resource.clear()
    st.session_state.clear()
    time.sleep(2)  # Just to show a delay for UX

# Redirect back to main app
st.success("Resources cleared. Redirecting...")
time.sleep(1)
st.switch_page("app.py")
