## en este archivo se guarda la historia de cambios mas importantes del proyecto

## primer sprint 

commit 24/8/2025: creé la estructura inicial del proyecto, carpetas y archivos base.

En el primer sprint me dediqué a la creación de la estructura base del proyecto. Organicé el repositorio en carpetas (core/, excepciones/, test/), preparé los archivos iniciales y configuré el entorno para asegurar un punto de partida ordenado. Esto me  permitió sentar las bases para desarrollar cada función del Backgammon y facilitar la incorporación de nuevas clases y pruebas en los sprints siguientes.

commit 2/9/2025: creación de la clase Player con sus métodos y validaciones.

Este commit permitió encapsular la lógica de los jugadores (nombre, color, dirección, UID) y sentar la base para la interacción dentro del juego.

commit 3/9/2025: creación del archivo test_player.py.

Se desarrollaron las pruebas unitarias para la clase Player, validando su construcción, métodos auxiliares y el cumplimiento de la convención de atributos.

## segundo sprint

commit 6/9/2025: creación de la clase Game y métodos iniciales de coordinación de turnos.
commit 8/9/2025: implementación de la clase Dice con tiradas de dados y manejo de dobles.
commit 9/9/2025: creación de test_dice.py con pruebas de tiradas, override y validaciones.
commit 10/9/2025: implementación de la clase Board con distribución inicial, métodos in_home y has_won.
commit 11/9/2025: creación de test_board.py validando la configuración inicial del tablero y estados básicos.

commit 13/9/2025: definición de excepciones personalizadas en exceptions/ (jugador, dados, tablero, barra, bearing off).
commit 14/9/2025: importación e integración de excepciones en las clases (Player, Dice, Board), reemplazando assert por validaciones más específicas.

commit 15/9/2025: inicio de la documentación con el archivo JUSTIFICACION.md.

En este commit y los siguientes me dediqué a la documentación del proyecto: justificación del diseño, clases y atributos, excepciones, estrategias de testing, además de la creación del archivo CHANGELOG.md para registrar la evolución del código. El próximo paso será completar el README.md como guía de uso e instalación.

commit 26/9/2025: Empece con el codigo dek archivo CLI.py.