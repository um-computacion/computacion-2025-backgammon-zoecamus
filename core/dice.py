import random
from excepciones.excepciones import InvalidDiceSidesError, InvalidDiceOverrideError


class Dice:
    """
    Maneja la lógica de tiradas de dados para Backgammon.
    
    Soporta dados de 6 caras y permite override de tiradas para testing.
    Los dobles (valores iguales) retornan 4 valores en lugar de 2.
    
    Attributes:
        __sides__: Número de caras del dado (siempre 6 para Backgammon)
        __rng__: Generador de números aleatorios
        __next_override__: Override para la próxima tirada (para testing)
        __last_roll__: Última tirada realizada
    """
    
    def __init__(self, seed=None, sides=6):
        """
        Inicializa los dados del juego.
        
        Args:
            seed: Semilla para el generador aleatorio (opcional, para testing)
            sides: Número de caras del dado (debe ser 6 para Backgammon)
            
        Raises:
            InvalidDiceSidesError: Si sides no es 6
        """
        if sides != 6:
            raise InvalidDiceSidesError(f"Backgammon usa dados de 6 caras, no {sides}.")
        self.__sides__ = sides
        self.__rng__ = random.Random(seed)
        self.__next_override__ = None
        self.__last_roll__ = None

    def roll(self):
        """
        Realiza una tirada de dados.
        
        Si hay un override configurado, lo usa y lo consume.
        Si los valores son iguales (dobles), retorna 4 valores.
        Si los valores son distintos, retorna 2 valores.
        
        Returns:
            Lista con 2 valores (distintos) o 4 valores (dobles)
        """
        if self.__next_override__ is not None:
            vals = self.__consume_override__()
        else:
            a = self.__rng__.randint(1, self.__sides__)
            b = self.__rng__.randint(1, self.__sides__)
            vals = [a, a, a, a] if a == b else [a, b]

        self.__last_roll__ = list(vals)
        return self.__last_roll__

    def set_next_override(self, values):
        """
        Configura un override para la próxima tirada (útil para testing).
        
        El override se consume en la siguiente llamada a roll().
        
        Args:
            values: Lista de 2 valores (tirada normal) o 4 valores iguales (dobles)
            
        Raises:
            InvalidDiceOverrideError: Si el formato o valores son inválidos
        """
        vals = list(values)
        self.__validate_override__(vals)
        self.__next_override__ = vals

    @property
    def last_roll(self):
        """
        Retorna la última tirada realizada.
        
        Returns:
            Lista con los valores de la última tirada, o None si no se ha tirado.
            Retorna una copia para evitar modificaciones externas.
        """
        return None if self.__last_roll__ is None else list(self.__last_roll__)

    def __consume_override__(self):
        """
        Consume el override configurado y lo limpia.
        
        Returns:
            Copia del override configurado
        """
        vals = self.__next_override__
        self.__next_override__ = None
        return list(vals)

    def __validate_override__(self, vals):
        """
        Valida que un override tenga formato y valores correctos.
        
        Args:
            vals: Lista de valores a validar
            
        Raises:
            InvalidDiceOverrideError: Si el override es inválido
        """
        if not vals:
            raise InvalidDiceOverrideError("Override vacío.")
        
        if len(vals) == 2:
            if not all(1 <= v <= self.__sides__ for v in vals):
                raise InvalidDiceOverrideError("Valores fuera de rango 1..6 en override de 2.")
            return
        
        if len(vals) == 4:
            if len(set(vals)) != 1:
                raise InvalidDiceOverrideError("Override de 4 valores debe ser todos iguales (dobles).")
            n = vals[0]
            if not (1 <= n <= self.__sides__):
                raise InvalidDiceOverrideError("Valores fuera de rango 1..6 en override de 4.")
            return
        
        raise InvalidDiceOverrideError("Formato de override inválido (usa 2 valores o 4 dobles).")