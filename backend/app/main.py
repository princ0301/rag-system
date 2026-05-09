from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload, chat, kb, database

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