from langgraph.prebuilt import create_react_agent
from tools.research_tools import finance_research_tool, general_research_tool
from utils.model_loader import MODEL


research_agent = create_react_agent(
    model=MODEL,
    tools=[finance_research_tool, general_research_tool],
    name="research_agent",
    prompt="""You are a world class researcher with access to finance_research_tool and general_research_tool.
    For general research, use general_research_tool.
    For finance, use finance_research_tool.
    Do not do any math."""
)