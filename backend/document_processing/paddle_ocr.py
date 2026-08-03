from paddleocr import PaddleOCR
import fitz
from .parser import ParsedDocument
import numpy as np

class OCRParser:

    def __init__(self):
        self.ocr = PaddleOCR(
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False,
            lang='en'
        )

    def extract(self, file_path: str):
        doc = fitz.open(file_path)
        doc_text = []

        for page in doc:
            pix = page.get_pixmap(dpi=300)

            img = np.array(pix.pil_image())

            res = self.ocr.predict(img)

            text = ""

            for block in res:
                if "rec_texts" in block:
                    text += " ".join(block["rec_text"])
                    text += "\n"

            doc_text.append(text)

        return ParsedDocument(
            file_name=file_path,
            total_pages=len(doc),
            content="\n\n".join(doc_text)
        )

