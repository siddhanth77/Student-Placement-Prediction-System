
import os

import requests
import streamlit as st


API_URL = os.getenv(
    "PLACEMENT_API_URL",
    "http://127.0.0.1:8000"
).rstrip("/")


def render_chatbot_page():
    st.title("💬 AI Placement Assistant")
    st.write(
        "Your AI assistant for placement preparation, "
        "Python interviews, resumes, technical skills, and career guidance."
    )

    # Keep conversation history during Streamlit reruns.
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    if st.button("🗑️ Clear conversation"):
        st.session_state.chat_messages = []
        st.rerun()

    # Display conversation history.
    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask your placement-related question...")

    if prompt:
        st.session_state.chat_messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Send the most recent 12 messages to FastAPI.
                    messages = st.session_state.chat_messages[-12:]

                    response = requests.post(
                        f"{API_URL}/chat",
                        json={"messages": messages},
                        timeout=60
                    )
                    response.raise_for_status()

                    answer = response.json().get("reply", "").strip()

                    if not answer:
                        answer = "The assistant returned an empty response."

                except requests.exceptions.ConnectionError:
                    answer = (
                        "Cannot connect to the AI backend. "
                        "Please start FastAPI on http://127.0.0.1:8000."
                    )

                except requests.exceptions.Timeout:
                    answer = "The request timed out. Please try again."

                except requests.exceptions.RequestException:
                    answer = (
                        "The chatbot request failed. "
                        "Check the FastAPI terminal for errors."
                    )

                st.markdown(answer)

        st.session_state.chat_messages.append({
            "role": "assistant",
            "content": answer
        })
