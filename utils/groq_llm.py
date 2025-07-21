# utils/groq_llm.py

import os

from groq import Groq
from langchain_core.messages import HumanMessage

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def groq_llm(prompt: str):
    chat_completion = client.chat.completions.create(
        model="llama3-70b-8192",  # ✅ Supported model
        messages=[
            {
                "role": "system",
                "content": "You are a scientific summarizer. Summarize technical research articles concisely."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=512,
    )
    return chat_completion.choices[0].message


