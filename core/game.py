from core.player import Player
from core.board import Board
from core.dice import Dice


class Game:
    """
    Coordina el flujo general del juego de Backgammon.
    
    Attributes:
        __board__: Tablero del juego
        __white__: Jugador con fichas blancas
        __black__: Jugador con fichas negras
        __dice__: Dados del juego
        __current_player__: Jugador que tiene el turno actual
        __winner__: Jugador ganador (None si no hay ganador aún)
        __last_roll__: Última tirada de dados realizada
    """

    def __init__(self, board, white, black, dice):
        """
        Inicializa una partida de Backgammon.
        
        Args:
            board: Tablero del juego
            white: Jugador con fichas blancas
            black: Jugador con fichas negras
            dice: Dados del juego
        """
        self.__board__ = board
        self.__white__ = white
        self.__black__ = black
        self.__dice__ = dice
        self.__current_player__ = white
        self.__winner__ = None
        self.__last_roll__ = None

    @property
    def current_player(self):
        """
        Retorna el jugador que tiene el turno actual.
        
        Returns:
            Jugador con el turno actual
        """
        return self.__current_player__

    @property
    def winner(self):
        """
        Retorna el jugador ganador de la partida.
        
        Returns:
            Jugador ganador o None si aún no hay ganador
        """
        return self.__winner__

    @property
    def last_roll(self):
        """
        Retorna la última tirada de dados realizada.
        
        Returns:
            Lista con valores de dados o None si no se ha tirado
        """
        return self.__last_roll__

    def roll_dice(self):
        """
        Tira los dados y almacena el resultado.
        
        Returns:
            Lista con los valores obtenidos (2 o 4 elementos)
        """
        self.__last_roll__ = self.__dice__.roll()
        return self.__last_roll__

    def legal_moves(self):
        """
        Obtiene los movimientos legales para el jugador actual.
        
        Returns:
            Lista de movimientos válidos según la última tirada,
            o lista vacía si no se han tirado los dados
        """
        if not self.__last_roll__:
            return []
        return self.__board__.legal_moves(self.__current_player__, self.__last_roll__)

    def make_move(self, move):
        """
        Ejecuta un movimiento en el tablero y verifica si hay ganador.
        
        Args:
            move: Movimiento a ejecutar (formato según tipo de movimiento)
        """
        self.__board__.apply_move(self.__current_player__, move)
        if self.__board__.has_won(self.__current_player__):
            self.__winner__ = self.__current_player__

    def end_turn(self):
        """
        Finaliza el turno actual y pasa al siguiente jugador.
        Limpia la última tirada de dados.
        """
        self.__current_player__ = (
            self.__black__ if self.__current_player__ is self.__white__ else self.__white__
        )
        self.__last_roll__ = None