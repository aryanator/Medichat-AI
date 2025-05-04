import streamlit as st
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
from transformers import T5ForConditionalGeneration, T5Tokenizer
import pickle
# print("Versions:")
# print(f"Streamlit: {st.__version__}")
# print(f"PyTorch: {torch.__version__}")
# print(f"Transformers: {transformers.__version__}")



# Set device (GPU if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
st.sidebar.write(f"Using device: {device}")

# Load models and tokenizer
@st.cache_resource
def load_models():
    st.sidebar.write("Loading models...")
    intent_model = DistilBertForSequenceClassification.from_pretrained("./intent_classifier_minimal").to(device)
    intent_tokenizer = DistilBertTokenizer.from_pretrained("./intent_classifier_minimal")
    
    answer_model = T5ForConditionalGeneration.from_pretrained("./generator_minimal").to(device)
    answer_tokenizer = T5Tokenizer.from_pretrained("./generator_minimal")

    with open("label_encoder.pkl", "rb") as f:
        le = pickle.load(f)

    return intent_model, intent_tokenizer, answer_model, answer_tokenizer, le

intent_model, intent_tokenizer, answer_model, answer_tokenizer, le = load_models()

# Function to predict the answer
def predict_answer(question):
    # Predict intent (focus area)
    inputs = intent_tokenizer(question, return_tensors="pt").to(device)
    with torch.no_grad():
        logits = intent_model(**inputs).logits
    predicted_label = torch.argmax(logits).item()
    focus_area = le.inverse_transform([predicted_label])[0]  # Convert label to text

    # Generate answer
    input_text = f"Focus: {focus_area} | Question: {question}"
    inputs = answer_tokenizer(input_text, return_tensors="pt", max_length=128, truncation=True).to(device)
    outputs = answer_model.generate(**inputs, max_length=256, no_repeat_ngram_size=2)
    
    return answer_tokenizer.decode(outputs[0], skip_special_tokens=True)

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
    answer = predict_answer(user_input)
    st.session_state.messages.append(("assistant", answer))
    with st.chat_message("assistant"):
        st.markdown(answer)
