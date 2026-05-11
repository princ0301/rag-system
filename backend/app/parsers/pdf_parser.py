import fitz
from app.parsers.base_parser import BaseParser, ParsedDocument

class PDFParser(BaseParser):

    def parse(self, source: str) -> ParsedDocument:
        doc = fitz.open(source)
        content = ""
        for page in doc:
            content += page.get_text()
        doc.close()
        return ParsedDocument(
            content=content.strip(),
            metadata={"source": source, "type": "pdf"}
        )