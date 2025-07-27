import json
import os

import streamlit as st

from tasks.search_task import run_task

st.title("🔬 Research Agent")

api_key = st.text_input("Enter your Groq API key:", type="password")
query = st.text_input("Enter your research query:")

if "show_results" not in st.session_state:
    st.session_state.show_results = False

if st.button("Run Research") and api_key and query:
    run_task(query, api_key)
    st.session_state.show_results = True
if st.session_state.show_results:
    if os.path.exists("science_articles.json"):
        with open("science_articles.json", "r") as f:
            data = json.load(f)
        st.markdown("---")
        st.subheader("📄 Article Summaries")
        for article in data:
            st.markdown(f"### [{article['title']}]({article['url']})")
            st.markdown(f"**Summary:** {article['summary']}")
            st.markdown("---")
if not st.session_state.get("just_loaded"):
    st.session_state.show_results = False
    st.session_state.just_loaded = True
