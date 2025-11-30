"""Streamlit UI for Omni-Teacher."""

import streamlit as st
import requests
from typing import List, Dict
import uuid

# API configuration
API_URL = "http://localhost:8000"

# Page configuration
st.set_page_config(
    page_title="Omni-Teacher",
    page_icon="\U0001F393",
    layout="wide"
)

# Initialize session state
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

if "api_healthy" not in st.session_state:
    try:
        response = requests.get(f"{API_URL}/health", timeout=2)
        st.session_state.api_healthy = response.status_code == 200
    except:
        st.session_state.api_healthy = False


def send_message(message: str) -> str:
    """Send a message to the API and return the response."""
    try:
        response = requests.post(
            f"{API_URL}/chat",
            json={
                "message": message,
                "session_id": st.session_state.session_id
            },
            timeout=60
        )
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        return f"Error communicating with API: {str(e)}"


# App header
st.title("\U0001F393 Omni-Teacher")
st.markdown("*Your AI-powered personalized learning assistant*")

# API status indicator
if st.session_state.api_healthy:
    st.success("Connected to Omni-Teacher API")
else:
    st.error("Cannot connect to API. Please ensure the FastAPI server is running on port 8000.")
    st.info("Start the API with: `python api.py`")

st.divider()

# Sidebar with information
with st.sidebar:
    st.header("About Omni-Teacher")
    st.markdown("""
    Omni-Teacher helps you learn anything with personalized guidance.

    **Features:**
    - \U0001F50D **Research**: Explore topics and find resources
    - \U0001F4DA **Lesson Planning**: Get structured learning paths
    - \U0001F469\u200D\U0001F3EB **Teaching**: Interactive lessons and explanations

    **How it works:**
    1. Share your learning goals
    2. Get a personalized plan
    3. Learn with AI guidance
    """)

    st.divider()

    st.subheader("Session Info")
    st.caption(f"Session ID: {st.session_state.session_id[:8]}...")

    if st.button("Start New Session"):
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.messages = []
        st.rerun()

# Chat interface
st.subheader("Chat")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to learn today?", disabled=not st.session_state.api_healthy):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = send_message(prompt)
            st.markdown(response)

    # Add assistant response to chat
    st.session_state.messages.append({"role": "assistant", "content": response})

# Welcome message if no messages yet
if len(st.session_state.messages) == 0 and st.session_state.api_healthy:
    with st.chat_message("assistant"):
        st.markdown("""
        Hello! I'm your Omni-Teacher, here to help you learn anything you want.

        To get started, tell me:
        - What topic would you like to learn?
        - What's your current experience level?
        - What are your learning goals?

        I'll help create a personalized learning experience just for you!
        """)
