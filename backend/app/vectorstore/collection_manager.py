from langchain_chroma import Chroma
from app.vectorstore.chroma_store import get_persistent_store, get_ephemeral_store

def get_store(mode: str, incognito: bool, session_id: str = None) -> Chroma:
    if mode == "quick_chat" or incognito:
        return get_ephemeral_store(session_id or "default")
    return get_persistent_store()

def add_documents(store: Chroma, chunks: list[dict]) -> int:
    texts = [c["content"] for c in chunks]
    metadatas = [c["metadata"] for c in chunks]
    store.add_texts(texts=texts, metadatas=metadatas)
    return len(texts)

def delete_source(source_name: str) -> bool:
    store = get_persistent_store()
    results = store.get(where={"source": source_name})
    if not results["ids"]:
        return False
    store.delete(ids=results["ids"])
    return True

def get_kb_stats() -> dict:
    store = get_persistent_store()
    results = store.get()
    sources = {}
    for metadata in results["metadatas"]:
        src = metadata.get("source", "unknown")
        sources[src] = sources.get(src, 0) + 1
    return {
        "total_chunks": len(results["ids"]),
        "sources": sources
    }