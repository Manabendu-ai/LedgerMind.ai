from document_processing.router import DocumentRouter
from document_processing.processor import DocumentProcessor

# router = DocumentRouter()

# result = router.classify_document("docs/LeetCode Java Practice Solved Questions.pdf")

# print(result)

document_processor = DocumentProcessor()
result = document_processor.extract_text("docs/1000073988.pdf")
print(result.total_pages)
print(result.content)