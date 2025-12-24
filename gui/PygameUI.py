import sys
import pygame
from core.board import Board
from core.player import Player
from core.dice import Dice
from core.game import Game
from excepciones.excepciones import BackgammonError

# Colores
MARRON_OSCURO = (101, 67, 33)
MARRON_MEDIO = (139, 90, 43)
MARRON_CLARO = (205, 133, 63)
BEIGE = (244, 164, 96)
BEIGE_CLARO = (255, 228, 196)
CREMA = (245, 222, 179)
MARRON_TRIANGULO_1 = (160, 100, 50)
MARRON_TRIANGULO_2 = (120, 80, 40)
CAFE = (111, 78, 55)
CHOCOLATE = (210, 105, 30)
MARRON_TEXTO = (80, 50, 20)
ARENA = (194, 178, 128)

TERRACOTA = (204, 119, 34)  # Para mensajes importantes
OCRE = (204, 153, 51)  # Para selección
MARRON_ROJIZO = (165, 42, 42)  # Para errores
DORADO_SUAVE = (218, 165, 32)  # Para ganador

# Fichas
FICHA_CLARA = (255, 255, 255)  # Blanco
FICHA_OSCURA = (30, 30, 30)  # Negro

# Dimensiones
ANCHO = 1400
ALTO = 900
MARGEN = 50
ANCHO_TRIANGULO = 70
ALTO_TRIANGULO = 280
ESPACIO_BAR = 80
FPS = 60


def pedir_nombres():
    """Pide nombres por consola."""
    print("\n" + "=" * 50)
    print("        BACKGAMMON ")
    print("=" * 50)

    nombre1 = input("\nJugador 1 (blancas): ").strip() or "Jugador 1"
    nombre2 = input("Jugador 2 (negras): ").strip() or "Jugador 2"

    print("\n¡Empieza la partida!")
    print(f"{nombre1} vs {nombre2}\n")

    return nombre1, nombre2


