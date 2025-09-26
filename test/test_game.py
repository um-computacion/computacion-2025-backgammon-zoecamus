import unittest
from unittest.mock import MagicMock

from core.game import Game
from core.player import Player

class TestGameBasics(unittest.TestCase):
    def setUp(self):
        self.board = MagicMock(name="BoardMock")
        self.dice = MagicMock(name="DiceMock")
        self.white = Player("White", "white")   # direccion inferido -1
        self.black = Player("Black", "black")   # direccion inferido +1
        self.game = Game(self.board, self.white, self.black, self.dice)

    def test_initial_state(self):
        self.assertIs(self.game.current_player, self.white)
        self.assertIsNone(self.game.winner)
        self.assertIsNone(self.game.last_roll)

    def test_roll_dice_stores_values(self):
        self.dice.roll.return_value = [3, 5]
        vals = self.game.roll_dice()
        self.assertEqual(vals, [3, 5])
        self.assertEqual(self.game.last_roll, [3, 5])
        self.dice.roll.assert_called_once()

    def test_legal_moves_delegates_to_board_with_last_roll(self):
        self.dice.roll.return_value = [2, 2, 2, 2]
        self.game.roll_dice()
        self.board.legal_moves.return_value = [("m1",), ("m2",)]
        moves = self.game.legal_moves()
        self.board.legal_moves.assert_called_once_with(self.white, [2, 2, 2, 2])
        self.assertEqual(moves, [("m1",), ("m2",)])

    def test_legal_moves_without_roll_returns_empty(self):
        self.assertEqual(self.game.legal_moves(), [])

    def test_make_move_delegates_and_sets_winner_if_has_won(self):
        self.dice.roll.return_value = [6, 6, 6, 6]
        self.game.roll_dice()
        self.board.apply_move.return_value = None
        self.board.has_won.return_value = True

        self.game.make_move(("dummy-move",))
        self.board.apply_move.assert_called_once_with(self.white, ("dummy-move",))
        self.board.has_won.assert_called_once_with(self.white)
        self.assertIs(self.game.winner, self.white)

    def test_end_turn_switches_player_and_clears_last_roll(self):
        self.dice.roll.return_value = [1, 4]
        self.game.roll_dice()
        self.game.end_turn()
        self.assertIs(self.game.current_player, self.black)
        self.assertIsNone(self.game.last_roll)

        self.game.end_turn()
        self.assertIs(self.game.current_player, self.white)


class TestAttributeConvention(unittest.TestCase):
    def test_instance_attributes_have_double_underscores(self):
        game = Game(MagicMock(), Player("W","white"), Player("B","black"), MagicMock())
        for attr in vars(game).keys():
            self.assertTrue(
                attr.startswith("__") and attr.endswith("__"),
                msg=f"Atributo sin __prefijo__/__sufijo__: {attr}"
            )


if __name__ == "__main__":
    unittest.main()
