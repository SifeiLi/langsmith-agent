from langgraph.graph import StateGraph, MessagesState

def echo(state: MessagesState):
    last = state["messages"][-1].content if state["messages"] else ""
    return {"messages": [{"role": "assistant", "content": f"Echo: {last}"}]}

workflow = StateGraph(MessagesState)
workflow.add_node("echo", echo)
workflow.set_entry_point("echo")
workflow.set_finish_point("echo")
workflow = workflow.compile()
