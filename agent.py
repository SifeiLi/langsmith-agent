from langchain_aws import ChatBedrock
from langgraph.prebuilt import create_react_agent

model = ChatBedrock(model_id="us.anthropic.claude-sonnet-4-20250514-v1:0")

workflow = create_react_agent(model=model, tools=[])
