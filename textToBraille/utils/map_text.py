"""
Serie de funciones que ayudan al manejo de los distintos
casos del uso de mayúsculas main() -> point_up
[n,m] = simulan los puntos que estarían marcados en una casilla de Braille
"""
# CASO 1
# #Hola > ϗhola | ϗ=[4,6]
# CASO 2
# #HOLA > ϐhola | ϐ=[4,6][4,6]
# #HOLA EXTRAÑO > ϐHOLA ϐEXTRAÑO
# CASO 3
# #HOLA EXTRAÑO, ESTO ES BRAILLE > λhola extraño, esto es ϗbraille | λ=[2,5][4,6][4,6]

# TEST: 'ALGUNAS PALABRAS SON GRAMATICALMENTE ERRÓNEAS.
# Pero se tiene que seguir transcribiendo'
# TEST2: 'El tiempo es un tema de reflexión tan apasionante como escurridizo'

# Caracteres especiales que se usarán para los distintos casos
CASE_CHARS = ("ϗ", "ϐ", "λ")

# Conjunto de FLAGS que ayudan al control e identificación de los distintos casos
FLAGS = {"pos_ini": 0, "pos_fin": 0, "count": 0, "case": 0}

P_MARKS = (",", ".", "-", "~", "¡", "!", "¿", "?", '"', "'", "\\", "/")


def reset_flags():
    for f in list(FLAGS.keys()):
        FLAGS[f] = 0


def clean_word(word: str) -> str:
    """
    Función que elimina los caracteres especiales del texto
    """
    for c in P_MARKS:
        if c in word:
            word = word.replace(c, "")
    return word


def is_case_one(word: str) -> bool:
    """
    Función que identifica si el texto está en formato para el Caso 1
    Caso 1: Primera letra mayúscula, resto minúscula
    Ejm: Hola > ϗhola >> ⠨⠓⠕⠇⠁
    ϗ: representa los puntos 4 y 6.
    """
    return word[0].isupper() and word[1:].islower() if word != "" else False


def is_case_two(word: str) -> bool:
    return word.isupper()


def all_up_case(text: str, n_words: int) -> str:
    """
    Función que devuelve el texto en formato para el Caso 4
    Caso 4: Más de 2 palabras consecutivas en mayúscula
    Ejm: NECESITAS ORDERNAR TU CÓDIGO! > λnecesitas ordenar tu ϗcódigo!
    >> ⠒⠨⠨⠝⠑⠉⠑⠎⠊⠞⠁⠎ ⠕⠗⠙⠑⠗⠝⠁⠗ ⠞⠥ ⠨⠉⠬⠙⠊⠛⠕⠖
    λ: representa los puntos [2,5][4,6][4,6].
    ϗ: representa los puntos 4 y 6.
    """
    map_text = CASE_CHARS[2]
    for i, word in enumerate(text.split()):
        if i < n_words - 1:
            map_text += word + " "
        elif i == n_words - 1:
            map_text += CASE_CHARS[0] + word + " "
    return map_text.lower()


def render_case(words: str, case: int):
    """
    Función que renderiza el caso actual. Se llama cada que
    se identifica un nuevo caso
    """
    if case <= 2:
        render = "".join(CASE_CHARS[1] + word + " " for word in words)
    elif case > 2:
        render = all_up_case(" ".join(words), len(words))
    return render


def point_up(text: str) -> str:
    """
    Función que mapea el texto con los caracteres especiales ('ϗ','ϐ','λ')
    dependiendo del caso que se trata.
    """
    n_words = len(text.split())
    # Filtro para texto en mayúscula y minúscula
    if all(w.isupper() for w in (t for t in text.split())) and n_words > 2:
        return all_up_case(text, n_words)
    else:
        if all(w.islower() for w in (t for t in text.split())):
            return text

    result_text = ""
    words = text.split()
    for i, word in enumerate(words):
        if is_case_one(
            clean_word(word)
        ):  # No se renderiza como los demás porque es un caso trivial
            if FLAGS["case"] == 2:
                result_text += render_case(
                    words[FLAGS["pos_ini"] : FLAGS["pos_fin"] + 1], FLAGS["count"]
                )
                reset_flags()
            result_text += CASE_CHARS[0] + word + " "
        elif is_case_two(clean_word(word)):
            if FLAGS["case"] == 0:
                FLAGS["case"] = 2
                FLAGS["pos_ini"] = FLAGS["pos_fin"] = i
                FLAGS["count"] += 1
            # Segunda palabra en mayúscula repetida, es como el caso 3
            # por eso pos_fin cambia a la posición de la segunda palabra
            elif FLAGS["case"] == 2:
                FLAGS["count"] += 1
                FLAGS["pos_fin"] = i
            else:
                result_text += render_case(
                    words=words[FLAGS["pos_ini"] : FLAGS["pos_fin"] + 1],
                    case=FLAGS["count"],
                )
                reset_flags()
        else:
            if FLAGS["case"] == 2:
                result_text += render_case(
                    words[FLAGS["pos_ini"] : FLAGS["pos_fin"] + 1], FLAGS["count"]
                )
                reset_flags()
            result_text += word + " "

    if FLAGS["case"] != 0:
        result_text += render_case(
            words[FLAGS["pos_ini"] : FLAGS["pos_fin"] + 1], FLAGS["count"]
        )
    return result_text.lower().strip()
