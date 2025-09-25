# Backgammon en Python 

Este proyecto implementa una versión del juego de **Backgammon**, parte de la materia **Computación 2025**

El objetivo es aplicar principios de diseño orientado a objetos, manejo de excepciones, 
testing y las prácticas de documentación

---

##  Requisitos del proyecto
- Clases principales: `Player`, `Dice`, `Board`, `Game`
- Carpeta `exceptions/` con jerarquía de errores propios
- Convención de atributos con `__prefijo__/__sufijo__` en todas las clases
- Archivos de documentación obligatorios:
  - `JUSTIFICACION.md`
  - `CHANGELOG.md`
  - `prompts-desarrollo.md`
  - `prompts-testing.md`
  - `README.md`

---

##  Estructura de la carpeta
core/
    - `Player.py`
    - `Excepciones.py`
    - `Dice.py`
    - `Board.py`
    - `Game.py`     
tests/
    - `test_Player.py`
    - `test_Dice.py`
    - `test_Board.py`
    - `test_Game.py`
JUSTIFICACION.md     
CHANGELOG.md       
prompts-desarrollo.md
prompts-documentacion.md
prompts-testing.md
README.md

---

## Correr los tests
Se utiliza unittest como framework de testing
- python -m unittest discover 
Los tests cubren: 
- `Player`
- `Dice`
- `Board`
- `Game`: flujo de turnos, tirada de dados, integración con Board y Dice usando MagicMock.

---


## Zoe Camus
