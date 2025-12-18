from fastapi import FastAPI
from pydantic import BaseModel

# import your pipeline function
# adjust import path if needed
from src.engine.pipeline import run_pipeline  

app = FastAPI(title="SHL GenAI Assessment Recommendation API")


class QueryRequest(BaseModel):
    query: str
    top_k: int = 5


@app.post("/recommend")
def recommend(req: QueryRequest):
    urls, explanation = run_pipeline(req.query, req.top_k)
    return {
        "query": req.query,
        "recommendations": urls,
        "explanation": explanation
    }









