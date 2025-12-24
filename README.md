#  Proyecto Backgammon — Computación 2025

## Descripción
Este proyecto implementa el juego **Backgammon** aplicando los principios de la **programación orientada a objetos (POO)**, pruebas unitarias y arquitectura modular.  
El sistema permite jugar tanto desde consola (**CLI**) como desde una interfaz visual desarrollada con **Pygame**.

## Estructura del Proyecto
core/ → Lógica principal del juego (Board, Player, Dice, Game, Checker)
cli/ → Interfaz de texto (CLI.py)
gui/ → Interfaz visual en Pygame (PygameUI.py)
excepciones/ → Jerarquía de errores personalizados
test/ → Pruebas unitarias (unittest + MagicMock)

## Instalación

### 1 Crear entorno virtual
bash
python -m venv venv
source venv/bin/activate  

### 2 Instalar dependencias
pip install -r requirements.txt

### Ejecución
# por consola
python -m cli.CLI
# por Pygame
python -m gui.PygameUI

### tests
# ejecutar todos los tests
coverage run -m unittest discover
# ver reporte de cobertura
coverage report -m
# ver reporte de pylint
pylint core cli excepciones gui

### Estándares aplicados

Encapsulamiento con prefijo y sufijo (__atributo__) según el requisito del proyecto

"""ZOE CAMUS — COMPUTACIÓN 2025"""


