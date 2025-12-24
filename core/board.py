from core.player import Player
from excepciones.excepciones import (
    InvalidMoveError, BlockedPointError, OutOfBoundsPointError,
    NotYourCheckerError,
    ReentryRequiredError, IllegalReentryPointError, BearOffNotAllowedError
)

class Board:
    """
    Representa el tablero de Backgammon con 24 puntos, barras y fichas sacadas.
    
    Attributes:
        __points__: Lista de 24 puntos del tablero
        __bar_white__: Cantidad de fichas blancas en la barra
        __bar_black__: Cantidad de fichas negras en la barra
        __borne_off_white__: Cantidad de fichas blancas sacadas
        __borne_off_black__: Cantidad de fichas negras sacadas
    """
    TOTAL_CHECKERS_PER_PLAYER = 15

    def __init__(self):
        """Inicializa el tablero con la configuración estándar de Backgammon."""
        self.__points__ = self._initial_points()
        self.__bar_white__ = 0
        self.__bar_black__ = 0
        self.__borne_off_white__ = 0
        self.__borne_off_black__ = 0

    @property
    def points(self):
        """
        Retorna una tupla de solo lectura con los puntos del tablero.
        
        Returns:
            Tupla con los 24 puntos del tablero
        """
        return tuple(self.__points__)

    @staticmethod
    def _empty_points():
        """
        Crea una lista de 24 puntos vacíos.
        
        Returns:
            Lista de 24 elementos None
        """
        return [None for _ in range(24)]

    def _initial_points(self):
        """
        Crea la configuración inicial del tablero según las reglas de Backgammon.
        
        Returns:
            Lista con la distribución estándar de fichas
        """
        pts = self._empty_points()

        def put(idx, color, count):
            pts[idx] = {"color": color, "count": count}

        # Fichas blancas
        put(23, "white", 2)
        put(12, "white", 5)
        put(7,  "white", 3)
        put(5,  "white", 5)

        # Fichas negras
        put(0,  "black", 2)
        put(11, "black", 5)
        put(16, "black", 3)
        put(18, "black", 5)

        return pts

    def total_on_board(self, color):
        """
        Cuenta el total de fichas de un color en el tablero.
        
        Args:
            color: Color de las fichas a contar ("white" o "black")
            
        Returns:
            Cantidad total de fichas del color especificado
        """
        total = 0
        for cell in self.__points__:
            if cell and cell["color"] == color:
                total += int(cell["count"])
        return total

    def bar_count(self, color):
        """
        Retorna la cantidad de fichas de un color en la barra.
        
        Args:
            color: Color de las fichas ("white" o "black")
            
        Returns:
            Cantidad de fichas en la barra
        """
        return self.__bar_white__ if color == "white" else self.__bar_black__

    def borne_off_count(self, color):
        """
        Retorna la cantidad de fichas sacadas de un color.
        
        Args:
            color: Color de las fichas ("white" o "black")
            
        Returns:
            Cantidad de fichas sacadas del tablero
        """
        return self.__borne_off_white__ if color == "white" else self.__borne_off_black__

    @staticmethod
    def home_range_for(color):
        """
        Retorna el rango de puntos que conforman la casa de un color.
        
        Args:
            color: Color del jugador ("white" o "black")
            
        Returns:
            range(0, 6) para blancas, range(18, 24) para negras
        """
        return range(0, 6) if color == "white" else range(18, 24)

    def in_home(self, player):
        """
        Verifica si todas las fichas restantes del jugador están en su casa.
        
        Args:
            player: Jugador a verificar
            
        Returns:
            True si todas las fichas están en casa y ninguna en la barra
        """
        color = player.color
        if self.bar_count(color) > 0:
            return False

        total_tablero = self.total_on_board(color)
        total_borne = self.borne_off_count(color)

        if total_borne == self.TOTAL_CHECKERS_PER_PLAYER:
            return True

        hr = self.home_range_for(color)
        dentro = 0
        for i in hr:
            cell = self.__points__[i]
            if cell and cell["color"] == color:
                dentro += int(cell["count"])
        return dentro == total_tablero

    def has_won(self, player):
        """
        Verifica si el jugador ha ganado la partida.
        
        Args:
            player: Jugador a verificar
            
        Returns:
            True si el jugador sacó sus 15 fichas
        """
        return self.borne_off_count(player.color) == self.TOTAL_CHECKERS_PER_PLAYER

    def __validate_point__(self, idx):
        """
        Valida que un índice de punto esté dentro del rango válido.
        
        Args:
            idx: Índice del punto a validar
            
        Raises:
            OutOfBoundsPointError: Si el índice no está entre 0 y 23
        """
        if not (0 <= idx <= 23):
            raise OutOfBoundsPointError(f"Índice fuera de 0..23: {idx}")
    def __is_blocked_for__(self, color, idx):
        """
        Verifica si un punto está bloqueado para un color.
        Un punto está bloqueado si tiene 2 o más fichas del color contrario.
        
        Args:
            color: Color que intenta entrar al punto
            idx: Índice del punto a verificar
            
        Returns:
            True si el punto está bloqueado
        """
        cell = self.__points__[idx]
        return bool(cell and cell["color"] != color and int(cell["count"]) >= 2)

    def __ensure_can_enter__(self, color, dst_idx):
        """
        Valida que un color pueda entrar a un punto específico.
        
        Args:
            color: Color que intenta entrar
            dst_idx: Índice del punto destino
            
        Raises:
            OutOfBoundsPointError: Si el índice es inválido
            IllegalReentryPointError: Si el punto está bloqueado
        """
        self.__validate_point__(dst_idx)
        if self.__is_blocked_for__(color, dst_idx):
            raise IllegalReentryPointError(f"Punto {dst_idx} bloqueado para reingreso")

    def legal_moves(self, player, dice_values):
        """
        Calcula todos los movimientos legales para el jugador actual.
        
        Args:
            player: Jugador que quiere mover
            dice_values: Lista con valores de dados disponibles (2 o 4 elementos)
            
        Returns:
            Lista de movimientos válidos. Cada movimiento es una tupla:
            - ("reentry", destino): reingreso desde barra
            - ("bearoff", origen): sacar ficha
            - (origen, destino): movimiento normal
        """
        if not dice_values:
            return []

        color = player.color
        direction = player.direction
        moves = []

        # Si hay fichas en la barra, SOLO se pueden hacer reingresos
        if self.bar_count(color) > 0:
            for die in set(dice_values):  # valores únicos
                entry_point = self.__calculate_entry_point__(color, die)
                if entry_point is not None and not self.__is_blocked_for__(color, entry_point):
                    moves.append(("reentry", entry_point))
            return moves

        # Si está en casa, considerar bearing off
        can_bear_off = self.in_home(player)

        # Buscar movimientos normales y bearing off
        for point_idx in range(24):
            cell = self.__points__[point_idx]
            if not cell or cell["color"] != color:
                continue

            # Para cada valor de dado disponible
            for die_value in set(dice_values):
                # Movimiento normal
                dest = point_idx + (die_value * direction)
                
                # Bearing off
                if can_bear_off:
                    if self.__can_bear_off_from__(point_idx, die_value, color, direction):
                        moves.append(("bearoff", point_idx))
                        continue

                # Movimiento normal dentro del tablero
                if 0 <= dest <= 23:
                    if not self.__is_blocked_for__(color, dest):
                        moves.append((point_idx, dest))
        return moves

    def __calculate_entry_point__(self, color, die_value):
        """
        Calcula el punto de entrada desde la barra según el color y el dado.
        
        Args:
            color: Color del jugador
            die_value: Valor del dado
            
        Returns:
            Índice del punto de entrada, o None si está fuera de rango
        """
        if color == "white":
            # Blancas entran desde el punto 24 (fuera del tablero) hacia 0
            entry = 24 - die_value
        else:
            # Negras entran desde el punto -1 (fuera del tablero) hacia 23
            entry = -1 + die_value
        
        return entry if 0 <= entry <= 23 else None

    def __can_bear_off_from__(self, point_index, die, color, direction):
        """Determina si una ficha puede ser retirada (bear off) según las reglas del Backgammon."""
        points = self.__points__

        if color == "white" and direction == -1:
            # Caso exacto
            if point_index - die == -1:
                return True
            # Dado alto (por encima del rango de casa)
            if point_index - die < -1:
                # Verificar si quedan fichas más lejos (puntos más grandes)
                for i in range(point_index + 1, 6):  # FIX: Verificar solo puntos MÁS LEJANOS
                    if points[i] and points[i]["color"] == "white":
                        return False
                # No quedan fichas más lejos → se puede sacar
                return True
            return False

        elif color == "black" and direction == 1:
            # Caso exacto
            if point_index + die == 24:
                return True
            # Dado alto (por encima del rango de casa)
            if point_index + die > 24:
                # Verificar si quedan fichas más lejos (puntos más pequeños)
                for i in range(18, point_index):
                    if points[i] and points[i]["color"] == "black":
                        return False
                return True
            return False

        return False



    def apply_move(self, player, move):
        """
        Aplica un movimiento al tablero, modificando su estado.
        
        Args:
            player: Jugador que realiza el movimiento
            move: Movimiento a aplicar (tupla según tipo de movimiento)
            
        Raises:
            ReentryRequiredError: Si hay fichas en barra y no se reingresa
            InvalidMoveError: Si el formato del movimiento es inválido
            NotYourCheckerError: Si intenta mover ficha que no es suya
            BlockedPointError: Si el destino está bloqueado
            BearOffNotAllowedError: Si intenta sacar sin estar en casa
        """
        color = player.color

        # Si hay fichas en la barra, DEBE reingresar
        if self.bar_count(color) > 0:
            if not isinstance(move, tuple) or len(move) != 2 or move[0] != "reentry":
                raise ReentryRequiredError("Tenés fichas en la barra: reingresá primero.")

        # Reingreso desde la barra
        if isinstance(move, tuple) and len(move) == 2 and move[0] == "reentry":
            dst = int(move[1])
            self.__ensure_can_enter__(color, dst)
            
            # Capturar si hay 1 ficha enemiga
            dst_cell = self.__points__[dst]
            if dst_cell and dst_cell["color"] != color and dst_cell["count"] == 1:
                self.__send_to_bar__(dst_cell["color"])
                self.__points__[dst] = None
            
            # Colocar la ficha
            if self.__points__[dst] is None:
                self.__points__[dst] = {"color": color, "count": 1}
            else:
                self.__points__[dst]["count"] += 1
            
            # Decrementar barra
            if color == "white":
                self.__bar_white__ -= 1
            else:
                self.__bar_black__ -= 1
            return

        # Bearing off
        if isinstance(move, tuple) and len(move) == 2 and move[0] == "bearoff":
            if not self.in_home(player):
                raise BearOffNotAllowedError("No podés hacer bearing off si no estás en casa.")
            
            src = int(move[1])
            self.__validate_point__(src)
            
            src_cell = self.__points__[src]
            if not src_cell or src_cell["color"] != color:
                raise NotYourCheckerError(f"No hay ficha tuya en el punto {src}.")
            
            # Sacar la ficha
            src_cell["count"] -= 1
            if src_cell["count"] == 0:
                self.__points__[src] = None
            
            if color == "white":
                self.__borne_off_white__ += 1
            else:
                self.__borne_off_black__ += 1
            return

        # Movimiento normal (origen, destino)
        if isinstance(move, tuple) and len(move) == 2:
            src, dst = int(move[0]), int(move[1])
            self.__validate_point__(src)
            self.__validate_point__(dst)

            src_cell = self.__points__[src]
            if not src_cell or src_cell["color"] != color:
                raise NotYourCheckerError(f"No hay ficha tuya en el punto {src}.")

            if self.__is_blocked_for__(color, dst):
                raise BlockedPointError(f"Destino {dst} bloqueado por el rival.")

            # Capturar si hay 1 ficha enemiga en destino
            dst_cell = self.__points__[dst]
            if dst_cell and dst_cell["color"] != color and dst_cell["count"] == 1:
                self.__send_to_bar__(dst_cell["color"])
                self.__points__[dst] = None

            # Mover la ficha
            src_cell["count"] -= 1
            if src_cell["count"] == 0:
                self.__points__[src] = None

            if self.__points__[dst] is None:
                self.__points__[dst] = {"color": color, "count": 1}
            else:
                self.__points__[dst]["count"] += 1
            return

        raise InvalidMoveError(f"Formato de movimiento inválido: {move!r}")

    def __send_to_bar__(self, color):
        """
        Envía una ficha de un color a la barra.
        
        Args:
            color: Color de la ficha a enviar a la barra
        """
        if color == "white":
            self.__bar_white__ += 1
        else:
            self.__bar_black__ += 1

    def render(self):
        """
        Genera una representación en texto simple del tablero.
        
        Returns:
            String con el estado del tablero punto por punto
        """
        filas = []
        for i, cell in enumerate(self.__points__):
            if cell:
                filas.append(f"{i:02d}: {cell['color'][0].upper()} x{cell['count']}")
            else:
                filas.append(f"{i:02d}: vacío")
        return "\n".join(filas)