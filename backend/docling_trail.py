import os

os.environ["CUDA_VISIBLE_DEVICES"] = ""


from docling.document_converter import DocumentConverter

converter = DocumentConverter()

result = converter.convert("docs/1000073988.pdf")

document = result.document
markdown_output = document.export_to_markdown()
json_output = document.export_to_dict()

