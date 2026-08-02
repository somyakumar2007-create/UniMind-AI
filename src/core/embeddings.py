from typing import List, Dict, Any

from langchain_huggingface import HuggingFaceEmbeddings

class EmbeddingGenerator:
    """
    A class responsible for generating vector embeddings from text chunks.

    This class uses a Hugging Face embedding model to convert each text chunk into a numerical vector that can later be stored in a vector database.
    """

    def __init__(
        self,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    ):
        """ 
        Initialize the embedding model.

        Args:
           model_name : Name of the Hugging Face embedding model.
        """
        self.embedding_model = HuggingFaceEmbeddings(model_name=model_name)

    def generate_embeddings(self, chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]: 
        """
        Generate embeddings for all text chunks and attach them to the chunk data.

        Args: 
           chunks: A list of chunk dictionaries returned by TextSplitter.
                   Each dictionary should contain: 
                   - filename
                   - page
                   - chunk_id
                   - text
        Returns:
           A new list of dictionaries where each chunk also has:
           - embedding
        """

        if not chunks:
            print("No chunks provided for embedding generation.")
            return []

        # Extract only the raw text from each chunk
        texts = []
        for i, chunk in enumerate(chunks, start=1):
            if "text" not in chunk:
                raise KeyError(f"Chunk {i} is missing the 'text' key.")
            texts.append(chunk["text"])

        # Generate embeddings for all chunk texts at once
        embeddings = self.embedding_model.embed_documents(texts)

        # Attach each embedding back to its original chunk
        embedded_chunks = []
        for chunk, embedding in zip(chunks, embeddings):
            new_chunk = chunk.copy()
            new_chunk["embedding"] = embedding
            embedded_chunks.append(new_chunk)

        return embedded_chunks