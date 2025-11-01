
# prompt 1
Estoy haciendo tests en Python y quiero aislar mi clase Game de Board y Dice. Cómo puedo usar magicmock para simular que el dado siempre devuelve un valor fijo y para verificar que se llamen los métodos de Board?
# Respuesta resumida
MagicMock sirve para crear objetos falsos configurables. Ejemplo:
fake_dice = MagicMock()
fake_dice.roll.return_value = [3,5]
...
Se puede usar assert_called_once_with para verificar llamadas
# Uso 
Usé esto para escribir mis tests en test/test_game.py

# prompt 2
Quiero que mi clase Dice en Python, cuando saque dobles, devuelva cuatro valores iguales en la lista (por ejemplo [6,6,6,6]) en lugar de solo dos valores. Cómo puedo implementarlo?
# Respuesta resumida
En el método roll(), tirás dos números con randint. Si son iguales, devolvés cuatro repeticiones de ese valor:
a = random.randint(1,6)
b = random.randint(1,6)
return [a,a,a,a] if a == b else [a,b]
# Uso
Usé esto en dice.py para que los dobles generen cuatro movimientos válidos en Backgammon

# prompt 3
Quiero que mi clase Board verifique si un punto está bloqueado para una ficha del color contrario (por ejemplo, más de una ficha enemiga en ese punto) Cómo puedo implementar y testear eso?
# Respuesta resumida
Podés crear un método privado como __is_blocked_for__(color, point) que devuelva True si hay 2 o más fichas del color opuesto.
En tests, simulás el tablero con ese punto configurado y verificás el resultado esperado
# Uso
Lo usé en board.py para restringir movimientos ilegales y en test_board.py para cubrir la validación de bloqueos

# prompt 4
Necesito probar que cuando un jugador hace un movimiento inválido el sistema lance una excepción personalizada
# Respuesta resumida
En unittest, usá with self.assertRaises(InvalidMoveError): y ejecutá el método que debería fallar.
En pytest, podés usar with pytest.raises(InvalidMoveError):.
# Uso
Lo apliqué en test_board.py y test_cli.py para validar la gestión de errores

# prompt 5
Quiero asegurarme de que en mi clase Game, cuando se termina el turno, se cambie correctamente de jugador y se reinicie el último lanzamiento de dados. Cómo puedo testear eso?
# Respuesta resumida
Simulá un estado de turno activo, llamá a end_turn() y luego verificá que current_player haya cambiado y last_roll esté vacío
# Uso
Lo usé en test_game.py para probar la transición de turnos sin afectar la lógica del tablero

# prompt 6
Estoy implementando un CLI interactivo para Backgammon. ¿Cómo puedo testear funciones que usan input() y print() sin que se detenga el test esperando entrada del usuario?
# Respuesta resumida
Usá unittest.mock.patch para reemplazar builtins.input y sys.stdout temporalmente:
@patch("builtins.input", side_effect=["1","3"])  
@patch("sys.stdout", new_callable=io.StringIO)
Así podés simular opciones del usuario y capturar el texto impreso
# Uso
Lo usé en test_cli.py para automatizar las pruebas del menú sin interacción manual

# prompt 7
En PygameUI, necesito que los clics del mouse sobre un punto del tablero seleccionen la ficha correspondiente. ¿Cómo puedo traducir las coordenadas del click a una posición lógica del tablero?
# Respuesta resumida
Definí un método como __obtener_punto_desde_click__(x, y) que calcule el índice según la posición del mouse y las dimensiones del tablero.
Usá divisiones enteras (x // ancho_casilla) y compensaciones visuales.
# Uso
Lo implementé en PygameUI.py para que el usuario pueda mover fichas con clics precisos