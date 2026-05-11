from app.parsers.base_parser import BaseParser, ParsedDocument

class TXTParser(BaseParser):

    def parse(self, source: str) -> ParsedDocument:
        with open(source, "r", encoding="utf-8") as f:
            content = f.read()
        return ParsedDocument(
            content=content.strip(),
            metadata={"source": source, "type": "txt"}
        ) 