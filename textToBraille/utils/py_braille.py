from textToBraille.utils.map_text import point_up
from textToBraille.utils.constants import (
    CHARACTERS_UNICODE,
    NUMBER_PUNCTUATIONS,
    ESCAPE_CHARACTERS,
    BRAILLE_UNICODE,
    SPECIAL_MARKS,
)
from pathlib import Path
import fitz  # PyMuPDF


def convert_text(text_to_convert):
    if type(text_to_convert) is not str:
        raise TypeError("¡Solo texto puede ser convertido!")
    return convert(text_to_convert)


def get_extension(path: str) -> str:
    return Path(path).suffix


def convert_file(file_to_convert: str) -> str:
    """
    Función que recibe un texto en formato .txt
    o .pdf y devuelve la transcripción a Braille del mismo.
    """
    if type(file_to_convert) is not str:
        return None
    ext = get_extension(file_to_convert)
    converted_text = ""
    if ext == ".txt":
        with open(file_to_convert, encoding="utf-8") as f:
            for line in f:
                converted_text += convert(line)
    elif ext == ".pdf":
        with fitz.open(file_to_convert) as doc:
            for page in doc:
                converted_text += convert(page.get_text())
    else:
        converted_text = None
    return converted_text


def show_diff(str1: str, str2: str):
    """
    Método que ayuda a mostrar las diferencias entre dos
    cadenas de texto
    """
    import difflib as dl

    d = dl.Differ()
    diff = d.compare(str1, str2)
    print("\n".join(diff))


def convert(text_to_convert: str) -> str:
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
            # | para remarcar (en tests) que existe un espacio,
            # luego reemplazar solo por ' '
            converted_text += " "
        else:
            try:
                converted_text += CHARACTERS_UNICODE.get(character)
            except TypeError:
                print("Caracter no encontrado: ", character)
    return converted_text


def braille_to_text(text: str) -> str:
    case = 0
    translated_text = ""
    for word in text:
        word = lookup_braille(word)
        if case == 2:
            word = word.upper()
            case = 0
        if case == 3:
            if "⠨" in word:  # Última palabra en mayúsculas
                word = word.replace("⠨", "").upper()
                case = 0
            else:
                word = word.upper()
        if "⠨" in word:  # Caso 1
            word = word.replace("⠨", "").capitalize()
        elif "⠨⠨" in word:  # Caso 2
            case = 2
            word = word.replace("⠨⠨", "").upper()
        elif "⠒⠨⠨" in word:
            case = 3
            word = word.replace("⠨⠨", "").upper()
        translated_text += word
        print(translated_text)
    return translated_text


def lookup_braille(braille_text: str) -> str:
    """
    Busca caracter por caracter de un texto en braille en el mapping
    actual de caracteres con el que se trabaja.
    """
    word = ""
    for c in braille_text:
        if c not in SPECIAL_MARKS:
            character = BRAILLE_UNICODE.get(c)
            if character:
                word += character
            else:
                raise ValueError(f"Caracter {c} no encontrado en el mapping actual.")
        else:
            word += c
    return word


print(braille_to_text("⠨⠓⠕⠇⠁"))
# print(convert("NECESITAS ORDERNAR TU CÓDIGO! "))
# if __name__ == '__main__':
# t1 = convert_text("ESTÁ PROHIBIDO FUMAR".lower())
# print(t1)
# t2 = convert_text("ESTÁ PROHIBIDO FUMAR")
# show_diff(t2, t1)
