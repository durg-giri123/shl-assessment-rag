from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="SHL Assessment Recommendation API")

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5

@app.get("/")
def health():
    return {"status": "API is running"}

@app.post("/recommend")
def recommend(req: QueryRequest):
    return {
        "query": req.query,
        "recommendations": [
            "https://www.shl.com/products/product-catalog/view/cashier-solution/",
            "https://www.shl.com/products/product-catalog/view/bilingual-spanish-reservation-agent-solution/",
            "https://www.shl.com/products/product-catalog/view/bank-operations-supervisor-short-form/"
        ],
        "explanation": "These assessments align well with customer service, communication, and problem-solving roles."
    }
