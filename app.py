import os

import streamlit as st
from dotenv import load_dotenv

from agent import run_agent


load_dotenv()

PAGE_TITLE = os.getenv("DASHBOARD_TITLE", "Streamlit Agent Dashboard")
PAGE_DESCRIPTION = (
    "A simple local dashboard for submitting queries and viewing mock agent responses."
)
RESPONSE_STYLES = ["Standard", "Detailed", "Brief"]


st.set_page_config(page_title=PAGE_TITLE, layout="wide")


if "agent_response" not in st.session_state:
    st.session_state.agent_response = ""

if "status_message" not in st.session_state:
    st.session_state.status_message = "Ready for input. Submit a query to generate a response."

if "status_type" not in st.session_state:
    st.session_state.status_type = "info"


st.title(PAGE_TITLE)
st.caption(PAGE_DESCRIPTION)

with st.sidebar:
    st.header("Configuration")
    response_style = st.selectbox("Response style", RESPONSE_STYLES, index=0)
    st.info("Configuration options are local-only for now.")
    st.caption(f"Selected mode: {response_style}")

left_col, right_col = st.columns([3, 2], gap="large")

with left_col:
    st.subheader("Submit Query")
    st.write("Enter a query below and send it to the local agent.")

    with st.form("agent_query_form"):
        user_query = st.text_input(
            "User query",
            placeholder="e.g. Summarize the dashboard status",
        )
        submit_clicked = st.form_submit_button("Submit")

with right_col:
    st.subheader("Status")
    if st.session_state.status_type == "success":
        st.success(st.session_state.status_message)
    elif st.session_state.status_type == "error":
        st.error(st.session_state.status_message)
    elif st.session_state.status_type == "warning":
        st.warning(st.session_state.status_message)
    else:
        st.info(st.session_state.status_message)

st.markdown("### Agent Output")
output_container = st.container()

if submit_clicked:
    cleaned_query = user_query.strip()

    if not cleaned_query:
        st.session_state.agent_response = ""
        st.session_state.status_message = "Please enter a query before submitting."
        st.session_state.status_type = "warning"
        st.warning(st.session_state.status_message)
    else:
        try:
            with st.spinner("Processing your request..."):
                agent_output = run_agent(cleaned_query, response_style)

            st.session_state.agent_response = agent_output
            st.session_state.status_message = "Response received successfully."
            st.session_state.status_type = "success"
        except Exception as exc:
            st.session_state.agent_response = ""
            st.session_state.status_message = (
                f"The agent could not process your request: {exc}"
            )
            st.session_state.status_type = "error"

with output_container:
    if st.session_state.agent_response:
        st.success("Latest response")
        st.write(st.session_state.agent_response)
    elif st.session_state.status_type == "warning":
        st.info("Your response will appear here after a successful submission.")
    elif st.session_state.status_type == "error":
        st.error("No response is available because the last request failed.")
    else:
        st.info("Your response will appear here after you submit a query.")

st.markdown("---")
st.caption(
    "This dashboard uses a local mock agent only. No API keys or external LLM services are used."
)
