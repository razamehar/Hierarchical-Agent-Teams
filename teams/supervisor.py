from langgraph_supervisor import create_supervisor
from agents.research_agent import research_agent
from agents.math_agent import math_agent
from agents.coding_agent import coding_agent
from utils.model_loader import LLM


WORKFLOW = create_supervisor(
    [research_agent, math_agent, coding_agent],
    model=LLM,
    output_mode="full_history", # can also include only the final agent response "last_message"
    prompt=(
        "You are a team supervisor managing a research expert, a math expert and a coding expert. "
        "For queries, use research_agent."
        "For math problems, use math_agent."
        "For coding problems or chart generation, use coding_agent."
    ),
)