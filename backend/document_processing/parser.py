from dataclasses import dataclass
import fitz

@dataclass
class ParsedDocument:
    file_name: str
    total_pages: int
    content: str


