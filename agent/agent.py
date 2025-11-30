"""Omni-Teacher: Learn Anything, Teach Anything - Coordinator Agent."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .subagents.researcher.agent import researcher_agent
from .subagents.lesson_planner.agent import lesson_planner_agent
from .subagents.teacher.agent import teacher_agent

MODEL = "gemini-2.5-pro"

omni_coordinator = LlmAgent(
    name="omni_coordinator",
    model=MODEL,
    description="Coordinate learning experiences and help users master any topic",
    instruction=prompt.COORDINATOR_PROMPT,
    tools=[
        AgentTool(researcher_agent),
        AgentTool(lesson_planner_agent),
        AgentTool(teacher_agent)
    ]
)

root_agent = omni_coordinator