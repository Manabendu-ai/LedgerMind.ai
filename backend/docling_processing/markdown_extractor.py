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
            print(f"Exception at Extracting: {e}")

    def save(self, persist_dir:str = "docs/"):
        try:
            os.makedirs(persist_dir, exist_ok=True)
    
            file_name = self.file_path.split(".")[0].split("/")[1]
            md_path = os.path.join(persist_dir, f"{file_name}.md")
    
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(self.content)
    
            print(f"[SUCCESS] File Saved at : {md_path}")
        except Exception as e:
            print(f"Exception at Saving : {e}")
        