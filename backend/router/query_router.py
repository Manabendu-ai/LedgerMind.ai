from fastapi import APIRouter
from ..services.rag_service import RagService

router = APIRouter(
    prefix="/query",
    tags=['query']
)

@router.post("")
async def rag_search(query: str):
    response = RagService(query).get_response()
    return response