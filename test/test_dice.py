import unittest
from core.dice import Dice
from excepciones.excepciones import InvalidDiceSidesError, InvalidDiceOverrideError


class TestDiceExtra(unittest.TestCase):
    """Tests adicionales para mejorar coverage de Dice"""
    
    def test_dice_invalid_sides(self):
        """Test crear dados con número inválido de caras"""
        with self.assertRaises(InvalidDiceSidesError):
            Dice(sides=4)
        
        with self.assertRaises(InvalidDiceSidesError):
            Dice(sides=8)
    
    def test_dice_valid_sides(self):
        """Test crear dados con 6 caras (válido)"""
        dice = Dice(sides=6)
        self.assertIsNotNone(dice)
    
    def test_override_empty(self):
        """Test override vacío"""
        dice = Dice()
        with self.assertRaises(InvalidDiceOverrideError):
            dice.set_next_override([])
    
    def test_override_invalid_length(self):
        """Test override con longitud inválida"""
        dice = Dice()
        
        # Longitud 1
        with self.assertRaises(InvalidDiceOverrideError):
            dice.set_next_override([3])
        
        # Longitud 3
        with self.assertRaises(InvalidDiceOverrideError):
            dice.set_next_override([3, 3, 3])
        
        # Longitud 5
        with self.assertRaises(InvalidDiceOverrideError):
            dice.set_next_override([1, 2, 3, 4, 5])
    
    def test_override_two_values_out_of_range(self):
        """Test override de 2 valores fuera de rango"""
        dice = Dice()
        
        with self.assertRaises(InvalidDiceOverrideError):
            dice.set_next_override([0, 3])
        
        with self.assertRaises(InvalidDiceOverrideError):
            dice.set_next_override([3, 7])
    
    def test_override_four_values_not_equal(self):
        """Test override de 4 valores no iguales"""
        dice = Dice()
        
        with self.assertRaises(InvalidDiceOverrideError):
            dice.set_next_override([3, 3, 3, 4])
        
        with self.assertRaises(InvalidDiceOverrideError):
            dice.set_next_override([2, 2, 3, 3])
    
    def test_override_four_values_out_of_range(self):
        """Test override de 4 dobles fuera de rango"""
        dice = Dice()
        
        with self.assertRaises(InvalidDiceOverrideError):
            dice.set_next_override([0, 0, 0, 0])
        
        with self.assertRaises(InvalidDiceOverrideError):
            dice.set_next_override([7, 7, 7, 7])
    
    def test_override_valid_two_values(self):
        """Test override válido de 2 valores"""
        dice = Dice()
        dice.set_next_override([3, 5])
        result = dice.roll()
        
        self.assertEqual(result, [3, 5])
    
    def test_override_valid_four_values(self):
        """Test override válido de 4 valores (dobles)"""
        dice = Dice()
        dice.set_next_override([4, 4, 4, 4])
        result = dice.roll()
        
        self.assertEqual(result, [4, 4, 4, 4])
    
    def test_last_roll_before_first_roll(self):
        """Test last_roll antes de tirar"""
        dice = Dice()
        self.assertIsNone(dice.last_roll)
    
    def test_last_roll_returns_copy(self):
        """Test que last_roll retorna una copia, no la lista original"""
        dice = Dice()
        dice.set_next_override([3, 4])
        dice.roll()
        
        last = dice.last_roll
        last.append(999)  # Modificar la copia
        
        # El original no debe cambiar
        self.assertEqual(dice.last_roll, [3, 4])
    
    def test_roll_with_seed(self):
        """Test roll con semilla para reproducibilidad"""
        dice1 = Dice(seed=42)
        dice2 = Dice(seed=42)
        
        result1 = dice1.roll()
        result2 = dice2.roll()
        
        # Misma semilla = mismo resultado
        self.assertEqual(result1, result2)
    
    def test_roll_doubles(self):
        """Test que dobles retornan 4 valores"""
        dice = Dice()
        dice.set_next_override([5, 5, 5, 5])
        result = dice.roll()
        
        self.assertEqual(len(result), 4)
        self.assertEqual(result, [5, 5, 5, 5])
    
    def test_roll_non_doubles(self):
        """Test que no-dobles retornan 2 valores"""
        dice = Dice()
        dice.set_next_override([3, 5])
        result = dice.roll()
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result, [3, 5])
    
    def test_override_consumed_after_roll(self):
        """Test que override se consume después de usar"""
        dice = Dice(seed=100)
        
        dice.set_next_override([1, 2])
        first_roll = dice.roll()
        self.assertEqual(first_roll, [1, 2])
        
        # Segundo roll debe usar random, no override
        second_roll = dice.roll()
        self.assertNotEqual(second_roll, [1, 2])


if __name__ == "__main__":
    unittest.main()