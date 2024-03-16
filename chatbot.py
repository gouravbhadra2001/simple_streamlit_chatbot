import streamlit as st
from transformers import pipeline

# Load the chatbot model
chatbot = pipeline("conversational")

# Streamlit app layout
st.title("Simple Chatbot")

# User input
user_input = st.text_input("You:", "")

# Process user input and generate response
if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Get response from chatbot model
        bot_response = chatbot(user_input)[0]['generated_text']
        st.text_area("Bot:", value=bot_response, height=100)
