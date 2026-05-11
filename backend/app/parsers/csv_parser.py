import pandas as pd
from app.parsers.base_parser import BaseParser, ParsedDocument

class CSVParser(BaseParser):

    def parse(self, source: str) -> ParsedDocument:
        df = pd.read_csv(source)
        content = df.to_string(index=False)
        return ParsedDocument(
            content=content.strip(),
            metadata={"source": source, "type": "csv", "rows": len(df), "columns": list(df.columns)}
        )