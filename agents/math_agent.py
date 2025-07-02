from langgraph.prebuilt import create_react_agent
from tools.math_tools import add_tool, subtract_tool, multiply_tool, divide_tool
from utils.model_loader import MODEL


math_agent = create_react_agent(
    model=MODEL,
    tools=[add_tool, subtract_tool, multiply_tool, divide_tool],
    name="math_expert",
    prompt="You are a math expert. Always use one tool at a time."
)