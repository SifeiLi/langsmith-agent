import logging
from langgraph.graph import StateGraph, MessagesState

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("agent")

def echo(state: MessagesState):
    last = state["messages"][-1].content if state["messages"] else ""
    logger.info(f"Received message: {last}")
    logger.info(f"Returning: Echo: {last}")
    return {"messages": [{"role": "assistant", "content": f"Echo: {last}"}]}

workflow = StateGraph(MessagesState)
workflow.add_node("echo", echo)
workflow.set_entry_point("echo")
workflow.set_finish_point("echo")
workflow = workflow.compile()
