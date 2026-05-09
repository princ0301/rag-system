from fastapi import APIRouter
from app.models.chat_models import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    return ChatResponse(
        answer="Phase 2 placeholder",
        sources=[],
        mode=request.mode,
        incognito=request.incognito
    )