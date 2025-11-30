"""Lesson planner subagent for creating structured learning plans."""

from google.adk.agents import LlmAgent

from . import prompt

MODEL = "gemini-2.5-flash"

lesson_planner_agent = LlmAgent(
    name="lesson_planner",
    model=MODEL,
    description="Create structured, personalized lesson plans tailored to user's goals and level",
    instruction=prompt.LESSON_PLANNER_PROMPT
)
