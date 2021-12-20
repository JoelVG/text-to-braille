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
    raise TypeError("Only strings can be converted")
  return convert(text_to_convert)


def convert_file(fileToConvert):
  if type(fileToConvert) is not str:
    raise TypeError("Please provide a valid file name")
  file = open(fileToConvert, "r")
  lines = file.readlines()
  converted_text = ''
  for line in lines:
    converted_text += convert(line)
  return converted_text  


def show_diff(str1, str2):
  import difflib as dl
  d = dl.Differ()
  diff = d.compare(str1, str2)
  print('\n'.join(diff))
  
  
def count_cap_words(i, text_to_convert):
  j = i
  while j < len(text_to_convert):
    if text_to_convert[j].isupper() or text_to_convert[j] in punctuation_marks:
      j += 1
      continue
    else:
      if j-i < 2:
        return -1
      elif text_to_convert[j].islower():
        break
  return len(text_to_convert[i:j].split(' '))-1


def get_charcaps(i, text_to_convert):
  n = count_cap_words(i, text_to_convert)
  #Case1
  if n == -1:
    return character_unicodes.get('caps')
  #CASE2
  if n < 3:
    return character_unicodes.get('caps')*2
  #CASE CASE CASE3....
  else:
  	return character_unicodes.get('pcaps')+character_unicodes.get('caps')*2
  
  
def convert(text_to_convert):
  n_chars = 0
  isNumber = False
  n_spaces = 0
  n_words = 0
  converted_text = ''
  cap_flag = 0
  for character in text_to_convert:
    n_chars += 1
    if character in escape_characters:
      converted_text += character
      continue
    #handling uppercase
    if character.isupper():
      cap_char = get_charcaps(n_chars, text_to_convert[n_chars-1:])
      n_words = len(cap_char)
      if cap_flag == 0:
        cap_flag = n_words
      if n_spaces == 0 and cap_flag == n_words:
        converted_text += cap_char
        n_spaces = count_cap_words(n_chars, text_to_convert[n_chars-1:]) 
      elif n_spaces == 1 and cap_flag == 2:
        converted_text += character_unicodes.get('caps')*2
        n_spaces = 0
      elif n_spaces == 1 and cap_flag > 2:
        converted_text += character_unicodes.get('caps')
        n_spaces = 0
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
  #   testing abc..
  # for i in character_unicodes.keys():
  #     print(f' {i}: {convert_text(str(i))}')
  # print(f'{convert_text("hola")}')
  # print(f'{convert_text("Hola")}')
  # print(f'{convert_text("HOLA")}')
  t1 = convert_text("ESTÁ PROHIBIDO FUMAR DENTRO DE LAS DEPENDENCIAS DE LA EMPRESA".lower())
  print(t1)
  t2 = convert_text("ESTÁ PROHIBIDO FUMAR DENTRO DE LAS DEPENDENCIAS DE LA EMPRESA")
  print(t2)
  show_diff(t2, t1)
