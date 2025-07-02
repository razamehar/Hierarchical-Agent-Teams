from langchain_tavily import TavilySearch
from langchain_core.tools import tool


#@tool
def finance_research_tool(topic: str) -> str:
    """
    Search for the finance topic on web using TavilySearch
    """

    tavilly_tool = TavilySearch(max_results=5, topic="finance")
    response = tavilly_tool.invoke({"query": topic})
    return response

#@tool
def general_research_tool(topic: str) -> str:
    """
    Search for the general topic on web using TavilySearch
    """

    tavilly_tool = TavilySearch(max_results=5, topic="general")
    response = tavilly_tool.invoke({"query": topic})
    return response