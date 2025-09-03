class Player:

    def __init__(self, name: str, color: str, direction: int):
        assert color in ("white", "black"), "color inválido"
        assert direction in (-1, 1), "dirección inválida"

        self.__name__ = name
        self.__color__ = color
        self.__direction__ = direction


    def __repr__(self):
        return f"Player(name={self.__name__!r}, color={self.__color__}, dir={self.__direction__})"

