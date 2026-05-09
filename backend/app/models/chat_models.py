from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    question: str
    mode: str
    session_id: Optional[str] = False
    incognito: bool = False

class SourceReference(BaseModel):
    source: str
    chunk: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[SourceReference]
    mode: str
    incognito: bool