character_unicodes = {'a': '\u2801', 'b': '\u2803', 'k': '\u2805', 'l': '\u2807', 'c': '\u2809', 'i': '\u280A',
'f': '\u280B', 'm': '\u280D', 's': '\u280E', 'p': '\u280F', 'e': '\u2811', 'h': '\u2813', 'o': '\u2815', 'r': '\u2817',
'd': '\u2819', 'j': '\u281A', 'g': '\u281B', 'n': '\u281D', 't': '\u281E', 'q': '\u281F', 'u': '\u2825', 'v': '\u2827',
'x': '\u282D', 'z': '\u2835', 'w': '\u283A', 'y': '\u283D', 'num': '\u283C', 'caps': '\u2828', '.': '\u2832',
"'": '\u2804', ',': '\u2802', '-': '\u2824', '/': '\u280C', '!' : '\u2816', '?': '\u2826', '$': '\u2832', ':': '\u2812',
';': '\u2830', '(': '\u2836', ')': '\u2836', ' ': ' ', '1': '\u2801', '2': '\u2803', '3': '\u2809', '4': '\u2819',
'5': '\u2811', '6': '\u280B', '7': '\u281B', '8': '\u2813', '9': '\u280A', '0': '\u281A', 'á': '\u2837', 'é': '\u282E', 'í': '\u280C',
'ó': '\u282C', 'ú': '\u283E', 'ü': '\u2833', 'ñ': '\u283B', '+': '\u2816', '-': '\u2824', '*': '\u2826','/': '\u2832',
'%': '\u2832', '=': '\u2836', 'pcaps': '\u2812'}

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
  with open(file_to_convert) as f:
    converted_text += convert(f.readline())
  return converted_text


def show_diff(str1, str2):
  import difflib as dl
  d = dl.Differ()
  diff = d.compare(str1, str2)
  print('\n'.join(diff))

#TODO usar map_text para mapear text_to_convert con los caracteres especiales
#TODO agregar caracteres especiales para mayúsculas a character_unicodes
def convert(text_to_convert):
  isNumber = False
  converted_text = ''
  for character in text_to_convert:
    if character in escape_characters:
      converted_text += character
      continue
    character = character.lower()
    if character.isdigit():
      if not isNumber:
        isNumber = True
        converted_text += character_unicodes.get('num')
    else:
      if isNumber and character not in number_punctuations:
        isNumber = False
    if n_spaces != 0 and character == ' ':
        n_spaces -= 1
    elif n_spaces == 1 and cap_flag > 2:
      converted_text += character_unicodes.get('caps')
      n_spaces = 0
      cap_flag = 0
    elif n_spaces == 1 and cap_flag == 2:
      n_spaces = 0
      cap_flag = 0
    if character == ' ':
      converted_text += '|'  
    else:
      converted_text += character_unicodes.get(character)
  return converted_text


if __name__ == '__main__':
  t1 = convert_text("ESTÁ PROHIBIDO FUMAR DENTRO DE LAS DEPENDENCIAS DE LA EMPRESA".lower())
  print(t1)
  t2 = convert_text("ESTÁ PROHIBIDO FUMAR DENTRO DE LAS DEPENDENCIAS DE LA EMPRESA")
  print(t2)
  show_diff(t2, t1)