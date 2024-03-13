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


def print_parameters(func):
    """
    Decorador que imprime los parámetros de una función.
    """

    def wrapper(*args, **kwargs):
        print("Function:", func.__name__)

        # Print positional arguments
        if args:
            print("Positional Arguments:")
            for i, arg in enumerate(args):
                print(f"  {i + 1}. {arg}")

        # Print keyword arguments
        if kwargs:
            print("Keyword Arguments:")
            for key, value in kwargs.items():
                print(f"  {key}: {value}")

        # Call the original function
        return func(*args, **kwargs)

    return wrapper
