from .router import DocumentRouter
from .parser import PDFParser


class DocumentProcessor:
    def __init__(self):
        self.router = DocumentRouter()
        self.parser = PDFParser()

    def extract_text(self, file_path):
        metrics = self.router.classify_document(file_path)

        if metrics.document_type.value == "digital":
            return self.parser.parse(file_path)