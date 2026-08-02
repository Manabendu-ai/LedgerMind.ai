import fitz

doc = fitz.open("docs/Java_Complete_Notes.pdf")
has_text = False

for page in doc:
    text = page.get_text().strip()
    if text:
        has_text = True
        break

print(has_text)