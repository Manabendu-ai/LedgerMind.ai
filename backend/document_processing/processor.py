from .router import DocumentRouter
from .parser import PDFParser
from .paddle_ocr import OCRParser

class DocumentProcessor:
    def __init__(self):
        self.router = DocumentRouter()
        self.parser = PDFParser()
        self.ocr = OCRParser()

    def extract_text(self, file_path):
        metrics = self.router.classify_document(file_path)

        if metrics.document_type.value == "digital":
            return self.parser.parse(file_path)
        else:
            return self.ocr.extract(file_path)