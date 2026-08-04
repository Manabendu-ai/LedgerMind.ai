from RAG.search import RAGSearch

class RagService:
    def __init__(self, query, top_k:int=3):
        self.query = query
        self.top_k = top_k
        self.rag = RAGSearch()

    def get_response(self)->str:
        response = self.rag.search_and_summarize(self.query, self.top_k)
        return response