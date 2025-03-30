# MediChat-AI: Healthcare LLM Assistant

![Demo](https://ai-health-chatbot.streamlit.app/?text=MediChat-AI+Demo) <!-- Add actual demo GIF/screenshot -->

An AI-powered healthcare chatbot that provides accurate medical information using **LLM (Llama 3.1)** and **intent classification**. Deployed with AWS cloud infrastructure.

## Features
- 🩺 **Specialized Medical QA**: Fine-tuned responses for healthcare queries
- ⚡ **Dual-Model Architecture**: 
  - DistilBERT for intent classification
  - T5/Llama-3 for answer generation
- 🌐 **Multi-Deployment Ready**:
  - Streamlit prototype (local/dev)
  - Flask API (production)
  - AWS EC2 + S3 (cloud deployment)

## Installation

### Prerequisites
- Python 3.9+
- [Together.ai API key](https://together.ai) (for Llama-3)
- AWS account (for cloud deployment)


git clone https://github.com/yourusername/MediChat-AI.git
cd MediChat-AI
pip install -r requirements.txt


Configuration
API Keys:

bash
Copy
echo "TOGETHER_API_KEY=your_api_key_here" > .env
Replace with your Together.ai API key

Model Paths:

Place your trained models in:

./intent_classifier_minimal/

./generator_minimal/

Or configure S3 paths in llm.py (for AWS deployment)

Usage
Local Prototype (Streamlit)
bash
Copy
streamlit run app.py
Runs on http://localhost:8501

Production API (Flask)
bash
Copy
python chatbot_webapp.py
API endpoint: POST /ask with JSON {"question": "your question"}

Deployment
AWS Infrastructure
mermaid
Copy
graph TD
    A[EC2 Instance] -->|Load Models| B(S3 Bucket)
    A -->|Serve API| C(CloudFront)
    D[User] -->|HTTPS| C
Key Components:

EC2: t2.xlarge instance (GPU recommended)

S3: Model storage (set AWS_ACCESS_KEY_ID in env)

Security: Configure IAM roles for S3 access

⚠️ AWS credentials are not included in this repo - configure your own in production

Architecture
mermaid
Copy
sequenceDiagram
    User->>+Frontend: Ask question
    Frontend->>+Intent Classifier: Classify query
    Intent Classifier->>+Answer Generator: Focus area + question
    Answer Generator->>+LLM: Augmented prompt
    LLM-->>-User: Verified response
Contributing
Fork the repository

Create feature branch (git checkout -b feature/your-feature)

Commit changes (git commit -m 'Add some feature')

Push to branch (git push origin feature/your-feature)

Open a Pull Request

License
Apache 2.0 - See LICENSE

Note: This repository contains prototype code. For production deployment:

Replace all placeholder API keys

Configure AWS services separately

Add error handling and monitoring

Copy

### Key Documentation Features:
1. **Clear API Key Warning**: Prominent notice about replacing credentials
2. **AWS Abstraction**: Mentions cloud deployment without exposing configs
3. **Dual Deployment Paths**: Highlights both local (Streamlit) and production (Flask) options
4. **Visual Architecture**: Mermaid diagrams for system design
5. **Contributor-Friendly**: Standard open-source workflow

Would you like me to add:
1. Screenshot templates?
2. Detailed AWS setup guide (in separate .md)?
3. Testing instructions?
