from .config import EXCEL_CONVERTER_API


class ExcelGenerator:
    def __init__(self, file):
        self.files = {
                "file" : (
                    file.name,
                    file, 
                    file.type
                )
            }