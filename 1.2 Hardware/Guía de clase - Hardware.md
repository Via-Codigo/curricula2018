# 1.2 Hardware

**Módulo 1 - Fundamentos**

## Objetivos

- Explicar las partes de una computadora y para qué sirven.
- Explicar de manera sencilla cómo funcionan las principales partes de una computadora.

## Descripción corta

Se enseñarán las principales partes que componen una computadora, para que sirven y a
grandes rasgos como funcionan.

## Presentación

[Link a las diapositivas](https://docs.google.com/presentation/d/1P5uVLogtP64aIEjp0XsE85laWADmGaTNhOoV4qOs3dk/edit?usp=sharing)

## Conceptos

- HDD
- RAM
- CPU
- Memoria Caché
- Placa madre
- puertos I/O

## Actividades

### I. La Computadora Humana

Construiremos una representación de una computadora utilizando el salón como Placa Madre y equipops de estudiantes para cada parte del Hardware que queremos
representar.
Se hará un pequeño un ejercicio para cada parte del sistema de modo que todos puedan ver su función y aprender en grupo.
Según se vayan explicando las partes en las diapositivas, se hará un pequeño ejercicio donde se explicará como vamos a trabajar.
Las pelotas de colores representarán los bits de información que fluyen por la computadora, y nuestra computadora tendrá un máximo de **4 bits en su versión básica** y **8 bits en su versión avanzada**.

Habrá tres variantes de ficitultad, la introductoria la básica y la avanzada. Al aplicar se pueden hacer los ejercicios básicos o los avanzados.
Comenzaremos siemrpe con el funcionamiento introductorio, y según el grupo iremos subiendo a **basica** y **avanzada**.
**Introducción**: Solo se pedirán cantidades de pelotas, no combinaciones.
La idea es que se pueda ir subiendo el nivel de cada parte de forma independiente.
Por ejemplo, podemos comenzar con un equipo de **RAM** que representa un solo DIMM, para luego aumentarlo a dos.

#### 1. Placa Madre

El salón o espacio de enseñanza representará la **placa madre**

#### 2. Periféricos (2 a 3 personas entre entrada y salida)

Los periféricos representan al usuario y son los que solicitarán o entregarán información al **CPU**.
Utilizarán una cartilla con las combinaciones de peticiones que pueden hacer.
No tiene niveles de dificultad

##### 2.1 Periféricos de entrada (1 a 2 personas)

Emiten comandos al Procesador

##### 2.2 Periféricos de salida (1 persona)

Representa el monitor y se le entregan los resultados de la solicitud procesada

#### 3. Disco Duro (2 a 3 personas)

El disco duro será una caja grande que es capaz de contener cientos de pelotas. La tarea de los participantes es conseguir las combinaciones de pelotas que les pida la **RAM**.
Durante la explicación de que es un **Disco Duro** se explicarṕa como se hace el guardado de datos y el borrado de los mismos en una pizarra utilizando una grilla para mostrar los sectores, pero el sistema de fragmentación, defragmentación y Jorunaling se enseñará con la caja de pelotas.

**Básica**: Los alumnos son un HDD windows donde mientrás más se use la caja, más se desordena, y en cierto punto, el usuario puede pedir que defragmenten el disco duro, ordenando las pelotas por sectores.

**Avanzada**: Para representar el Journaling, los alumnos deberán mantener cierto orden por niveles o capas cada vez que saquen pelotas.

**Extra**: Se explica un **SSD** a través de una superficie plana donde todo está al alcance y a la vista de quienes buscan.

#### 4. RAM (Memoria de Acceso Rápido) (Una persona por DIMM )

**Capacidad Máxima**: 32bits por DIMM

Cada DIMM de **RAM** será representado por una persona que tiene una superficie menor para acumular sus pelotas.
El **RAM** recibe peticiones del **CPU** de cadenas de pelotas, si tiene **todo** lo solicitado, se lo entrega al **CPU**, de no tenerlo, debe
transmitir la petición al **DIsco Duro**, y luego de recibirla, transmitirla al **CPU**. El **CPU** revisa la información, la ejecuta y devuelve al **RAM**.

Si el **RAM** no tiene espacio para recibir una nueva cadena de bits, debe deshacerse (devolver al **Disco Duro**) las pelotas que no cree convenientes para poder recibir nuevas.

**Básico**: Un solo DIMM

**Avanzado**: Ampliamos la RAM, de cualquiera de dos formas, podemos ampliar un solo DIM de RAM dándole capacidad de almacenar hasta 64 bits, o podemos
ampliar con otro DIMM (una segunda persona) de 32 bits.

#### 5. Memoria Caché (1 persona)

Esta parte no tendrá dos niveles de dificultad.
La **Memoria Caché** estará ubicada entre el **CPU** y la **RAM**. Tendrá una capacidad máxima del mismo tamaño que los bits del procesador.
Cuando el **CPU** realiza un pedido, o acción, siempre mira primero si las piezas que necesita las tiene la **Memoria Caché**. De ser así, se las pide.

#### 6. CPU (Procesador) (1 a 3 personas)

El procesador es la pieza más compleja de nuestro sistema, y estará en el centro de todas las acciones del computador humano.
Para una mejor representación, la **memoria caché** será una pieza aparte (otra persona).

**básica**: El **CPU** recibe un comando de los usuarios. En cuanto recibe las cadenas de bits de la memoria que se las entregó (ya sea **Memoria Caché** o **RAM**)debe dar tres vueltas en círculo (para representar los ciclos de procesamiento) y devolver las cadenas de bits a la memoria que se la entregó. Luego le entrega la acción de salida al **Periférico de salida** para que muestre el resultado. Lo primero que hace es buscar lo solicitado en la **Memoria Caché**, de no encontrar ahí la información, se la pide a la **RAM**.

**avanzada**: Antes de aumentar los núcleos hacemos que el usuario pida las cosas de dos en dos. Luego aumentamos los núcleos del **CPU** aumentando una persona que realiza las mismas acciones en paralelo.
Además el CPU contará con una persona extra (**gestor de procesos**) que gestiona que pelotas se retornan a la **RAM** o se devuelven directamente al **Disco Duro** según crea que genera un sistema más eficiente.

Tendrá una lista procesamientos que le dirán que entregar al **Periférico de salida**.

**_Pasos:_**

0. Los **Periféricos de salida** hace un requerimiento de información o acción al **CPU**.

1. El **CPU** procesa la petición y busca la información en la **Caché**.

1. Si la información requerida no se encuentra en **Caché**, el **CPU** hace la misma petición a la **RAM**.

1. La **RAM** busca la petición en su bandeja, de tenerla la entrega al **CPU**.

1. Si la **RAM** no tiene la información, la pide al **HDD**.

1. El HDD tendrá una caja con distintas pelotas de colores en donde buscará la información y, si la encuentra, la entregará a la RAM.

1. El **CPU** recibe la información, la procesa en su tabla y realiza dos acciones:

- Entrega el resultado del procesamiento al **Periférico de salida**
- Devuelve las pelotas a la memoria que se las dió.
- **extra**: si se usa el método avanzado una persona extra decide si se le retornan a la **RAM** o se le retornan al **Disco Duro**.

![Diagrama Computadora](https://github.com/Via-Codigo/curricula2018/blob/master/assets/diagrama-simula-computadora.png?raw=true)

## Material

- Pelotas (100+)
- Caja grande para Disco Duro
- Bandeja o caja chica para RAM
- Caja pequeña o bandeja pequeña para caché
- [Tarjetas de peticiones para periféricos de entrada](https://docs.google.com/document/d/1Sss2r9dAI1Ka6PytNnfMZntBZI-8d6yNmAfrYnfTPZQ/edit?usp=sharing)
- [Tabla de procesos del CPU](https://docs.google.com/spreadsheets/d/1KzIJDL9AXDnjzwrk-CCPKhWwYYOAFtxbhgSoGbUTbf4/edit?usp=sharing)
- [Tarjetas de resultados para periférico de salida](https://docs.google.com/document/d/1Sss2r9dAI1Ka6PytNnfMZntBZI-8d6yNmAfrYnfTPZQ/edit?usp=sharing)
- Cajas de procesos donde quepan las cantidades de bits requeridas (4 y 8)
