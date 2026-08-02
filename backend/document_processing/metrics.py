from dataclasses import dataclass
from .models import DocumentType

@dataclass
class DocumentMetrics:
    total_pages : int
    total_words : int
    total_characters : int
    avg_words_per_page: int
    avg_characters_per_page: int
    document_type: DocumentType



# class Metrcis:

#     def __init__(self, path : str):


