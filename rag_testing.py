from RAG.data_loader import DocumentLoader
from RAG.embeddings import EmbeddingPipeline

if __name__ == "__main__":
    docs = DocumentLoader().load_all_documents()
    chunks  = EmbeddingPipeline().chunk_documents(docs)
    vectors = EmbeddingPipeline().embed_chunks(chunks)
    print(vectors)