import streamlit as st
from pdf2docx import Converter
import os
import tempfile

# Title of the application
st.title("PDF to Word Converter")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded PDF file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
        tmp.write(uploaded_file.getvalue())
        file_path = tmp.name

    # Convert PDF to Word
    output_file_path = file_path.replace('.pdf', '.docx')
    cv = Converter(file_path)
    cv.convert(output_file_path)
    cv.close()

    # Download link for converted file
    with open(output_file_path, "rb") as file:
        btn = st.download_button(
                label="Download Word File",
                data=file,
                file_name="converted.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    # Clean up: remove temporary files
    os.remove(file_path)
    os.remove(output_file_path)
