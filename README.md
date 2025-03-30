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

```bash
git clone https://github.com/yourusername/MediChat-AI.git
cd MediChat-AI
pip install -r requirements.txt
