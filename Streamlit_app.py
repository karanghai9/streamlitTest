import streamlit as st

# Input for user's name
name = st.text_input('Enter your name')

# Display title with the entered name live while typing
st.title(f'Hello, I am {name}')

st.text("This is my first Streamlit deployment")



