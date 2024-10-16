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

sms = st.text_input('Enter your SMS')

if st.button("Predict"):
    if sms:
        sms_vectorized = vectorizer.transform([sms])
        prediction = model.predict(sms_vectorized)
        st.write(f"Prediction: {prediction[0]}")
    else:
        st.write("Please enter an SMS for prediction.")

