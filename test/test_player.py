import unittest
from core.player import Player
from excepciones.excepciones import InvalidColorError, InvalidDirectionError


class TestPlayerExtra(unittest.TestCase):
    """Tests adicionales para mejorar coverage de Player"""
    
    def test_player_invalid_color(self):
        """Test crear player con color inválido"""
        with self.assertRaises(InvalidColorError):
            Player("Test", "rojo")
    
    def test_player_invalid_direction(self):
        """Test crear player con dirección inválida"""
        with self.assertRaises(InvalidDirectionError):
            Player("Test", "white", direction=0)
        
        with self.assertRaises(InvalidDirectionError):
            Player("Test", "white", direction=2)
    
    def test_player_explicit_direction(self):
        """Test crear player con dirección explícita"""
        # Blanco con dirección -1 explícita
        white = Player("White", "white", direction=-1)
        self.assertEqual(white.direction, -1)
        
        # Negro con dirección 1 explícita
        black = Player("Black", "black", direction=1)
        self.assertEqual(black.direction, 1)
    
    def test_player_home_range(self):
        """Test rangos de casa para cada jugador"""
        white = Player("White", "white")
        black = Player("Black", "black")
        
        # Casa blanca: 0-5
        self.assertEqual(list(white.home_range()), list(range(0, 6)))
        
        # Casa negra: 18-23
        self.assertEqual(list(black.home_range()), list(range(18, 24)))
    
    def test_player_opponent_color(self):
        """Test obtener color del oponente"""
        white = Player("White", "white")
        black = Player("Black", "black")
        
        self.assertEqual(white.opponent_color(), "black")
        self.assertEqual(black.opponent_color(), "white")
    
    def test_player_repr(self):
        """Test representación string de player"""
        player = Player("TestPlayer", "white", uid="ABC123")
        repr_str = repr(player)
        
        self.assertIn("TestPlayer", repr_str)
        self.assertIn("white", repr_str)
        self.assertIn("-1", repr_str)
        self.assertIn("ABC123", repr_str)
    
    def test_player_equality_with_uid(self):
        """Test igualdad con UID"""
        p1 = Player("Player1", "white", uid="A")
        p2 = Player("Player2", "black", uid="A")
        p3 = Player("Player1", "white", uid="B")
        
        # Mismo UID = iguales
        self.assertEqual(p1, p2)
        # Diferente UID = diferentes
        self.assertNotEqual(p1, p3)
    
    def test_player_equality_without_uid(self):
        """Test igualdad sin UID"""
        p1 = Player("TestPlayer", "white")
        p2 = Player("TestPlayer", "white")
        p3 = Player("TestPlayer", "black")
        p4 = Player("OtherPlayer", "white")
        
        # Mismo nombre y color = iguales
        self.assertEqual(p1, p2)
        # Diferente color = diferentes
        self.assertNotEqual(p1, p3)
        # Diferente nombre = diferentes
        self.assertNotEqual(p1, p4)
    
    def test_player_equality_with_non_player(self):
        """Test igualdad con objeto no-Player"""
        player = Player("Test", "white")
        
        self.assertNotEqual(player, "not a player")
        self.assertNotEqual(player, 42)
        self.assertNotEqual(player, None)
    
    def test_player_properties(self):
        """Test todas las propiedades del player"""
        player = Player("TestName", "black", uid="XYZ")
        
        self.assertEqual(player.name, "TestName")
        self.assertEqual(player.color, "black")
        self.assertEqual(player.direction, 1)
        self.assertEqual(player.uid, "XYZ")


if __name__ == "__main__":
    unittest.main()