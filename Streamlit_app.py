import streamlit as st
import pickle

# 1. Load the saved pickle model and vectorizer
@st.cache_resource
def load_model():
    with open('model_pickle.pkl', 'rb') as f:
        vectorizer, model = pickle.load(f)
    return vectorizer, model

# Load the model once using the load_model function
vectorizer, model = load_model()

# 2. Streamlit interface to take SMS as input
st.title("SMS Classification")

# Input for the user's SMS
sms = st.text_input('Enter your SMS')

# 3. Prediction button
if st.button("Predict"):
    if sms:
        # 4. Vectorize the SMS input
        sms_vectorized = vectorizer.transform([sms])
        
        # 5. Predict using the loaded model
        prediction = model.predict(sms_vectorized)
        
        # 6. Display the prediction result
        st.write(f"Prediction: {prediction[0]}")
    else:
        st.write("Please enter an SMS for prediction.")




