import unittest
from core.player import Player 


class TestPlayerBasics(unittest.TestCase):
    def test_construct_valid_white(self):
        p = Player("White", "white", -1)
        # Acceso intencional a atributos con name mangling para asserts
        self.assertEqual(p._Player__name__, "White")
        self.assertEqual(p._Player__color__, "white")
        self.assertEqual(p._Player__direction__, -1)

    def test_construct_valid_black(self):
        p = Player("Black", "black", 1)
        self.assertEqual(p._Player__name__, "Black")
        self.assertEqual(p._Player__color__, "black")
        self.assertEqual(p._Player__direction__, 1)

    def test_repr_contains_name_and_color(self):
        p = Player("Zoe", "white", -1)
        r = repr(p)
        self.assertIn("Zoe", r)
        self.assertIn("white", r)
        # formato esperado: Player(name='Zoe', color=white, dir=-1)
        self.assertTrue(r.startswith("Player(") and "dir=" in r)


class TestPlayerValidations(unittest.TestCase):
    def test_invalid_color_raises(self):
        with self.assertRaises(AssertionError):
            Player("Bad", "WHITE", -1)  # case-sensitive, solo 'white' o 'black'
        with self.assertRaises(AssertionError):
            Player("Bad", "amarillo", -1)

    def test_invalid_direction_raises(self):
        with self.assertRaises(AssertionError):
            Player("Bad", "white", 0)
        with self.assertRaises(AssertionError):
            Player("Bad", "black", 2)
        with self.assertRaises(AssertionError):
            Player("Bad", "black", -2)


class TestPlayerAttributeConvention(unittest.TestCase):
    def test_instance_attributes_have_double_underscores(self):
        p = Player("Conv", "white", -1)
        # Todos los atributos de instancia deben tener __prefijo__ y __sufijo__
        for attr in vars(p).keys():
            self.assertTrue(
                attr.startswith("__") and attr.endswith("__"),
                msg=f"Atributo sin __prefijo__/__sufijo__: {attr}"
            )


if __name__ == "__main__":
    unittest.main()
