import streamlit as st
from excel_generator import ExcelGenerator
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
        if uploaded_file is not None:
            st.session_state.uploaded_file = uploaded_file
        if "file_name" not in st.session_state:
            st.session_state.file_name=""

        st.session_state.file_name = st.text_input("name of your excel file ")
        submit_btn = st.form_submit_button(label="Genrate the excel sheet")

        if submit_btn:
            file = st.session_state.get("uploaded_file")
            if file is None:
                st.error("Please Upload a File!")
            else:
                reponse = ExcelGenerator(
                    file, 
                    st.session_state.get("file_name")
                ).convert()
                st.success(reponse)


        