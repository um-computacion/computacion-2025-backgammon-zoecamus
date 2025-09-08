# core/dice.py
import random
from typing import Iterable, List, Optional
from excepciones.excepciones import InvalidDiceSidesError, InvalidDiceOverrideError

class Dice:
    def __init__(self, seed: Optional[int] = None, sides: int = 6):
        if sides != 6:
            raise InvalidDiceSidesError(f"Backgammon usa dados de 6 caras, no {sides}.")
        self.__sides__ = sides
        self.__rng__ = random.Random(seed)
        self.__next_override__: Optional[List[int]] = None
        self.__last_roll__: Optional[List[int]] = None

    def roll(self) -> List[int]:
        if self.__next_override__ is not None:
            vals = self.__consume_override__()
        else:
            a = self.__rng__.randint(1, self.__sides__)
            b = self.__rng__.randint(1, self.__sides__)
            vals = [a, a, a, a] if a == b else [a, b]

        self.__last_roll__ = list(vals)
        return self.__last_roll__

    def set_next_override(self, values: Iterable[int]) -> None:
        vals = list(values)
        self.__validate_override__(vals)
        self.__next_override__ = vals

    @property
    def last_roll(self) -> Optional[List[int]]:
        """Devuelve la última tirada realizada (o None si aún no se tiró)."""
        return None if self.__last_roll__ is None else list(self.__last_roll__)

    def __consume_override__(self) -> List[int]:
        vals = self.__next_override__
        self.__next_override__ = None
        return list(vals)  

    def __validate_override__(self, vals: List[int]) -> None:
        if not vals:
            raise InvalidDiceOverrideError("Override vacío.")
        if len(vals) == 2:
            if not all(1 <= v <= self.__sides__ for v in vals):
                raise InvalidDiceOverrideError("Valores fuera de rango 1..6 en override de 2.")
            # 2 valores pueden ser iguales o distintos; si iguales, Game/Board lo tratarán como dobles expandidos luego.
            return
        if len(vals) == 4:
            if len(set(vals)) != 1:
                raise InvalidDiceOverrideError("Override de 4 valores debe ser todos iguales (dobles).")
            n = vals[0]
            if not (1 <= n <= self.__sides__):
                raise InvalidDiceOverrideError("Valores fuera de rango 1..6 en override de 4.")
            return
        raise InvalidDiceOverrideError("Formato de override inválido (usa 2 valores o 4 dobles).")
