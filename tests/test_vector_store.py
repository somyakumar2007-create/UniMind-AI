import os
import sys
from pathlib import Path

# Add the project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.pdf_loader import PDFLoader
from src.core.text_splitter import TextSplitter
from src.core.embeddings import EmbeddingGenerator
from src.core.vector_store import VectorStoreManager



def main():
    # PDF Path
    pdf_paths = [
       Path("data/sample_pdfs/Complete_Professional_EDA_Guide_By_Sruthi_Tarimana.pdf"),
       Path("data/sample_pdfs/linear_regression_beginners_guide.pdf")
    ]

    # Step 1: Load Pdf
    loader = PDFLoader()
    pages = loader.load_pdfs(pdf_paths)

    print("\n" + "=" * 80)
    print("PDF LOADING SUMMARY")
    print("=" * 80)
    print(f"Pages Extracted : {len(pages)}")

    print(f"Number of PDFs Loaded : {len(pdf_paths)}")

    print("\nPDFs Loaded:")

    for pdf in pdf_paths:
      print(f"- {pdf.name}")

    if not pages:
        print("No pages were extracted.")
        return

    # Step 2: Split the text into chunks
    splitter = TextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = splitter.split_text(pages)

    print("\n" + "=" * 80)
    print("TEXT SPLITTING SUMMARY")
    print("=" * 80)
    print(f"Total Chunks Created : {len(chunks)}")

    if not chunks:
        print("No chunks were created.")
        return

    pages_represented = len(
        set(
            (chunk["filename"], chunk["page"])
            for chunk in chunks
        )
    )

    print(f"Pages Represented : {pages_represented}")
    print(f"First Chunk Length : {len(chunks[0]['text'])}")
    print(f"Last Chunk Length : {len(chunks[-1]['text'])}")

    # Step 3: Generate embeddings
    embedder = EmbeddingGenerator()
    embedded_chunks = embedder.generate_embeddings(chunks)

    print("\n" + "=" * 80)
    print("EMBEDDING SUMMARY")
    print("=" * 80)
    print(f"Total Embedded Chunks : {len(embedded_chunks)}")

    if not embedded_chunks:
        print("No embeddings were generated.")
        return

    print(f"Embedding Dimension (First Chunk) : {len(embedded_chunks[0]['embedding'])}")
    print(f"Embedding Dimension (Last Chunk) : {len(embedded_chunks[-1]['embedding'])} ")

    # Step 4: Create vector store
    manager = VectorStoreManager()
    vector_store = manager.create_vector_store(embedded_chunks)

    print("\n" + "=" * 80)
    print("VECTOR STORE SUMMARY")
    print("=" * 80)
    print("FAISS vector store created successfully.")

    # Step 5: Save vector store
    save_path = "data/vector_db"
    manager.save_vector_store(vector_store, save_path)
    print(f"Vector store saved at: {save_path}")

    # Step 6: Test retrieval
    print("\n" + "=" * 80)
    print("SAMPLE RETRIEVAL TEST")
    print("=" * 80)

    queries = [
        "What is EDA?",
        "What is linear regression?"
    ]


    for query in queries:
      print("\n" + "=" * 80)
      print(f"Query: {query}")
      print("=" * 80)

      results = vector_store.similarity_search(query, k=3)

      print(f"Top Results: {len(results)}")

      for i, doc in enumerate(results, start=1):
        print("\n" + "-" * 50)
        print(f"Result {i}")
        print(f"Filename : {doc.metadata.get('filename')}")
        print(f"Page : {doc.metadata.get('page')}")
        print(f"Chunk ID : {doc.metadata.get('chunk_id')}")
        print(f"Text : {doc.page_content[:250]}")


if __name__ == "__main__":
    main()




