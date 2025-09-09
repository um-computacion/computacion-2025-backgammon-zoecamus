
# prompt 1
Estoy haciendo tests en Python y quiero aislar mi clase Game de Board y Dice. ¿Cómo puedo usar magicmock para simular que el dado siempre devuelve un valor fijo y para verificar que se llamen los métodos de Board?
# Respuesta resumida
MagicMock sirve para crear objetos falsos configurables. Ejemplo:
fake_dice = MagicMock()
fake_dice.roll.return_value = [3,5]
...
Se puede usar assert_called_once_with para verificar llamadas.
# Uso 
Usé esto para escribir mis tests en test/test_game.py.

# prompt 2
Quiero que mi clase Dice en Python, cuando saque dobles, devuelva cuatro valores iguales en la lista (por ejemplo [6,6,6,6]) en lugar de solo dos valores. ¿Cómo puedo implementarlo?
# Respuesta resumida
En el método roll(), tirás dos números con randint. Si son iguales, devolvés cuatro repeticiones de ese valor:
a = random.randint(1,6)
b = random.randint(1,6)
return [a,a,a,a] if a == b else [a,b]
# Uso
Usé esto en dice.py para que los dobles generen cuatro movimientos válidos en Backgammon.