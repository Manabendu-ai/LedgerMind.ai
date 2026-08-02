from dataclasses import dataclass
import fitz
from .models import DocumentType

@dataclass
class DocumentMetrics:
    def __init__(self, metrics : dict):
        self.total_pages = metrics["total_pages"]
        self.total_words = metrics["total_words"]
        self.total_characters = metrics["total_characters"]
        self.avg_words_per_page= metrics["avg_words_per_page"]
        self.avg_characters_per_page= metrics["avg_characters_per_page"]
        self.document_type= metrics["document_type"]
    



class Metrcis:

    def get_metrcis(self, file_path : str):
        doc = fitz.open(file_path)

        total_words = 0
        total_characters = 0
        for page in doc:
            text = page.get_text().strip()
            total_words += len(text.split())
            total_characters += len(text)

        total_pages = len(doc)

        return {
            "total_pages" : total_pages,
            "total_words" : total_words,
            "total_characters" : total_characters,
            "avg_words_per_page": total_words/total_pages,
            "avg_characters_per_page": total_characters/total_pages
        }




