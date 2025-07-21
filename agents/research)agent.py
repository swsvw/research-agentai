import os

from crewai import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from tools.science_tool import ScienceMagazineTool

load_dotenv()

llm = ChatOpenAI(
    temperature=0,
    model_name="llama-3.3-70b-versatile",  # or another Groq-supported model
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

research_agent = Agent(
    role="Research Analyst",
    goal="Summarize research articles from approved sources.",
    backstory="AI agent trained to read and analyze biomedical research articles using LLMs.",
    tools=[ScienceMagazineTool()],
    llm=llm,
    verbose=True
)
