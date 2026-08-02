from document_processing.router import DocumentRouter

router = DocumentRouter()

result = router.classify_document("docs/Java_Complete_Notes.pdf")

print(result)