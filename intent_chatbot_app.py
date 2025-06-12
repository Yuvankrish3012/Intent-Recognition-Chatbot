import streamlit as st
import pickle
import numpy as np
import re

# Load trained components
model = pickle.load(open("D:\ML PROJECTS\Chatbot using NLP (Rule-Based + ML Hybrid)\intent_model.pkl", "rb"))
vectorizer = pickle.load(open("D:\ML PROJECTS\Chatbot using NLP (Rule-Based + ML Hybrid)\intent_vectorizer.pkl", "rb"))
label_encoder = pickle.load(open("D:\ML PROJECTS\Chatbot using NLP (Rule-Based + ML Hybrid)\intent_label_encoder.pkl", "rb"))

# Title and UI
st.set_page_config(page_title="Intent Recognition Chatbot", layout="centered")
st.title("🤖 Intent Recognition Chatbot")
st.markdown("Type a message and I'll classify its **intent** using NLP + ML")

# Function to clean and predict
def predict_intent(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    label = label_encoder.inverse_transform([pred])[0]
    return label

# Input Box
user_input = st.text_input("💬 Your message:")

# Show prediction
if user_input:
    intent = predict_intent(user_input)
    st.success(f"🎯 Predicted Intent: **{intent}**")
