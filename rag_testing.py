from RAG.data_loader import DocumentLoader
from RAG.embeddings import EmbeddingPipeline
from RAG.search import RAGSearch

if __name__ == "__main__":
    # docs = DocumentLoader().load_all_documents()
    # chunks  = EmbeddingPipeline().chunk_documents(docs)
    # vectors = EmbeddingPipeline().embed_chunks(chunks)
    # print(vectors)
    rag_search = RAGSearch()
    query = "What is the invoice total?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)