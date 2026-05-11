from bs4 import BeautifulSoup
from app.parsers.base_parser import BaseParser, ParsedDocument

class HTMLParser(BaseParser):

    def parse(self, source: str) -> ParsedDocument:
        with open(source, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        content = soup.get_text(separator="\n", strip=True)
        return ParsedDocument(
            content=content.strip(),
            metadata={"source": source, "type": "html"}
        )