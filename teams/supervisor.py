from langgraph_supervisor import create_supervisor
from teams.mid_supervisor import research_team
from agents.doc_saving_agent import doc_saving_agent
from agents.summary_agent import summary_agent
from utils.model_loader import MODEL
from config.config import CHECKPOINTER, STORE



top_level_supervisor = create_supervisor(
    [research_team, summary_agent, doc_saving_agent],
    model=MODEL,
    prompt="""
     You are the top-level supervisor overseeing a research_team, a summary_agent, and a doc_saving_agent.
    Delegate initial research and data collection tasks to research_team.
    Use summary_agent to generate and present the final summarized response.
    Use doc_saving_agent to save the final summarized response in pdf or doc format.
    """,
    supervisor_name="top_level_supervisor"
).compile(name="top_level_supervisor", checkpointer=CHECKPOINTER, store=STORE)