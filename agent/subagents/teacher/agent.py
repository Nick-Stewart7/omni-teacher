"""Teacher subagent for delivering lessons and explanations."""

from google.adk.agents import LlmAgent

from . import prompt

MODEL = "gemini-2.5-flash"

teacher_agent = LlmAgent(
    name="teacher",
    model=MODEL,
    description="Deliver engaging lessons, explanations, and interactive teaching experiences",
    instruction=prompt.TEACHER_PROMPT
)
