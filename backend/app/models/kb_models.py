from pydantic import BaseModel

class KbSource(BaseModel):
    id: str
    filename: str
    file_type: str
    chunks: int
    uploaded_at: str

class KBStatsResponse(BaseModel):
    total_sources: int
    total_chunks: int
    sources: list[KbSource]

class DeleteResponse(BaseModel):
    success: bool
    message: str
    