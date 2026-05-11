from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload, chat, kb, database
from app.parsers.parser_factory import get_parser, is_supported
from app.vectorstore.collection_manager import add_documents, get_kb_stats
from app.embeddings.chunker import Chunker
from app.parsers.base_parser import ParsedDocument

app = FastAPI(title="RAG System", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(chat.router)
app.include_router(kb.router)
app.include_router(database.router)

@app.get("/")
def root():
    return {"status": "ok", "message": "RAG System running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/test-parsers")
def test_parsers():
    return {
        "pdf":  is_supported("test.pdf"),
        "docx": is_supported("test.docx"),
        "csv":  is_supported("test.csv"),
        "url":  is_supported("https://example.com"),
        "mp3":  is_supported("test.mp3"),
    }

@app.get("/test-vectorstore")
def test_vectorstore():
    doc = ParsedDocument(
        content="LangChain is a framework for building LLM applications. It supports many providers.",
        metadata={"source": "test.txt", "type": "txt"}
    )
    chunker = Chunker()
    chunks = chunker.split(doc)
    from app.vectorstore.chroma_store import get_persistent_store
    store = get_persistent_store()
    count = add_documents(store, chunks)
    stats = get_kb_stats()
    return {"chunks_added": count, "kb_stats": stats}