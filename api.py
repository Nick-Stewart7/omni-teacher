"""FastAPI application for Omni-Teacher agent."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.memory.in_memory_memory_service import InMemoryMemoryService
from agent.agent import root_agent
from google.genai.types import Content, Part
from dotenv import load_dotenv

#Global Variables
APP_NAME = "omni_teacher"
USER_ID = "user"
SESSION_ID = "session1_id"

# Load environment variables
load_dotenv(".env")

# Initialize FastAPI app
app = FastAPI(
    title="Omni-Teacher API",
    description="AI-powered personalized learning assistant",
    version="1.0.0"
)

# Initialize in-memory services
session_service = InMemorySessionService()
memory_service = InMemoryMemoryService()

# Initialize agent runner
agent_runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service,
    memory_service=memory_service
)

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"


class ChatResponse(BaseModel):
    response: str
    session_id: str


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "Omni-Teacher API",
        "version": "1.0.0"
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint for interacting with the Omni-Teacher agent.

    Args:
        request: ChatRequest containing the user message and session_id

    Returns:
        ChatResponse with the agent's response
    """
    try:
        #Create Session
        await agent_runner.session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)

        # Run the agent
        response_text = "(No final response)"
        user_message = Content(parts=[Part(text=request.message)], role="user")
        async for event in agent_runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=user_message):
            if event.is_final_response() and event.content and event.content.parts:
                response_text = event.content.parts[0].text

        return ChatResponse(
            response=response_text,
            session_id=request.session_id
        )

    except Exception as e:
        print(f"Error processing chat request: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")


@app.get("/health")
async def health():
    """Detailed health check endpoint."""
    return {
        "status": "healthy",
        "agent": root_agent.name,
        "services": {
            "session": "in-memory",
            "memory": "in-memory"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
