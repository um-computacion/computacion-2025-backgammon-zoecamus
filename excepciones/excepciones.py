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

class InvalidDiceSidesError(BackgammonError):
    """Se intentó crear un dado con cantidad de caras inválida para Backgammon."""
    pass

class InvalidDiceOverrideError(BackgammonError):
    """El override de tirada no cumple con el formato/valores permitidos."""
    pass
