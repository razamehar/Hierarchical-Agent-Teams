from langgraph.prebuilt import create_react_agent
from tools.doc_saver import save_doc_tool
from utils.model_loader import MODEL


doc_saving_agent = create_react_agent(
    model=MODEL,
    tools=[save_doc_tool],
    name="doc_saving_agent",
    prompt="You are a doc saving expert."
)