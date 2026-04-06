from strands import Agent
from langgraph.func import entrypoint, task
import operator

agent = Agent(
    tools=[],
    system_prompt="You are a helpful assistant.",
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",
)

@task
def invoke_agent(messages):
    result = agent(messages)
    return [result.message]

@entrypoint()
def workflow(messages, previous):
    messages = operator.add(previous or [], messages)
    response = invoke_agent(messages).result()
    return entrypoint.final(value=response, save=operator.add(messages, response))
