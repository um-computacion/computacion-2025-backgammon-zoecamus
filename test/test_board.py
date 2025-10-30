import unittest
from core.board import Board
from core.player import Player
from excepciones.excepciones import (
    InvalidMoveError, BlockedPointError, OutOfBoundsPointError,
    NotYourCheckerError, ReentryRequiredError, BearOffNotAllowedError
)


class TestBoardInitialSetup(unittest.TestCase):
    """Tests para la configuración inicial del tablero."""
    
    def setUp(self):
        self.b = Board()

    def test_distribution_totals(self):
        """Verifica que cada jugador comience con 15 fichas."""
        self.assertEqual(self.b.total_on_board("white"), 15)
        self.assertEqual(self.b.total_on_board("black"), 15)

    def test_specific_points(self):
        """Verifica las posiciones iniciales estándar de Backgammon."""
        pts = self.b.points
        # White
        self.assertEqual(pts[23], {"color": "white", "count": 2})
        self.assertEqual(pts[12], {"color": "white", "count": 5})
        self.assertEqual(pts[7],  {"color": "white", "count": 3})
        self.assertEqual(pts[5],  {"color": "white", "count": 5})
        # Black
        self.assertEqual(pts[0],  {"color": "black", "count": 2})
        self.assertEqual(pts[11], {"color": "black", "count": 5})
        self.assertEqual(pts[16], {"color": "black", "count": 3})
        self.assertEqual(pts[18], {"color": "black", "count": 5})

    def test_home_ranges(self):
        """Verifica que los rangos de casa sean correctos."""
        self.assertEqual(list(Board.home_range_for("white")), list(range(0,6)))
        self.assertEqual(list(Board.home_range_for("black")), list(range(18,24)))


class TestBoardStates(unittest.TestCase):
    """Tests para estados del tablero (in_home, has_won)."""
    
    def setUp(self):
        self.b = Board()
        self.white = Player("W", "white")
        self.black = Player("B", "black")

    def test_in_home_false_at_start(self):
        """Al inicio, ningún jugador está en casa."""
        self.assertFalse(self.b.in_home(self.white))
        self.assertFalse(self.b.in_home(self.black))

    def test_has_won_false_initial(self):
        """Al inicio, nadie ha ganado."""
        self.assertFalse(self.b.has_won(self.white))
        self.assertFalse(self.b.has_won(self.black))

    def test_has_won_true_when_borne_off_15(self):
        """Un jugador gana cuando saca las 15 fichas."""
        # Acceder directamente al atributo interno
        self.b.__borne_off_white__ = 15
        self.assertTrue(self.b.has_won(self.white))


class TestLegalMovesBasic(unittest.TestCase):
    """Tests básicos para legal_moves()."""
    
    def setUp(self):
        self.white = Player("W", "white")
        self.black = Player("B", "black")

    def test_empty_dice_returns_empty(self):
        """Sin dados, no hay movimientos legales."""
        b = Board()
        self.assertEqual(b.legal_moves(self.white, []), [])

    def test_legal_moves_from_initial_position(self):
        """Desde posición inicial, debe haber movimientos válidos."""
        b = Board()
        moves = b.legal_moves(self.white, [3, 5])
        self.assertGreater(len(moves), 0)
        for move in moves:
            self.assertIsInstance(move, tuple)

    def test_legal_moves_with_doubles(self):
        """Con dobles, debe considerar 4 movimientos posibles."""
        b = Board()
        moves = b.legal_moves(self.white, [6, 6, 6, 6])
        self.assertGreater(len(moves), 0)


class TestLegalMovesWithBar(unittest.TestCase):
    """Tests para legal_moves() con fichas en la barra."""
    
    def setUp(self):
        self.white = Player("W", "white")
        self.black = Player("B", "black")

    def test_only_reentry_moves_when_on_bar(self):
        """Con fichas en barra, SOLO se pueden hacer reingresos."""
        b = Board()
        b.__bar_white__ = 1
        
        moves = b.legal_moves(self.white, [3, 5])
        
        # Todos los movimientos deben ser reingresos
        for move in moves:
            self.assertEqual(move[0], "reentry")


