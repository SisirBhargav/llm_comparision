from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from utils.parallel import run_parallel
from utils.report import generate_report

st.set_page_config(
    page_title="The one and only LLM(Clanker) comparision tool,FOR BOTSLUUUUTS",
    page_icon="🤪",
    layout="wide"
)

st.title("⚡🤪⚡ LLM comparision tool")

st.markdown(
    """
    Compare **ChatGPT** and **Gemini** using a **single unified prompt**
    """
)

prompt = st.text_area(
    "Enter your prompt",
    height=150,
    placeholder="Ask the same question to all models..."
)

if st.button("Compare Models"):
    if not prompt.strip():
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Running models in parallel..."):
            responses = run_parallel(prompt)

        st.subheader("ChatGPT")
        st.write(responses.get("ChatGPT", ""))

        st.subheader("Gemini")
        st.write(responses.get("Gemini", ""))

        report_path = generate_report(prompt, responses)

        with open(report_path, "rb") as f:
            st.download_button(
                label="📥 Download Comparison Report (CSV)",
                data=f,
                file_name="llm_comparison_report.csv",
                mime="text/csv"
            )

        st.success("Comparison completed successfully!")
