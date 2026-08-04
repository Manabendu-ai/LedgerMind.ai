import streamlit as st

st.set_page_config(
    page_title = "LedgerMind.ai",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("LedgerMind.ai")

st.markdown(
    """
    #### Enterprise AI platform that transform invoices, receipts, tax documents, and financial records into structured intelligence.
    """
)
# st.divider()
# with st.form(key = "upload_documnet"):
#     st.markdown("##### Upload Your Document")