class TestApplyMoveNormal(unittest.TestCase):
    """Tests para apply_move() con movimientos normales."""
    
    def setUp(self):
        self.white = Player("W", "white")
        self.black = Player("B", "black")

    def test_normal_move_updates_board(self):
        """Un movimiento normal actualiza correctamente el tablero."""
        b = Board()
        initial_count_12 = b.points[12]["count"]
        
        # Mover de punto 12 a punto 10
        b.apply_move(self.white, (12, 10))
        
        # Verificar que se movió la ficha
        self.assertEqual(b.points[12]["count"], initial_count_12 - 1)
        self.assertIsNotNone(b.points[10])
        self.assertEqual(b.points[10]["color"], "white")


class TestApplyMoveReentry(unittest.TestCase):
    """Tests para reingresos desde la barra."""
    
    def setUp(self):
        self.white = Player("W", "white")
        self.black = Player("B", "black")

    def test_must_reenter_before_normal_move(self):
        """Con fichas en barra, se debe reingresar antes de mover."""
        b = Board()
        b.__bar_white__ = 1
        
        with self.assertRaises(ReentryRequiredError):
            b.apply_move(self.white, (12, 10))


class TestBoardRender(unittest.TestCase):
    """Tests para el método render()."""
    
    def test_render_initial_board(self):
        """Verifica que render() genere texto con todos los puntos."""
        b = Board()
        rendered = b.render()
        
        # Debe contener 24 líneas (una por cada punto)
        lines = rendered.split('\n')
        self.assertEqual(len(lines), 24)
        
        # Verificar algunos puntos específicos
        self.assertIn("00:", lines[0])
        self.assertIn("23:", lines[23])
    
    def test_render_shows_occupied_points(self):
        """Verifica que los puntos ocupados muestren color y cantidad."""
        b = Board()
        rendered = b.render()
        
        lines = rendered.split('\n')
        # Punto 0 tiene 2 fichas negras
        self.assertIn("B", lines[0])
        self.assertIn("x2", lines[0])
        
        # Punto 23 tiene 2 fichas blancas  
        self.assertIn("W", lines[23])
        self.assertIn("x2", lines[23])


class TestBoardValidation(unittest.TestCase):
    """Tests para validaciones de puntos."""
    
    def test_validate_point_out_of_bounds_negative(self):
        """Verifica que puntos negativos lancen OutOfBoundsPointError."""
        b = Board()
        white = Player("W", "white")
        
        with self.assertRaises(OutOfBoundsPointError):
            b.apply_move(white, (12, -1))
    
    def test_validate_point_out_of_bounds_too_high(self):
        """Verifica que puntos > 23 lancen OutOfBoundsPointError."""
        b = Board()
        white = Player("W", "white")
        
        with self.assertRaises(OutOfBoundsPointError):
            b.apply_move(white, (12, 24))


class TestBoardApplyMoveErrors(unittest.TestCase):
    """Tests para casos de error en apply_move()."""
    
    def test_invalid_move_format_raises(self):
        """Movimiento con formato inválido lanza InvalidMoveError."""
        b = Board()
        white = Player("W", "white")
        
        with self.assertRaises(InvalidMoveError):
            b.apply_move(white, "string_invalido")


class TestBoardEmptyPoints(unittest.TestCase):
    """Tests para el método _empty_points()."""
    
    def test_empty_points_creates_24_elements(self):
        """Verifica que _empty_points() cree 24 elementos."""
        pts = Board._empty_points()
        self.assertEqual(len(pts), 24)
        self.assertTrue(all(p is None for p in pts))


class TestAttributeConvention(unittest.TestCase):
    """Tests para convención de atributos."""
    
    def test_instance_attributes_have_double_underscores(self):
        """Todos los atributos deben tener prefijo y sufijo __."""
        b = Board()
        for attr in vars(b).keys():
            self.assertTrue(
                attr.startswith("__") and attr.endswith("__"),
                msg=f"Atributo sin __prefijo__/__sufijo__: {attr}"
            )


if __name__ == "__main__":
    unittest.main()