import os
import shutil
import uuid
from app.parsers.parser_factory import get_parser, is_supported
from app.embeddings.chunker import Chunker
from app.vectorstore.collection_manager import get_store, add_documents

TEMP_DIR = "./temp_uploads"
os.makedirs(TEMP_DIR, exist_ok=True)

chunker = Chunker()

def process_upload(file_path: str, filename: str, mode: str, session_id: str, incognito: bool) -> dict:
    if not is_supported(filename):
        raise ValueError(f"Unsupported file type: {filename}")

    parser = get_parser(filename)
    document = parser.parse(file_path)

    document.metadata["source"] = filename

    if not document.content.strip():
        raise ValueError("No text content extracted from file")

    chunks = chunker.split(document)

    store = get_store(mode=mode, incognito=incognito, session_id=session_id)
    count = add_documents(store, chunks)

    collection_name = f"session_{session_id}" if (mode == "quick_chat" or incognito) else "kb_persistent"

    return {
        "filename": filename,
        "chunks_created": count,
        "collection": collection_name
    }