import streamlit as st
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
from transformers import T5ForConditionalGeneration, T5Tokenizer
import pickle
from llm import generate_response



# Streamlit UI
st.title("💬 AI Health Assistant")
st.write("Ask a health-related question and get an AI-generated response.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    role, text = message
    with st.chat_message(role):
        st.markdown(text)

# User input
if user_input := st.chat_input("Ask your health-related question..."):
    # Display user message
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate and display response
    answer = generate_response(user_input)
    st.session_state.messages.append(("assistant", answer))
    with st.chat_message("assistant"):
        st.markdown(answer)
