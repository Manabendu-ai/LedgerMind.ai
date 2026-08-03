from docling.document_converter import DocumentConverter
import os

os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
os.environ["CUDA_VISIBLE_DEVICES"] = ""

class MDExtractor:
    def __init__(self):
        self.converter = DocumentConverter()

    def extract(self, file_path:str)->str:
        try:
            self.file_path = file_path
            doc = self.converter.convert(file_path)
            self.content = doc.document.export_to_markdown()
            return self.content
        except Exception as e:
            print(f"Exception : {e}")
        