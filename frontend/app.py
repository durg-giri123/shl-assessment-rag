import streamlit as st
import pandas as pd
import faiss
import numpy as np
import google.generativeai as genai
import os

# ---------- CONFIG ----------
st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")

# ---------- LOAD DATA ----------
chunked_df = pd.read_csv("../data/processed/shl_products.csv")

# Fix titles if needed
chunked_df["product_title"] = chunked_df["title"].fillna(
    chunked_df["url"].apply(lambda x: x.split("/")[-2].replace("-", " ").title())
)

# Load embeddings
embeddings = np.vstack(chunked_df["embedding"].apply(eval).values)

# Build FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Load embedding model
from sentence_transformers import SentenceTransformer
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
llm = genai.GenerativeModel("models/gemini-2.5-flash")

# ---------- FUNCTIONS ----------
def recommend(query, k=3):
    q_emb = embedding_model.encode([query], normalize_embeddings=True)
    D, I = index.search(q_emb, k)
    return chunked_df.iloc[I[0]]

def explain(query, rows):
    context = ""
    for _, r in rows.iterrows():
        context += f"- {r['product_title']}: {r['description']}\n"

    prompt = f"""
You are an expert talent assessment consultant.

User Query:
{query}

Explain why the following SHL assessments are suitable:

{context}
"""
    return llm.generate_content(prompt).text

# ---------- UI ----------
st.title("🔍 SHL Assessment Recommendation Engine")

query = st.text_area("Enter hiring requirement / job description:")

if st.button("Recommend Assessments"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        results = recommend(query)
        explanation = explain(query, results)

        st.subheader("Recommended Assessments")
        for _, r in results.iterrows():
            st.markdown(f"**{r['product_title']}**")
            st.write(r["url"])
            st.markdown("---")

        st.subheader("Explanation")
        st.write(explanation)
