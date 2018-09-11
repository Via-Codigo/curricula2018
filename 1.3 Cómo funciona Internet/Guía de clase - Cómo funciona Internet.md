# 1.3 Cómo funciona Internet

**Módulo 1 - Fundamentos**

## Objetivos

## Descripción corta

Los alumnos aprenderán como se estructura internet, los distintos componentes implicados y el por qué de esta estructura.
Se harpan ejercicios que les permitan entender las principales partes que componen Internet, y como estas funcionan.
Con esto entenderán donde entra el trabajo de un maquetador web, y los conceptos básicos que deben conocer.

## Actividades

### Ver video sobe el cableado de internet

Se muestra video sobre como se extienden los cables submarinos de internet por el mundo.

#### Pedido de imagen por internet

Se simula un **Request** de una imagen a un servidor.

Una persona será el servidor. 4 Personas serán los que llevan los paquetes. Una última será el cliente.

0. El cliente y el Servidor se colocan una etiqueta con sus IP
1. Se envía un sobre con un mensaje que dice "Dame una foto de gato" al servidor con la IP del servidor como destinatario y la del cliente como emisor
1. El Servidor muestra como no cabe la foto en un solo sobre, la parte en 4 y las coloca en cada sobre. Cada sobre
   deberá decír su número y total ej. _1/4_, _3/4_. Debe tener además como destinatario al cliente y como emisor al servidor.
1. Cada mensajero lleva un sobre al Cliente
1. El cliente ordena los sobres y reconstruye la foto

#### Representación del internet con personas

En este ejercicio se representará en mayor profundidad el flujo de uso de un típico usuario de internet, buscando explicar el
funcionamiento de la tecnología que existe detras.

##### Usuario

1. Pueden ser varias personas, los usuarios construyen búsquedas de google usando los keywords
   del listado que se les entrega. Deben entregar una ficha con la búsqueda al _Cliente_

2. Una vez el _Cliente_ recibe el listado de páginas sugerido por _El Motor de Búsqueda_ debe presentarselo al _Usuario_.

3. Cuando el _Usuario_ elige la página que desea recibir, el _Cliente_ entrega la tarjeta con el Request al _Servidor DNS_

4. Al recibir el sobre con la págiona web de el _Cliente_ el usuario lo abre completando así el ciclo.

##### Cliente

1. El cliente será una persona, su función es recibir el pedido de búsqueda de los _usuarios_ y entregarlo al equipo
   que es el _motor de búsqueda_.

2. Una vez que el _Cliente_ reciba el listado de resultados de _El motro de Búsqueda_ debe presentarlo al _usuario_ que hizo el pedido para que este elija que página desea ver.

3. Al recibir la web del _Servidor Hosting_ el _Cliente_ entrega el sobre al _Usuario_.

##### El Motor de Búsqueda

Es un equipo de personas que tiene una caja con las fichas que contienen las páginas web que han indexado.

1. Deben analizar la búsqueda que les envía el _Cliente_ y devolver las páginas que consideren relevantes en orden de relevancia al _Cliente_

##### Servidor DNS

Es una persona

1. Al recibir un Request del _Cliente_ debe buscar el dominio que le solicitan en su **tabla de servidores**. Al encontrarlo, debe agregar esa **dirección IP**
   al pedido y entregarla al _Servidor de Hosting_ adecuado.

##### Servidor de Hosting

Cada persona representa un Hosting compartido y tiene 8 sobres con 8 páginas web. Los sobres tienen por fuera el **dominio** de la página web y por dentro
el archivo con información de mentira de _Response_ de una web.

1. El Hosting recibe una petición de URL del _Servidor DNS_ y busca el sobre para esa web. Al encontrarlo lo retorna
   directamente al _Cliente_ agregando la IP del cliente al sobre.

## Conceptos

- Cliente/Servidor
- Dirección IP (4 billones)
- paquetes TCP/IP
- ISP
- Dominio
- DNS
- Hosting
- Router
- Browser (Navegador)
- Search Engine
- Request/Response

## Material

- 5 Sobres pequeños
- Una imagen impresa para partir en los 4 sobres y enviar en varios requests
- Etiquetas de nombre (nametags) para cada parte del sistema con su nombre e IP
- Tarjetas o fichas con los datos de las webs como salen en la búsqueda de Google por un lado y los datos para realizar el request por el otro
- Listado de webs con IP para el servidor DNS
- [Listado de webs/IP's y meta descriptions para crear las tarjetas](https://docs.google.com/spreadsheets/d/1HGAipLs-1gfowMCLJTw2m3R_G4aTsO9WWhv8anxWzHQ/edit?usp=sharing)
- [Listado de Keywords con los que se pueden construir búsquedas de google](https://docs.google.com/spreadsheets/d/1HGAipLs-1gfowMCLJTw2m3R_G4aTsO9WWhv8anxWzHQ/edit?usp=sharing)
- Sobres con la IP de cada una de las webs que tiene cada servidor con [un archivo con información de mentira](https://docs.google.com/document/d/14qrmNviaCWQc1MmzxSaMB4Y9ijWE-c8BC2xh72bgn20/edit?usp=sharing) dentro
- [video de cables de internet](https://www.youtube.com/watch?v=IlAJJI-qG2k)

## Tareas

`NONE`
