# Manual de UnSemantic Grid

## Para comenzar

Recuerda que para que las webs escalen bien en responsive, debes agregar el meta de **viewport**, Visual Studio Code suele agregarlo automáticamente.

```
<meta name="viewport" content="width=device-width, initial-scale=1.0" />

```

Luego solo tienes que agregar el css de unsemantic luego de tu css de reset pero antes de tu css de la web.

## Clases del Grid (grilla)

Todos los elementos del grid (columnas) deben ser contenidos por un elemento superior (fila). En este caso la fila se llama **grid-container** y las columnas dicen **grid-x** acompañado por el número que define el porcentaje de ancho de la columna.

Por defecto, la clase grid-container tiene un ancho máximo de 1200px

Ejemplo:

```
<div class="grid-container">
  <div class="grid-50">
    Yo mido el 50% de ancho
  </div>
  <div class="grid-25">
    Yo mido el 25% de ancho
  </div>
  <div class="grid-25">
    Yo mido el 25% de ancho
  </div>
</div>

```

Las clases para columna **grid-x** permiten que **x** sea un multiplo de 5, hasta el 100 — grid-5, grid-10 … grid-95, grid-100.

Además hay clases para dividir la página en tercios: grid-33 y grid-66 que son 33.3333% y 66.6667% de ancho

Cada columna con gid-x tiene 10px de padding-right y padding-left, esto hace que cada columna se separe de otra columna a su costado por un total de 20px (se suman).

## Contenedores anidados y padding cero

Si quieres anidar un contenedor dentro de otro (fila dentro de fila), tienes que usar la clase **grid-parent** en el elemento que será el papá. Esto hará que el papá tenga cero padding y que tengas control sobre las distancias. Esta clase sirve también cuando quieres tener columnas sin separación.

```
<div class="grid-container">
  <div class="grid-50">
    contenido alto que irá junto a las columnas de la siguiente sección
  </div>

  <!--
    columnas anidadas
  -->

  <div class="grid-50 grid-parent">
    <div class="grid-50">
      fila 1:
        yo ocupo 25% (50% de 50%)
    </div>
    <div class="grid-50">
      fila 1:
        yo ocupo 25% (50% de 50%)
    </div>
    <div class="grid-50">
      fila 2:
        yo ocupo 25% (50% de 50%)
    </div>
    <div class="grid-50">
      fila 2:
        yo ocupo 25% (50% de 50%)
    </div>
  </div>
</div>

```

## Clases para celulares, tablets y como esconder elementos

También existen clases **mobile-grid-x** que nos permiten dar anchos distintos a las columnas cuando estamos en un celular, aplicarán esta medida a todos los dispositivos con ancho menor a 768px.
Se aplican combinandolas con las clases para escritorio.

También puedes esconder elementos de la web según el tamaño de la pantalla.

ej.

```

<div class="grid-container">
  <div class="grid-50 mobile-grid-100">
    yo ocupo 50% de ancho en  escritorio.
    yo ocupo 100% de ancho en  celulares.
  </div>
  <div class="grid-25 mobile-grid-50">
    yo ocupo 25% de ancho en  escritorio.
    yo ocupo 50% de ancho en  celulares.
  </div>
  <div class="grid-25 mobile-grid-50">
    <span class="hide-on-desktop">
      yo me escondo en escritorio.
    </span>
    <span class="hide-on-mobile">
      yo me escondo en celulares.
    </span>
  </div>
</div>


```

Para tables existen las mismas clases, solo reemplaza la palabra **mobile** por **tablet**, esto afectará a todas las pantallas entre 768px y 1024px

por ej.

```
<div class="grid-container">
  <div class="grid-container">
    <div class="grid-50 mobile-grid-100 tablet-grid-60%">
        yo ocupo 50% de ancho en  escritorio.
        yo ocupo 60% de ancho en tablet
        yo ocupo 100% de ancho en  celulares.
    </div>
    <div class="grid-25 mobile-grid-50 tablet-grid-20">
        yo ocupo 25% de ancho en  escritorio.
        yo ocupo 20% de ancho en tablet
        yo ocupo 50% de ancho en  celulares.
    </div>
    <div class="grid-25 mobile-grid-50 tablet-grid-20">
        <span class="hide-on-desktop">
        yo me escondo en escritorio.
        </span>
        <span class="hide-on-mobile">
        yo me escondo en celulares.
        </span>
        <span class="hide-on-tablet">
        yo me escondo en tablets.
        </span>

    </div>
    </div>
</div>

```

## Clases para empujar y jalar

Si quieres cambiar como se ven elementos en la web, pero no quieres cambiar el orden en que está el código HTML, puedes usar clases push-x y pull-x classes, y/o sus variantes mobile/tablet mobile-push-x and mobile-pull-x, tablet-push-x, tablet-pull-x

ej.

```
<!--
  Ejemplo básico
-->

<div class="grid-container">
  <div class="grid-50 push-50">
    Me veo en segundo lugar en escritorio.
  </div>
  <div class="grid-50 pull-50">
    Me veo en primer lugar en escritorio.
  </div>
</div>
<!--
  Ejemplo avanzado
-->

<div class="grid-container">
  <div class="grid-50 push-50 mobile-grid-50 mobile-push-50">
    Soy el tercero en escritorio
    Soy el segundo en celular
  </div>
  <div class="grid-25 pull-50 mobile-grid-50 mobile-pull-50">
    Soy el primero en escritorio
    Soy el primero en celular
  </div>
  <div class="grid-25 pull-50 mobile-grid-100">
    Soy el segundo en escritorio
    ocupo el 100% de ancho en celular
  </div>
</div>
```

# Crear espacios en blanco con prefijos y sufijos

Si solo quieres crear espacios en blanco (que la columna comience a partir del 40% de la web por ej.), y no cambiar de sitio los elementos, puedes crear un espacio vacío, o columnas en blanco. Para hacerlo, usas las clases **prefix-x** para dejar un espacio antes, o **sufix-x** para dejar un espacio después. Lo mismo funciona para tablets y celulares agregandoles **mobile-** y **tablet-**

ej.

```
<div class="grid-container">
  <div class="grid-30 suffix-20">
    Yo mido 30% de ancho, y estoy seguido por...
  </div>
  <div class="grid-30 prefix-20">
  Otra columna que mide 30% pero esta alejada por un espacio en blanco del 20%.
  </div>
</div>
```
