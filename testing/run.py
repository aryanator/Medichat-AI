import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Device (GPU if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load minimal models
intent_model = DistilBertForSequenceClassification.from_pretrained("./intent_classifier_minimal").to(device)
intent_tokenizer = DistilBertTokenizer.from_pretrained("./intent_classifier_minimal")

answer_model = T5ForConditionalGeneration.from_pretrained("./generator_minimal").to(device)
answer_tokenizer = T5Tokenizer.from_pretrained("./generator_minimal")

# Load label encoder (ensure you saved it before)
import pickle
with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

# Function to predict the answer
def predict_answer(question):
    # Predict intent (focus area)
    inputs = intent_tokenizer(question, return_tensors="pt").to(device)  # Move inputs to device
    with torch.no_grad():
        logits = intent_model(**inputs).logits
    predicted_label = torch.argmax(logits).item()
    focus_area = le.inverse_transform([predicted_label])[0]  # Convert label to text

    # Generate answer
    input_text = f"Focus: {focus_area} | Question: {question}"
    inputs = answer_tokenizer(input_text, return_tensors="pt", max_length=128, truncation=True).to(device)
    outputs = answer_model.generate(**inputs, max_length=256, no_repeat_ngram_size=2)
    
    return answer_tokenizer.decode(outputs[0], skip_special_tokens=True)

# Test
question = "What are the symptoms of Glaucoma?"
print(predict_answer(question))
