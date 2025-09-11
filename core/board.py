from typing import Optional, Dict, List
from core.player import Player

class Board:
    TOTAL_CHECKERS_PER_PLAYER = 15

    def __init__(self):
        self.__points__: List[Optional[Dict[str, object]]] = self._initial_points()
        self.__bar_white__: int = 0
        self.__bar_black__: int = 0
        self.__borne_off_white__: int = 0
        self.__borne_off_black__: int = 0

    @staticmethod
    def _empty_points() -> List[Optional[Dict[str, object]]]:
        return [None for _ in range(24)]

    def _initial_points(self) -> List[Optional[Dict[str, object]]]:
        pts = self._empty_points()

        def put(idx: int, color: str, count: int):
            pts[idx] = {"color": color, "count": count}

        put(23, "white", 2)
        put(12, "white", 5)
        put(7,  "white", 3)
        put(5,  "white", 5)

        put(0,  "black", 2)
        put(11, "black", 5)
        put(16, "black", 3)
        put(18, "black", 5)

        return pts

    @property
    def points(self):
        """Solo lectura (tupla) para tests/debug."""
        return tuple(self.__points__)

    def total_on_board(self, color: str) -> int:
        total = 0
        for cell in self.__points__:
            if cell and cell["color"] == color:
                total += int(cell["count"])
        return total

    def bar_count(self, color: str) -> int:
        return self.__bar_white__ if color == "white" else self.__bar_black__

    def borne_off_count(self, color: str) -> int:
        return self.__borne_off_white__ if color == "white" else self.__borne_off_black__

    @staticmethod
    def home_range_for(color: str):
        """
        Casa:
        - white: 0..5
        - black: 18..23
        """
        return range(0, 6) if color == "white" else range(18, 24)

    def in_home(self, player: Player) -> bool:
        """ True si todas fichas restantes del jugador están en casa
        (y no hay fichas en barra)."""
        color = player.color
        if self.bar_count(color) > 0:
            return False

        total_tablero = self.total_on_board(color)
        total_borne = self.borne_off_count(color)

        if total_borne == self.TOTAL_CHECKERS_PER_PLAYER:
            return True

        hr = self.home_range_for(color)
        dentro = 0
        for i in hr:
            cell = self.__points__[i]
            if cell and cell["color"] == color:
                dentro += int(cell["count"])
        return dentro == total_tablero

    def has_won(self, player: Player) -> bool:
        return self.borne_off_count(player.color) == self.TOTAL_CHECKERS_PER_PLAYER

    def legal_moves(self, player: Player, dice_values):
        """Se implementará en la próxima iteración."""
        return []

    def apply_move(self, player: Player, move):
        """Se implementará en la próxima iteración (incluye hits, barra, borne-off)."""
        raise NotImplementedError("apply_move aún no implementado.")
