from app.parsers.pdf_parser import PDFParser
from app.parsers.docx_parser import DOCXParser
from app.parsers.txt_parser import TXTParser
from app.parsers.csv_parser import CSVParser
from app.parsers.json_parser import JSONParser
from app.parsers.html_parser import HTMLParser
from app.parsers.url_parser import URLParser
from app.parsers.base_parser import BaseParser

SUPPORTED_EXTENSIONS = {
    ".pdf": PDFParser,
    ".docx": DOCXParser,
    ".txt": TXTParser,
    ".md": TXTParser,
    ".csv": CSVParser,
    ".json": JSONParser,
    ".html": HTMLParser,
    ".htm": HTMLParser,
}

def get_parser(filename: str) -> BaseParser:
    if filename.startswith("http://") or filename.startswith("https://"):
        return URLParser()
    ext = "." + filename.split(".", 1)[-1].lower()
    if ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {ext}")
    return SUPPORTED_EXTENSIONS[ext]()

def is_supported(filename: str) -> bool:
    if filename.startswith("http://") or filename.startswith("https://"):
        return True
    ext = "." + filename.rsplit(".", 1)[-1].lower()
    return ext in SUPPORTED_EXTENSIONS