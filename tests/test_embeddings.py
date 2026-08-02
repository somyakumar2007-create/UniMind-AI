import os
import sys
from pathlib import Path

# Add the project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.pdf_loader import PDFLoader
from src.core.text_splitter import TextSplitter
from src.core.embeddings import EmbeddingGenerator

def main():
    # Path to the PDF
    pdf_files = [
        Path("data/sample_pdfs/Complete_Professional_EDA_Guide_By_Sruthi_Tarimana.pdf")
    ]

    # Step 1: Load PDF
    loader = PDFLoader()
    pages = loader.load_pdfs(pdf_files)

    print("\n" + "=" * 80)
    print("PDF LOADING SUMMARY")
    print("=" * 80)
    print(f"Pages Extracted : {len(pages)}")

    if not pages:
        print("No pages were extracted.")
        return

    # Step 2 : Split text into chunks
    splitter = TextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = splitter.split_text(pages)

    print("\n" + "=" * 80)
    print("TEXT SPLITTING SUMMARY")
    print("=" * 80)
    print(f"Total Chunks Created : {len(chunks)}")

    if not chunks:
        print("No chunks were created.")
        return

    pages_represented = len(set(chunk["page"] for chunk in chunks))
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

    first_embedding = embedded_chunks[0]["embedding"]
    last_embedding =  embedded_chunks[-1]["embedding"]

    print(f"Embedding Dimension (First Chunk) : {len(first_embedding)}")
    print(f"Embedding Dimension (Last CHunk) : {len(last_embedding)}")

    #  Step 4: Display first 3 embedded chunks
    print("\nDisplaying first 3 embedded chunks...\n")

    for chunk in embedded_chunks[:3]:
        print("=" * 80)
        print(f"Filename : {chunk['filename']}")
        print(f"Page : {chunk['page']}")
        print(f"Chunk ID : {chunk['chunk_id']}")
        print(f"Text len : {len(chunk['text'])}")
        print(f"Embedding len : {len(chunk['embedding'])}")
        print("-" * 80)
        print(chunk["text"][:250])
        print("=" * 80)
        print()

if __name__ == "__main__":
    main()

