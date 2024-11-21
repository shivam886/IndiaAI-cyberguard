from fastapi import FastAPI, HTTPException
from app.model import predict_category, predict_subcategory

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Welcome to CyberGuard AI!"}

@app.post("/predict/")
async def predict(text: str):
    if not text:
        raise HTTPException(status_code=400, detail="Text input is required")
    
    category = predict_category(text)
    subcategory = predict_subcategory(text)
    
    return {
        "category": category,
        "subcategory": subcategory
    }
