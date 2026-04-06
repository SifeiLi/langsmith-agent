from langchain_core.language_models import FakeListChatModel
from langgraph.prebuilt import create_react_agent

model = FakeListChatModel(responses=["Hello! I'm a test agent running on LangSmith."])

workflow = create_react_agent(model=model, tools=[])
