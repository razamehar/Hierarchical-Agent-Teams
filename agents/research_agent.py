from langgraph.prebuilt import create_react_agent
from tools.research_tool import search_tool
from utils.model_loader import LLM


research_agent = create_react_agent(
    model=LLM,
    tools=[search_tool],
    name="research_expert",
    prompt="You are a world class researcher with access to web search. Do not do any math."
)