from langchain_chroma import Chroma
from app.embeddings.embedder import Embedder
from app.config import settings

embedder = Embedder()

def get_persistent_store() -> Chroma:
    return Chroma(
        collection_name=settings.chroma_collection_name,
        embedding_function=embedder.get_model(),
        persist_directory=settings.chroma_persist_dir
    )

def get_ephemeral_store(session_id: str) -> Chroma:
    return Chroma(
        collection_name=f"session_{session_id}",
        embedding_function=embedder.get_model()
    )