import pygame
import sys
from core.board import Board
from core.player import Player
from core.dice import Dice
from core.game import Game
from excepciones.excepciones import BackgammonError

# Colores
MARRON_OSCURO = (101, 67, 33)
MARRON_CLARO = (205, 133, 63)
BEIGE = (244, 164, 96)
BLANCO = (255, 255, 255)
NEGRO = (30, 30, 30)
VERDE = (34, 139, 34)
ROJO = (220, 20, 60)
AZUL = (70, 130, 180)
DORADO = (255, 215, 0)

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
    
    nombre1 = input("\nJugador 1 (blancas ⚪): ").strip() or "Jugador 1"
    nombre2 = input("Jugador 2 (negras ⚫): ").strip() or "Jugador 2"
    
    print(f"\n¡Empieza la partida!")
    print(f"{nombre1} vs {nombre2}\n")
    
    return nombre1, nombre2


class BackgammonUI:
    """Interfaz gráfica de Backgammon."""
    
    def __init__(self, nombre1, nombre2):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption(" Backgammon")
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
        self.color_mensaje = BLANCO
        
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
        
        # Puntos del tablero - USAR LA MISMA LÓGICA QUE dibujar_triangulo
        y_medio = self.tablero_y + self.tablero_alto // 2
        
        if self.tablero_y <= y < y_medio:
            # SUPERIOR (puntos 11-0)
            # Calcular columna visual (0-11)
            if x < self.bar_x:  # IZQUIERDA
                col = int((x - self.tablero_x) // ANCHO_TRIANGULO)
            elif x >= self.bar_x + self.bar_ancho:  # DERECHA  
                col = int((x - self.bar_x - self.bar_ancho) // ANCHO_TRIANGULO) + 6
            else:
                return None
            
            # Convertir col a idx: idx = 11 - col (inverso de dibujar_triangulo)
            if 0 <= col <= 11:
                idx = 11 - col
                print(f"SUPERIOR: x={x}, col={col}, idx={idx}")
                return idx
                
        elif y >= y_medio:
            # INFERIOR (puntos 12-23)
            # Calcular columna visual (0-11)
            if x < self.bar_x:  # IZQUIERDA
                col = int((x - self.tablero_x) // ANCHO_TRIANGULO)
            elif x >= self.bar_x + self.bar_ancho:  # DERECHA
                col = int((x - self.bar_x - self.bar_ancho) // ANCHO_TRIANGULO) + 6
            else:
                return None
            
            # Convertir col a idx: idx = col + 12 (directo de dibujar_triangulo)
            if 0 <= col <= 11:
                idx = col + 12
                print(f"INFERIOR: x={x}, col={col}, idx={idx}")
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
                # Buscar dado exacto o mayor
                if dado in self.dados_disponibles:
                    return dado
                for d in sorted(self.dados_disponibles, reverse=True):
                    if d >= dado:
                        return d
        return None
    
    def dibujar_tablero(self):
        """Dibuja el tablero base."""
        # Fondo
        self.screen.fill(MARRON_OSCURO)
        
        # Tablero
        pygame.draw.rect(self.screen, MARRON_CLARO, 
                        (self.tablero_x, self.tablero_y, self.tablero_ancho, self.tablero_alto))
        
        # Borde del tablero
        pygame.draw.rect(self.screen, DORADO,
                        (self.tablero_x, self.tablero_y, self.tablero_ancho, self.tablero_alto), 3)
        
        # Línea divisoria horizontal
        y_medio = self.tablero_y + self.tablero_alto // 2
        pygame.draw.line(self.screen, MARRON_OSCURO,
                        (self.tablero_x, y_medio),
                        (self.tablero_x + self.tablero_ancho, y_medio), 3)
        
        # Bar
        pygame.draw.rect(self.screen, MARRON_OSCURO,
                        (self.bar_x, self.bar_y, self.bar_ancho, self.bar_alto))
        txt = self.font_big.render("BAR", True, DORADO)
        txt_rect = txt.get_rect(center=(self.bar_x + self.bar_ancho//2, y_medio))
        self.screen.blit(txt, txt_rect)
        
        # Triángulos
        for i in range(24):
            self.dibujar_triangulo(i)
    
    def dibujar_triangulo(self, idx):
        """Dibuja un triángulo (punto)."""
        if idx < 0 or idx > 23:
            return
        
        # Calcular posición base
        if idx <= 11:  # Superior
            col = 11 - idx
            y_base = self.tablero_y
            direccion = 1  # Apunta hacia abajo
        else:  # Inferior
            col = idx - 12
            y_base = self.tablero_y + self.tablero_alto
            direccion = -1  # Apunta hacia arriba
        
        # Ajustar X por el bar
        if col >= 6:
            x_base = self.tablero_x + col * ANCHO_TRIANGULO + ESPACIO_BAR
        else:
            x_base = self.tablero_x + col * ANCHO_TRIANGULO
        
        # Color alternado
        color = BEIGE if idx % 2 == 0 else MARRON_OSCURO
        
        # Puntos del triángulo
        if direccion == 1:  # Apunta abajo
            puntos = [
                (x_base, y_base),
                (x_base + ANCHO_TRIANGULO, y_base),
                (x_base + ANCHO_TRIANGULO // 2, y_base + ALTO_TRIANGULO)
            ]
        else:  # Apunta arriba
            puntos = [
                (x_base, y_base),
                (x_base + ANCHO_TRIANGULO, y_base),
                (x_base + ANCHO_TRIANGULO // 2, y_base - ALTO_TRIANGULO)
            ]
        
        pygame.draw.polygon(self.screen, color, puntos)
        pygame.draw.polygon(self.screen, NEGRO, puntos, 2)
        
        # Número del punto
        txt = self.font_small.render(str(idx), True, 
                                     NEGRO if color == BEIGE else BEIGE)
        if direccion == 1:
            txt_rect = txt.get_rect(center=(x_base + ANCHO_TRIANGULO//2, y_base + 15))
        else:
            txt_rect = txt.get_rect(center=(x_base + ANCHO_TRIANGULO//2, y_base - 15))
        self.screen.blit(txt, txt_rect)
    
    def dibujar_fichas(self):
        """Dibuja todas las fichas."""
        for idx in range(24):
            cell = self.board.points[idx]
            if not cell:
                continue
            
            coords = self.punto_a_coords(idx)
            if not coords:
                continue
            
            x, y = coords
            color = BLANCO if cell["color"] == "white" else NEGRO
            count = cell["count"]
            
            # Dirección de apilado
            if idx <= 11:  # Superior
                dy = 30
            else:  # Inferior
                dy = -30
            
            # Dibujar hasta 5 fichas
            max_show = min(count, 5)
            for j in range(max_show):
                y_ficha = y + j * dy
                
                # Highlight si seleccionado
                if self.punto_seleccionado == idx:
                    pygame.draw.circle(self.screen, AZUL, (x, y_ficha), 27)
                
                pygame.draw.circle(self.screen, color, (x, y_ficha), 25)
                pygame.draw.circle(self.screen, NEGRO, (x, y_ficha), 25, 2)
            
            # Número si hay más de 5
            if count > 5:
                txt = self.font_big.render(str(count), True, ROJO)
                txt_rect = txt.get_rect(center=(x, y + 2.5 * dy))
                self.screen.blit(txt, txt_rect)
    
    def dibujar_bar(self):
        """Dibuja fichas en el bar."""
        x_center = self.bar_x + self.bar_ancho // 2
        
        # Blancas (abajo)
        count_w = self.board.bar_count("white")
        if count_w > 0:
            y_start = self.tablero_y + self.tablero_alto - 50
            for j in range(min(count_w, 5)):
                y = y_start - j * 30
                if self.punto_seleccionado == -1 and self.game.current_player.color == "white":
                    pygame.draw.circle(self.screen, AZUL, (x_center, y), 27)
                pygame.draw.circle(self.screen, BLANCO, (x_center, y), 25)
                pygame.draw.circle(self.screen, NEGRO, (x_center, y), 25, 2)
            if count_w > 5:
                txt = self.font.render(str(count_w), True, ROJO)
                self.screen.blit(txt, (x_center - 10, y_start - 160))
        
        # Negras (arriba)
        count_b = self.board.bar_count("black")
        if count_b > 0:
            y_start = self.tablero_y + 50
            for j in range(min(count_b, 5)):
                y = y_start + j * 30
                if self.punto_seleccionado == -1 and self.game.current_player.color == "black":
                    pygame.draw.circle(self.screen, AZUL, (x_center, y), 27)
                pygame.draw.circle(self.screen, NEGRO, (x_center, y), 25)
                pygame.draw.circle(self.screen, BLANCO, (x_center, y), 25, 2)
            if count_b > 5:
                txt = self.font.render(str(count_b), True, ROJO)
                self.screen.blit(txt, (x_center - 10, y_start + 160))
    
    def dibujar_bearoff(self):
        """Dibuja zonas de bear-off."""
        # Blancas (abajo derecha)
        pygame.draw.rect(self.screen, MARRON_CLARO,
                        (self.bearoff_white_x, self.bearoff_white_y, 
                         self.bearoff_ancho, self.bearoff_alto))
        pygame.draw.rect(self.screen, DORADO,
                        (self.bearoff_white_x, self.bearoff_white_y,
                         self.bearoff_ancho, self.bearoff_alto), 3)
        
        count_w = self.board.borne_off_count("white")
        txt = self.font_big.render(str(count_w), True, BLANCO)
        txt_rect = txt.get_rect(center=(self.bearoff_white_x + self.bearoff_ancho//2,
                                        self.bearoff_white_y + self.bearoff_alto//2))
        self.screen.blit(txt, txt_rect)
        
        txt_out = self.font_small.render("OUT", True, DORADO)
        self.screen.blit(txt_out, (self.bearoff_white_x + 20, self.bearoff_white_y + 10))
        
        # Negras (arriba derecha)
        pygame.draw.rect(self.screen, MARRON_CLARO,
                        (self.bearoff_black_x, self.bearoff_black_y,
                         self.bearoff_ancho, self.bearoff_alto))
        pygame.draw.rect(self.screen, DORADO,
                        (self.bearoff_black_x, self.bearoff_black_y,
                         self.bearoff_ancho, self.bearoff_alto), 3)
        
        count_b = self.board.borne_off_count("black")
        txt = self.font_big.render(str(count_b), True, NEGRO)
        txt_rect = txt.get_rect(center=(self.bearoff_black_x + self.bearoff_ancho//2,
                                        self.bearoff_black_y + self.bearoff_alto//2))
        self.screen.blit(txt, txt_rect)
        
        txt_out = self.font_small.render("OUT", True, DORADO)
        self.screen.blit(txt_out, (self.bearoff_black_x + 20, self.bearoff_black_y + 10))
    
    def dibujar_panel(self):
        """Dibuja panel de control."""
        # Fondo panel
        pygame.draw.rect(self.screen, (50, 50, 50),
                        (self.panel_x, 0, self.panel_ancho, ALTO))
        
        # Jugador actual
        p = self.game.current_player
        emoji = "⚪" if p.color == "white" else "⚫"
        txt = self.font_big.render(f"{emoji} {p.name}", True, DORADO)
        self.screen.blit(txt, (self.panel_x + 10, 20))
        
        # Botón tirar dados
        color_tirar = VERDE if not self.dados_disponibles else (100, 100, 100)
        pygame.draw.rect(self.screen, color_tirar, self.btn_tirar, border_radius=8)
        txt = self.font.render("TIRAR DADOS", True, BLANCO)
        txt_rect = txt.get_rect(center=self.btn_tirar.center)
        self.screen.blit(txt, txt_rect)
        
        # Botón pasar turno
        color_pasar = ROJO if self.dados_disponibles else (100, 100, 100)
        pygame.draw.rect(self.screen, color_pasar, self.btn_pasar, border_radius=8)
        txt = self.font.render("PASAR TURNO", True, BLANCO)
        txt_rect = txt.get_rect(center=self.btn_pasar.center)
        self.screen.blit(txt, txt_rect)
        
        # Dados disponibles
        if self.dados_disponibles:
            y = 200
            txt = self.font.render("Dados:", True, DORADO)
            self.screen.blit(txt, (self.panel_x + 10, y))
            
            for i, d in enumerate(self.dados_disponibles):
                x = self.panel_x + 20 + (i % 2) * 65
                y_dado = y + 35 + (i // 2) * 65
                pygame.draw.rect(self.screen, VERDE, (x, y_dado, 55, 55), border_radius=5)
                txt_dado = self.font_big.render(str(d), True, BLANCO)
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
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))
            
            txt = self.font_big.render(f"¡{self.game.winner.name} GANÓ!", True, DORADO)
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
                    self.color_mensaje = ROJO
                    self.game.end_turn()
                    self.dados_disponibles = []
                else:
                    bar_count = self.board.bar_count(self.game.current_player.color)
                    if bar_count > 0:
                        self.mensaje = f"Dados: {valores}. ¡Saca del BAR!"
                        self.color_mensaje = ROJO
                    else:
                        self.mensaje = f"Dados: {valores}. ¡Mueve!"
                        self.color_mensaje = VERDE
            return
        
        # Botón pasar turno
        if self.btn_pasar.collidepoint(x, y):
            if self.dados_disponibles:
                self.game.end_turn()
                self.dados_disponibles = []
                self.punto_seleccionado = None
                self.mensaje = f"Turno de {self.game.current_player.name}"
                self.color_mensaje = BLANCO
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
                    self.color_mensaje = AZUL
                else:
                    self.mensaje = "¡Primero saca del BAR!"
                    self.color_mensaje = ROJO
            else:
                if punto == -1:
                    self.mensaje = "BAR vacío"
                    self.color_mensaje = ROJO
                elif punto == -2:
                    self.mensaje = "Selecciona una ficha primero"
                    self.color_mensaje = ROJO
                else:
                    cell = self.board.points[punto]
                    print(f"DEBUG: Punto {punto}, Cell: {cell}, Color jugador: {self.game.current_player.color}")
                    if cell and cell["color"] == self.game.current_player.color:
                        self.punto_seleccionado = punto
                        self.mensaje = f"Punto {punto} seleccionado"
                        self.color_mensaje = AZUL
                    else:
                        if cell:
                            self.mensaje = f"Punto {punto} tiene {cell['color']}, tú eres {self.game.current_player.color}"
                        else:
                            self.mensaje = f"Punto {punto} está vacío"
                        self.color_mensaje = ROJO
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
                            self.mensaje = f"✓ Sacaste del {move[1]}"
                        elif isinstance(move, tuple) and move[0] == "reentry":
                            self.mensaje = f"✓ BAR → {punto}"
                        else:
                            self.mensaje = f"✓ {self.punto_seleccionado} → {punto}"
                        
                        self.color_mensaje = VERDE
                        self.punto_seleccionado = None
                        
                        # Verificar ganador
                        if self.game.winner:
                            self.mensaje = f"¡{self.game.winner.name} GANÓ!"
                            self.color_mensaje = DORADO
                        # Auto-terminar si no hay dados
                        elif not self.dados_disponibles:
                            self.game.end_turn()
                            self.mensaje = f"Turno de {self.game.current_player.name}"
                            self.color_mensaje = BLANCO
                        # Auto-terminar si no hay movimientos
                        else:
                            moves = self.board.legal_moves(self.game.current_player, self.dados_disponibles)
                            if not moves:
                                self.game.end_turn()
                                self.dados_disponibles = []
                                self.mensaje = "Sin más movimientos"
                                self.color_mensaje = ROJO
                    else:
                        self.mensaje = "Error calculando dado"
                        self.color_mensaje = ROJO
                        self.punto_seleccionado = None
                except BackgammonError as e:
                    self.mensaje = f"Error: {str(e)[:30]}"
                    self.color_mensaje = ROJO
                    self.punto_seleccionado = None
            else:
                self.mensaje = "Movimiento ilegal"
                self.color_mensaje = ROJO
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