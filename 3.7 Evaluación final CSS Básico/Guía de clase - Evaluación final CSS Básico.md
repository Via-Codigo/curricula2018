# Evaluación HTML/CSS

**Módulo 3 - CSS Básico**

## Objetivos

- Evaluar todos los conocimientos aprendidos durante este tema.

## Descripción corta

Los alumnos deberán realizar una página web que cumpla con los requerimientos planteados en la evaluación.
Basandose en los archivos PDF que muestran la web final, deben crear el HTML para esas páginas.
No se evaluará que completen, sino la calidad de lo que hagan.

### Presentación

[Link a las diapositivas](https://drive.google.com/open?id=18OLWn8BsVQ9tejw-ZiQuPQQEFU248AsMuXAdQ19zdO0)

## Conceptos

- Etiquetas básicas `<h1> --> <h6>`, `<p>`
- Anidación de elementos HTML
- Etiquetas de lista HTML: `<ul>`, `<ol>`, `<li>`
- Etiqueta `<img>`
- Atributos HTML
- Atributos **src**, **title** y **alt**
- Rutas relativas y absolutas
- Etiqueta `<a>`
- Linkeo de páginas internas y externas
- Atributos **id** y **href**
- Etiqueta `<section>`
- Etiqueta `<header>`
- Etiqueta `<footer>`
- Etiqueta `<aside>`
- Etiqueta `<nav>`
- Etiqueta `<article>`
- Etiqueta `<main>`
- Etiqueta `<div>`
- Margin
- Padding
- border
- border-radius
- font-family
- Font-style
- Font-size
- font-family
- font-weight
- list-style
- text-decoration
- text-align
- color
- Background-image
- position
- Reset: no usa \*, sino que crea sus propiedades y usa box-sizing
- Usa selectores de clase
- Usa selectores descendentes
- Usa selectores de etiqueta solo en valores generales o descendentes
- Reutiliza clases
- Usa clases múltiples por etiqueta HTML
- Usa margins adecuadamente
- Usa paddings adecuadamente
- Usa flex para posicionar contenidos
- Usa contenedor para centrar elementos en la página
- Usa variables
- Usar imágenes de fondo en css

---

## Instrucciones

En esta evaluación analizaremos tu capacidad de organizar la información usando todas las etiquetas HTML que has aprendido.
Además deberás crear el diseño completo de una web real con CSS
No hay una única forma correcta de hacerlo. Piensa bien lo que estas haciendo y por qué lo estas haciendo.

Puedes usar tu manual de clase, tus notas de cuaderno y tus trabajos previos para ayudarte a resolver el exámen.

### Estructura de la web

Debes crear la web del archivo : `kamanqa.pe/diseño-index-html.png`

### Links

Los links que no lleven a ningún sitio deber ponerles el simbolo "#" dentro del atributo href

### Imágenes

Hay más imágenes que las que necesitas, si no encuentras la que quieres, puedes usar otra similar, sin embargo si tendremos en cuenta si utlizas los atributos **alt** y **title** de forma correcta, recuerda, una imagen debe ser así:

```
<img src="ruta/al/archivo.jpg" alt="texto alternativo para cuando no carga" title="titulo que describe la imagen">
```

### Etiquetas

las etiquetas semánticas pueden ser difíciles de colocar, porque el contenido a veces nos confunde, es un **section**? es un **article** o solamente es un **div**? Piensalo bien.

### Comentarios

Recuerda que en HTML puedes poner comentarios que no lee la computadora. Puedes poner estos comentarios si quieres decir algo a tus evaluadores, por ejemplo, explicar por qué elegiste una etiqueta en vez de otra.

Los comentarios se ponen así:

```
<!-- comentario HTML -->
```

### Estilos css

Recuerda que debes pensar bien tu CSS antes de comenzar a escribirlo

## Tabla de corrección

| Etiqueta                                               | Descripción de uso correcto                                                                                                                                                                                                                                            | puntaje | obtenido?                                                           |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------- |
| `<h1> --> <h6>`                                        | Utiliza las etiquetas para transmitir ideas principales que explican el contenido de la web o sección                                                                                                                                                                  | 1 pto   |                                                                     |
| `<h1>`                                                 | Solo utiliza una etiqueta de título principal por página                                                                                                                                                                                                               | 1pto    |                                                                     |
| Jerarquía de títulos                                   | Utiliza las etiquetas en orden jerárquico adecuado, no saltando orden                                                                                                                                                                                                  | 2 ptos  |                                                                     |
| `<p>`                                                  | Utiliza la etiqueta párrafo de forma correcta, comunicando la información que necesita                                                                                                                                                                                 | 1 pto   |                                                                     |
| `<p>` por párrafo                                      | Entiende que cada párrafo va en una etiqueta distinta, separandolos aunque estén seguidos                                                                                                                                                                              | 1 pto   |                                                                     |
| `<ul>, <ol> y <li>`                                    | Utiliza los elementos de listado de forma correcta, agrupando información relacionada.                                                                                                                                                                                 | 1 pto   |                                                                     |
| `<img>`                                                | Sabe llamar imágenes con rutas relativas                                                                                                                                                                                                                               | 1 pto   |                                                                     |
| uso de atributos **title** y **alt**                   | Utiliza ambos atributos en sus etiquetas IMG                                                                                                                                                                                                                           | 1 pto   |                                                                     |
| Contenido descriptivo en atributos **title** y **alt** | hace descripciones complejas y correctas de las imágenes                                                                                                                                                                                                               | 1 pto   |                                                                     |
| atributo **id**                                        | Usa el atributo **id** para llevar a una subsección de la web                                                                                                                                                                                                          | 1 pto   |                                                                     |
| Rutas a archivos                                       | Las rutas a los archivos y los links llevan a donde deben. No están armadas de forma extraña (saliendo niveles extra para volver a entrar por ejemplo)                                                                                                                 | 1 pto   |                                                                     |
| `<a>`                                                  | Utiliza la etiqueta anchor de forma correcta (con href)                                                                                                                                                                                                                | 1 pto   |                                                                     |
| **target="\_blank"**                                   | Utiliza target blank en los links a páginas de redes sociales                                                                                                                                                                                                          | 1 pto   |                                                                     |
| sitemap                                                | Las páginas del exámen extan correctamente vínculadas entre si                                                                                                                                                                                                         | 1 pto   |                                                                     |
| atributos de href **mailto** y **tel**                 | Utiliza al menos una vez uno de estos tipos de link en donde debe                                                                                                                                                                                                      | 1 pto   |                                                                     |
| `<a>` avanzado                                         | Utiliza la etiqueta anchor para rodear elementos y convertir en link a otros elementos HTML                                                                                                                                                                            | 1 pto   |                                                                     |
| `<section>`                                            | Utiliza la etiqueta de forma adecuada para separar secciones generales e importantes de la web                                                                                                                                                                         | 1 pto   |                                                                     |
| Título de `<section>`                                  | Cada sección tiene un primer hijo que es una etiqueta `<h#>`. Si no es el primer hijo por un tema de diseño, se perdona                                                                                                                                                | 1 pto   |                                                                     |
| `<header>`                                             | Utliza la etiqueta encabezado en las secciones que se repíten de la web                                                                                                                                                                                                | 1 pto   |                                                                     |
| `<footer>`                                             | Utiliza la etiqueta pie de página en las secciones que se repíten de la web                                                                                                                                                                                            | 1 pto   |                                                                     |
| `<aside>`                                              | Utiliza Aside de forma correcta. Si no la utiliza no pasa nada                                                                                                                                                                                                         | 1 pto   |                                                                     |
| `<nav>`                                                | Utliza la etioqueta de navegación para rodear elementos de listado que son menúes importantes, se considera importante cualquier menú que claramente lo es en caso de duda evaluar con criterio la relevancia del menú, es mejor puntuar positivo ante un buen intento | 1 pto   |
| `<article>`                                            | Utiliza la etiqueta artículo en elementos que cumplen con ser contenidos completos si se sacan de contexto                                                                                                                                                             | 1 pto   |                                                                     |
| `<main>`                                               | Utiliza la etiqueta de contenido principal en secciones relevantes que no incluyen el header o el footer                                                                                                                                                               | 1 pto   |                                                                     |
| `<div>`                                                | Utiliza el elemento agrupador **div** para agrupar elementos que tienen relación contextual entre sí. Realizar la evaluación en función del diseño del exámen, entendiendo que los estudiantes aún no aprenden CSS                                                     | 1 pto   |                                                                     |
| reset                                                  | 1 pto                                                                                                                                                                                                                                                                  |         | Reset: no usa \*, sino que crea sus propiedades y usa box-sizing    |
| clases                                                 | 1 pto                                                                                                                                                                                                                                                                  |         | Usa selectores de clase                                             |
| descendencia                                           | 1 pto                                                                                                                                                                                                                                                                  |         | Usa selectores descendentes                                         |
| estilos en etiquetas                                   | 1 pto                                                                                                                                                                                                                                                                  |         | Usa selectores de etiqueta solo en valores generales o descendentes |
| reutilización de clases                                | 1 pto                                                                                                                                                                                                                                                                  |         | Reutiliza clases para comaprtir estilos                             |
| clases multiples                                       | 1 pto                                                                                                                                                                                                                                                                  |         | Usa clases múltiples por etiqueta HTML                              |
| margins                                                | 1 pto                                                                                                                                                                                                                                                                  |         | Usa margins adecuadamente                                           |
| paddings                                               | 1 pto                                                                                                                                                                                                                                                                  |         | Usa paddings adecuadamente                                          |
| flex layouts                                           | 1 pto                                                                                                                                                                                                                                                                  |         | Usa flex para posicionar contenidos                                 |
| contenedor/wrapper                                     | 1 pto                                                                                                                                                                                                                                                                  |         | Usa contenedor para centrar elementos en la página                  |
| variables css                                          | 1 pto                                                                                                                                                                                                                                                                  |         | Usa variables                                                       |
| fondos                                                 | 1 pto                                                                                                                                                                                                                                                                  |         | Usar imágenes de fondo en css                                       |
