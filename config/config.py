from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore


CHECKPOINTER = InMemorySaver()
STORE = InMemoryStore()