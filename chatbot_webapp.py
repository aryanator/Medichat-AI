from flask import Flask, request, jsonify, render_template
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
from transformers import T5ForConditionalGeneration, T5Tokenizer
import pickle

# Initialize Flask app
app = Flask(__name__)

# Device (GPU if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load minimal models
print("Loading models...")
intent_model = DistilBertForSequenceClassification.from_pretrained("./intent_classifier_minimal").to(device)
intent_tokenizer = DistilBertTokenizer.from_pretrained("./intent_classifier_minimal")

answer_model = T5ForConditionalGeneration.from_pretrained("./generator_minimal").to(device)
answer_tokenizer = T5Tokenizer.from_pretrained("./generator_minimal")

# Load label encoder
with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)
print("Models and label encoder loaded.")

# Function to predict the answer
def predict_answer(question):
    # Predict intent (focus area)
    print("Predicting answer...")
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

# Define routes
@app.route('/')
def index():
    print("Rendering index page...")
    return render_template('index.html')  # Render the HTML page

@app.route('/ask', methods=['POST'])
def ask():
    print("Received request at /ask endpoint")
    data = request.get_json()
    if 'question' not in data:
        return jsonify({"error": "No question provided!"}), 400
    
    question = data['question']
    answer = predict_answer(question)
    print(f"Answer generated: {answer}")
    
    return jsonify({"answer": answer})

if __name__ == '__main__':
    print("Running app...")
    app.run(host="127.0.0.1", port=5000, debug=True)
