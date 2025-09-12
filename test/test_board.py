# tests/test_board.py
import unittest
from core.board import Board
from core.player import Player

class TestBoardInitialSetup(unittest.TestCase):
    def setUp(self):
        self.b = Board()

    def test_distribution_totals(self):
        self.assertEqual(self.b.total_on_board("white"), 15)
        self.assertEqual(self.b.total_on_board("black"), 15)

    def test_specific_points(self):
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
        self.assertEqual(list(Board.home_range_for("white")), list(range(0,6)))
        self.assertEqual(list(Board.home_range_for("black")), list(range(18,24)))

class TestBoardStates(unittest.TestCase):
    def setUp(self):
        self.b = Board()
        self.white = Player("W", "white")
        self.black = Player("B", "black")

    def test_in_home_false_at_start(self):
        self.assertFalse(self.b.in_home(self.white))
        self.assertFalse(self.b.in_home(self.black))

    def test_has_won_false_initial(self):
        self.assertFalse(self.b.has_won(self.white))
        self.assertFalse(self.b.has_won(self.black))

    def test_has_won_true_when_borne_off_15(self):
        self.b.__borne_off_white__ = 15
        self.assertTrue(self.b.has_won(self.white))

class TestAttributeConvention(unittest.TestCase):
    def test_instance_attributes_have_double_underscores(self):
        b = Board()
        for attr in vars(b).keys():
            self.assertTrue(
                attr.startswith("__") and attr.endswith("__"),
                msg=f"Atributo sin __prefijo__/__sufijo__: {attr}"
            )

if __name__ == "__main__":
    unittest.main()
