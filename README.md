# RAG Based PDF Reader ChatBot

This project is a RAG (Retrieve and Generate) based PDF reader chatbot using the Ollama Large Language Model (LLM). The chatbot allows users to upload PDF files and ask questions about their content, providing accurate and relevant answers based on the extracted text.

## Features

- **PDF Upload:** Users can upload a PDF file to the application.
- **Text Extraction:** The content of the uploaded PDF is extracted using PyPDF2 for further processing.
- **Question Answering:** Users can ask questions about the content of the PDF, and the chatbot provides answers using the Ollama LLM.
- **Streamlit UI:** A user-friendly interface built with Streamlit to interact with the chatbot.

## Technology Stack

- **Streamlit:** For building the user interface.
- **Ollama LLM:** For generating responses based on the content of the PDF.
- **PyPDF2:** For extracting text from PDF files.
- **langchain:** For integrating the Ollama model and managing the language processing pipeline.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Murghendra/RAG-PDF-ChatBot.git
   cd RAG-PDF-ChatBot
   
2. Install Dependencies:
    ```bash
   pip install -r requirements.txt

3. Run the Streamlit server:
   ```bash
   streamlit run streamlit.py 

## Screenshots

Here are some screenshots of the application:

### Home Page
<img src="Screenshot 2024-08-17 163642.png" alt="Home Page" width="800"/>

### About Project Page
<img src="Screenshot 2024-08-17 163659.png" alt="About Project Page" width="800"/>

### PDF Query Prediction
<img src="Screenshot 2024-08-17 163957.png" alt="PDF Query Prediction" width="800"/>
