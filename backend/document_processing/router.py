from .metrics import Metrcis, DocumentMetrics
from .models import DocumentType


class DocumentRouter:

    def classify_document(self, file_path: str):
        metrics = Metrcis().get_metrcis(file_path)
        if metrics['total_words'] > 50 and metrics['total_characters'] > 300:
            metrics["document_type"] = DocumentType.DIGITAL
        else:
            metrics["document_type"] = DocumentType.SCANNED
        return DocumentMetrics(metrics)