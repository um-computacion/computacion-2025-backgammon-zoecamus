from __future__ import annotations
from typing import Optional, Literal
from core.player import Player
try:
    from excepciones.excepciones import InvalidColorError
except Exception:
    InvalidColorError = ValueError

BoardState = Literal["board", "bar", "borne_off"]


class Checker:
    """Representa una ficha individual de Backgammon."""

    __VALID_COLORS__ = ("white", "black")

    def __init__(
        self,
        color: str,
        owner: Player,
        point: Optional[int] = None,
        uid: Optional[str] = None,
    ) -> None:
        color = str(color).strip().lower()
        if color not in self.__VALID_COLORS__:
            raise InvalidColorError(f"Color inválido en Checker: {color!r}")

        self.__color__ = color
        self.__owner__ = owner
        self.__uid__ = uid

        if point is None:
            self.__point__ = None
            self.__state__ = "bar"
        else:
            self._validate_point(point)
            self.__point__ = point
            self.__state__ = "board"

    # === PROPERTIES ===
    @property
    def color(self) -> str:
        return self.__color__

    @property
    def owner(self) -> Player:
        return self.__owner__

    @property
    def point(self) -> Optional[int]:
        return self.__point__

    @property
    def state(self) -> BoardState:
        return self.__state__

    @property
    def uid(self) -> Optional[str]:
        return self.__uid__

    # === HELPERS DE ESTADO ===
    def is_on_board(self) -> bool:
        return self.__state__ == "board"

    def is_on_bar(self) -> bool:
        return self.__state__ == "bar"

    def is_borne_off(self) -> bool:
        return self.__state__ == "borne_off"

    # === ACCIONES ===
    def move_to(self, point: int) -> None:
        if self.__state__ == "borne_off":
            raise ValueError("No se puede mover una ficha ya borne off.")
        self._validate_point(point)
        self.__point__ = point
        self.__state__ = "board"

    def send_to_bar(self) -> None:
        self.__point__ = None
        self.__state__ = "bar"

    def bear_off(self) -> None:
        self.__point__ = None
        self.__state__ = "borne_off"

    # === INTERNOS ===
    @staticmethod
    def _validate_point(point: int) -> None:
        if not isinstance(point, int) or not (0 <= point <= 23):
            raise ValueError(f"Punto inválido: {point!r} (esperado 0..23)")

    # === DUNDERS ===
    def __repr__(self) -> str:
        return (
            f"Checker(color={self.__color__!r}, owner={self.__owner__.name!r}, "
            f"point={self.__point__!r}, state={self.__state__!r}, uid={self.__uid__!r})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Checker):
            return NotImplemented
        if self.__uid__ and other.__uid__:
            return self.__uid__ == other.__uid__
        return (
            self.__color__,
            self.__owner__.name,
            self.__point__,
            self.__state__,
        ) == (
            other.__color__,
            other.__owner__.name,
            other.__point__,
            other.__state__,
        )
