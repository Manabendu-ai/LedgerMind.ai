import fitz

doc = fitz.open("docs/Java_Complete_Notes.pdf")
has_text = False

for i,page in enumerate(doc):
    text = page.get_text().strip()
    print(f"\n--------Page {i+1}------")
    print(repr(text[:500]))
    

