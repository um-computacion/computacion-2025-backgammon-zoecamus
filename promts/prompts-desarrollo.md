# promt 1
Estoy haciendo tests en Python y quiero aislar mi clase Game de Board y Dice. ¿Cómo puedo usar magicmock para simular que el dado siempre devuelve un valor fijo y para verificar que se llamen los métodos de Board?
# Respuesta resumida
MagicMock sirve para crear objetos falsos configurables. Ejemplo:
fake_dice = MagicMock()
fake_dice.roll.return_value = [3,5]
...
Se puede usar assert_called_once_with para verificar llamadas.
# Uso 
Usé esto para escribir mis tests en test/test_game.py.