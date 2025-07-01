#app.py
import streamlit as st
from intent_classifier import classify_intent

st.title("Customer Suppot Chatbot")
user_input = st.text_input("You:", placeholder="Type your question or issue...")

if user_input:
    intent, response = classify_intent(user_input)
    st.markdown(f"**Predicted intent:** `{intent}`")
    st.markdown("**Chatbot:**" + response)
