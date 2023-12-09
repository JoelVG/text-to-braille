import fitz

path = ""
with fitz.open("D:/Repos/text-to-braille/docs/data/test2.pdf") as doc:
    text = ""
    for i, page in enumerate(doc):
        print("line# ", i)
        print("type: ", type(page.get_text()))
        text += page.get_text()

print(text)
