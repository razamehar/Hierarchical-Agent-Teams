from langgraph.prebuilt import create_react_agent
from tools.summarize_tool import get_summary
from utils.model_loader import MODEL


summary_agent = create_react_agent(
    model=MODEL,
    tools=[get_summary],
    name="summary_agent",
    prompt="You are a summary generator expert."
)