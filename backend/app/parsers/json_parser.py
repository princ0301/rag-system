import json
from app.parsers.base_parser import BaseParser, ParsedDocument

class JSONParser(BaseParser):

    def parse(self, source: str) -> ParsedDocument:
        with open(source, "r", encoding="utf-8") as f:
            data = json.load(f)
        content = json.dumps(data, indent=2)
        return ParsedDocument(
            content=content.strip(),
            metadata={"source": source, "type": "json"}
        )