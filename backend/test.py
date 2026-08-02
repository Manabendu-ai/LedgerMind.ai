from document_processing.router import DocumentRouter

router = DocumentRouter()

result = router.classify_document("docs/LeetCode Java Practice Solved Questions.pdf")

print(result)