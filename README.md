# 🤖 UniMind AI - AI Powered PDF Chat Assistant

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/Vector%20Database-FAISS-orange)

## 🌐 Live Demo

🚀 Try the deployed application:

https://unimind-ai-anou2gn6gpq9nmpupqkstm.streamlit.app/

---

# 📌 About The Project

**UniMind AI** is an AI-powered PDF chatbot built using **Retrieval-Augmented Generation (RAG)**.

It allows users to upload PDF documents and ask questions about their content. The application extracts information from documents, converts it into vector embeddings, retrieves relevant information, and generates accurate answers using a Large Language Model.

This project demonstrates the practical implementation of:

- Document processing
- Text chunking
- Semantic search
- Vector databases
- Embeddings
- Retrieval-Augmented Generation
- LLM-based question answering

---

# ✨ Features

## 📂 PDF Document Upload

- Upload one or multiple PDF files
- Extract text automatically
- Preserve document metadata:
  - Filename
  - Page number
  - Chunk information


## 🧠 AI Document Understanding

- Creates embeddings from document chunks
- Stores embeddings using FAISS vector database
- Retrieves relevant information based on user queries


## 💬 Chat With PDFs

Users can ask questions such as:

- Summarize a chapter
- Explain a concept
- Find information from documents
- Generate explanations from uploaded notes


## 📚 Source References

Every response provides:

- Source PDF name
- Page number
- Chunk ID


## ⚡ Streaming Responses

AI responses are generated in real-time for a ChatGPT-like experience.

---

# 🏗️ System Architecture

```
                User
                 |
                 |
          Upload PDF Files
                 |
                 |
            PDF Loader
                 |
                 |
          Text Splitter
                 |
                 |
        Embedding Generator
                 |
                 |
          FAISS Vector DB
                 |
                 |
            Retriever
                 |
                 |
             Groq LLM
                 |
                 |
          AI Generated Answer
```

---

# 🛠️ Tech Stack

## Programming Language

- Python


## Frontend

- Streamlit


## AI Framework

- LangChain


## Large Language Model

- Groq API
- Llama 3.3 70B


## Embedding Model

```
sentence-transformers/all-MiniLM-L6-v2
```


## Vector Database

- FAISS


## PDF Processing

- PyPDF

---

# 📁 Project Structure

```
UniMind-AI/

│
├── app.py
│
├── src/
│   │
│   └── core/
│       │
│       ├── pdf_loader.py
│       ├── text_splitter.py
│       ├── embeddings.py
│       ├── vector_store.py
│       └── rag_pipeline.py
│
├── assets/
│   └── screenshots/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# ⚙️ Installation & Setup

## Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK

cd UniMind-AI
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

For Streamlit Cloud:

Go to:

```
Streamlit Cloud
→ App Settings
→ Secrets
```

Add:

```toml
GROQ_API_KEY="your_api_key_here"
```

---

# ▶️ Run Locally

Start the application:

```bash
streamlit run app.py
```

Application will open:

```
http://localhost:8501
```

---

# 📸 Screenshots

## Home Page

![Home](assets/screenshots/home.png)


## PDF Upload

![Upload](assets/screenshots/upload.png)


## Chat Interface

![Chat](assets/screenshots/chat.png)


## AI Response

![Response](assets/screenshots/response.png)

---

# 🔄 How UniMind AI Works

1. User uploads PDF documents

2. PDF loader extracts text

3. Text splitter divides text into chunks

4. Embedding model converts chunks into vectors

5. FAISS stores the vectors

6. User asks a question

7. Retriever finds relevant chunks

8. LLM generates the final answer using retrieved context

---

# 🚀 Deployment

The application is deployed using:

- Streamlit Cloud

Deployment process:

1. Push project to GitHub
2. Connect repository with Streamlit Cloud
3. Add API key in Secrets
4. Deploy application

---

# 🔮 Future Improvements

- Conversation memory
- Better document management
- Multiple user accounts
- Support for more file formats
- Voice interaction
- Improved UI animations
- Cloud vector database support

---

# 👨‍💻 Author

**Your Name**

Computer Science Engineering Student  
Interested in Artificial Intelligence, Machine Learning and Generative AI

---

# 🙏 Acknowledgements

- Streamlit
- LangChain
- HuggingFace
- FAISS
- Groq

---

⭐ If you like this project, consider giving it a star!