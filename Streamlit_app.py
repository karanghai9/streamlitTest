import streamlit as st
import pickle

# 1. Load the saved pickle model and vectorizer
@st.cache_resource
def load_model():
    with open('model_pickle_new.pkl', 'rb') as f:
        vectorizer, model = pickle.load(f)  # Load both
    return vectorizer, model

vectorizer, model = load_model()

# Streamlit UI for SMS input
st.title("SMS Classification")

