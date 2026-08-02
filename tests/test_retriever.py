import os 
import sys

# Adding project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.vector_store import VectorStoreManager
from src.core.retriever import Retriever


def main():

    # Path where FAISS vector databse is stored
    vector_db_path = "data/vector_db"

    # Loading the saved vector store
    vector_manager = VectorStoreManager()

    vector_store = vector_manager.load_vector_store(
        vector_db_path
    )

    print("/n" + "=" * 80)
    print("VECTOR STORE LOADING SUMMARY")
    print("=" * 80)

    print("FAISS Vector Store Loaded SUccessfully")

    # Creating Retriever 
    retriever = Retriever(
        vector_store=vector_store,
        top_k = 3
    )

    print("\n" + "=" * 80)
    print("RETRIEVER CREATED")
    print("=" * 80)

    print("Top K Results :", retriever.top_k)

    # Testing Query
    query = "What is Exploratory Data Analysis?"

    results = retriever.retrieve(query)

    print("\n" + "=" * 80)
    print("RETRIEVAL RESULTS")
    print("=" * 80)

    print(f"Query: {query}")
    print(f"Documemts Retrieved: {len(results)}")

    for i, document in enumerate(results, start=1):

        print("\n" + "=" * 80)

        print(f"RESULT {i}")

        print("-" * 80)

        print(
            "Filename : ",
            document.metadata.get("filename")
        )

        print(
            "Page :",
            document.metadata.get("page")
        )

        print(
            "Chunk ID :",
            document.metadata.get("chunk_id")
        )

        print("-" * 80)

        print(
            document.page_content[:300]
        )

        print("=" * 80)


if __name__ == "__main__":
    main()
    