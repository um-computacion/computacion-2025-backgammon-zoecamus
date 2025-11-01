import pygame
import sys
from core.board import Board
from core.player import Player
from core.dice import Dice
from core.game import Game
from excepciones.excepciones import BackgammonError

# Colores - Paleta de marrones
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

# Colores de acento (tonos tierra)
TERRACOTA = (204, 119, 34)  # Para mensajes importantes
OCRE = (204, 153, 51)  # Para selección
MARRON_ROJIZO = (165, 42, 42)  # Para errores
DORADO_SUAVE = (218, 165, 32)  # Para ganador

# Fichas
FICHA_CLARA = (255, 255, 255)  # Blanco puro
FICHA_OSCURA = (30, 30, 30)    # Negro

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
    print("\n" + "="*50)
    print("        BACKGAMMON ")
    print("="*50)
    
    nombre1 = input("\nJugador 1 (claras): ").strip() or "Jugador 1"
    nombre2 = input("Jugador 2 (oscuras): ").strip() or "Jugador 2"
    
    print(f"\n¡Empieza la partida!")
    print(f"{nombre1} vs {nombre2}\n")
    
    return nombre1, nombre2


class BackgammonUI:
    """Interfaz gráfica de Backgammon."""
    
    def __init__(self, nombre1, nombre2):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Backgammon")
        self.clock = pygame.time.Clock()
        
        # Fuentes
        self.font_small = pygame.font.SysFont("Arial", 16)
        self.font = pygame.font.SysFont("Arial", 20)
        self.font_big = pygame.font.SysFont("Arial", 28, bold=True)
        
        # Lógica del juego
        self.board = Board()
        self.white = Player(nombre1, "white")
        self.black = Player(nombre2, "black")
        self.dice = Dice()
        self.game = Game(self.board, self.white, self.black, self.dice)
        
        # Estado UI
        self.dados_disponibles = []
        self.punto_seleccionado = None
        self.mensaje = f"{nombre1}, haz click en 'TIRAR DADOS'"
        self.color_mensaje = CREMA
        
        self.running = True
        
        # Calcular posiciones
        self.calcular_geometria()
    
    def calcular_geometria(self):
        """Calcula todas las posiciones del tablero."""
        # Área del tablero
        self.tablero_x = MARGEN
        self.tablero_y = MARGEN
        self.tablero_ancho = 12 * ANCHO_TRIANGULO + ESPACIO_BAR
        self.tablero_alto = 2 * ALTO_TRIANGULO + 60
        
        # Bar
        self.bar_x = self.tablero_x + 6 * ANCHO_TRIANGULO
        self.bar_y = self.tablero_y
        self.bar_ancho = ESPACIO_BAR
        self.bar_alto = self.tablero_alto
        
        # Panel derecho
        self.panel_x = self.tablero_x + self.tablero_ancho + 20
        self.panel_ancho = ANCHO - self.panel_x - MARGEN
        
        # Botones
        btn_x = self.panel_x + 10
        self.btn_tirar = pygame.Rect(btn_x, 80, 180, 45)
        self.btn_pasar = pygame.Rect(btn_x, 135, 180, 45)
        
        # Zonas bear-off
        self.bearoff_ancho = 100
        self.bearoff_alto = 150
        # Blancas (derecha abajo)
        self.bearoff_white_x = self.tablero_x + self.tablero_ancho + 10
        self.bearoff_white_y = self.tablero_y + self.tablero_alto - self.bearoff_alto - 10
        # Negras (derecha arriba)
        self.bearoff_black_x = self.tablero_x + self.tablero_ancho + 10
        self.bearoff_black_y = self.tablero_y + 10
    
    def punto_a_coords(self, idx):
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
            x = self.tablero_x + col * ANCHO_TRIANGULO + ANCHO_TRIANGULO // 2 + ESPACIO_BAR
        else:
            x = self.tablero_x + col * ANCHO_TRIANGULO + ANCHO_TRIANGULO // 2
        
        # Y según si es superior o inferior
        if idx <= 11:  # Superior
            y = self.tablero_y + 30
        else:  # Inferior
            y = self.tablero_y + self.tablero_alto - 30
        
        return (int(x), int(y))
    
    def coords_a_punto(self, x, y):
        """Convierte coordenadas a índice de punto. -1=bar, -2=bearoff, None=nada."""
        # Bear-off
        if self.bearoff_white_x <= x <= self.bearoff_white_x + self.bearoff_ancho:
            if self.bearoff_white_y <= y <= self.bearoff_white_y + self.bearoff_alto:
                return -2
        if self.bearoff_black_x <= x <= self.bearoff_black_x + self.bearoff_ancho:
            if self.bearoff_black_y <= y <= self.bearoff_black_y + self.bearoff_alto:
                return -2
        
        # Bar
        if self.bar_x <= x <= self.bar_x + self.bar_ancho:
            if self.bar_y <= y <= self.bar_y + self.bar_alto:
                if self.board.bar_count(self.game.current_player.color) > 0:
                    return -1
        
        # Puntos del tablero
        y_medio = self.tablero_y + self.tablero_alto // 2
        
        if self.tablero_y <= y < y_medio:
            # SUPERIOR (puntos 11-0)
            if x < self.bar_x:  # IZQUIERDA
                col = int((x - self.tablero_x) // ANCHO_TRIANGULO)
            elif x >= self.bar_x + self.bar_ancho:  # DERECHA  
                col = int((x - self.bar_x - self.bar_ancho) // ANCHO_TRIANGULO) + 6
            else:
                return None
            
            if 0 <= col <= 11:
                idx = 11 - col
                return idx
                
        elif y >= y_medio:
            # INFERIOR (puntos 12-23)
            if x < self.bar_x:  # IZQUIERDA
                col = int((x - self.tablero_x) // ANCHO_TRIANGULO)
            elif x >= self.bar_x + self.bar_ancho:  # DERECHA
                col = int((x - self.bar_x - self.bar_ancho) // ANCHO_TRIANGULO) + 6
            else:
                return None
            
            if 0 <= col <= 11:
                idx = col + 12
                return idx
        
        return None
    
    def calcular_dado_usado(self, move):
        """Calcula qué dado se usó."""
        if isinstance(move, tuple) and len(move) == 2:
            if isinstance(move[0], int) and isinstance(move[1], int):
                # Movimiento normal
                dist = abs(move[1] - move[0])
                return dist if dist in self.dados_disponibles else None
            elif move[0] == "reentry":
                # Reingreso
                dst = move[1]
                color = self.game.current_player.color
                if color == "white":
                    dado = 24 - dst
                else:
                    dado = dst + 1
                return dado if dado in self.dados_disponibles else None
            elif move[0] == "bearoff":
                # Bear-off
                src = move[1]
                color = self.game.current_player.color
                if color == "white":
                    dado = src + 1
                else:
                    dado = 24 - src
                return dado if dado in self.dados_disponibles else None
        return None
    
    def dibujar_tablero(self):
        """Dibuja el tablero."""
        self.screen.fill(MARRON_OSCURO)
        
        # Fondo del tablero
        pygame.draw.rect(self.screen, BEIGE, (self.tablero_x, self.tablero_y, self.tablero_ancho, self.tablero_alto))
        
        # Triángulos
        for i in range(24):
            self.dibujar_triangulo(i)
        
        # Bar
        pygame.draw.rect(self.screen, MARRON_CLARO, (self.bar_x, self.bar_y, self.bar_ancho, self.bar_alto))
        txt = self.font_big.render("BAR", True, MARRON_TEXTO)
        txt_rect = txt.get_rect(center=(self.bar_x + self.bar_ancho // 2, self.bar_y + self.bar_alto // 2))
        self.screen.blit(txt, txt_rect)
        
        # Línea divisoria
        y_medio = self.tablero_y + self.tablero_alto // 2
        pygame.draw.line(self.screen, MARRON_OSCURO, (self.tablero_x, y_medio), (self.tablero_x + self.tablero_ancho, y_medio), 3)
    
    def dibujar_triangulo(self, idx):
        """Dibuja un triángulo del tablero."""
        # Calcular posición
        if idx <= 11:  # Superior (11→0)
            col = 11 - idx
            y_base = self.tablero_y
            y_punta = y_base + ALTO_TRIANGULO
            hacia_abajo = True
        else:  # Inferior (12→23)
            col = idx - 12
            y_base = self.tablero_y + self.tablero_alto
            y_punta = y_base - ALTO_TRIANGULO
            hacia_abajo = False
        
        # Ajustar X por el bar
        if col >= 6:
            x_izq = self.tablero_x + col * ANCHO_TRIANGULO + ESPACIO_BAR
        else:
            x_izq = self.tablero_x + col * ANCHO_TRIANGULO
        
        x_der = x_izq + ANCHO_TRIANGULO
        x_medio = (x_izq + x_der) // 2
        
        # Puntos del triángulo
        if hacia_abajo:
            puntos = [(x_izq, y_base), (x_der, y_base), (x_medio, y_punta)]
        else:
            puntos = [(x_izq, y_base), (x_der, y_base), (x_medio, y_punta)]
        
        # Color alternado (tonos marrones)
        color = MARRON_TRIANGULO_1 if (idx % 2 == 0) else MARRON_TRIANGULO_2
        pygame.draw.polygon(self.screen, color, puntos)
        pygame.draw.aalines(self.screen, MARRON_OSCURO, True, puntos, 2)
        
        # Número del punto
        txt_color = CREMA if color == MARRON_TRIANGULO_2 else MARRON_TEXTO
        txt = self.font_small.render(str(idx), True, txt_color)
        txt_rect = txt.get_rect(center=(x_medio, y_base + 10 if hacia_abajo else y_base - 10))
        self.screen.blit(txt, txt_rect)
    
    def dibujar_fichas(self):
        """Dibuja todas las fichas en el tablero."""
        for idx in range(24):
            cell = self.board.points[idx]
            if not cell:
                continue
            
            coords = self.punto_a_coords(idx)
            if not coords:
                continue
            
            x, y = coords
            color = cell["color"]
            count = cell["count"]
            
            # Color de la ficha
            ficha_color = FICHA_CLARA if color == "white" else FICHA_OSCURA
            borde_color = (30, 30, 30) if color == "white" else (255, 255, 255)
            
            # Verificar si este punto está seleccionado
            es_seleccionado = (self.punto_seleccionado == idx)
            
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
                pygame.draw.circle(self.screen, ficha_color, (x, int(y_ficha)), radio)
                pygame.draw.circle(self.screen, borde_color, (x, int(y_ficha)), radio, 2)
                
                # Si está seleccionado, dibujar anillo SOLO en la última ficha (la más alta/visible)
                if es_seleccionado and i == max_visible - 1:
                    pygame.draw.circle(self.screen, OCRE, (x, int(y_ficha)), radio + 4, 4)
            
            # Número si hay más de 5
            if count > 5:
                y_num = y + max_visible * (radio * 2 + espacio) if idx <= 11 else y - max_visible * (radio * 2 + espacio)
                txt = self.font.render(f"+{count - 5}", True, TERRACOTA)
                txt_rect = txt.get_rect(center=(x, int(y_num)))
                self.screen.blit(txt, txt_rect)
    
    def dibujar_bar(self):
        """Dibuja las fichas en la barra."""
        white_count = self.board.bar_count("white")
        black_count = self.board.bar_count("black")
        
        radio = 22
        x_bar = self.bar_x + self.bar_ancho // 2
        
        # Verificar si la barra está seleccionada
        bar_seleccionado = (self.punto_seleccionado == -1)
        
        # Blancas (abajo)
        if white_count > 0:
            y_start = self.bar_y + self.bar_alto - 30
            for i in range(min(white_count, 5)):
                y = y_start - i * (radio * 2 + 5)
                pygame.draw.circle(self.screen, (255, 255, 255), (x_bar, int(y)), radio)
                pygame.draw.circle(self.screen, (30, 30, 30), (x_bar, int(y)), radio, 2)
                # Anillo de selección SOLO en la ficha superior
                if bar_seleccionado and self.game.current_player.color == "white" and i == min(white_count, 5) - 1:
                    pygame.draw.circle(self.screen, OCRE, (x_bar, int(y)), radio + 4, 4)
            if white_count > 5:
                txt = self.font.render(f"+{white_count - 5}", True, CREMA)
                txt_rect = txt.get_rect(center=(x_bar, y_start - 5 * (radio * 2 + 5) - 20))
                self.screen.blit(txt, txt_rect)
        
        # Negras (arriba)
        if black_count > 0:
            y_start = self.bar_y + 30
            for i in range(min(black_count, 5)):
                y = y_start + i * (radio * 2 + 5)
                pygame.draw.circle(self.screen, (30, 30, 30), (x_bar, int(y)), radio)
                pygame.draw.circle(self.screen, (255, 255, 255), (x_bar, int(y)), radio, 2)
                # Anillo de selección SOLO en la ficha superior
                if bar_seleccionado and self.game.current_player.color == "black" and i == min(black_count, 5) - 1:
                    pygame.draw.circle(self.screen, OCRE, (x_bar, int(y)), radio + 4, 4)
            if black_count > 5:
                txt = self.font.render(f"+{black_count - 5}", True, CREMA)
                txt_rect = txt.get_rect(center=(x_bar, y_start + 5 * (radio * 2 + 5) + 20))
                self.screen.blit(txt, txt_rect)
    
    def dibujar_bearoff(self):
        """Dibuja las zonas de bear-off."""
        # Blancas
        pygame.draw.rect(self.screen, MARRON_MEDIO, 
                        (self.bearoff_white_x, self.bearoff_white_y, self.bearoff_ancho, self.bearoff_alto), 
                        border_radius=10)
        pygame.draw.rect(self.screen, BEIGE_CLARO, 
                        (self.bearoff_white_x, self.bearoff_white_y, self.bearoff_ancho, self.bearoff_alto), 
                        3, border_radius=10)
        
        white_off = self.board.borne_off_count("white")
        txt_w = self.font_big.render(str(white_off), True, CREMA)
        txt_rect_w = txt_w.get_rect(center=(self.bearoff_white_x + self.bearoff_ancho // 2, 
                                             self.bearoff_white_y + self.bearoff_alto // 2))
        self.screen.blit(txt_w, txt_rect_w)
        
        # Negras
        pygame.draw.rect(self.screen, MARRON_MEDIO, 
                        (self.bearoff_black_x, self.bearoff_black_y, self.bearoff_ancho, self.bearoff_alto), 
                        border_radius=10)
        pygame.draw.rect(self.screen, MARRON_OSCURO, 
                        (self.bearoff_black_x, self.bearoff_black_y, self.bearoff_ancho, self.bearoff_alto), 
                        3, border_radius=10)
        
        black_off = self.board.borne_off_count("black")
        txt_b = self.font_big.render(str(black_off), True, MARRON_OSCURO)
        txt_rect_b = txt_b.get_rect(center=(self.bearoff_black_x + self.bearoff_ancho // 2, 
                                             self.bearoff_black_y + self.bearoff_alto // 2))
        self.screen.blit(txt_b, txt_rect_b)
    
    def dibujar_panel(self):
        """Dibuja el panel lateral."""
        # Fondo
        pygame.draw.rect(self.screen, CAFE, (self.panel_x, 0, self.panel_ancho, ALTO))
        
        # Título
        txt_titulo = self.font_big.render("BACKGAMMON", True, DORADO_SUAVE)
        self.screen.blit(txt_titulo, (self.panel_x + 10, 20))
        
        # Turno actual
        txt_turno = self.font.render(f"Turno: {self.game.current_player.name}", True, CREMA)
        self.screen.blit(txt_turno, (self.panel_x + 10, 55))
        
        # Botones
        pygame.draw.rect(self.screen, CHOCOLATE, self.btn_tirar, border_radius=5)
        txt_btn1 = self.font.render("TIRAR DADOS", True, CREMA)
        txt_rect1 = txt_btn1.get_rect(center=self.btn_tirar.center)
        self.screen.blit(txt_btn1, txt_rect1)
        
        color_pasar = MARRON_MEDIO if self.dados_disponibles else MARRON_OSCURO
        pygame.draw.rect(self.screen, color_pasar, self.btn_pasar, border_radius=5)
        txt_btn2 = self.font.render("PASAR TURNO", True, CREMA)
        txt_rect2 = txt_btn2.get_rect(center=self.btn_pasar.center)
        self.screen.blit(txt_btn2, txt_rect2)
        
        # Dados disponibles
        if self.dados_disponibles:
            y = 200
            txt_dados = self.font.render("Dados disponibles:", True, CREMA)
            self.screen.blit(txt_dados, (self.panel_x + 10, y))
            
            for i, d in enumerate(self.dados_disponibles):
                x = self.panel_x + 15 + (i % 2) * 65
                y_dado = y + 35 + (i // 2) * 65
                pygame.draw.rect(self.screen, TERRACOTA, (x, y_dado, 55, 55), border_radius=5)
                txt_dado = self.font_big.render(str(d), True, CREMA)
                txt_rect = txt_dado.get_rect(center=(x + 27, y_dado + 27))
                self.screen.blit(txt_dado, txt_rect)
        
        # Mensaje
        y_msg = 450
        palabras = self.mensaje.split()
        linea = ""
        y_actual = y_msg
        
        for palabra in palabras:
            test = linea + palabra + " "
            if self.font.size(test)[0] < self.panel_ancho - 20:
                linea = test
            else:
                if linea:
                    txt = self.font.render(linea, True, self.color_mensaje)
                    self.screen.blit(txt, (self.panel_x + 10, y_actual))
                    y_actual += 25
                linea = palabra + " "
        
        if linea:
            txt = self.font.render(linea, True, self.color_mensaje)
            self.screen.blit(txt, (self.panel_x + 10, y_actual))
        
        # Ganador
        if self.game.winner:
            overlay = pygame.Surface((ANCHO, ALTO))
            overlay.set_alpha(200)
            overlay.fill((50, 30, 10))
            self.screen.blit(overlay, (0, 0))
            
            txt = self.font_big.render(f"¡{self.game.winner.name} GANÓ!", True, DORADO_SUAVE)
            txt_rect = txt.get_rect(center=(ANCHO//2, ALTO//2))
            self.screen.blit(txt, txt_rect)
    
    def manejar_click(self, x, y):
        """Maneja clicks del mouse."""
        if self.game.winner:
            return
        
        # Botón tirar dados
        if self.btn_tirar.collidepoint(x, y):
            if not self.dados_disponibles:
                valores = self.game.roll_dice()
                self.dados_disponibles = list(valores)
                moves = self.board.legal_moves(self.game.current_player, self.dados_disponibles)
                
                if not moves:
                    self.mensaje = "Sin movimientos. Auto-pasando turno..."
                    self.color_mensaje = MARRON_ROJIZO
                    self.game.end_turn()
                    self.dados_disponibles = []
                else:
                    bar_count = self.board.bar_count(self.game.current_player.color)
                    if bar_count > 0:
                        self.mensaje = f"Dados: {valores}. ¡Saca del BAR!"
                        self.color_mensaje = TERRACOTA
                    else:
                        self.mensaje = f"Dados: {valores}. ¡Mueve!"
                        self.color_mensaje = OCRE
            return
        
        # Botón pasar turno
        if self.btn_pasar.collidepoint(x, y):
            if self.dados_disponibles:
                self.game.end_turn()
                self.dados_disponibles = []
                self.punto_seleccionado = None
                self.mensaje = f"Turno de {self.game.current_player.name}"
                self.color_mensaje = CREMA
            return
        
        # Clicks en el tablero
        if not self.dados_disponibles:
            return
        
        punto = self.coords_a_punto(x, y)
        if punto is None:
            return
        
        bar_count = self.board.bar_count(self.game.current_player.color)
        
        # Primera selección
        if self.punto_seleccionado is None:
            if bar_count > 0:
                if punto == -1:
                    self.punto_seleccionado = -1
                    self.mensaje = "BAR seleccionado. Click destino"
                    self.color_mensaje = OCRE
                else:
                    self.mensaje = "¡Primero saca del BAR!"
                    self.color_mensaje = MARRON_ROJIZO
            else:
                if punto == -1:
                    self.mensaje = "BAR vacío"
                    self.color_mensaje = MARRON_ROJIZO
                elif punto == -2:
                    self.mensaje = "Selecciona una ficha primero"
                    self.color_mensaje = MARRON_ROJIZO
                else:
                    cell = self.board.points[punto]
                    if cell and cell["color"] == self.game.current_player.color:
                        self.punto_seleccionado = punto
                        self.mensaje = f"Punto {punto} seleccionado. Click destino"
                        self.color_mensaje = OCRE
                    else:
                        if cell:
                            self.mensaje = f"Punto {punto} no es tuyo"
                        else:
                            self.mensaje = f"Punto {punto} está vacío"
                        self.color_mensaje = MARRON_ROJIZO
        else:
            # Segunda selección (movimiento)
            moves = self.board.legal_moves(self.game.current_player, self.dados_disponibles)
            
            # Construir movimiento
            if self.punto_seleccionado == -1:
                move = ("reentry", punto)
            else:
                bearoff_move = ("bearoff", self.punto_seleccionado)
                if bearoff_move in moves and (punto == -2 or punto == self.punto_seleccionado):
                    move = bearoff_move
                else:
                    move = (self.punto_seleccionado, punto)
            
            # Ejecutar si es legal
            if move in moves:
                try:
                    dado = self.calcular_dado_usado(move)
                    if dado and dado in self.dados_disponibles:
                        self.game.make_move(move)
                        self.dados_disponibles.remove(dado)
                        
                        if isinstance(move, tuple) and move[0] == "bearoff":
                            self.mensaje = f"✓ Sacaste del punto {move[1]}"
                        elif isinstance(move, tuple) and move[0] == "reentry":
                            self.mensaje = f"✓ BAR → punto {punto}"
                        else:
                            self.mensaje = f"✓ Punto {self.punto_seleccionado} → {punto}"
                        
                        self.color_mensaje = OCRE
                        self.punto_seleccionado = None
                        
                        # Verificar ganador
                        if self.game.winner:
                            self.mensaje = f"¡{self.game.winner.name} GANÓ!"
                            self.color_mensaje = DORADO_SUAVE
                        # Auto-terminar si no hay dados
                        elif not self.dados_disponibles:
                            self.game.end_turn()
                            self.mensaje = f"Turno de {self.game.current_player.name}"
                            self.color_mensaje = CREMA
                        # Auto-terminar si no hay movimientos
                        else:
                            moves = self.board.legal_moves(self.game.current_player, self.dados_disponibles)
                            if not moves:
                                self.game.end_turn()
                                self.dados_disponibles = []
                                self.mensaje = "Sin más movimientos"
                                self.color_mensaje = MARRON_ROJIZO
                    else:
                        self.mensaje = "Error calculando dado"
                        self.color_mensaje = MARRON_ROJIZO
                        self.punto_seleccionado = None
                except BackgammonError as e:
                    self.mensaje = f"Error: {str(e)[:30]}"
                    self.color_mensaje = MARRON_ROJIZO
                    self.punto_seleccionado = None
            else:
                self.mensaje = "Movimiento ilegal"
                self.color_mensaje = MARRON_ROJIZO
                self.punto_seleccionado = None
    
    def run(self):
        """Loop principal."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.manejar_click(*event.pos)
            
            self.dibujar_tablero()
            self.dibujar_fichas()
            self.dibujar_bar()
            self.dibujar_bearoff()
            self.dibujar_panel()
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()


def main():
    nombre1, nombre2 = pedir_nombres()
    juego = BackgammonUI(nombre1, nombre2)
    juego.run()


if __name__ == "__main__":
    main()