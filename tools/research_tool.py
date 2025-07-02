import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch


load_dotenv()
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")

search_tool=TavilySearch(tavily_api_key=TAVILY_API_KEY)