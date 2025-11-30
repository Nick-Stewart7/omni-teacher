# Omni-Teacher

An AI-powered personalized learning assistant built with Google ADK that helps you learn anything with tailored advice and approach.

## Overview

Omni-Teacher is a multi-agent AI system that provides personalized learning experiences. It calibrates to your learning goals, current level, and preferences, then helps you through research, lesson planning, and interactive teaching.

### Architecture

The system consists of:
- **Coordinator Agent**: Orchestrates the learning experience and manages user calibration
- **Researcher Agent**: Gathers information and resources using Google Search
- **Lesson Planner Agent**: Creates structured, personalized lesson plans
- **Teacher Agent**: Delivers interactive lessons and explanations

## Features

- Initial calibration questionnaire to understand learner profile
- Web-based research for current, accurate information
- Structured lesson plans tailored to individual needs
- Interactive teaching with examples and practice
- Ephemeral sessions with in-memory storage

## Tech Stack

- **Google ADK**: Agent Development Kit for building AI agents
- **FastAPI**: REST API backend
- **Streamlit**: Interactive web UI
- **Python 3.13+**: Programming language

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- Google Cloud account with Gemini API access
- API key for Google AI Studio

### Installation

1. Clone or navigate to the project directory:
```bash
cd omni-teacher
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Set up environment variables:
```bash
# Copy the example env file
cp .env.example .env

# Edit agent/.env and add your Google API key
# GOOGLE_API_KEY=your_api_key_here
```

## Running the Application

### Start the FastAPI Backend

In one terminal window:

```bash
python api.py
```

The API will start on `http://localhost:8000`

You can check the API health at: `http://localhost:8000/health`

### Start the Streamlit UI

In another terminal window:

```bash
streamlit run app.py
```

The UI will open in your browser at `http://localhost:8501`

## Usage

1. Open the Streamlit interface in your browser
2. The Omni-Teacher will greet you and ask about your learning goals
3. Answer the calibration questions to personalize your experience
4. Start learning! You can:
   - Ask the researcher to explore topics
   - Request a lesson plan for structured learning
   - Engage with the teacher for interactive lessons

## Project Structure

```
omni-teacher/
├── agent/                      # Agent definitions
│   ├── agent.py               # Coordinator agent
│   ├── prompt.py              # Coordinator prompt
│   └── subagents/             # Specialized subagents
│       ├── researcher/        # Research agent
│       ├── lesson_planner/    # Lesson planning agent
│       └── teacher/           # Teaching agent
├── api.py                     # FastAPI application
├── app.py                     # Streamlit UI
├── .env                       # Environment variables
├── requirements.txt           # Python dependencies
├── architecture.md            # Architecture documentation
├── resources.md              # Useful resources
└── README.md                 # This file
```

## API Endpoints

### POST /chat
Send a message to the Omni-Teacher agent.

**Request:**
```json
{
  "message": "I want to learn Python programming",
  "session_id": "optional-session-id"
}
```

**Response:**
```json
{
  "response": "Great! Let me help you learn Python...",
  "session_id": "session-id"
}
```

### GET /health
Check API health status.

## Development

This is a barebones local version with ephemeral sessions. Future enhancements could include:
- Persistent storage for user profiles and progress
- Multi-session support with session management
- Enhanced memory and context retention
- Additional specialized subagents
- Progress tracking and analytics

## Troubleshooting

**API not starting:**
- Ensure your Google API key is set in `.env`
- Check that port 8000 is not in use

**Streamlit can't connect:**
- Ensure the FastAPI server is running first
- Check that both servers are using the correct ports

**Agent errors:**
- Verify your Google API key has access to Gemini models
- Check your internet connection for Google Search functionality

## Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Google ADK Python Repository](https://github.com/google/adk-python)
- [ADK Samples](https://github.com/google/adk-samples)
- [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)

## License

This is a capstone project for educational purposes.

