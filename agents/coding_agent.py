from langgraph.prebuilt import create_react_agent
from tools.coding_tool import python_repl_tool
from utils.model_loader import LLM


coding_agent = create_react_agent(
    model=LLM,
    tools=[python_repl_tool],
    name="coding_expert",
    prompt="You are a world class Python coding expert."
)