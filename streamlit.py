import streamlit as st
from PyPDF2 import PdfReader
from langchain_community.llms import Ollama
import os

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About Project", "Prediction"])

# Main page
if app_mode == "Home":
    st.header("RAG Based PDF Reader ChatBot Using Ollama")
    image_path = "RAG.png"
    st.image(image_path)

elif app_mode == "About Project":
    st.header("About Our Project")
    st.subheader("Project Overview")
    st.text("This project is a RAG (Retrieve and Generate) based PDF reader chatbot using the Ollama LLM.")
    st.text("The chatbot allows users to interact with and query the content of uploaded PDFs.")
    
    st.subheader("Technology Used")
    st.text("1. **Streamlit**: For building the user interface.")
    st.text("2. **Ollama LLM**: For generating responses based on the content of the PDF.")
    st.text("3. **PyPDF2**: For extracting text from PDF files.")
    
    st.subheader("Functionality")
    st.text("1. **PDF Upload**: Users can upload a PDF file.")
    st.text("2. **Text Extraction**: The content of the PDF is extracted for processing.")
    st.text("3. **Question Answering**: Users can ask questions about the PDF content, and the chatbot provides answers based on the extracted text.")
    
    st.subheader("Technical Details")
    st.text("1. **PDF Content Extraction**: The text from the uploaded PDF is processed to make it queryable.")
    st.text("2. **Ollama Model Integration**: The chatbot uses the Ollama LLM to generate answers based on the PDF content.")
    st.text("3. **Streamlit UI**: Provides a user-friendly interface for interaction.")

elif app_mode == "Prediction":
    st.header("PDF Query Prediction")
    st.write("Upload a PDF file and ask questions about its content.")

    # Initialize the Ollama model
    llm = Ollama(model="phi")

    def extract_text_from_pdf(pdf_file):
        reader = PdfReader(pdf_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

    # File uploader
    pdf_file = st.file_uploader("Choose a PDF file", type="pdf")

    if pdf_file is not None:
        with st.spinner('Extracting text from the PDF...'):
            pdf_text = extract_text_from_pdf(pdf_file)

        st.write("PDF Uploaded and Text Extracted. You can now ask questions.")

        # Input for user questions
        question = st.text_input("Ask a question about the PDF")

        if st.button("Get Answer"):
            if question:
                with st.spinner('Getting the answer from the model...'):
                    response = llm.invoke(f"Answer this question based on the PDF content: {question}\nPDF Content: {pdf_text}")
                    st.write("**Answer:**", response)
            else:
                st.write("Please enter a question.")
