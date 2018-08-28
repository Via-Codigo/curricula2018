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

session_template = """
# {}

**Módulo III - Proyectos reales**

## Objetivos

## Descripción corta

## Actividades

* **nombre actividad**: descripción

## Conceptos

## Material

## Tareas

`NONE`
""".format(title)


# Check if number arg was passed, convert negative numbers

if number:
    session_number = "{}".format(abs(number))
   
   

else:
    session_number = "--"

folder_name = "{} {}".format(session_number, title)

# create folder and file
try:
    os.makedirs(folder_name)
    with open("{}/Guía de clase - {}.md".format(folder_name, title), "w+") as class_guide:
        class_guide.write(session_template)
except Exception as e:
    print(e)
    print("Esa carpeta ya existe")
