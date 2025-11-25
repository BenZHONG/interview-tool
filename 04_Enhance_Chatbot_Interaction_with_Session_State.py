# Importing necessary libraries
from openai import OpenAI
import streamlit as st


def initialize_openai_client():
    # Setting up the Streamlit page configuration
    st.set_page_config(page_title="Streamlit Chat", page_icon="💬")
    st.title("Chatbot")

    # Initializing the OpenAI client using the API key from Streamlit's secrets
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # Setting up the OpenAI model in session state if it is not already defined
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4o"

    return client


def implement_chat_functionality(client):
    if not st.session_state.setup_complete:
        return

    # Display a welcome message and prompt the user to introduce themselves
    st.info(
        """
        Start by introducing yourself.
        """,
        icon="👋",
    )

    # Initializing the 'messages' list and add a system message
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "system",
                "content": (f"You are an HR executive that interviews an interviewee called {st.session_state['name']} "
                        f"with experience {st.session_state['experience']} and skills {st.session_state['skills']}. "
                        f"You should interview him for the position {st.session_state['level']} {st.session_state['position']} "
                        f"at the company {st.session_state['company']}")
            }
        ]

    # Looping through the 'messages' list to display each message except system messages
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Input field for the user to send a new message
    if prompt := st.chat_input("Your answer."):
        # Appending the user's input to the 'messages' list in session state
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display the user's message in a chat bubble
        with st.chat_message("user"):
            st.markdown(prompt)

        # Assistant's response
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,  # This line enables streaming for real-time response
            )
            # Display the assistant's response as it streams
            response = st.write_stream(stream)
        # Append the assistant's full response to the 'messages' list
        st.session_state.messages.append({"role": "assistant", "content": response})


# Personal Information Section
def build_setup_page():
    if st.session_state.setup_complete:
        return

    st.subheader("Personal information", divider="rainbow")

    if "name" not in st.session_state:
        st.session_state["name"] = ""
    if "experience" not in st.session_state:
        st.session_state["experience"] = ""
    if "skills" not in st.session_state:
        st.session_state["skills"] = ""

    # Input fields for collecting user's personal information
    st.session_state["name"] = st.text_input(
        label="Name", max_chars=None, placeholder="Enter your name"
    )

    st.session_state["experience"] = st.text_area(
        label="Experience",
        value="",
        height=None,
        max_chars=None,
        placeholder="Describe your experience",
    )

    st.session_state["skills"] = st.text_area(
        label="Skills",
        value="",
        height=None,
        max_chars=None,
        placeholder="List your skills",
    )

    # Test labels for personal information
    st.write(f"**Your Name**: {st.session_state["name"]}")
    st.write(f"**Your Experience**: {st.session_state["experience"]}")
    st.write(f"**Your Skills**: {st.session_state["skills"]}")

    # Company and Position Section
    st.subheader("Company and Position", divider="rainbow")

    if "level" not in st.session_state:
        st.session_state["level"] = "Junior"
    if "position" not in st.session_state:
        st.session_state["position"] = "Data Scientist"
    if "company" not in st.session_state:
        st.session_state["company"] = "Amazon"

    # Field for selecting the job level, position and company
    col1, col2 = st.columns(2)
    with col1:
        st.session_state["level"] = st.radio(
            "Choose level",
            key="visibility",
            options=["Junior", "Mid-level", "Senior"],
        )
    with col2:
        st.session_state["position"] = st.selectbox(
            "Choose a position",
            (
                "Data Scientist",
                "Data Engineer",
                "ML Engineer",
                "BI Analyst",
                "Financial Analyst",
            ),
        )

    st.session_state["company"] = st.selectbox(
        "Choose a Company",
        ("Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify"),
    )
    # Test labels for company and position information
    st.write(
        f"**Your information**: {st.session_state["level"]} {st.session_state["position"]} at {st.session_state["company"]}"
    )

    # A button to complete the setup stage and start the interview
    if st.button("Start Interview", on_click=complete_setup):
        st.write("Setup complete. Starting interveiew...")


# Helper function to update session state
def complete_setup():
    st.session_state.setup_complete = True


# Initialize session state variable to track setup complection
if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False


client = initialize_openai_client()
implement_chat_functionality(client)
build_setup_page()
