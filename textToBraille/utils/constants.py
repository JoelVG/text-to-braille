# https://www.fileformat.info/info/unicode/block/braille_patterns/list.htm
# λ=[2,5][4,6][4,6]
# ϐ=[4,6][4,6]
# ϗ=[4,6]
# ɳ = [3,4,5,6]

# Notas:
# - No se tiene registro en braille para los caracteres: #, @, ^, &, _, `, ~
CHARACTERS_UNICODE = {
    "a": "\u2801",
    "b": "\u2803",
    "c": "\u2809",
    "d": "\u2819",
    "e": "\u2811",
    "f": "\u280B",
    "g": "\u281B",
    "h": "\u2813",
    "i": "\u280A",
    "j": "\u281A",
    "k": "\u2805",
    "l": "\u2807",
    "m": "\u280D",
    "n": "\u281D",
    "ñ": "\u283B",
    "o": "\u2815",
    "p": "\u280F",
    "q": "\u281F",
    "r": "\u2817",
    "s": "\u280E",
    "t": "\u281E",
    "u": "\u2825",
    "v": "\u2827",
    "w": "\u283A",
    "x": "\u282D",
    "y": "\u283D",
    "z": "\u2835",
    "ϗ": "\u2828",
    ".": "\u2832",
    "'": "\u2820",
    '"': "\u2826",
    ",": "\u2802",
    "-": "\u2824",
    "/": "\u280C",
    "¡": "\u2816",
    "!": "\u2816",
    "?": "\u2822",
    "¿": "\u2822",
    "$": "\u2832",
    ":": "\u2812",
    ";": "\u2830",
    "(": "\u2836",
    ")": "\u2836",
    " ": " ",
    "1": "\u2801",
    "2": "\u2803",
    "3": "\u2809",
    "4": "\u2819",
    "5": "\u2811",
    "6": "\u280B",
    "7": "\u281B",
    "8": "\u2813",
    "9": "\u280A",
    "0": "\u281A",
    "á": "\u2837",
    "é": "\u282E",
    "í": "\u280C",
    "ó": "\u282C",
    "ú": "\u283E",
    "ü": "\u2833",
    "+": "\u2816",
    "*": "\u2814",
    # "/": "\u2832",
    "%": "\u2832",
    "=": "\u2836",
    "pcaps": "\u2812",
    "ϐ": "\u2828" * 2,
    "λ": "\u2812" + "\u2828" * 2,
    "ɳ": "\u283C",
}

NUMBER_PUNCTUATIONS = (".", ",", "-", "/", "$")

PUNCTUATION_MARKS = (
    ",",
    "-",
    "!",
    "¡",
    "¿",
    "?",
    ":",
    "(",
    ")",
    ";",
    ".",
    '"',
    "'",
    " ",
)

ESCAPE_CHARACTERS = ["\n", "\r", "\t"]

BRAILLE_UNICODE = dict((v, k) for k, v in CHARACTERS_UNICODE.items())

# Representación en braille de los distintos casos
SPECIAL_MARKS = ("⠨", "⠨⠨", "⠒⠨⠨", "⠼")

# Caracteres especiales que se usarán para los distintos casos
CASE_CHARS = ("ϗ", "ϐ", "λ", "ɳ")

# Conjunto de FLAGS que ayudan al control e identificación de los distintos casos
FLAGS = {"pos_ini": 0, "pos_fin": 0, "count": 0, "case": 0}

P_MARKS = (",", ".", "-", "~", "¡", "!", "¿", "?", '"', "'", "\\", "/")
