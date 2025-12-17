# SHL GenAI Assessment Recommendation Engine

## Problem Statement
Build a GenAI-powered recommendation system that suggests the most relevant SHL assessments
based on a hiring query or job description. The solution must leverage SHL’s assessment catalog
and generate explainable recommendations.

---

## Solution Overview
This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that:
1. Crawls the SHL assessment product catalog
2. Creates embeddings for assessment descriptions
3. Retrieves the most relevant assessments using vector similarity
4. Uses a Large Language Model (LLM) to explain recommendations in natural language

---

## Architecture

**Query → Embedding → FAISS Retrieval → LLM Explanation**

---

## Data Collection
- The SHL assessment catalog is scraped directly from the official SHL website.
- Each assessment page is parsed to extract:
  - Product title
  - Description
  - URL
- The scraped data is stored in `data/processed/shl_products.csv`.

> This step satisfies the requirement:  
> *“Solutions built without scraping and storing SHL product catalogue will be rejected.”*

---

## Embeddings & Retrieval
- Text chunks are created from assessment descriptions.
- Sentence embeddings are generated using **SentenceTransformers**.
- A **FAISS** vector index enables efficient similarity search.

---

## LLM Explanation Layer
- Google **Gemini API** is used to generate human-readable explanations.
- The model explains *why* a particular assessment is recommended for a given query.

---

## Evaluation
- A labeled **Train Set** (provided by SHL) is used to evaluate recall.
- Metric used: **Recall@5**
- This allows iterative improvement of retrieval and prompting logic.

---

## Test Predictions
- Final predictions are generated on the **Unlabeled Test Set**.
- Output format:
  - Query
  - Predicted Assessment URLs
  - Natural language explanation
- Saved as `test_predictions.csv`.

---

## Web Interface
- A **Streamlit UI** allows users to:
  - Enter hiring queries
  - Receive recommended assessments
  - View explanations interactively

---

## Tech Stack
- Python
- BeautifulSoup / Requests
- SentenceTransformers
- FAISS
- Google Gemini API
- Streamlit
- Pandas / NumPy

---

## How to Run

```bash
pip install -r requirements.txt
streamlit run frontend/app.py
# shl-assessment-rag



