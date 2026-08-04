from fastapi import APIRouter, UploadFile


router = APIRouter(
    prefix="/excel",
    tags=["PDF 2 EXCEL"]
)


# @router.post("/generate")
# async def excel_generator(file : UploadFile):

#     file_path = await FileService().save(file)
