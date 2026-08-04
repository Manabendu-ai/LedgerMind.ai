from typing import List, Any
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np
from data_loader import DocumentLoader

class EmbeddingPipeline:
    def __init__(
            self,
            model_name:str = "all-MiniLM-L6-v2",
            chunk_size:int = 2000,
            chunk_overlap:int = 200
    ):
        self.model = SentenceTransformer(model_name)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.doc_loader = DocumentLoader()
        print(f"[INFO] loaded Embedding Model{model_name}")

    def chunk_documents(self, documents: List[Any]) -> List[Any]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function = len,
            seperators = ["\n\n","\n", " ",""] 
        )
        chunks = splitter.split_documents(documents)
        return chunks