import unittest
from core.player import Player
from excepciones.excepciones import InvalidColorError, InvalidDirectionError


class TestPlayerConstruction(unittest.TestCase):
    def test_valid_white_and_black(self):
        p1 = Player("Zoe", "white")
        self.assertEqual(p1.color, "white")
        self.assertEqual(p1.direction, -1)

        p2 = Player("Bot", "black")
        self.assertEqual(p2.color, "black")
        self.assertEqual(p2.direction, 1)

    def test_invalid_color_raises(self):
        with self.assertRaises(InvalidColorError):
            Player("Bad", "verde")

    def test_invalid_direction_raises(self):
        with self.assertRaises(InvalidDirectionError):
            Player("Bad", "white", direction=0)


class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.white = Player("Alice", "white")
        self.black = Player("Bob", "black")

    def test_home_range(self):
        self.assertEqual(list(self.white.home_range()), list(range(0, 6)))
        self.assertEqual(list(self.black.home_range()), list(range(18, 24)))

    def test_opponent_color(self):
        self.assertEqual(self.white.opponent_color(), "black")
        self.assertEqual(self.black.opponent_color(), "white")


class TestEqAndRepr(unittest.TestCase):
    def test_repr(self):
        p = Player("Ana", "white", uid="u1")
        self.assertIn("Ana", repr(p))
        self.assertIn("white", repr(p))

    def test_eq_with_uid(self):
        a = Player("A", "white", uid="id1")
        b = Player("B", "black", uid="id1")
        self.assertTrue(a == b)

    def test_eq_without_uid(self):
        a = Player("X", "white")
        b = Player("X", "white")
        c = Player("X", "black")
        self.assertTrue(a == b)
        self.assertFalse(a == c)


class TestAttributeConvention(unittest.TestCase):
    def test_instance_attributes_have_double_underscores(self):
        p = Player("Conv", "white")
        for attr in vars(p).keys():
            self.assertTrue(
                attr.startswith("__") and attr.endswith("__"),
                msg=f"Atributo sin __prefijo__/__sufijo__: {attr}"
            )


if __name__ == "__main__":
    unittest.main()
