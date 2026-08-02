# 🤖 UniMind AI - Personal AI Assistant for PDFs

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/Vector%20Database-FAISS-orange)

## 📚 Overview

**UniMind AI** is an AI-powered PDF assistant that allows users to upload documents and interact with them using natural language.

Instead of manually searching through long PDFs, users can ask questions and UniMind retrieves relevant information from the documents and generates accurate responses using a Retrieval-Augmented Generation (RAG) pipeline.

This project demonstrates the practical implementation of:

- Document processing
- Text chunking
- Embeddings generation
- Vector databases
- Semantic search
- Large Language Models
- Retrieval-Augmented Generation (RAG)


---

## ✨ Features

✅ Upload multiple PDF documents

✅ Extract text from documents

✅ Split documents into meaningful chunks

✅ Generate semantic embeddings

✅ Store embeddings using FAISS vector database

✅ Retrieve relevant document sections

✅ Ask questions about uploaded PDFs

✅ Generate AI responses using LLMs

✅ Display source references (file name, page number, chunk)


---

## 🏗️ Project Architecture

```
PDF Upload
     |
     ↓
PDF Loader
     |
     ↓
Text Splitter
     |
     ↓
Embedding Generator
     |
     ↓
FAISS Vector Database
     |
     ↓
Retriever
     |
     ↓
RAG Pipeline
     |
     ↓
AI Generated Answer
```


---

## 🛠️ Tech Stack

### Programming Language
- Python 3.14

### Frontend
- Streamlit

### AI / ML Frameworks
- LangChain
- HuggingFace Embeddings
- Groq LLM

### Vector Database
- FAISS

### Document Processing
- PyPDF


---

## 📂 Project Structure

```
UniMind-AI
│
├── app.py                 # Streamlit application
│
├── src
│   └── core
│       ├── pdf_loader.py
│       ├── text_splitter.py
│       ├── embeddings.py
│       ├── vector_store.py
│       └── rag_pipeline.py
│
├── data
│   └── sample_pdfs
│
├── tests
│   ├── test_vector_store.py
│   ├── test_retriever.py
│   └── test_rag_pipeline.py
│
├── requirements.txt
│
└── README.md
```


---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/UniMind-AI.git
```

### 2. Navigate into the project

```bash
cd UniMind-AI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```


### 5. Install dependencies

```bash
pip install -r requirements.txt
```


---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your Groq API key.


---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💬 Example Usage

1. Upload PDF files

2. Click **Process Documents**

3. Ask questions like:

```
What is Exploratory Data Analysis?
```

```
Explain linear regression
```

```
Summarize chapter 1
```

4. UniMind retrieves relevant information and generates an answer.


---

## 🧪 Testing

Run individual tests:

```bash
python tests/test_vector_store.py
```

```bash
python tests/test_retriever.py
```

```bash
python tests/test_rag_pipeline.py
```


---

## 🚀 Future Improvements

Some planned improvements:

- Conversation memory
- Support for more document formats
- Better chunk optimization
- User authentication
- Cloud deployment
- Improved UI/UX
- Multiple LLM provider support


---

## 🎯 Learning Outcomes

Through this project, I learned:

- How Retrieval-Augmented Generation systems work
- Building AI applications using LangChain
- Working with embeddings and vector databases
- Connecting LLMs with custom knowledge sources
- Developing AI applications using Streamlit


---

## 👨‍💻 Author

**Somya Kumar**

Computer Science Engineering Student  
Interested in Artificial Intelligence and Machine Learning


---

⭐ If you find this project interesting, feel free to explore and improve it!