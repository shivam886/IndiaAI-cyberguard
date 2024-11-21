# IndiaAI-cyberguard
An NLP model for classifying cybercrime descriptions into categories and subcategories for the IndiaAI CyberGuard Hackathon. Built with FastAPI, it features text preprocessing, classification models, and a real-time API interface for efficient cybercrime reporting and handling.
# IndiaAI CyberGuard NLP Model
# Overview
This project is a submission for the IndiaAI CyberGuard Hackathon, focusing on building an NLP model to classify text into categories and subcategories. The project leverages state-of-the-art machine learning techniques and pre-trained transformers to process raw, unstructured data efficiently. A FastAPI-powered backend exposes the model for API-based predictions.

# Our Solution
Our solution is an NLP-based classification model designed to automatically analyze and categorize fraud complaints. By leveraging Natural Language Processing, the model quickly identifies key elements within each complaint, such as:

Fraud Type: Categorizes cases into phishing, identity theft, cyberstalking, and more.
Victim Type: Distinguishes between individual and organizational victims.
Severity and Urgency: Flags high-severity cases for quick response.
# Key Features
Automated Categorization: Reduces manual workload by instantly classifying incoming complaints.
Resource Prioritization: Helps teams focus on critical cases, ensuring efficient use of resources.
# Benefits
Increased Efficiency: Faster classification means quicker response times.
Enhanced Decision-Making: Prioritized cases enable focused and effective resource allocation.
Trend Detection: Analyzing patterns in fraud complaints helps in anticipating and countering potential spikes in specific fraud types.
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

# Clone the repository:
git clone https://github.com/shivam886/IndiaAI-cyberguard.git

# Install dependencies:
pip install -r requirements.txt

# Run the Model;
Main.py

uvicorn app.main:app --reload

# Team Members
Nikhil Bansal - Leader
Shivam Pal
Simran titoria
Himani Sharma
