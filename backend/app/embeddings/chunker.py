from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.parsers.base_parser import ParsedDocument

class Chunker:
    def __init__(self, chunk_size: int = 1500, chunk_overlap: int = 300):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ".", " ", ""]
        )

    def split(self, document: ParsedDocument) -> list[dict]:
        chunks = self.splitter.split_text(document.content)
        return [
            {"content": chunk, "metadata": document.metadata}
            for chunk in chunks
        ]