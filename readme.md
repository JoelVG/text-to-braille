# PROTOTIPO PARA LA TRANSCRIPCIÓN DE TEXTO A BRAILLE

> El prototipo de este transcriptor está enfocado para Braille de grado 1.
> Se aplica criterios de abreviación de palabras según las reglas del Braille boliviano.
> Se considera únicamente la transcripción del lenguaje Español.

## Objetivos
- La herramienta permitirá la transcripción de libros digitales al sistema Braille de Grado 1.
- Los documentos se restringen a aquellos con complejidad mínima para el aprendizaje del sistema Braille.
- El idioma que se manejará para la transcripción será únicamente el español y Braille adoptado en Bolivia.
- El manejo de esta herramienta no está contemplado para personas invidentes.
- Se contempla la transcripción únicamente de textos cortos de hasta 1000 palabras.

## Endpoints
```
POST /api/text/       Crea una "traducción" de un texto que se le pasa.
GET	 /api/text/{id}   Muestra el texto original y su equivalente en Braille.
GET	 /api/file/	      Recibe el path de un archivo .txt o .pdf, extrae y devuelve su equivalente en Braille.
```
