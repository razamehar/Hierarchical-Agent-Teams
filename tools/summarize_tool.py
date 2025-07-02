from langchain_core.tools import tool
from utils.model_loader import MODEL


@tool
def get_summary(response: str) -> str:
    """Generate and return a concise summary of the given response."""
    summary = MODEL.invoke(f"Generate summary of {response} in 300 words.")
    return summary