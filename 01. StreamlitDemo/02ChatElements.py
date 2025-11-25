import streamlit as st

prompt = st.chat_input("Type your message", max_chars=50)
if prompt:
    st.write(f"User message: {prompt}")