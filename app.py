#app.py
import streamlit as st
from intent_classifier import classify_intent

st.title("Mini Call Center Intent Classifier")
user_input = st.text_input("Enter customer message:")

if user_input:
    prediction = classify_intent(user_input)
    st.write(f"Predicted intent: **{prediction}**")
