# tasks/search_task.py

import json

from tools.science_tool import (fetch_science_articles,
                                summarize_article_content)


def run_task(user_query: str):
    print(f"🔍 Running research task for: {user_query}")

    # Step 1: Fetch articles from Science Magazine API
    articles = fetch_science_articles(user_query)
    if not articles:
        print("❌ No relevant articles found.")
        return

    summaries = []
    
    # Step 2: Summarize each article
    for article in articles:
        content = article.get("content")
        if not content:
            continue
        summary = summarize_article_content(content)
        summaries.append({
            "title": article.get("title"),
            "url": article.get("url"),
            "summary": summary
        })

    # Step 3: Save output
    with open("science_articles.json", "w") as f:
        json.dump(summaries, f, indent=2)

    print("✅ Research task completed. Summaries saved to science_articles.json")
    print("\n🔬 Top Research Summaries:\n")
    for i, article in enumerate(summaries, 1):
        print(f"{i}. 📝 Title: {article['title']}")
        print(f"🔗 URL: {article['url']}")
        print(f"📄 Summary:\n{article['summary']}\n")
        print("-" * 80)

    
