import unittest
from core.player import Player
from core.checker import Checker
try:
    from excepciones.excepciones import InvalidColorError
except Exception:
    InvalidColorError = ValueError


class TestCheckerBasic(unittest.TestCase):
    def setUp(self):
        self.white = Player("Zoe", "white")
        self.black = Player("Guada", "black")

    def test_construct_on_board(self):
        c = Checker("white", self.white, point=5)
        self.assertTrue(c.is_on_board())
        self.assertEqual(c.point, 5)
        self.assertEqual(c.color, "white")
        self.assertEqual(c.owner.name, "Zoe")

    def test_construct_on_bar_by_default(self):
        c = Checker("black", self.black)
        self.assertTrue(c.is_on_bar())
        self.assertIsNone(c.point)

    def test_move_to_sets_board_state(self):
        c = Checker("white", self.white)  # en barra
        c.move_to(11)
        self.assertTrue(c.is_on_board())
        self.assertEqual(c.point, 11)

    def test_send_to_bar(self):
        c = Checker("black", self.black, point=3)
        c.send_to_bar()
        self.assertTrue(c.is_on_bar())
        self.assertIsNone(c.point)

    def test_bear_off(self):
        c = Checker("white", self.white, point=0)
        c.bear_off()
        self.assertTrue(c.is_borne_off())
        self.assertIsNone(c.point)

    def test_invalid_color_raises(self):
        with self.assertRaises(InvalidColorError):
            Checker("verde", self.white, point=0)

    def test_invalid_point_raises(self):
        with self.assertRaises(ValueError):
            Checker("white", self.white, point=24)
        with self.assertRaises(ValueError):
            Checker("white", self.white, point=-1)

    def test_attribute_convention_double_underscores(self):
        c = Checker("white", self.white, point=0)
        keys = c.__dict__.keys()
        # todos los atributos internos deben estar con __nombre__
        self.assertTrue(all(k.startswith("_Checker__") for k in keys))


if __name__ == "__main__":
    unittest.main()
