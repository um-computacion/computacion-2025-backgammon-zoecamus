# JUSTIFICACIÓN DEL PROYECTO BACKGAMMON

## 1. Introducción
El proyecto **Backgammon** fue desarrollado como parte del curso de *Computación 2025* con el objetivo de aplicar los principios de la programación orientada a objetos, buenas prácticas de diseño, encapsulamiento estricto y pruebas unitarias.

El sistema implementa la lógica completa del juego Backgammon, permitiendo su ejecución tanto en modo **CLI (consola)** como en modo **Pygame (interfaz visual)**. Además, incorpora una jerarquía de excepciones personalizada y una estructura modular que facilita la mantenibilidad y extensibilidad del código.

---

## 2. Arquitectura general
El proyecto sigue una **arquitectura modular** y desacoplada:

- **core/** → Contiene la lógica central del juego (`Board`, `Player`, `Checker`, `Dice`, `Game`).
- **cli/** → Implementa la interfaz por consola (`CLI.py`) para la interacción textual.
- **gui/** → Incluye la interfaz gráfica (`PygameUI.py`) para visualizar el tablero y los movimientos.
- **excepciones/** → Define las clases de error personalizadas y controladas.
- **test/** → Incluye los tests unitarios con `unittest` y `MagicMock`.

El flujo principal está coordinado por la clase `Game`, que administra el turno de los jugadores, las tiradas de dados (`Dice`) y las actualizaciones en el tablero (`Board`). Las interfaces (CLI y PygameUI) comunican las acciones del usuario con el motor de juego.

---

## 3. Diseño y Responsabilidades
Cada clase cumple un rol específico bajo el principio de **responsabilidad única**:

| Clase | Rol principal | Interacciones |
|--------|----------------|----------------|
| `Game` | Coordina la partida y los turnos | `Board`, `Dice`,`Player` |
| `Board` | Representa el tablero y reglas de movimiento | `Checker`, `Game` |
| `Checker` | Modela las fichas individuales | `Board` |
| `Player` | Representa a cada jugador y su color | `Game`, `Board` |
| `Dice` | Genera valores aleatorios de tirada | `Game` |
| `CLI` | Interfaz textual para ejecutar el juego | `Game` |
| `PygameUI` | Interfaz visual basada en Pygame | `Game`, `Board` |

---

## 4. Convención de nombres de atributos
En cumplimiento con los **requisitos del proyecto**, se adoptó una convención de **doble prefijo y sufijo** para los atributos internos, con el fin de reforzar el encapsulamiento y la visibilidad.

| Estilo | Ejemplo | Justificación |
|---------|----------|---------------|
| `__atributo__` | `__color__`, `__points__`, `__board__` | Indica atributos encapsulados con prefijo y sufijo doble según el estándar del proyecto. |

Este estilo garantiza un control estricto del acceso y evita conflictos entre módulos.

---

## 5. Manejo de Excepciones
Las excepciones fueron diseñadas de forma jerárquica dentro del módulo `excepciones/`, asegurando un manejo controlado de errores.

| Excepción | Descripción | Clase que la usa |
|------------|--------------|------------------|
| `InvalidMoveError` | Movimiento fuera de las reglas del juego | `Board` |
| `NotYourCheckerError` | Intento de mover una ficha del oponente | `Board` |
| `BlockedPointError` | Punto ocupado por fichas del adversario | `Board` |
| `IllegalReentryPointError` | Reingreso inválido desde la barra | `Board` |

---

## 6. Pruebas y Cobertura
El proyecto cuenta con un conjunto extenso de tests unitarios en la carpeta `test/`, cubriendo el 88% del código.  
Se utilizó **`unittest`** junto con **`MagicMock`** para aislar componentes y simular comportamientos sin depender del azar ni del estado real del tablero.

Ejemplo de mock aplicado:
```python
fake_dice = MagicMock()
fake_dice.roll.return_value = [3, 5]

Esto permitió verificar comportamientos de Game sin necesidad de ejecutar el tablero completo.

## 7 Convenciones de estilo y calidad de código

Se aplicó Pylint (v4.0.2) para asegurar un estilo consistente y legible. Tras correcciones de docstrings y espacios en blanco, se obtuvo una puntuación de 9.8/10.

Ejemplo de correcciones realizadas:

Eliminación de trailing whitespace.

Homogeneización de nombres de atributos (__atributo__).

Inclusión de docstrings en métodos públicos y privados.

## 8. Interfaces: CLI y PygameUI
CLI

Provee una interfaz de texto clara, pensada para depuración y pruebas unitarias. Permite ejecutar el juego, tirar los dados y mover fichas desde consola.

PygameUI

Desarrollada con Pygame, ofrece una visualización completa del tablero. Representa cada punto, ficha y barra gráficamente, sincronizada con el estado de Board. Incluye un panel lateral con contador, turnos y estado del juego.

##9. Principios de diseño aplicados

Responsabilidad única: Cada clase tiene un rol definido.

Bajo acoplamiento: Las dependencias se reducen usando mocks y propiedades.

Encapsulamiento: Atributos protegidos con doble prefijo y sufijo.

Extensibilidad: El diseño modular permite futuras ampliaciones (por ejemplo, modo en red o IA).

## 10. Conclusión

El desarrollo del Backgammon permitió aplicar conceptos de POO, testing, diseño modular y principios SOLID, logrando un sistema robusto, reutilizable y fácilmente mantenible.
La integración de Pygame elevó el proyecto a un entorno interactivo y visual, reflejando fielmente la dinámica real del juego.
