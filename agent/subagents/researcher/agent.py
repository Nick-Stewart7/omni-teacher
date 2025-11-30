"""Researcher subagent for gathering information and resources."""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-flash"

researcher_agent = LlmAgent(
    name="researcher",
    model=MODEL,
    description="Research topics and find learning resources using web search",
    instruction=prompt.RESEARCHER_PROMPT,
    tools=[google_search]
)
