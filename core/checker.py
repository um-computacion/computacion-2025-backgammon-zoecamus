from __future__ import annotations
from core.player import Player
try:
    from excepciones.excepciones import InvalidColorError
except Exception:
    InvalidColorError = ValueError


class Checker:
    """
    Representa una ficha individual de Backgammon.
    
    Una ficha puede estar en tres estados:
    - "board": En un punto del tablero (0-23)
    - "bar": En la barra (capturada)
    - "borne_off": Sacada del tablero (ganada)
    
    Attributes:
        __color: Color de la ficha ("white" o "black")
        __owner: Jugador dueño de la ficha
        __point: Punto del tablero donde está (None si no está en tablero)
        __state: Estado actual de la ficha
        __uid: Identificador único opcional
    """

    __VALID_COLORS__ = ("white", "black")

    def __init__(self, color, owner, point=None, uid=None):
        """
        Inicializa una ficha de Backgammon.
        
        Args:
            color: Color de la ficha ("white" o "black")
            owner: Jugador dueño de la ficha
            point: Punto inicial (0-23). Si es None, la ficha inicia en la barra
            uid: Identificador único opcional
            
        Raises:
            InvalidColorError: Si el color no es válido
            ValueError: Si el punto no está en rango 0-23
        """
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
    def color(self):
        """
        Retorna el color de la ficha.
        
        Returns:
            "white" o "black"
        """
        return self.__color__

    @property
    def owner(self):
        """
        Retorna el jugador dueño de la ficha.
        
        Returns:
            Objeto Player dueño de la ficha
        """
        return self.__owner__

    @property
    def point(self):
        """
        Retorna el punto donde está la ficha.
        
        Returns:
            Número de punto (0-23) o None si no está en tablero
        """
        return self.__point__

    @property
    def state(self):
        """
        Retorna el estado actual de la ficha.
        
        Returns:
            "board", "bar" o "borne_off"
        """
        return self.__state__

    @property
    def uid(self):
        """
        Retorna el identificador único de la ficha.
        
        Returns:
            UID de la ficha o None
        """
        return self.__uid__

    # === HELPERS DE ESTADO ===
    def is_on_board(self):
        """
        Verifica si la ficha está en el tablero.
        
        Returns:
            True si está en un punto del tablero
        """
        return self.__state__ == "board"

    def is_on_bar(self):
        """
        Verifica si la ficha está en la barra.
        
        Returns:
            True si está en la barra (capturada)
        """
        return self.__state__ == "bar"

    def is_borne_off(self):
        """
        Verifica si la ficha fue sacada del tablero.
        
        Returns:
            True si ya fue sacada (borne off)
        """
        return self.__state__ == "borne_off"

    # === ACCIONES ===
    def move_to(self, point):
        """
        Mueve la ficha a un punto del tablero.
        
        Args:
            point: Punto destino (0-23)
            
        Raises:
            ValueError: Si la ficha ya fue sacada o el punto es inválido
        """
        if self.__state__ == "borne_off":
            raise ValueError("No se puede mover una ficha ya borne off.")
        self._validate_point(point)
        self.__point__ = point
        self.__state__ = "board"

    def send_to_bar(self):
        """
        Envía la ficha a la barra (captura).
        """
        self.__point__ = None
        self.__state__ = "bar"

    def bear_off(self):
        """
        Saca la ficha del tablero (bearing off).
        """
        self.__point__ = None
        self.__state__ = "borne_off"

    # === INTERNOS ===
    @staticmethod
    def _validate_point(point):
        """
        Valida que un punto esté en el rango válido.
        
        Args:
            point: Número de punto a validar
            
        Raises:
            ValueError: Si el punto no está entre 0 y 23
        """
        if not isinstance(point, int) or not (0 <= point <= 23):
            raise ValueError(f"Punto inválido: {point!r} (esperado 0..23)")

    # === DUNDERS ===
    def __repr__(self):
        """
        Retorna una representación en string de la ficha.
        
        Returns:
            String con formato "Checker(color=..., owner=..., point=..., state=..., uid=...)"
        """
        return (
            f"Checker(color={self.__color__!r}, owner={self.__owner__.name!r}, "
            f"point={self.__point__!r}, state={self.__state__!r}, uid={self.__uid__!r})"
        )

    def __eq__(self, other):
        """
        Compara dos fichas por igualdad.
        
        Args:
            other: Objeto a comparar
            
        Returns:
            True si son la misma ficha (por UID o por atributos)
        """
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