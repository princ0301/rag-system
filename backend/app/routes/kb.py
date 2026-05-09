from fastapi import APIRouter
from app.models.kb_models import KBStatsResponse, DeleteResponse

router = APIRouter(prefix="/kb", tags=["knowledge-base"])

@router.get("/", response_model=KBStatsResponse)
async def get_kb_status():
    return KBStatsResponse(
        total_sources=0,
        total_chunks=0,
        sources=[]
    )

@router.delete("/{source_id}", response_model=DeleteResponse)
async def delete_source(source_id: str):
    return DeleteResponse(
        success=True,
        message=f"Source {source_id} deleted"
    )