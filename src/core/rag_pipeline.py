import os
from typing import List

import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

class RAGPipeline:
    """
    A class responsible for connecting the retriever with the LLM to generate answers.
    """

    def __init__(
        self,
        retriever,
        model_name: str = "llama-3.3-70b-versatile",
    ):
        """
        Initialize the RAG pipeline.

        Args:
           retriever: Retriever object responsible for finding relevant documents.

        model_name:
             Groq LLM model name.
        """

        load_dotenv()

        if "GROQ_API_KEY" in st.secrets:
            api_key = st.secrets["GROQ_API_KEY"]

        else:
            api_key = os.getenv("GROQ_API_KEY")


        if not api_key:
            raise ValueError(
              "GROQ_API_KEY not found."
            )

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found. Check your .env file."
            )

        self.retriever = retriever

        self.llm = ChatGroq(
            model=model_name,
            temperature=0,
            api_key=api_key,
            streaming=True
        )

        self.prompt = ChatPromptTemplate.from_template(
            """
            You are UniMind AI, an assistant that answers questions using the provided context.

            Answer only using the context given below.

            If the answer is not available in the context,
            say:
            "I could not find the answer in the provided documents."

            
            Context:
            {context}

            
            
            Question:
            {question}



            Answer:
            """
        )

    def generate_answer(self, question: str) -> dict:
     """
        Generate an answer using retrieved documents.
     """

     # Retrieve relevant documents
     documents = self.retriever.invoke(question)

     if not documents:
        return {
            "answer": "No relevant information found.",
            "sources": []
        }


     # Combine retrieved text
     context = "\n\n".join(
        [
            document.page_content
            for document in documents
        ]
     )


     # Create prompt
     messages = self.prompt.format_messages(
        context=context,
        question=question
     )


     # Generate response
     response = self.llm.invoke(messages)


     # Collect sources
     sources = []

     for document in documents:

        sources.append(
            {
                "filename": document.metadata.get(
                    "filename",
                    "Unknown"
                ),

                "page": document.metadata.get(
                    "page",
                    "Unknown"
                ),

                "chunk_id": document.metadata.get(
                    "chunk_id",
                    "Unknown"
                )
            }
        )


     return {
        "answer": response.content,
        "sources": sources
     }

    def stream_answer(self, question: str):

     """
       Generate streaming response from LLM.
     """

     # Retrieve documents
     documents = self.retriever.invoke(question)

     if not documents:
        return iter(["No relevant information found."]), []

 
     # Combine context
     context = "\n\n".join(
        [
            document.page_content
            for document in documents
        ]
     )


     messages = self.prompt.format_messages(
        context=context,
        question=question
     )


      # Collect sources
     sources = []

     for document in documents:

        sources.append(
            {
                "filename": document.metadata.get(
                    "filename",
                    "Unknown"
                ),

                "page": document.metadata.get(
                    "page",
                    "Unknown"
                ),

                "chunk_id": document.metadata.get(
                    "chunk_id",
                    "Unknown"
                )
            }
        )


     # Stream response
     response = self.llm.stream(messages)


     return response, sources