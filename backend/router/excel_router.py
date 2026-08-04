from fastapi import APIRouter, UploadFile
from ..services.file_service import FileService
from ..services.excel_service import ExcelService

router = APIRouter(
    prefix="/excel",
    tags=["PDF 2 EXCEL"]
)


@router.post("/generate")
async def excel_generator(file : UploadFile, excel_filename: str):

    file_path = await FileService().save(file)
    excel_file_path = await ExcelService().convert(file_path, excel_filename)

    return {
       "status" : "Excel File Generated Successfully",
       "file" : excel_filename, 
       "saved_at" : excel_file_path
    }
