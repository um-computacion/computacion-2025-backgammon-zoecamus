import unittest
from core.dice import Dice
from excepciones.excepciones import InvalidDiceSidesError, InvalidDiceOverrideError


class TestDiceBasic(unittest.TestCase):
   def test_roll_values_in_range(self):
       d = Dice(seed=123)
       for _ in range(50):
           vals = d.roll()
           self.assertTrue(all(1 <= v <= 6 for v in vals))


   def test_doubles_return_four_values(self):
       d = Dice()
       d.set_next_override([4, 4, 4, 4])
       vals = d.roll()
       self.assertEqual(vals, [4, 4, 4, 4])


   def test_non_doubles_return_two_values(self):
       d = Dice()
       d.set_next_override([3, 5])
       vals = d.roll()
       self.assertEqual(vals, [3, 5])


   def test_override_is_consumed(self):
       d = Dice()
       d.set_next_override([2, 6])
       self.assertEqual(d.roll(), [2, 6]) 
       vals = d.roll()
       self.assertIn(len(vals), (2, 4))


   def test_last_roll_property(self):
       d = Dice(seed=1)
       self.assertIsNone(d.last_roll)
       vals = d.roll()
       self.assertEqual(d.last_roll, vals) 
       lr = d.last_roll
       lr.append(99)
       self.assertNotEqual(lr, d.last_roll)


class TestDiceValidation(unittest.TestCase):
   def test_invalid_sides_raises(self):
       with self.assertRaises(InvalidDiceSidesError):
           Dice(sides=5)


   def test_invalid_override_length(self):
       d = Dice()
       with self.assertRaises(InvalidDiceOverrideError):
           d.set_next_override([])          # vacío
       with self.assertRaises(InvalidDiceOverrideError):
           d.set_next_override([1])         # 1 valor
       with self.assertRaises(InvalidDiceOverrideError):
           d.set_next_override([1,2,3])     # 3 valores


   def test_invalid_override_values(self):
       d = Dice()
       with self.assertRaises(InvalidDiceOverrideError):
           d.set_next_override([0, 7])  # fuera de rango 1..6


       with self.assertRaises(InvalidDiceOverrideError):
           d.set_next_override([2, 2, 2, 3])  # 4 valores no todos iguales


   def test_attribute_convention(self):
       d = Dice()
       for attr in vars(d).keys():
           self.assertTrue(
               attr.startswith("__") and attr.endswith("__"),
               msg=f"Atributo sin __prefijo__/__sufijo__: {attr}"
           )


if __name__ == "__main__":
   unittest.main()
