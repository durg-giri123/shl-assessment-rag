import streamlit as st
import requests

st.set_page_config(page_title="SHL GenAI Assessment Recommender")

st.title("SHL GenAI Assessment Recommendation Engine")

st.write(
    "Enter a hiring requirement or job description. "
    "The system will recommend relevant SHL assessments with an explanation."
)

query = st.text_area(
    label="Hiring Requirement / Job Description",
    height=180,
    placeholder="e.g. We are hiring a customer support executive with strong communication skills"
)

top_k = st.slider("Number of recommendations", 3, 5, 5)

API_URL = "https://shl-assessment-rag-opa5.onrender.com/recommend"

if st.button("Recommend Assessments", key="recommend_btn"):
    if not query.strip():
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("Waking up recommendation engine (first request may take ~1 minute)..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"query": query, "top_k": top_k},
                    timeout=120  # IMPORTANT: increased timeout
                )

                if response.status_code == 200:
                    data = response.json()

                    st.subheader("Recommended Assessments")
                    for url in data.get("recommendations", []):
                        st.markdown(f"- {url}")

                    st.subheader("Explanation")
                    st.write(data.get("explanation", ""))

                else:
                    st.error("API responded but returned an error.")

            except requests.exceptions.ReadTimeout:
                st.error(
                    "⏳ The backend is waking up (Render free tier sleep).\n\n"
                    "Please wait 30–60 seconds and click **Recommend** again."
                )

            except Exception as e:
                st.error(f"Unexpected error: {e}")

