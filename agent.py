from langgraph.func import entrypoint

@entrypoint()
def workflow(inputs):
    messages = inputs.get("messages", [])
    last_message = messages[-1]["content"] if messages else ""
    return {
        "messages": [
            *messages,
            {"role": "assistant", "content": f"Echo: {last_message}"}
        ]
    }
