from ..docling_processing.markdown_extractor import MDExtractor
from ..llm.llm_model import ModelEngine
from ..excel.excel_generator import ExcelGenerator

class ExcelService:
    def __init__(self, file_path: str, excel_filename:str):
        self.file_path = file_path
        self.excel_filename = excel_filename
        self.extractor = MDExtractor()
        self.model = ModelEngine()
        self.excel_gen = ExcelGenerator()

    def markdown_generator(self)->str:
        self.markdown = self.extractor.extract(self.file_path)
        self.md_path = self.extractor.save("md_files/")
        return self.md_path

    def json_converter(self)->str:
        self.response = self.model.run(self.markdown)
        self.json_path = self.model.save(self.excel_filename, "json_files/")
        return self.json_path

    

    
