## El proyecto implementa una versión simplificada del juego Backgammon en Python, estructurado com clases separadas
 ## Se siguió una arquitectura modular con paquetes:
        ## core/ → clases principales (Player, Dice, Board, Game)
        ## excepciones/ → clases de excepciones
        ## test/ → pruebas unitarias con unittest.

## Justificación de las clases elegidas

 ## Player: Representa a cada jugador. Responsabilidad: encapsular nombre, color y dirección
        → Justificación: separa la lógica de jugador del resto, permite validar color/dirección

 ## Dice: Modela los dados de 6 caras. Responsabilidad: generar tiradas y manejar dobles
        → Justificación: el backgammon depende de las tiradas

 ## Board: Representa los 24 puntos del tablero. Responsabilidad: distribución inicial, estado de fichas, validaciones de movimientos
        → Justificación: lógica del tablero aislada permite extender reglas sin mezclar con la clase Game.

 ## Game: La partida. Responsabilidad: gestionar turnos, usar Board y Dice, verificar fin de juego.
        → Justificación: es la capa que une a todos los componentes.

 ## Excepciones: Jerarquía de errores
        → Justificación: manejar errores específicos