import fitz

path = ""
with fitz.open(
    "D:\\REPOS\\PROYECTO DE GRADO\\text-to-braille\\test_texts\\testpdf.pdf"
) as doc:
    text = ""
    for i, page in enumerate(doc):
        print("line# ", i)
        print("type: ", type(page.get_text()))
        text += page.get_text()

print(text)
