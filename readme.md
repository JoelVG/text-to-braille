# PROTOTIPO PARA LA TRANSCRIPCIÓN DE TEXTO A BRAILLE

El prototipo de este transcriptor está enfocado para Braille de grado 1, se aplica criterios de abreviación de palabras según las reglas del Braille boliviano y se considera únicamente la transcripción del lenguaje Español.

## Objetivos
- La herramienta permitirá la transcripción de libros digitales al sistema Braille de Grado 1.
- Los documentos se restringen a aquellos con complejidad mínima para el aprendizaje del sistema Braille.
- El idioma que se manejará para la transcripción será únicamente el español y Braille adoptado en Bolivia.
- El manejo de esta herramienta no está contemplado para personas invidentes.
- Se contempla la transcripción únicamente de textos cortos de hasta 1000 palabras.

## Reglas de transcripción para los distintos casos de palabras en mayúsculas
Se identificaron ciertos casos para optimizar el espacio en la escritura del sistema Braille de grado 1.
En el siguiente cuadro se muestran los mismos:

| Caso | Texto | Braille |
| ------ | ------ | ------ |
| Caso 1 | Hola | ⠨⠓⠕⠇⠁ |
| Caso 2 | HOLA | ⠨⠨⠓⠕⠇⠁ |
| Caso 3 | HOLA EXTRAÑO | ⠨⠨⠓⠕⠇⠁ ⠨⠨⠑⠭⠞⠗⠁⠻⠕ |
| Caso 4 | HOLA AMIGOS, ¿CÓMO ESTÁN? | ⠒⠨⠨⠓⠕⠇⠁ ⠁⠍⠊⠛⠕⠎⠂ ⠢⠉⠬⠍⠕ ⠨⠑⠎⠞⠷⠝⠢ |

- Caso 1: Se tiene la primera letra en mayúscula donde se aplica el caracter especial `⠨` para denotar
que la primera letra de la palabra inicia con mayúscula.
- Caso 2 y 3: Se tiene `una` o `dos` palabras completas en mayúscula y se aplica los caracteres `⠨⠨` al inicio 
de la o las palabras para dicho caso.
- Caso 4: Cuando se tiene 3 o más palabras completas en mayúscula se aplian los caracteres `⠒⠨⠨` al inicio
de la primera palabra que lleva la frase y a inicios de la última palabra los caracteres `⠨` para concluir o cerrar.

## Endpoints
```
POST /api/text/       Crea una "traducción" de un texto que se le pasa.
GET	 /api/text/{id}   Muestra el texto original y su equivalente en Braille.
GET	 /api/file/	      Recibe el path de un archivo .txt o .pdf, extrae y devuelve su equivalente en Braille.
```


## Correr el proyecto
### Docker
Tener el docker corriendo
Ejecutar:
```
docker compose up --build (buildear por primera vez)
docker compose up (levantar el servicio)
docker compose down (detener el servicio)
```

### Requirements
Python 3.8.*
```
pip install -r requirements.txt
python mananage.py migrate
python mananage.py runserver
```
