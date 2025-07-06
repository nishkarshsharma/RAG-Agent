from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="rag_agent",
    description="A Retrieval-Augmented Generation (RAG) agent.",
    model= "gemini-2.0-flash",
    tools=[google_search],
    instruction="""
    You are a Retrieval-Augmented Generation (RAG) agent."""
)

