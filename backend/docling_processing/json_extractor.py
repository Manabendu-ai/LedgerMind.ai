from docling.document_converter import DocumentConverter
import os
import json

os.environ["CUDA_VISIBLE_DEVICES"] = ""

class JsonExtractor:
    def __init__(self):
        self.converter = DocumentConverter()

    def extract(self, file_path: str) -> dict:
        try:
            self.file_path = file_path
            doc = self.converter.convert(file_path)
            self.content = doc.document.export_to_dict()
            return self.content
        except Exception as e:
            print(f"Exception : {e}")

    def save(self, persist_dir:str = "docs/"):
        try:
            os.makedirs(persist_dir, exist_ok=True)

            file_name = self.file_path.split(".")[0].split("/")[1]
            json_path = os.path.join(persist_dir, f"{file_name}.json")

            with open(json_path, "w") as f:
                json.dump(self.content, f, indent = 4)

            print(f"[SUCCESS] File Saved at : {json_path}")
        except Exception as e:
                    print(f"Exception : {e}")