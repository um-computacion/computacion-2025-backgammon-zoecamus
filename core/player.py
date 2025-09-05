from excepciones.excepciones import InvalidColorError, InvalidDirectionError

class Player:

    __VALID_COLORS__ = ("white", "black")

    def __init__(self, name: str, color: str, direction: int | None = None, uid: str | None = None):
        color = str(color).strip()
        if color not in self.__VALID_COLORS__:
            raise InvalidColorError(f"Color inválido: {color!r}")

        if direction is None:
            direction = -1 if color == "white" else 1

        if direction not in (-1, 1):
            raise InvalidDirectionError(f"Dirección inválida: {direction!r}")

        self.__name__ = name
        self.__color__ = color
        self.__direction__ = direction
        self.__uid__ = uid

    @property
    def name(self) -> str:
        return self.__name__

    @property
    def color(self) -> str:
        return self.__color__

    @property
    def direction(self) -> int:
        return self.__direction__

    @property
    def uid(self) -> str | None:
        return self.__uid__

    def home_range(self) -> range:
        return range(0, 6) if self.__color__ == "white" else range(18, 24)

    def opponent_color(self) -> str:
        return "black" if self.__color__ == "white" else "white"

    def __repr__(self) -> str:
        return f"Player(name={self.__name__!r}, color={self.__color__}, dir={self.__direction__}, uid={self.__uid__!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return NotImplemented
        if self.__uid__ and other.__uid__:
            return self.__uid__ == other.__uid__
        return (self.__name__, self.__color__) == (other.__name__, other.__color__)
