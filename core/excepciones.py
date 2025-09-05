# exceptions/exceptions.py

class BackgammonError(Exception):
    """Excepción base para el juego Backgammon."""
    pass


class InvalidColorError(BackgammonError):
    """Se intentó crear un jugador con un color inválido."""
    pass


class InvalidDirectionError(BackgammonError):
    """Se intentó asignar una dirección inválida a un jugador."""
    pass
