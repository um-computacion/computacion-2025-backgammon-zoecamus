import unittest
from core.checker import Checker
from core.player import Player


class TestCheckerEdgeCases(unittest.TestCase):
    """Tests adicionales para mejorar coverage de Checker"""
    
    def setUp(self):
        self.player = Player("Test", "white")
    
    def test_checker_invalid_color(self):
        """Test crear checker con color inválido"""
        from excepciones.excepciones import InvalidColorError
        with self.assertRaises(InvalidColorError):
            Checker("rojo", self.player)
    
    def test_checker_invalid_point(self):
        """Test crear checker con punto inválido"""
        with self.assertRaises(ValueError):
            Checker("white", self.player, point=25)
        
        with self.assertRaises(ValueError):
            Checker("white", self.player, point=-1)
    
    def test_move_to_borne_off_checker(self):
        """Test que no se puede mover una ficha borne off"""
        checker = Checker("white", self.player, point=2)
        checker.bear_off()
        
        with self.assertRaises(ValueError):
            checker.move_to(3)
    
    def test_checker_equality_with_uid(self):
        """Test igualdad de checkers con UID"""
        c1 = Checker("white", self.player, point=2, uid="A")
        c2 = Checker("white", self.player, point=5, uid="A")
        c3 = Checker("white", self.player, point=2, uid="B")
        
        # Mismos UIDs son iguales
        self.assertEqual(c1, c2)
        # Diferentes UIDs son diferentes
        self.assertNotEqual(c1, c3)
    
    def test_checker_equality_without_uid(self):
        """Test igualdad de checkers sin UID"""
        c1 = Checker("white", self.player, point=2)
        c2 = Checker("white", self.player, point=2)
        
        # Deben ser iguales por atributos
        self.assertEqual(c1, c2)
    
    def test_checker_equality_with_non_checker(self):
        """Test igualdad con objeto no-Checker"""
        checker = Checker("white", self.player)
        self.assertNotEqual(checker, "not a checker")
        self.assertNotEqual(checker, 42)
    
    def test_checker_repr(self):
        """Test representación string de checker"""
        checker = Checker("white", self.player, point=5, uid="X")
        repr_str = repr(checker)
        
        self.assertIn("white", repr_str)
        self.assertIn("5", repr_str)
        self.assertIn("board", repr_str)
        self.assertIn("X", repr_str)
    
    def test_checker_state_transitions(self):
        """Test todas las transiciones de estado"""
        checker = Checker("white", self.player, point=5)
        
        # Estado inicial: board
        self.assertTrue(checker.is_on_board())
        self.assertFalse(checker.is_on_bar())
        self.assertFalse(checker.is_borne_off())
        
        # Enviar a barra
        checker.send_to_bar()
        self.assertFalse(checker.is_on_board())
        self.assertTrue(checker.is_on_bar())
        self.assertFalse(checker.is_borne_off())
        self.assertIsNone(checker.point)
        
        # Volver al tablero
        checker.move_to(10)
        self.assertTrue(checker.is_on_board())
        self.assertFalse(checker.is_on_bar())
        self.assertEqual(checker.point, 10)
        
        # Bear off
        checker.bear_off()
        self.assertFalse(checker.is_on_board())
        self.assertFalse(checker.is_on_bar())
        self.assertTrue(checker.is_borne_off())
        self.assertIsNone(checker.point)
    
    def test_checker_created_on_bar(self):
        """Test crear checker directamente en barra"""
        checker = Checker("black", self.player, point=None)
        
        self.assertTrue(checker.is_on_bar())
        self.assertFalse(checker.is_on_board())
        self.assertIsNone(checker.point)
        self.assertEqual(checker.state, "bar")


if __name__ == "__main__":
    unittest.main()