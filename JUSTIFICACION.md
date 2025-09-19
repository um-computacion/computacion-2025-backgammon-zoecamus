## En el proyecto implemento una versión simplificada del juego Backgammon en codigo Python, estructurado com clases separadas

              core/ → clases principales (Player, Dice, Board, Game)
              excepciones/ → clases de excepciones
              test/ → pruebas unitarias con unittest.

## Justificación de las clases elegidas

       #Player: Representa a cada jugador. Responsabilidad: encapsular nombre, color y dirección
       #Dice: Modela los dados de 6 caras. Responsabilidad: generar tiradas y manejar dobles
       #Board: Representa los 24 puntos del tablero. Responsabilidad: distribución inicial, estado de fichas, validaciones de movimientos
       #Game: La partida. Responsabilidad: gestionar turnos, usar Board y Dice, verificar fin de juego.
       #Excepciones: Jerarquía de errores
        → Justificación: manejar errores específicos

## Decisiones de diseño

       Board inicial: implemente _initial_points() con la distribución estándar del backgammon.
       Testing aislado: use MagicMock en tests de Game para simular en board y dice.

## Excepciones y manejo de errores
       #Jerarquía en excepciones.py:
              PLayer: InvalidColorError, InvalidDirectionError.
              Dice: InvalidDiceSidesError, InvalidDiceOverrideError.
              Board: InvalidMoveError, BlockedPointError, OutOfBoundsPointError, NotYourCheckError.
       → Justificación: facilita testing y claridad de reglas.