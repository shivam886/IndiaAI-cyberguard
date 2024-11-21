import pickle
from app.utils import clean_text

# Load pre-trained models and vectorizer
with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("models/category_model.pkl", "rb") as f:
    category_model = pickle.load(f)

with open("models/subcategory_model.pkl", "rb") as f:
    subcategory_model = pickle.load(f)

def predict_category(text):
    """Predict the category of the input text."""
    cleaned_text = clean_text(text)
    features = vectorizer.transform([cleaned_text])
    return category_model.predict(features)[0]

def predict_subcategory(text):
    """Predict the subcategory of the input text."""
    cleaned_text = clean_text(text)
    features = vectorizer.transform([cleaned_text])
    return subcategory_model.predict(features)[0]
