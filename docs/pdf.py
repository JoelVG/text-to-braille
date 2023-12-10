import fitz

path = ""
with fitz.open("/text-to-braille/docs/data/test2.pdf") as doc:
    text = ""
    for i, page in enumerate(doc):
        print("PAGE# ", i)
        text = page.get_text()
        print(text)

        # text += page.get_text()

# print(text)
