from pathlib import Path
from typing import List, Dict, Any

from pypdf import PdfReader 

class PDFLoader:
    """ 
    A class is responsible for loading and extracting text from PDF files.

    This class reads one or more PDF files and returns the extracted text while preserving useful metadata such as the filename and page number.
    """

    def __init__(self):
        """ Initialize the PDFLoader """
        pass

    def load_pdfs(
        self, 
        pdf_paths: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Load one or more PDF files.
        """

        pages = []

        for pdf in pdf_paths:

           pdf_path = pdf["path"]
           original_name = pdf["filename"]

           try: 

               reader = PdfReader(pdf_path)

               for page_number, page in enumerate(
                   reader.pages, 
                   start=1
                ):

                   text = page.extract_text()

                   if not text:
                       continue

                   pages.append(
                       {
                          "filename": original_name,
                           "page": page_number,
                            "text": text
                        }
                    )

           except Exception as e:
               print(
                   f"Error reading {original_name}: {e}"
               )

               continue
        return pages
