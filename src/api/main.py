from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="SHL GenAI Recommendation API")


class QueryRequest(BaseModel):
    query: str
    top_k: int = 5


@app.post("/recommend")
def recommend(req: QueryRequest):
    # TEMPORARY DUMMY RESPONSE (for deployment sanity)
    return {
        "query": req.query,
        "recommendations": [
            "https://www.shl.com/products/product-catalog/view/cashier-solution/",
            "https://www.shl.com/products/product-catalog/view/bilingual-spanish-reservation-agent-solution/"
        ],
        "explanation": "These assessments evaluate customer service, communication, and problem-solving skills."
    }
