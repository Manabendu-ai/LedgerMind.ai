from .metrics import Metrics, DocumentMetrics
from .models import DocumentType


class DocumentRouter:

    def classify_document(self, file_path: str):
        metrics = Metrics().get_metrics(file_path)
        if metrics['total_words'] > 50 and metrics['total_characters'] > 300:
            doc_type = DocumentType.DIGITAL
        else:
            doc_type = DocumentType.SCANNED
        return DocumentMetrics(
            total_pages=metrics["total_pages"],
            total_words=metrics["total_words"],
            total_characters=metrics["total_characters"],
            avg_words_per_page=metrics["avg_words_per_page"],
            avg_characters_per_page=metrics["avg_characters_per_page"],
            document_type=doc_type
        )