from pydantic import BaseModel
from typing import Optional

class UploadResponse(BaseModel):
    success: bool
    filename: str
    chunks_created: int
    collection: str
    message: str

class UploadRequest(BaseModel):
    mode: str
    session_id: Optional[str] = None
    incognito: bool = False