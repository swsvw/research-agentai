from urllib.parse import quote

import feedparser

from utils.groq_llm import groq_llm


def fetch_science_articles(query: str):
    print(f"🔎 Searching arXiv for: {query}")
    encoded_query = quote(query)
    search_url = f"http://export.arxiv.org/api/query?search_query=all:{encoded_query}&start=0&max_results=5"

    feed = feedparser.parse(search_url)
    results = []

    for entry in feed.entries:
        article = {
            "title": entry.title,
            "url": entry.link,
            "content": entry.summary
        }
        results.append(article)

    return results


def summarize_article_content(content: str) -> str:
    prompt = f"""
    You are a scientific summarizer.
    Given this raw content from a research article, extract the core scientific insight in 3–5 lines.

    Article content:
    {content}

    Summary:
    """
    response = groq_llm(prompt)
    return response.content.strip()
