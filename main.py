from dotenv import load_dotenv

load_dotenv()

import os

from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "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"
os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"

llm = ChatOpenAI(
    temperature=0,
    model_name="llama3-70b-8192",
    openai_api_base=os.environ["OPENAI_API_BASE"]
)

from tasks.search_task import run_task

if __name__ == "__main__":
    print("🧠 Welcome to the Science Summary Agent!")
    query = input("🔎 Enter your research query: ")
    run_task(query)
