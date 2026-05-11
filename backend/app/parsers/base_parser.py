from abc import ABC, abstractclassmethod

class ParsedDocument:

    def __init__(self, content: str, metadata: dict):
        self.content = content
        self.metadata = metadata

class BaseParser(ABC):
    @abstractclassmethod
    def parse(self, source: str) -> ParsedDocument:
        pass
    