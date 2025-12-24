from excepciones.excepciones import InvalidColorError, InvalidDirectionError


class Player:
    """
    Representa un jugador de Backgammon.
    
    Attributes:
        __name__: Nombre del jugador
        __color__: Color de las fichas ("white" o "black")
        __direction__: Dirección de movimiento (-1 para blancas, 1 para negras)
        __uid__: Identificador único opcional del jugador
    """

    __VALID_COLORS__ = ("white", "black")

    def __init__(self, name, color, direction=None, uid=None):
        """
        Inicializa un jugador de Backgammon.
        
        Args:
            name: Nombre del jugador
            color: Color de las fichas ("white" o "black")
            direction: Dirección de movimiento (-1 o 1). Si es None, se infiere del color
            uid: Identificador único opcional
            
        Raises:
            InvalidColorError: Si el color no es "white" o "black"
            InvalidDirectionError: Si la dirección no es -1 o 1
        """
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
    def name(self):
        """
        Retorna el nombre del jugador.
        
        Returns:
            Nombre del jugador
        """
        return self.__name__

    @property
    def color(self):
        """
        Retorna el color de las fichas del jugador.
        
        Returns:
            "white" o "black"
        """
        return self.__color__

    @property
    def direction(self):
        """
        Retorna la dirección de movimiento del jugador.
        
        Returns:
            -1 para blancas, 1 para negras
        """
        return self.__direction__

    @property
    def uid(self):
        """
        Retorna el identificador único del jugador.
        
        Returns:
            UID del jugador o None si no tiene
        """
        return self.__uid__

    def home_range(self):
        """
        Retorna el rango de puntos que conforman la casa del jugador.
        
        Returns:
            range(0, 6) para blancas, range(18, 24) para negras
        """
        return range(0, 6) if self.__color__ == "white" else range(18, 24)

    def opponent_color(self):
        """
        Retorna el color del oponente.
        
        Returns:
            "black" si el jugador es blanco, "white" si es negro
        """
        return "black" if self.__color__ == "white" else "white"

    def __repr__(self):
        """
        Retorna una representación en string del jugador.
        
        Returns:
            String con formato "Player(name=..., color=..., dir=..., uid=...)"
        """
        return f"Player(name={self.__name__!r}, color={self.__color__}, dir={self.__direction__}, uid={self.__uid__!r})"

    def __eq__(self, other):
        """
        Compara dos jugadores por igualdad.
        
        Args:
            other: Objeto a comparar
            
        Returns:
            True si son el mismo jugador (por UID o por nombre+color)
        """
        if not isinstance(other, Player):
            return NotImplemented
        if self.__uid__ and other.__uid__:
            return self.__uid__ == other.__uid__
        return (self.__name__, self.__color__) == (other.__name__, other.__color__)