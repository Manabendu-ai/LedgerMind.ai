from docling.document_converter import DocumentConverter
import os

os.environ["CUDA_VISIBLE_DEVICES"] = ""

class JsonExtractor:
    def __init__(self):
        self.converter = DocumentConverter()

    def extract(self, file_path: str) -> dict:
        try:
            doc = self.converter.convert(file_path)
            self.content = doc.document.export_to_dict()
            return self.content
        except Exception as e:
            print(f"File Exception : {e}")