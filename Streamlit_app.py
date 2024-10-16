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
st.title("Spam or Non-spam Email Classifier")

sms = st.text_input('Enter your Email')

if st.button("Predict"):
    if sms:
        # Vectorize the input Email
        sms_vectorized = vectorizer.transform([sms])
        prediction = model.predict(sms_vectorized)

        # Display the result based on the prediction
        if prediction[0] == 1:
            st.write("Prediction: **Spam**")
        else:
            st.write("Prediction: **Not Spam**")
    else:
        st.write("Please enter an Email for prediction.")

