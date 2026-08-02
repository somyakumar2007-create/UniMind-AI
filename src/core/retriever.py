from typing import List

from langchain_community.vectorstores import FAISS


class Retriever:
    """
    A class responsible for retrieving relevant documents from the FAISS vector store.
    """

    def __init__(
            self,
            vector_store: FAISS,
            top_k: int = 3
    ):
        """
        Initialize retriever.

        Args:
           vector_store: FAISS vector database
           top_k : Number of relevant chunks to retrieve
        """
        self.vector_store = vector_store
        self.top_k = top_k

    def retrieve(self, query: str) -> List:
        """
        Retrieve relevant chunks for a user query.

        Args: 
           query: User's question

        Returns: List of relevant documents
        """

        if not query.strip():
            raise ValueError("Query cannot be empty.")

        results = self.vector_store.similarity_search(
            query,
            k=self.top_k
        )


        return results