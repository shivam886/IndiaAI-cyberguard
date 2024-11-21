import re
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_text(text):
    """Clean the input text by removing special characters, numbers, and extra spaces."""
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'\d', '', text)  # Remove digits
    return text.strip().lower()
