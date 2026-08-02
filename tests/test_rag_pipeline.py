import os
import sys

# Adding project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.vector_store import VectorStoreManager
from src.core.retriever import Retriever
from src.core.rag_pipeline import RAGPipeline

def main():

    # Path where FAISS vector database is stored.
    vector_db_path = "data/vector_db"

    # Step 1: Load Vector Database

    vector_manager = VectorStoreManager()

    vector_store = vector_manager.load_vector_store(
        vector_db_path
    )

    print("\n" + "=" * 80)
    print("VECTOR STORE LOADED")
    print("=" * 80)

    print("FAISS database loaded successfully.")

    # Step 2: Create Retriever

    retriever = Retriever(
        vector_store=vector_store,
        top_k = 3
    )

    print("\n" + "=" * 80)
    print("RETRIEVER CREATED")
    print("=" * 80)

    print("Top K documents:", retriever.top_k)

    # Step 3: Create RAG Pipeline

    rag = RAGPipeline(
        retriever=retriever
    )

    print("\n" + "=" * 80)
    print("RAG PIPELINE CREATED")
    print("=" * 80)

    print("Groq LLM connected successfully.")

    # Step 4: Ask questions

    questions = [
        "What is EDA?",
        "Why is feature scaling needed?",
        "What are duplicate values?"
    ]

    for question in questions:

        print("\n" + "=" * 80)
        print("QUESTION")
        print("=" * 80)

        print(question)

        response = rag.generate_answer(question)

        print("\n" + "=" * 80)
        print("ANSWER")
        print("=" * 80)

        print(response["answer"])

        print("\nSources:")
        for source in response["sources"]:
            print(
                f"- {source['filename']} | "
                f"Page: {source['page']} | "
                f"Chunk: {source['chunk_id']}"
            )


if __name__ == "__main__":
    main()