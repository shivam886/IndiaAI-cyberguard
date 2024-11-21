# IndiaAI-cyberguard
An NLP model for classifying cybercrime descriptions into categories and subcategories for the IndiaAI CyberGuard Hackathon. Built with FastAPI, it features text preprocessing, classification models, and a real-time API interface for efficient cybercrime reporting and handling.
# IndiaAI CyberGuard NLP Model
# Overview
This project is a submission for the IndiaAI CyberGuard Hackathon, focusing on building an NLP model to classify text into categories and subcategories. The project leverages state-of-the-art machine learning techniques and pre-trained transformers to process raw, unstructured data efficiently. A FastAPI-powered backend exposes the model for API-based predictions.

# Features
Text Classification:
Classifies raw text data into predefined categories and subcategories.
Fine-tuned Models:
Models are trained and fine-tuned on clean datasets for optimal accuracy.
Interactive API:
Offers an API endpoint for predictions, making the model accessible for real-world use.
Scalable Architecture:
Modular design for easy integration and scalability.


# Installation
# Prerequisites
Python 3.8 or later
Virtual environment tool (optional but recommended)
Steps
# Clone the repository:

git clone https://github.com/shivam886/IndiaAI-cyberguard.git
cd IndiaAI_cyberguard-AI
# Set up a virtual environment:

python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
# Install dependencies:

pip install -r requirements.txt
# Start the API server:

uvicorn app.main:app --reload
