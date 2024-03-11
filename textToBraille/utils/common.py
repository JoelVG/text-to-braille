from pathlib import Path
import difflib as dl


def get_extension(path: str) -> str:
    return Path(path).suffix


def show_diff(str1: str, str2: str):
    """
    Método que ayuda a mostrar las diferencias entre dos
    cadenas de texto
    """
    d = dl.Differ()
    diff = d.compare(str1, str2)
    print("TEXT 1: ", str1)
    print("TEXT 2: ", str2)
    print("DIFF: ")
    print("\n".join(diff))
