import os
import sys
from pathlib import Path

# Adding the project root to Python Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from src.core.pdf_loader import PDFLoader
from src.core.text_splitter import TextSplitter


def main():

    # Specifying the PDF Path
    pdf_paths = [
        Path("data/sample_pdfs/Complete_Professional_EDA_Guide_By_Sruthi_Tarimana.pdf"),
         Path("data/sample_pdfs/linear_regression_beginners_guide.pdf")
    ]

    # Extracting the text from PDF
    loader = PDFLoader()
    pages = loader.load_pdfs(pdf_paths)

    print("\n" + "=" * 80)
    print("PDF LOADING SUMMARY")
    print("=" * 80)

    print(f"Number of PDFs Loaded : {len(pdf_paths)}")

    print(f"Pages Extracted : {len(pages)}")

    print("\nPDFs Loaded:")

    for pdf in pdf_paths:
      print(f"- {pdf.name}")

    # Splitting the extracted text into chunks
    splitter = TextSplitter()
    chunks = splitter.split_text(pages)

    print("\n" + "=" * 80)
    print("TEXT SPLITTING SUMMARY")
    print("=" * 80)

    print(f"Total Chunks Created : {len(chunks)}")
    
    if not chunks:
        print("No chunks were created.")
        return
    
    # To count how many different pdf pages contributed to the chunk
    pages_used = len(
        set(
            (chunk["filename"], chunk["page"])
            for chunk in chunks
        )
    )
    print(f"Pages Represented : {pages_used}")
    
    print(f"First Chunk Length : {len(chunks[0]['text'])}")
    print(f"Last Chunk Length : {len(chunks[-1]['text'])}")

    # Displaying first 5 elements
    print("\nDisplaying first 5 Chunks....\n ")

    for chunk in chunks[:5]:
        print("=" * 80)
        print(f"Filename : {chunk['filename']}")
        print(f"Page : {chunk['page']}")
        print(f"Chunk Id : {chunk['chunk_id']}")
        print(f"Length : {len(chunk['text'])}")
        print("-" * 80)

        print(chunk["text"][:300])  #To show the first 300 characters

        print("=" * 80)
        print()

    # To display the last chunk 
    print("=" * 80)
    print("LAST CHUNK")
    print("=" * 80)

    last_chunk = chunks[-1]

    print(f"Filename : {last_chunk['filename']}")
    print(f"Page : {last_chunk['page']}")
    print(f"Chunk ID : {last_chunk['chunk_id']}")
    print(f"Length : {len(last_chunk['text'])}")

    print("=" * 80)
    print(last_chunk["text"][:300])

    print("=" * 80)

if __name__ == "__main__":
    main()