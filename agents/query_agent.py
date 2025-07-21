import os

from crewai import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from utils.groq_llm import groq_llm

load_dotenv()

groq_llm = ChatOpenAI(
    temperature=0,
    model_name="llama-3.3-70b-versatile",
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

query_agent = Agent(
    role="Research Agent",
    goal="Summarize scientific articles for the user",
    backstory="This agent uses Groq LLaMA to provide relevant research summaries.",
    llm=groq_llm
)

from tools.science_tool import ScienceMagazineTool

query_agent = Agent(
    role="Research Agent",
    goal="Summarize scientific articles from structured data.",
    backstory="This agent uses Groq LLaMA to filter and summarize Science Magazine content.",
    tools=[ScienceMagazineTool()],
    llm=groq_llm
)