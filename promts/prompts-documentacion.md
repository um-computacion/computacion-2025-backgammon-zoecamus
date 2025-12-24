# prompt 1
Estoy armando el archivo JUSTIFICACION.md de mi proyecto Backgammon. ¿Qué cosas puedo agregar o mejorar en la estructura?
# Respuesta resumida
Conviene armar un índice con: las decisiones de diseño (Board inicial, ¿en qué usaste MagicMock?), arquitectura, tabla de clases/responsabilidades, tabla de atributos/relaciones, manejo de excepciones.
# Uso 
Lo voy a usar para completar la justificación con secciones mas claras

# prompt 2
Estoy completando la documentación de mi proyecto Backgammon y quiero explicar brevemente la arquitectura general. Cómo puedo describir la relación entre Game, Board, Player, Dice y CLI/PygameUI
# Respuesta resumida
Podés explicarlo como una cadena de responsabilidades:
Game coordina la partida.
Board gestiona las posiciones.
Player representa a cada jugador.
Dice provee los valores aleatorios.
CLI y PygameUI son las interfaces que comunican al usuario con Game.
Usá un diagrama simple o lista jerárquica para mostrarlo.
# Uso
Lo usé en la sección Arquitectura y Responsabilidades de JUSTIFICACION.md.

# prompt 3
Necesito mostrar que mi código cumple principios de diseño como responsabilidad única y bajo acoplamiento. ¿Cómo lo puedo escribir en el informe??
# Respuesta resumida
Podés decir:
Cada clase cumple un rol específico sin depender directamente de otras. Por ejemplo, Board administra las posiciones pero no conoce la lógica del turno; eso recae en Game.
# Uso
Lo usé en la sección Principios de Diseño Aplicados
