import streamlit as st
from .excel_generator import ExcelGenerator
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
st.divider()
with st.form(key = "upload_documnet"):
    left, center, right = st.columns([3,4,3])
    with center:
        st.markdown("##### Upload Your Document")

        uploaded_file = st.file_uploader(
            "Tax Invoices, Receipts, Bills",
            type=["pdf"]
        )
        file_name = st.text_input("name of your excel file ")
        submit_btn = st.form_submit_button(label="Genrate the excel sheet")

if submit_btn:
    reponse = ExcelGenerator(uploaded_file).convert()
    st.success(reponse)
        