from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
from app.models.upload_models import UploadResponse

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/", response_model=UploadResponse)
async def upload_file(
    file: UploadFile = File(...),
    mode: str = Form(...),
    session_id: Optional[str] = Form(None),
    incognito: bool = Form(False)
):
    return UploadResponse(
        success=True,
        filename=file.filename,
        chunks_created=0,
        collections="placeholder",
        message="Phase 2 Placeholder"
    )