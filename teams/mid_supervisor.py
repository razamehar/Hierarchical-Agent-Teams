from langgraph_supervisor import create_supervisor
from utils.model_loader import MODEL
from agents.research_agent import research_agent
from agents.math_agent import math_agent


research_team = create_supervisor(
    [research_agent, math_agent],
    model=MODEL,
    prompt="""
    You are the research supervisor managing two specialized agents: research_agent and math_agent.
    DO NOT answer user queries yourself.

    Your tasks:
    1. Route general (non-math) queries to research_agent.
    2. When the research_agent returns data that requires numeric calculations (like totals or sums), parse the relevant numbers from the response.
    3. Formulate math queries to the math_agent to compute the required sums step-by-step.
    4. Collect math_agent’s results and combine them if necessary.
    5. Pass the final processed answer to the top_level_supervisor.

    Always use the math_agent for any numeric calculations, do not calculate yourself.
    """,
    supervisor_name="research_supervisor"
).compile(name="research_team")