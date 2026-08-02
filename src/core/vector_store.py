from pathlib import Path
from typing import List, Dict, Any

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

class VectorStoreManager:
    """
    A class responsible for creating, saving, and loading a FAISS vector store.

    This class takes embedded chunks and builds a searchable vector database so that relevant text can be retrived later using semantic similarity.
    """

    def __init__(
            self,
            model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    ):
        """
        Initialize the embedding model.

        Args:
           model_name: Name of the Hugging Face embedding model.
        """

        self.embedding_model = HuggingFaceEmbeddings(model_name=model_name)

    def create_vector_store(self, embedded_chunks: List[Dict[str, Any]]) -> FAISS:
        """
        Create a FAISS vector store from embedded chunks.

        Args:
           embedded_chunks: A list of dictionaries returned by EmbeddingGenerator.
                            Each dictionary should contain:
                            - filename
                            - page
                            - chunk_id
                            - text 
                            - embedding

        Returns:
            A FAISS vector store object.
        """
        if not embedded_chunks:
            raise ValueError("No embedded chunks provided to create the vector store.")

        text_embeddings = []
        metadatas = []

        for i, chunk in enumerate(embedded_chunks, start=1):
            if "text" not in chunk:
                raise KeyError(f"Chunk {i} is missing the 'text' key.")
            if "embedding" not in chunk:
                raise KeyError(f"Chunk {i} is missing the 'embedding' key.")

            text_embeddings.append((chunk["text"], chunk["embedding"]))
            metadatas.append(
                {
                    "filename": chunk.get("filename", "unknown"),
                    "page": chunk.get("page", "unknown"),
                    "chunk_id": chunk.get("chunk_id", "unknown"),
                }
            )

        vector_store = FAISS.from_embeddings(
            text_embeddings=text_embeddings,
            embedding=self.embedding_model,
            metadatas=metadatas,
        )
        return vector_store

    def save_vector_store(self, vector_store: FAISS, save_path: str) -> None:
        """
        Save the FAISS vector store to disk.

        Args:
            vector_store : The FAISS vector store object
            save_path : Folder path where the vector store will be saved.
        """

        path = Path(save_path)
        path.mkdir(parents=True, exist_ok=True)
        vector_store.save_local(str(path))

    def load_vector_store(self, save_path: str) -> FAISS:
       """
       Load a FAISS vector store from disk.

        Args:
        save_path: Folder path where the vector store was saved.

        Returns:
        Loaded FAISS vector store object.
     """

       return FAISS.load_local(
        save_path,
        self.embedding_model,
        allow_dangerous_deserialization=True
    )


    def create_retriever(
      self,
      vector_store: FAISS,
      k: int = 3
    ):
      """
      Create a retriever from the FAISS vector store.

      Args:
        vector_store: The FAISS vector store.
        k: Number of documents to retrieve.

      Returns:
        A retriever object.
     """

      retriever = vector_store.as_retriever(
        search_kwargs={"k": k}
      )

      return retriever