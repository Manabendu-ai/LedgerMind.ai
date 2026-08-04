from fastapi import APIRouter, UploadFile

router = APIRouter(
    prefix="/excel",
    tags=["PDF 2 EXCEL"]
)


@router.post("/generate")
async def excel_generator(file : UploadFile, filename: str):

    file_path = await FileService().save(file)
    excel_file_path = await ExcelService().convert(file_path, filename)

    return {
       "status" : "Excel File Generated Successfully",
       "file" : filename, 
       "saved_at" : excel_file_path
    }
