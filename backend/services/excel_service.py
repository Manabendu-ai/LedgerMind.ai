from ..docling_processing.markdown_extractor import MDExtractor
from ..llm.llm_model import ModelEngine
from ..excel.excel_generator import ExcelGenerator

class ExcelService:
    def __init__(self, file_path: str, excel_filename:str):
        self.file_path = file_path
        self.excel_filename = excel_filename
