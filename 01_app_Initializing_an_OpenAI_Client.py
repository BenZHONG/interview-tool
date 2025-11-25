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


initialize_openai_client()
