# Streamlit Agent Dashboard

## System Overview

This project is a simple local Streamlit dashboard for testing an agent-style workflow without using any external API or LLM. The problem it solves is providing a clean starting point for a dashboard interface that accepts a user query, sends it to a local agent module, and displays the result in a structured UI.

### Workflow

1. The user opens the dashboard with Streamlit.
2. The user enters a query in the main panel.
3. The app validates the input and shows feedback if it is empty.
4. The query is passed to the local `agent.py` module.
5. The mock agent returns a formatted response.
6. The dashboard displays the result with status messages.

### Key Components

- `app.py` — Streamlit UI, layout, form handling, feedback messages, and environment loading.
- `agent.py` — local mock agent function that processes a string input and returns a mock response.
- `.env` — local configuration values such as dashboard title and response prefix.
- `requirements.txt` — project dependencies.

## How to Run

1. Open a terminal in `streamlit_agent_dashboard`.
2. Activate the virtual environment.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Update `.env` if needed.
5. Start the app:
   `streamlit run app.py`

## Dashboard Screenshot

Add a real screenshot of the running Streamlit dashboard and save it as `screenshot.png` in this project folder. Replace the placeholder below with your final screenshot if needed.

![Dashboard Screenshot Placeholder](screenshot.png)

## Features Implemented

- Streamlit dashboard layout with sidebar and main content area
- User query input with submit button
- Local mock agent integration
- Loading indicator with `st.spinner()`
- Success, warning, info, and error feedback messages
- Empty-input validation
- Environment variable loading with `python-dotenv`
- No hardcoded API keys or external API calls

## Key Design Decisions

- **Local-first agent design:** the agent is mocked locally to keep setup simple and avoid API dependencies.
- **Form-based submission:** using a form reduces unnecessary reruns and keeps the UI cleaner.
- **Environment-based configuration:** configurable values are stored in `.env` to avoid hardcoding and support future extension.
- **Simple modular structure:** separating `app.py` and `agent.py` makes the project easier to test and extend later.
