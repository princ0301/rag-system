from fastapi import APIRouter
from app.models.chat_models import ChatRequest, ChatResponse, SourceReference
from app.vectorstore.collection_manager import get_store
from app.rag.pipeline import run_pipeline

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    store = get_store(
        mode=request.mode,
        incognito=request.incognito,
        session_id=request.session_id
    )

    result = run_pipeline(store=store, question=request.question)

    return ChatResponse(
        answer=result["answer"],
        sources=[SourceReference(**s) for s in result["sources"]],
        mode=request.mode,
        incognito=request.incognito
    )