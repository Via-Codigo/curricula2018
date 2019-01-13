# coding: utf8
"""
Script para crear sesiones de clase

uso:
$  python create-session.py "titulo de la sesión entre comillas" -n <numero de sesión opcional>

Si no se coloca número de sesión, se creará el módulo sin el número
Si ya existe el número de sesión, dará error
"""

# Generating parser
import argparse
import os

parser = argparse.ArgumentParser(description="crea una nueva clase del modulo")

# Arguments
parser.add_argument("title", type=str,
                    help="Titulo de la clase entre comillas")
parser.add_argument("-n", "--number", type=float,
                    help="Numero de sesión a crear (float)")

args = parser.parse_args()

# Variables
title = args.title
number = args.number
if number:
    module = int(number)
else:
    module = "[X]"


session_template = """
# {}

**Módulo {} - [PONER Título]**

## Objetivos

## Descripción corta

### Presentación

[Link a las diapositivas]()

## Conceptos

## Actividades

---

### I. nombre actividad

Explicación breve actividad

**Participantes**: #

**Instrucciones**: instrucciones de la actividad

#### Material Actividad

---



""".format(title, module)


# Check if number arg was passed, convert negative numbers

if number:
    session_number = "{}".format(abs(number))


else:
    session_number = "--"

folder_name = "{} {}".format(session_number, title)

# create folder and file for the basic class
try:
    os.makedirs(folder_name)
    with open("{}/Guía de clase - {}.md".format(folder_name, title), "w+") as class_guide:
        class_guide.write(session_template)
except Exception as e:
    print(e)
    print("Esa carpeta ya existe")

# create all other required folders

try:
    os.makedirs(f"{folder_name}/ejercicios")
    # Estos deberían salir de una opción de configuración
    # os.makedirs(f"{folder_name}/inicio")
    # os.makedirs(f"{folder_name}/final")
except Exception as e:
    print(e)
    print("Alguna carpeta ya existe")
