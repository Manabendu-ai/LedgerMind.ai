from dataclasses import dataclass
import fitz
from .models import DocumentType

@dataclass
class DocumentMetrics:
    total_pages : int
    total_words : int
    total_characters : int
    avg_words_per_page: int
    avg_characters_per_page: int
    document_type: DocumentType



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




