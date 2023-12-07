from textToBraille.utils.map_text import point_up
from textToBraille.utils.constants import (
    CHARACTERS_UNICODE,
    NUMBER_PUNCTUATIONS,
    ESCAPE_CHARACTERS,
)
from pathlib import Path
import codecs
import fitz


def convert_text(text_to_convert):
    if type(text_to_convert) is not str:
        raise TypeError("¡Solo texto puede ser convertido!")
    return convert(text_to_convert)


def get_extension(path: str):
    return Path(path).suffix


def convert_file(file_to_convert: str):
    """
    Función que recibe un texto en formato .txt
    o .pdf y devuelve la transcripción del mismo
    """
    if type(file_to_convert) is not str:
        return None
    ext = get_extension(file_to_convert)
    converted_text = ""
    if ext == ".txt":
        with codecs.open(file_to_convert, encoding="utf-8") as f:
            for line in f:
                converted_text += convert(line)
    elif ext == ".pdf":
        with fitz.open(file_to_convert) as doc:
            for page in doc:
                converted_text += convert(page.get_text())
    else:
        converted_text = None
    return converted_text


def show_diff(str1, str2):
    """
    Método que ayuda a mostrar las diferencias entre dos
    cadenas de texto
    """
    import difflib as dl

    d = dl.Differ()
    diff = d.compare(str1, str2)
    print("\n".join(diff))


def convert(text_to_convert: str):
    """
    Función que se encarga de la converción
    de texto a Braille
    """
    is_number = False
    converted_text = ""
    marked_text = point_up(text_to_convert)
    for character in marked_text:
        if character in ESCAPE_CHARACTERS:
            converted_text += character
            continue
        character = character.lower()
        if character.isdigit():
            if not is_number:
                is_number = True
                converted_text += CHARACTERS_UNICODE.get("num")
        else:
            if is_number and character not in NUMBER_PUNCTUATIONS:
                is_number = False
        if character == " ":
            # | para remarcar (en tests) que existe un espacio, luego reemplazar solo por ' '
            converted_text += " "
        else:
            try:
                converted_text += CHARACTERS_UNICODE.get(character)
            except TypeError:
                print("Caracter no encontrado: ", character)
    return converted_text


# if __name__ == '__main__':
# t1 = convert_text("ESTÁ PROHIBIDO FUMAR DENTRO DE LAS DEPENDENCIAS DE LA EMPRESA".lower())
# print(t1)
# t2 = convert_text("ESTÁ PROHIBIDO FUMAR DENTRO DE LAS DEPENDENCIAS DE LA EMPRESA")
# show_diff(t2, t1)
# print(convert_file("D:\\REPOS/PROYECTO DE GRADO\\text-to-braille\\test_texts\\t1.txt"))
# print(get_extension("D:\\REPOS/PROYECTO DE GRADO\\text-to-braille\\test_texts\\t1.txt"))
