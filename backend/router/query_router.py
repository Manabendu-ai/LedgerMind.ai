from fastapi import APIRouter
from ..services.rag_service import RagService

router = APIRouter(
    prefix="/query",
    tags=['query']
)

@router.post("")
async def rag_search(query: str):
    response = RagService.get_response(query)
    return response