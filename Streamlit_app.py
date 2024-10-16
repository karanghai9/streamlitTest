import streamlit as st

# Input for user's name
name = st.text_input('Enter your name')

# Display title with the entered name
if name:  # This checks if a name has been entered
    st.title(f'Hello, I am {name}')
else:
    st.title('Hello, I am...')

st.text("This is my first Streamlit deployment")


