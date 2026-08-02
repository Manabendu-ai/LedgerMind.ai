import fitz

doc = fitz.open("docs/Java_Complete_Notes.pdf")
total_words = 0

for i,page in enumerate(doc):
    text = page.get_text().strip()
    total_words += len(text.split())

print(total_words)

if total_words > 50:
    print("Digital PDF")

else:
    print("Scanned PDF")
    

