class BackgammonError(Exception):
    "Excepción base para el juego de Backgammon"
    pass

class InvalidColorError(BackgammonError):
    "Color inválido al crear un jugador"
    pass

class InvalidDirectionError(BackgammonError):
    "Dirección inválida al crear un jugador"
    pass

class InvalidDiceSidesError(BackgammonError):
    "Se intentó crear un dado con número de caras distinto a 6"
    pass

class InvalidDiceOverrideError(BackgammonError):
    "El override de la tirada de dados es inválido"
    pass

# movimientos 
class InvalidMoveError(BackgammonError):
    "Movimiento que no respeta la regla de Backgammon"
    pass

class BlockedPointError(BackgammonError):
    "Destino bloqueado por 2 o más fichas del rival"
    pass

class OutOfBoundsPointError(BackgammonError):
    "El índice de punto está fuera de 0..23"
    pass

class NotYourCheckerError(BackgammonError):
    "El jugador intentó mover una ficha que no es suya"
    pass

class ReentryRequiredError(BackgammonError):
    "El jugador tiene fichas en la barra y debe reingresarlas primero"
    pass

class IllegalReentryPointError(BackgammonError):
    "El punto de reingreso está bloqueado"
    pass

class BearOffNotAllowedError(BackgammonError):
    "El jugador intentó sacar fichas sin tener todas en casa"
    pass
