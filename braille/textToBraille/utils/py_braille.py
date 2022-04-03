from textToBraille.utils.map_text import point_up
from pathlib import Path
import codecs

character_unicodes = {
  'a': '\u2801', 'b': '\u2803', 'c': '\u2809', 'd': '\u2819', 'e': '\u2811', 'f': '\u280B', 'g': '\u281B', 'h': '\u2813', 'i': '\u280A',
  'j': '\u281A', 'k': '\u2805', 'l': '\u2807', 'm': '\u280D', 'n': '\u281D', 'ñ': '\u283B', 'o': '\u2815', 'p': '\u280F', 'q': '\u281F',
  'r': '\u2817', 's': '\u280E', 't': '\u281E', 'u': '\u2825', 'v': '\u2827', 'w': '\u283A', 'x': '\u282D', 'y': '\u283D', 'z': '\u2835',
  'num': '\u283C', 'ϗ': '\u2828', '.': '\u2832', "'": '\u2820', '"': '\u2826', ',': '\u2802', '-': '\u2824', '/': '\u280C', '¡' : '\u2816', 
  '!' : '\u2816', '?': '\u2822',  '¿': '\u2822', '$': '\u2832', ':': '\u2812', ';': '\u2830', '(': '\u2836', ')': '\u2836', ' ': ' ',
  '1': '\u2801', '2': '\u2803', '3': '\u2809', '4': '\u2819', '5': '\u2811', '6': '\u280B', '7': '\u281B', '8': '\u2813', '9': '\u280A', '0': '\u281A',
  'á': '\u2837', 'é': '\u282E', 'í': '\u280C', 'ó': '\u282C', 'ú': '\u283E', 'ü': '\u2833', '+': '\u2816', '-': '\u2824', '*': '\u2814',
  '/': '\u2832', '%': '\u2832', '=': '\u2836', 'pcaps': '\u2812', 'ϐ': '\u2828'*2, 'λ': '\u2812'+'\u2828'*2,
}
# https://www.fileformat.info/info/unicode/block/braille_patterns/list.htm
# λ=[2,5][4,6][4,6]
# ϐ=[4,6][4,6]
# ϗ=[4,6]

number_punctuations = ['.', ',', '-', '/', '$']
punctuation_marks = [',', '-', '!', '¡', '¿', '?', ':', '(', ')', ';', '.', '"', "'", ' ']
escape_characters = ['\n', '\r', '\t']

def convert_text(text_to_convert):
  if type(text_to_convert) is not str:
    raise TypeError("¡Solo texto puede ser convertido!")
  return convert(text_to_convert)


def convert_file(file_to_convert):
  if type(file_to_convert) is not str:
    raise TypeError("Nombre de archivo incorrecto")
  converted_text = ''
  # Path(file_to_convert) tal vez se use para los paths de windows
  with codecs.open(file_to_convert, encoding='utf-8') as f:
    for line in f:
      converted_text += convert(line)
  return converted_text


def show_diff(str1, str2):
  '''
  Método que ayuda a mostrar las diferencias entre dos
  cadenas de texto
  '''
  import difflib as dl
  d = dl.Differ()
  diff = d.compare(str1, str2)
  print('\n'.join(diff))


def convert(text_to_convert):
  is_number = False
  converted_text = ''
  marked_text = point_up(text_to_convert)
  for character in marked_text:
    if character in escape_characters:
      converted_text += character
      continue
    character = character.lower()
    if character.isdigit():
      if not is_number:
        is_number = True
        converted_text += character_unicodes.get('num')
    else:
      if is_number and character not in number_punctuations:
        is_number = False
    if character == ' ':
      converted_text += ' ' # | para remarcar (en tests) que existe un espacio, luego reemplazar solo por ' ' 
    else:
      try:
        converted_text += character_unicodes.get(character)
      except TypeError:
        print("Caracter no encontrado: ", character)
  return converted_text


# if __name__ == '__main__':
  # t1 = convert_text("ESTÁ PROHIBIDO FUMAR DENTRO DE LAS DEPENDENCIAS DE LA EMPRESA".lower())
  # print(t1)
  # t2 = convert_text("ESTÁ PROHIBIDO FUMAR DENTRO DE LAS DEPENDENCIAS DE LA EMPRESA")
  # show_diff(t2, t1)
  # print(convert_file("D:\\REPOS/PROYECTO DE GRADO\\text-to-braille\\test_texts\\t1.txt"))