class BackgammonUI:
    """Interfaz gráfica de Backgammon."""

    def __init__(self, nombre1, nombre2):
        pygame.init()
        self.__screen__ = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Backgammon")
        self.__clock__ = pygame.time.Clock()

        # Fuentes
        self.__font_small__ = pygame.font.SysFont("Arial", 16)
        self.__font__ = pygame.font.SysFont("Arial", 20)
        self.__font_big__ = pygame.font.SysFont("Arial", 28, bold=True)

        # Lógica del juego
        self.__board__ = Board()
        self.__white__ = Player(nombre1, "white")
        self.__black__ = Player(nombre2, "black")
        self.__dice__ = Dice()
        self.__game__ = Game(self.__board__, self.__white__, self.__black__, self.__dice__)

        # Estado UI
        self.__dados_disponibles__ = []
        self.__punto_seleccionado__ = None
        self.__mensaje__ = f"{nombre1}, haz click en 'TIRAR DADOS'"
        self.__color_mensaje__ = CREMA

        self.__running__ = True

        # Calcular posiciones
        self.__calcular_geometria__()

    # ==========================
    # PROPIEDADES (opcional)
    # ==========================
    @property
    def __mensaje(self):
        return self.__mensaje__

    @property
    def __color_mensaje(self):
        return self.__color_mensaje__

    # ==========================
    # GEOMETRÍA
    # ==========================
    def __calcular_geometria__(self):
        """Calcula todas las posiciones del tablero."""
        # Área del tablero
        self.__tablero_x__ = MARGEN
        self.__tablero_y__ = MARGEN
        self.__tablero_ancho__ = 12 * ANCHO_TRIANGULO + ESPACIO_BAR
        self.__tablero_alto__ = 2 * ALTO_TRIANGULO + 60

        # Bar
        self.__bar_x__ = self.__tablero_x__ + 6 * ANCHO_TRIANGULO
        self.__bar_y__ = self.__tablero_y__
        self.__bar_ancho__ = ESPACIO_BAR
        self.__bar_alto__ = self.__tablero_alto__

        # Panel derecho
        self.__panel_x__ = self.__tablero_x__ + self.__tablero_ancho__ + 20
        self.__panel_ancho__ = ANCHO - self.__panel_x__ - MARGEN

        # Botones
        btn_x = self.__panel_x__ + 10
        self.__btn_tirar__ = pygame.Rect(btn_x, 80, 180, 45)
        self.__btn_pasar__ = pygame.Rect(btn_x, 135, 180, 45)

        # Zonas bear-off
        self.__bearoff_ancho__ = 100
        self.__bearoff_alto__ = 150
        # Blancas (derecha abajo)
        self.__bearoff_white_x__ = self.__tablero_x__ + self.__tablero_ancho__ + 10
        self.__bearoff_white_y__ = self.__tablero_y__ + self.__tablero_alto__ - self.__bearoff_alto__ - 10
        # Negras (derecha arriba)
        self.__bearoff_black_x__ = self.__tablero_x__ + self.__tablero_ancho__ + 10
        self.__bearoff_black_y__ = self.__tablero_y__ + 10

    # ==========================
    # CONVERSIONES
    # ==========================
    def __punto_a_coords__(self, idx):
        """Convierte índice de punto a coordenadas (x, y) del centro."""
        if idx < 0 or idx > 23:
            return None

        # Calcular columna (0-11)
        if idx <= 11:  # Superior
            col = 11 - idx
        else:  # Inferior
            col = idx - 12

        # Ajustar por el bar
        if col >= 6:
            x = (
                self.__tablero_x__
                + col * ANCHO_TRIANGULO
                + ANCHO_TRIANGULO // 2
                + ESPACIO_BAR
            )
        else:
            x = self.__tablero_x__ + col * ANCHO_TRIANGULO + ANCHO_TRIANGULO // 2

        # Y según si es superior o inferior
        if idx <= 11:  # Superior
            y = self.__tablero_y__ + 30
        else:  # Inferior
            y = self.__tablero_y__ + self.__tablero_alto__ - 30

        return (int(x), int(y))

    def __coords_a_punto__(self, x, y):
        """Convierte coordenadas a índice de punto. -1=bar, -2=bearoff, None=nada."""
        # Bear-off
        if self.__bearoff_white_x__ <= x <= self.__bearoff_white_x__ + self.__bearoff_ancho__:
            if self.__bearoff_white_y__ <= y <= self.__bearoff_white_y__ + self.__bearoff_alto__:
                return -2
        if self.__bearoff_black_x__ <= x <= self.__bearoff_black_x__ + self.__bearoff_ancho__:
            if self.__bearoff_black_y__ <= y <= self.__bearoff_black_y__ + self.__bearoff_alto__:
                return -2

        # Bar
        if self.__bar_x__ <= x <= self.__bar_x__ + self.__bar_ancho__:
            if self.__bar_y__ <= y <= self.__bar_y__ + self.__bar_alto__:
                if self.__board__.bar_count(self.__game__.current_player.color) > 0:
                    return -1

        # Puntos del tablero
        y_medio = self.__tablero_y__ + self.__tablero_alto__ // 2

        if self.__tablero_y__ <= y < y_medio:
            # SUPERIOR (puntos 11-0)
            if x < self.__bar_x__:  # IZQUIERDA
                col = int((x - self.__tablero_x__) // ANCHO_TRIANGULO)
            elif x >= self.__bar_x__ + self.__bar_ancho__:  # DERECHA
                col = int((x - self.__bar_x__ - self.__bar_ancho__) // ANCHO_TRIANGULO) + 6
            else:
                return None

            if 0 <= col <= 11:
                idx = 11 - col
                return idx

        elif y >= y_medio:
            # INFERIOR (puntos 12-23)
            if x < self.__bar_x__:  # IZQUIERDA
                col = int((x - self.__tablero_x__) // ANCHO_TRIANGULO)
            elif x >= self.__bar_x__ + self.__bar_ancho__:  # DERECHA
                col = int((x - self.__bar_x__ - self.__bar_ancho__) // ANCHO_TRIANGULO) + 6
            else:
                return None

            if 0 <= col <= 11:
                idx = col + 12
                return idx

        return None

    def __calcular_dado_usado__(self, move):
        """Calcula qué dado se usó."""
        if isinstance(move, tuple) and len(move) == 2:
            if isinstance(move[0], int) and isinstance(move[1], int):
                # Movimiento normal
                dist = abs(move[1] - move[0])
                return dist if dist in self.__dados_disponibles__ else None
            if move[0] == "reentry":
                # Reingreso
                dst = move[1]
                color = self.__game__.current_player.color
                if color == "white":
                    dado = 24 - dst
                else:
                    dado = dst + 1
                return dado if dado in self.__dados_disponibles__ else None
            if move[0] == "bearoff":
                # Bear-off
                src = move[1]
                color = self.__game__.current_player.color
                if color == "white":
                    dado = src + 1
                else:
                    dado = 24 - src
                return dado if dado in self.__dados_disponibles__ else None
        return None

    # ==========================
    # DIBUJO
    # ==========================
    def __dibujar_tablero__(self):
        """Dibuja el tablero."""
        self.__screen__.fill(MARRON_OSCURO)

        # Fondo del tablero
        pygame.draw.rect(
            self.__screen__,
            BEIGE,
            (
                self.__tablero_x__,
                self.__tablero_y__,
                self.__tablero_ancho__,
                self.__tablero_alto__,
            ),
        )

        # Triángulos
        for i in range(24):
            self.__dibujar_triangulo__(i)

        # Bar
        pygame.draw.rect(
            self.__screen__,
            MARRON_CLARO,
            (self.__bar_x__, self.__bar_y__, self.__bar_ancho__, self.__bar_alto__),
        )
        txt = self.__font_big__.render("BAR", True, MARRON_TEXTO)
        txt_rect = txt.get_rect(
            center=(
                self.__bar_x__ + self.__bar_ancho__ // 2,
                self.__bar_y__ + self.__bar_alto__ // 2,
            )
        )
        self.__screen__.blit(txt, txt_rect)

        # Línea divisoria
        y_medio = self.__tablero_y__ + self.__tablero_alto__ // 2
        pygame.draw.line(
            self.__screen__,
            MARRON_OSCURO,
            (self.__tablero_x__, y_medio),
            (self.__tablero_x__ + self.__tablero_ancho__, y_medio),
            3,
        )

    def __dibujar_triangulo__(self, idx):
        """Dibuja un triángulo del tablero."""
        # Calcular posición
        if idx <= 11:  # Superior (11→0)
            col = 11 - idx
            y_base = self.__tablero_y__
            y_punta = y_base + ALTO_TRIANGULO
            hacia_abajo = True
        else:  # Inferior (12→23)
            col = idx - 12
            y_base = self.__tablero_y__ + self.__tablero_alto__
            y_punta = y_base - ALTO_TRIANGULO
            hacia_abajo = False

        # Ajustar X por el bar
        if col >= 6:
            x_izq = self.__tablero_x__ + col * ANCHO_TRIANGULO + ESPACIO_BAR
        else:
            x_izq = self.__tablero_x__ + col * ANCHO_TRIANGULO

        x_der = x_izq + ANCHO_TRIANGULO
        x_medio = (x_izq + x_der) // 2

        # Puntos del triángulo
        if hacia_abajo:
            puntos = [(x_izq, y_base), (x_der, y_base), (x_medio, y_punta)]
        else:
            puntos = [(x_izq, y_base), (x_der, y_base), (x_medio, y_punta)]

        # Color alternado (tonos marrones)
        color = MARRON_TRIANGULO_1 if (idx % 2 == 0) else MARRON_TRIANGULO_2
        pygame.draw.polygon(self.__screen__, color, puntos)
        pygame.draw.aalines(self.__screen__, MARRON_OSCURO, True, puntos, 2)

        # Número del punto
        txt_color = CREMA if color == MARRON_TRIANGULO_2 else MARRON_TEXTO
        txt = self.__font_small__.render(str(idx), True, txt_color)
        txt_rect = txt.get_rect(
            center=(x_medio, y_base + 10 if hacia_abajo else y_base - 10)
        )
        self.__screen__.blit(txt, txt_rect)

    def __dibujar_fichas__(self):
        """Dibuja todas las fichas en el tablero."""
        for idx in range(24):
            cell = self.__board__.points[idx]
            if not cell:
                continue

            coords = self.__punto_a_coords__(idx)
            if not coords:
                continue

            x, y = coords
            color = cell["color"]
            count = cell["count"]

            # Color de la ficha
            ficha_color = FICHA_CLARA if color == "white" else FICHA_OSCURA
            borde_color = (30, 30, 30) if color == "white" else (255, 255, 255)

            # Verificar si este punto está seleccionado
            es_seleccionado = self.__punto_seleccionado__ == idx

            # Dibujar hasta 5 fichas visibles
            max_visible = min(count, 5)
            radio = 22
            espacio = 5

            for i in range(max_visible):
                if idx <= 11:  # Superior
                    y_ficha = y + i * (radio * 2 + espacio)
                else:  # Inferior
                    y_ficha = y - i * (radio * 2 + espacio)

                # Dibujar ficha
                pygame.draw.circle(self.__screen__, ficha_color, (x, int(y_ficha)), radio)
                pygame.draw.circle(self.__screen__, borde_color, (x, int(y_ficha)), radio, 2)

                # Si está seleccionado, dibujar anillo SOLO en la última ficha
                if es_seleccionado and i == max_visible - 1:
                    pygame.draw.circle(self.__screen__, OCRE, (x, int(y_ficha)), radio + 4, 4)

            # Número si hay más de 5
            if count > 5:
                if idx <= 11:
                    y_num = y + max_visible * (radio * 2 + espacio)
                else:
                    y_num = y - max_visible * (radio * 2 + espacio)
                txt = self.__font__.render(f"+{count - 5}", True, TERRACOTA)
                txt_rect = txt.get_rect(center=(x, int(y_num)))
                self.__screen__.blit(txt, txt_rect)

    def __dibujar_bar__(self):
        """Dibuja las fichas en la barra."""
        white_count = self.__board__.bar_count("white")
        black_count = self.__board__.bar_count("black")

        radio = 22
        x_bar = self.__bar_x__ + self.__bar_ancho__ // 2

        # Verificar si la barra está seleccionada
        bar_seleccionado = self.__punto_seleccionado__ == -1

        # Blancas (abajo)
        if white_count > 0:
            y_start = self.__bar_y__ + self.__bar_alto__ - 30
            for i in range(min(white_count, 5)):
                y = y_start - i * (radio * 2 + 5)
                pygame.draw.circle(self.__screen__, (255, 255, 255), (x_bar, int(y)), radio)
                pygame.draw.circle(self.__screen__, (30, 30, 30), (x_bar, int(y)), radio, 2)
                if (
                    bar_seleccionado
                    and self.__game__.current_player.color == "white"
                    and i == min(white_count, 5) - 1
                ):
                    pygame.draw.circle(self.__screen__, OCRE, (x_bar, int(y)), radio + 4, 4)
            if white_count > 5:
                txt = self.__font__.render(f"+{white_count - 5}", True, CREMA)
                txt_rect = txt.get_rect(
                    center=(x_bar, y_start - 5 * (radio * 2 + 5) - 20)
                )
                self.__screen__.blit(txt, txt_rect)

        # Negras (arriba)
        if black_count > 0:
            y_start = self.__bar_y__ + 30
            for i in range(min(black_count, 5)):
                y = y_start + i * (radio * 2 + 5)
                pygame.draw.circle(self.__screen__, (30, 30, 30), (x_bar, int(y)), radio)
                pygame.draw.circle(self.__screen__, (255, 255, 255), (x_bar, int(y)), radio, 2)
                if (
                    bar_seleccionado
                    and self.__game__.current_player.color == "black"
                    and i == min(black_count, 5) - 1
                ):
                    pygame.draw.circle(self.__screen__, OCRE, (x_bar, int(y)), radio + 4, 4)
            if black_count > 5:
                txt = self.__font__.render(f"+{black_count - 5}", True, CREMA)
                txt_rect = txt.get_rect(
                    center=(x_bar, y_start + 5 * (radio * 2 + 5) + 20)
                )
                self.__screen__.blit(txt, txt_rect)

    def __dibujar_bearoff__(self):
        """Dibuja las zonas de bear-off."""
        # Blancas
        pygame.draw.rect(
            self.__screen__,
            MARRON_MEDIO,
            (
                self.__bearoff_white_x__,
                self.__bearoff_white_y__,
                self.__bearoff_ancho__,
                self.__bearoff_alto__,
            ),
            border_radius=10,
        )
        pygame.draw.rect(
            self.__screen__,
            BEIGE_CLARO,
            (
                self.__bearoff_white_x__,
                self.__bearoff_white_y__,
                self.__bearoff_ancho__,
                self.__bearoff_alto__,
            ),
            3,
            border_radius=10,
        )

        white_off = self.__board__.borne_off_count("white")
        txt_w = self.__font_big__.render(str(white_off), True, CREMA)
        txt_rect_w = txt_w.get_rect(
            center=(
                self.__bearoff_white_x__ + self.__bearoff_ancho__ // 2,
                self.__bearoff_white_y__ + self.__bearoff_alto__ // 2,
            )
        )
        self.__screen__.blit(txt_w, txt_rect_w)

        # Negras
        pygame.draw.rect(
            self.__screen__,
            MARRON_MEDIO,
            (
                self.__bearoff_black_x__,
                self.__bearoff_black_y__,
                self.__bearoff_ancho__,
                self.__bearoff_alto__,
            ),
            border_radius=10,
        )
        pygame.draw.rect(
            self.__screen__,
            MARRON_OSCURO,
            (
                self.__bearoff_black_x__,
                self.__bearoff_black_y__,
                self.__bearoff_ancho__,
                self.__bearoff_alto__,
            ),
            3,
            border_radius=10,
        )

        black_off = self.__board__.borne_off_count("black")
        txt_b = self.__font_big__.render(str(black_off), True, MARRON_OSCURO)
        txt_rect_b = txt_b.get_rect(
            center=(
                self.__bearoff_black_x__ + self.__bearoff_ancho__ // 2,
                self.__bearoff_black_y__ + self.__bearoff_alto__ // 2,
            )
        )
        self.__screen__.blit(txt_b, txt_rect_b)

    def __dibujar_panel__(self):
        """Dibuja el panel lateral."""
        # Fondo
        pygame.draw.rect(self.__screen__, CAFE, (self.__panel_x__, 0, self.__panel_ancho__, ALTO))

        # Título
        txt_titulo = self.__font_big__.render("BACKGAMMON", True, DORADO_SUAVE)
        self.__screen__.blit(txt_titulo, (self.__panel_x__ + 10, 20))

        # Turno actual
        txt_turno = self.__font__.render(
            f"Turno: {self.__game__.current_player.name}", True, CREMA
        )
        self.__screen__.blit(txt_turno, (self.__panel_x__ + 10, 55))

        # Botones
        pygame.draw.rect(self.__screen__, CHOCOLATE, self.__btn_tirar__, border_radius=5)
        txt_btn1 = self.__font__.render("TIRAR DADOS", True, CREMA)
        txt_rect1 = txt_btn1.get_rect(center=self.__btn_tirar__.center)
        self.__screen__.blit(txt_btn1, txt_rect1)

        color_pasar = MARRON_MEDIO if self.__dados_disponibles__ else MARRON_OSCURO
        pygame.draw.rect(self.__screen__, color_pasar, self.__btn_pasar__, border_radius=5)
        txt_btn2 = self.__font__.render("PASAR TURNO", True, CREMA)
        txt_rect2 = txt_btn2.get_rect(center=self.__btn_pasar__.center)
        self.__screen__.blit(txt_btn2, txt_rect2)

        # Dados disponibles
        if self.__dados_disponibles__:
            y = 200
            txt_dados = self.__font__.render("Dados disponibles:", True, CREMA)
            self.__screen__.blit(txt_dados, (self.__panel_x__ + 10, y))

            for i, d in enumerate(self.__dados_disponibles__):
                x = self.__panel_x__ + 15 + (i % 2) * 65
                y_dado = y + 35 + (i // 2) * 65
                pygame.draw.rect(
                    self.__screen__, TERRACOTA, (x, y_dado, 55, 55), border_radius=5
                )
                txt_dado = self.__font_big__.render(str(d), True, CREMA)
                txt_rect = txt_dado.get_rect(center=(x + 27, y_dado + 27))
                self.__screen__.blit(txt_dado, txt_rect)

        # Mensaje
        y_msg = 450
        palabras = self.__mensaje__.split()
        linea = ""
        y_actual = y_msg

        for palabra in palabras:
            test = linea + palabra + " "
            if self.__font__.size(test)[0] < self.__panel_ancho__ - 20:
                linea = test
            else:
                if linea:
                    txt = self.__font__.render(linea, True, self.__color_mensaje__)
                    self.__screen__.blit(txt, (self.__panel_x__ + 10, y_actual))
                    y_actual += 25
                linea = palabra + " "

        if linea:
            txt = self.__font__.render(linea, True, self.__color_mensaje__)
            self.__screen__.blit(txt, (self.__panel_x__ + 10, y_actual))

        # Ganador
        if self.__game__.winner:
            overlay = pygame.Surface((ANCHO, ALTO))
            overlay.set_alpha(200)
            overlay.fill((50, 30, 10))
            self.__screen__.blit(overlay, (0, 0))

            txt = self.__font_big__.render(
                f"¡{self.__game__.winner.name} GANÓ!", True, DORADO_SUAVE
            )
            txt_rect = txt.get_rect(center=(ANCHO // 2, ALTO // 2))
            self.__screen__.blit(txt, txt_rect)

    # ==========================
    # INPUT
    # ==========================
    def __manejar_click__(self, x, y):
        """Maneja clicks del mouse."""
        if self.__game__.winner:
            return

        # Botón tirar dados
        if self.__btn_tirar__.collidepoint(x, y):
            if not self.__dados_disponibles__:
                valores = self.__game__.roll_dice()
                self.__dados_disponibles__ = list(valores)
                moves = self.__board__.legal_moves(
                    self.__game__.current_player, self.__dados_disponibles__
                )

                if not moves:
                    self.__mensaje__ = "Sin movimientos. Auto-pasando turno..."
                    self.__color_mensaje__ = MARRON_ROJIZO
                    self.__game__.end_turn()
                    self.__dados_disponibles__ = []
                else:
                    bar_count = self.__board__.bar_count(self.__game__.current_player.color)
                    if bar_count > 0:
                        self.__mensaje__ = f"Dados: {valores}. ¡Saca del BAR!"
                        self.__color_mensaje__ = TERRACOTA
                    else:
                        self.__mensaje__ = f"Dados: {valores}. ¡Mueve!"
                        self.__color_mensaje__ = OCRE
            return

        # Botón pasar turno
        if self.__btn_pasar__.collidepoint(x, y):
            if self.__dados_disponibles__:
                self.__game__.end_turn()
                self.__dados_disponibles__ = []
                self.__punto_seleccionado__ = None
                self.__mensaje__ = f"Turno de {self.__game__.current_player.name}"
                self.__color_mensaje__ = CREMA
            return

        # Clicks en el tablero
        if not self.__dados_disponibles__:
            return

        punto = self.__coords_a_punto__(x, y)
        if punto is None:
            return

        bar_count = self.__board__.bar_count(self.__game__.current_player.color)

        # Primera selección
        if self.__punto_seleccionado__ is None:
            if bar_count > 0:
                if punto == -1:
                    self.__punto_seleccionado__ = -1
                    self.__mensaje__ = "BAR seleccionado. Click destino"
                    self.__color_mensaje__ = OCRE
                else:
                    self.__mensaje__ = "¡Primero saca del BAR!"
                    self.__color_mensaje__ = MARRON_ROJIZO
            else:
                if punto == -1:
                    self.__mensaje__ = "BAR vacío"
                    self.__color_mensaje__ = MARRON_ROJIZO
                elif punto == -2:
                    self.__mensaje__ = "Selecciona una ficha primero"
                    self.__color_mensaje__ = MARRON_ROJIZO
                else:
                    cell = self.__board__.points[punto]
                    if cell and cell["color"] == self.__game__.current_player.color:
                        self.__punto_seleccionado__ = punto
                        self.__mensaje__ = f"Punto {punto} seleccionado. Click destino"
                        self.__color_mensaje__ = OCRE
                    else:
                        if cell:
                            self.__mensaje__ = f"Punto {punto} no es tuyo"
                        else:
                            self.__mensaje__ = f"Punto {punto} está vacío"
                        self.__color_mensaje__ = MARRON_ROJIZO
        else:
            # Segunda selección (movimiento)
            moves = self.__board__.legal_moves(
                self.__game__.current_player, self.__dados_disponibles__
            )

            # Construir movimiento
            if self.__punto_seleccionado__ == -1:
                move = ("reentry", punto)
            else:
                bearoff_move = ("bearoff", self.__punto_seleccionado__)
                if bearoff_move in moves and (punto == -2 or punto == self.__punto_seleccionado__):
                    move = bearoff_move
                else:
                    move = (self.__punto_seleccionado__, punto)

            # Ejecutar si es legal
            if move in moves:
                try:
                    dado = self.__calcular_dado_usado__(move)
                    if dado and dado in self.__dados_disponibles__:
                        self.__game__.make_move(move)
                        self.__dados_disponibles__.remove(dado)

                        if isinstance(move, tuple) and move[0] == "bearoff":
                            self.__mensaje__ = f"Sacaste del punto {move[1]}"
                        elif isinstance(move, tuple) and move[0] == "reentry":
                            self.__mensaje__ = f"BAR → punto {punto}"
                        else:
                            self.__mensaje__ = (
                                f"Punto {self.__punto_seleccionado__} → {punto}"
                            )

                        self.__color_mensaje__ = OCRE
                        self.__punto_seleccionado__ = None

                        # Verificar ganador
                        if self.__game__.winner:
                            self.__mensaje__ = f"¡{self.__game__.winner.name} GANÓ!"
                            self.__color_mensaje__ = DORADO_SUAVE
                        # Auto-terminar si no hay dados
                        elif not self.__dados_disponibles__:
                            self.__game__.end_turn()
                            self.__mensaje__ = f"Turno de {self.__game__.current_player.name}"
                            self.__color_mensaje__ = CREMA
                        # Auto-terminar si no hay movimientos
                        else:
                            moves = self.__board__.legal_moves(
                                self.__game__.current_player, self.__dados_disponibles__
                            )
                            if not moves:
                                self.__game__.end_turn()
                                self.__dados_disponibles__ = []
                                self.__mensaje__ = "Sin más movimientos"
                                self.__color_mensaje__ = MARRON_ROJIZO
                    else:
                        self.__mensaje__ = "Error calculando dado"
                        self.__color_mensaje__ = MARRON_ROJIZO
                        self.__punto_seleccionado__ = None
                except BackgammonError as exc:
                    self.__mensaje__ = f"Error: {str(exc)[:30]}"
                    self.__color_mensaje__ = MARRON_ROJIZO
                    self.__punto_seleccionado__ = None
            else:
                self.__mensaje__ = "Movimiento ilegal"
                self.__color_mensaje__ = MARRON_ROJIZO
                self.__punto_seleccionado__ = None

    # ==========================
    # LOOP PRINCIPAL
    # ==========================
    def run(self):
        """Loop principal."""
        while self.__running__:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running__ = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__manejar_click__(*event.pos)

            self.__dibujar_tablero__()
            self.__dibujar_fichas__()
            self.__dibujar_bar__()
            self.__dibujar_bearoff__()
            self.__dibujar_panel__()

            pygame.display.flip()
            self.__clock__.tick(FPS)

        pygame.quit()
        sys.exit()


def main():
    nombre1, nombre2 = pedir_nombres()
    juego = BackgammonUI(nombre1, nombre2)
    juego.run()


if __name__ == "__main__":
    main()
