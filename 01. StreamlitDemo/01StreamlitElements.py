"""
pip install streamlit
"""

import streamlit as st

st.title("Hello, Jayden!")
st.title("Hello, _Jayden_!")
st.title("Hello, :blue[JayJay]")
st.title("Hello, :speech_balloon:")

st.title('$E = mc^2$')

st.header('This is a header')
st.subheader('This is a subheader')

st.text('This is plain text with no formmating')
st.markdown('# This is a header\n **This is bold text** \n - This is a list item')

st.write('This is plain text using st.write')

data = {
    "name": "Jayden", 
    "Age": 8, 
    "Occupation": "Engineer", 
}
st.write(data)
