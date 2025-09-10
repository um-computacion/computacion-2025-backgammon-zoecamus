from core.player import Player
from core.board import Board
from core.dice import Dice

class Game:

    def __init__(self, board: Board, white: Player, black: Player, dice: Dice):
        self.__board__ = board
        self.__white__ = white
        self.__black__ = black
        self.__dice__ = dice
        self.__current_player__ = white
        self.__winner__ = None
        self.__last_roll__ = None  

    @property
    def current_player(self) -> Player:
        return self.__current_player__

    @property
    def winner(self) -> Player | None:
        return self.__winner__

    @property
    def last_roll(self) -> list[int] | None:
        return self.__last_roll__

    #turnos
    def roll_dice(self) -> list[int]:
        self.__last_roll__ = self.__dice__.roll()
        return self.__last_roll__

    def legal_moves(self) -> list:
        if not self.__last_roll__:
            return []
        return self.__board__.legal_moves(self.__current_player__, self.__last_roll__)

    def make_move(self, move) -> None:
        self.__board__.apply_move(self.__current_player__, move)
        if self.__board__.has_won(self.__current_player__):
            self.__winner__ = self.__current_player__

    def end_turn(self) -> None:
        self.__current_player__ = (
            self.__black__ if self.__current_player__ is self.__white__ else self.__white__
        )
        self.__last_roll__ = None
