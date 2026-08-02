from dataclasses import dataclass
import fitz

@dataclass
class ParsedDocument:
    file_name: str
    total_pages: int
    content: str


class PDFParser:

    def parse(self, file_path: str)->ParsedDocument:
        doc = fitz.open(file_path)

        pages = []
        for page in doc:
            text = page.get_text()
            if text.strip():
                pages.add(text)

        file_content = "\n\n".join(pages)
        return ParsedDocument(
            file_name=file_path,
            total_pages=len(doc),
            content=file_content
        )
