from typing import Any
from pydantic import BaseModel


class Worksheet(BaseModel):
    worksheet_name: str
    columns: list[str]
    rows: list[list[Any]]


class Workbook(BaseModel):
    worksheets: list[Worksheet]


class JsonFormatResponse(BaseModel):
    document_type: str
    workbook: Workbook