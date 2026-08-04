from config import EXCEL_CONVERTER_API
import requests

class ExcelGenerator:
    def __init__(self, file, filename:str):
        self.files = {
                "file" : (
                    file.name,
                    file, 
                    file.type
                )
            }
        self.params = {
            "excel_filename" : filename
        }

    def convert(self):
        try:
            response = requests.post(EXCEL_CONVERTER_API, params=self.params, files=self.files)
            if response.status_code == 200:
                return response.json()["saved_at"]
            else:
                return {
                        "status": "error",
                        "status_code": response.status_code,
                        "message": response.text
                    }
        except Exception as e:
            print(f"[FILE UPLOAD ERROR] : {e}")