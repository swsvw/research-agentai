# tasks/search_task.py
import json

import streamlit as st

from tools.science_tool import (fetch_science_articles,
                                summarize_article_content)
from utils.groq_llm import get_groq_client


def run_task(user_query: str, api_key):
    articles = fetch_science_articles(user_query)
    enriched = []

    for article in articles:
        content = article.get("content", "")
        if content:
            client = get_groq_client(api_key)  # ✅ get proper Groq object
            summary = summarize_article_content(content, client)

            article["summary"] = summary
        enriched.append(article)

    with open("science_articles.json", "w") as f:
        json.dump(enriched, f, indent=2)
with open("science_articles.json", "r") as f:
    data = json.load(f)

st.subheader("📄 Article Summaries")
for article in data:
    st.markdown(f"### [{article['title']}]({article['url']})")
    st.markdown(f"**Summary:** {article['summary']}")
    st.markdown("---")