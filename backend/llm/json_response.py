from pydantic import BaseModel, Field
from typing import Any

class JsonFormatResponse(BaseModel):
    content: dict = Field(description="Json Object from the Extracted Data")