from pydantic import BaseModel

class RAGResponse(BaseModel):
    query : str
    answer : str
    summary : str
    confidence : str
    key_points : list[str]
    examples : list[str]