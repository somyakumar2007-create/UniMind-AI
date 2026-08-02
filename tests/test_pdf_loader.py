import sys
from pathlib import Path 

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.core.pdf_loader import PDFLoader

pdf_paths = [
     Path("data/sample_pdfs/Complete_Professional_EDA_Guide_By_Sruthi_Tarimana.pdf"),
     Path("data/sample_pdfs/linear_regression_beginners_guide.pdf")
    ]

print("\nLoaded PDFs: ")

for pdf in pdf_paths:
    print("-", pdf.name)

loader = PDFLoader()
pages = loader.load_pdfs(pdf_paths)


print(f"Pages extracted: {len(pages)}")
print("\nNumber of PDFs loaded:", len(pdf_paths))

for doc in pages:
    print("-" * 50)
    print(f"File: {doc['filename']}")
    print(f"Page: {doc['page']}")
    print(doc["text"][:200])