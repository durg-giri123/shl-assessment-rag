import streamlit as st

st.set_page_config(page_title="SHL GenAI Assessment Recommender")

st.title("🔍 SHL Assessment Recommendation Engine")
st.write(
    "Enter a hiring query or job description to get recommended SHL assessments "
    "along with an explanation."
)

query = st.text_area(
    "Enter your hiring query / JD:",
    height=200,
    placeholder="e.g. I want to assess customer service and communication skills"
)

top_k = st.slider("Number of recommendations", 3, 5, 5)

if st.button("Recommend Assessments"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Finding best assessments..."):
            urls, explanation = run_pipeline(query, top_k=top_k)

        if urls:
            st.subheader("Recommended Assessments")
            for i, url in enumerate(urls, 1):
                st.markdown(f"**{i}.** [{url}]({url})")
        else:
            st.info("No suitable assessments found.")

        if explanation:
            st.subheader("Why these assessments?")
            st.write(explanation)

