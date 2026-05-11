import requests
from bs4 import BeautifulSoup
from app.parsers.base_parser import BaseParser, ParsedDocument

class URLParser(BaseParser):

    def parse(self, source: str) -> ParsedDocument:
        response = requests.get(source, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        content = soup.get_text(separator="\n", strip=True)
        return ParsedDocument(
            content=content.strip(),
            metadata={"source": source, "type": "url"}
        )