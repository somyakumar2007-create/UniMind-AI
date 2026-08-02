from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextSplitter:
    """
    A class responsible for splitting extracted PDF text into smaller chunks.

    This class uses LangChain's RecursiveCharacterTextSplitter to divide large pieces of text into manageable chunks while preserving context through chunk overlap.
    """

    def __init__(
            self,
            chunk_size: int = 1000,
            chunk_overlap: int = 200,

     ):
        """
        Initialize the text splitter.

        Args:
          Chunk_size : Maximum number of characters in each chunk.
          Chunk_overlap : Number of overlappping characters between consecutive chunks
        """

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size = chunk_size,  
            chunk_overlap = chunk_overlap,
        )    

    def split_text(self, pages: List[dict]) -> List[dict]:
        """
        Split the extracted PDF text into smaller chunks while preserving metadata.

        Args:
           pages: A list of dictionaries returned by PDFLoader.
                  Each dictionary contains:
                  - filename
                  - page
                  - text

            Returns: 
               A list of dictionay containing:
               - filename
               - page
               - chunk id
               - text
        """

        chunks = [] #List to store all generated chunks
        chunk_id = 1 #Unique ID for every chunk
        
        # Processes one page at a time

        for page in pages:

            page_chunks = self.splitter.split_text(page["text"]) #Split the page text into smaller chunks
            
            # Processes every generated chunk
            
            for text_chunk in page_chunks:

                chunks.append(
                    {
                        "filename": page["filename"],
                        "page": page["page"],
                        "chunk_id": chunk_id,
                        "text": text_chunk,
                    }
                )

                chunk_id += 1

        return chunks