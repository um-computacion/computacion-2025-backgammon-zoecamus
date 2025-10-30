import pygame
import sys
from core.board import Board
from core.player import Player
from core.dice import Dice
from core.game import Game
from excepciones.excepciones import BackgammonError

# Colores simples
MARRON = (139, 69, 19)
BEIGE = (245, 222, 179)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (50, 200, 50)
ROJO = (200, 50, 50)
AZUL = (100, 150, 255)
GRIS = (120, 120, 120)

# Dimensiones
ANCHO = 1200
ALTO = 750
FPS = 60


def pedir_nombres():
    """Pide los nombres por consola antes de abrir pygame."""
    print("\n" + "="*50)
    print("       🎲 BACKGAMMON 🎲")
    print("="*50)
    
    nombre1 = input("\nNombre Jugador 1 (blancas ⚪): ").strip()
    if not nombre1:
        nombre1 = "Jugador 1"
    
    nombre2 = input("Nombre Jugador 2 (negras ⚫): ").strip()
    if not nombre2:
        nombre2 = "Jugador 2"
    
    print(f"\n¡Que comience {nombre1} vs {nombre2}!")
    print("Cerrando consola, abriendo ventana...\n")
    
    return nombre1, nombre2


class BackgammonSimple:
    """Versión simple de Backgammon con Pygame."""
    
    def __init__(self, nombre1, nombre2):
        """Inicializa el juego."""
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Backgammon")
        self.clock = pygame.time.Clock()
        
        # Fuentes
        self.font = pygame.font.SysFont("Arial", 18)
        self.font_big = pygame.font.SysFont("Arial", 24, bold=True)
        
        # Juego
        self.board = Board()
        self.white = Player(nombre1, "white")
        self.black = Player(nombre2, "black")
        self.dice = Dice()
        self.game = Game(self.board, self.white, self.black, self.dice)
        
        # Estado
        self.dados_disponibles = []
        self.punto_seleccionado = None
        self.mensaje = f"{nombre1}, tirá los dados para empezar"
        self.color_mensaje = BLANCO
        
        # Botones simples
        self.btn_tirar = pygame.Rect(1020, 100, 150, 40)
        self.btn_pasar = pygame.Rect(1020, 150, 150, 40)
        
        self.running = True

    def posicion_punto(self, idx):
        """Calcula posición de un punto con espacio en el medio para el bar."""
        w = 70  # Ancho de cada triángulo (más grande)
        bar_gap = 80  # Espacio en el medio para el bar
        
        if idx < 12:  # Parte superior (puntos 11 a 0)
            col = 11 - idx
            if col < 6:  # Derecha (puntos 11-6)
                x = 50 + col * w + w//2 + bar_gap
            else:  # Izquierda (puntos 5-0)
                x = 50 + (col - 6) * w + w//2
            y = 100
        else:  # Parte inferior (puntos 12 a 23)
            col = idx - 12
            if col < 6:  # Izquierda (puntos 12-17)
                x = 50 + col * w + w//2
            else:  # Derecha (puntos 18-23)
                x = 50 + (col - 6) * w + w//2 + bar_gap
            y = 600
        return (x, y)

    def punto_desde_click(self, pos):
        """Detecta qué punto se clickeó. Retorna -1 si es el bar, -2 si es zona de bear off."""
        x, y = pos
        w = 70
        bar_gap = 80
        bar_x_center = 50 + 6*w + bar_gap//2
        
        # Verificar si es click en zona de bear off (zona "OUT")
        if 920 <= x <= 980:
            if 520 <= y <= 600:  # Zona bear off blancas
                return -2
            elif 100 <= y <= 180:  # Zona bear off negras
                return -2
        
        # Verificar si es click en el bar (área del medio)
        if abs(x - bar_x_center) <= 40 and 150 <= y <= 550:
            # Verificar si hay fichas del jugador actual en el bar
            if self.board.bar_count(self.game.current_player.color) > 0:
                return -1
        
        # Parte superior (puntos 11-0)
        if 50 <= y <= 350:
            # Mitad derecha (puntos 11-6)
            if 50 + bar_gap <= x <= 50 + 6*w + bar_gap:
                col = (x - (50 + bar_gap)) // w
                if col < 6:
                    return 11 - col
            # Mitad izquierda (puntos 5-0)
            elif 50 <= x <= 50 + 6*w:
                col = (x - 50) // w
                if col < 6:
                    return 5 - col
        
        # Parte inferior (puntos 12-23)
        elif 400 <= y <= 650:
            # Mitad izquierda (puntos 12-17)
            if 50 <= x <= 50 + 6*w:
                col = (x - 50) // w
                if col < 6:
                    return 12 + col
            # Mitad derecha (puntos 18-23)
            elif 50 + bar_gap <= x <= 50 + 6*w + bar_gap:
                col = (x - (50 + bar_gap)) // w
                if col < 6:
                    return 18 + col
        
        return None

    def calcular_dado_usado(self, move):
        """Calcula qué dado se usó para un movimiento dado."""
        # Bear off: formato ("bearoff", src)
        if isinstance(move, tuple) and move[0] == "bearoff":
            src = move[1]
            direction = self.game.current_player.direction
            
            # Calcular qué dado se necesita para sacar desde este punto
            if self.game.current_player.color == "white":
                # Blancas sacan desde puntos 0-5 hacia "fuera" (negativo)
                # Punto 0 con dado 1, punto 1 con dado 2, etc.
                dado_exacto = src + 1
                # Verificar si el dado exacto está disponible
                if dado_exacto in self.dados_disponibles:
                    return dado_exacto
                # Si no, buscar un dado mayor que también sirva
                for d in sorted(self.dados_disponibles, reverse=True):
                    if d > dado_exacto:
                        return d
            else:
                # Negras sacan desde puntos 18-23 hacia "fuera" (>23)
                # Punto 23 con dado 1, punto 22 con dado 2, etc.
                dado_exacto = 24 - src
                if dado_exacto in self.dados_disponibles:
                    return dado_exacto
                for d in sorted(self.dados_disponibles, reverse=True):
                    if d > dado_exacto:
                        return d
            return None
        
        # Movimiento desde el bar: formato ("reentry", dst)
        if isinstance(move, tuple) and move[0] == "reentry":
            dst = move[1]
            # Para blancas: entran en puntos 18-23 con dados 1-6
            # Para negras: entran en puntos 0-5 con dados 1-6
            if self.game.current_player.color == "white":
                # Blancas entran desde el "punto 24" (fuera) hacia abajo
                # Dado 1 -> punto 23, Dado 2 -> punto 22, ..., Dado 6 -> punto 18
                dado = 24 - dst
            else:
                # Negras entran desde el "punto -1" (fuera) hacia arriba
                # Dado 1 -> punto 0, Dado 2 -> punto 1, ..., Dado 6 -> punto 5
                dado = dst + 1
            
            if dado in self.dados_disponibles:
                return dado
            return None
        
        # Movimiento normal: formato (src, dst)
        if isinstance(move, tuple) and len(move) == 2:
            src, dst = move
            distancia = abs(dst - src)
            if distancia in self.dados_disponibles:
                return distancia
        
        return None

    def auto_terminar(self):
        """Termina el turno automáticamente."""
        self.game.end_turn()
        self.dados_disponibles = []
        self.punto_seleccionado = None
        self.mensaje = f"Turno de {self.game.current_player.name}"
        self.color_mensaje = BLANCO

    def verificar_auto_terminar(self):
        """Verifica si debe terminar el turno."""
        if not self.dados_disponibles:
            self.auto_terminar()
            return True
        
        moves = self.board.legal_moves(self.game.current_player, self.dados_disponibles)
        if not moves:
            self.mensaje = "Sin movimientos. Turno terminado."
            self.color_mensaje = ROJO
            self.auto_terminar()
            return True
        
        return False

    def dibujar_tablero(self):
        """Dibuja el tablero con espacio en el medio para el bar y números."""
        self.screen.fill(MARRON)
        
        w = 70
        bar_gap = 80
        
        # Fondo tablero
        pygame.draw.rect(self.screen, (100, 60, 20), (30, 30, 900, 680))
        
        # Línea del medio
        pygame.draw.line(self.screen, (80, 40, 10), (30, 360), (930, 360), 4)
        
        # Dibujar triángulos y números
        for i in range(24):
            if i < 12:  # Parte superior (11-0)
                col = 11 - i
                if col < 6:  # Derecha
                    x_base = 50 + col * w + bar_gap
                else:  # Izquierda
                    x_base = 50 + (col - 6) * w
                
                color = BEIGE if i % 2 == 0 else (90, 50, 15)
                pts = [
                    (x_base, 50),
                    (x_base + w, 50),
                    (x_base + w//2, 330)
                ]
                pygame.draw.polygon(self.screen, color, pts)
                
                # Número del punto
                txt = self.font.render(str(i), True, NEGRO if i % 2 == 0 else BEIGE)
                self.screen.blit(txt, (x_base + w//2 - 8, 55))
                
            else:  # Parte inferior (12-23)
                col = i - 12
                if col < 6:  # Izquierda
                    x_base = 50 + col * w
                else:  # Derecha
                    x_base = 50 + (col - 6) * w + bar_gap
                
                color = BEIGE if i % 2 == 0 else (90, 50, 15)
                pts = [
                    (x_base, 670),
                    (x_base + w, 670),
                    (x_base + w//2, 390)
                ]
                pygame.draw.polygon(self.screen, color, pts)
                
                # Número del punto
                txt = self.font.render(str(i), True, NEGRO if i % 2 == 0 else BEIGE)
                self.screen.blit(txt, (x_base + w//2 - 8, 650))

    def dibujar_fichas(self):
        """Dibuja las fichas."""
        for idx in range(24):
            p = self.board.points[idx]
            if not p or not p.get("color"):
                continue
            
            x, y = self.posicion_punto(idx)
            color = BLANCO if p["color"] == "white" else NEGRO
            cant = p["count"]
            
            # Dirección
            dir_y = 1 if idx < 12 else -1
            
            # Dibujar fichas
            for j in range(min(cant, 5)):
                pygame.draw.circle(self.screen, color, (x, y + j*40*dir_y), 18)
                pygame.draw.circle(self.screen, GRIS, (x, y + j*40*dir_y), 18, 2)
            
            # Número si >5
            if cant > 5:
                txt = self.font_big.render(str(cant), True, ROJO)
                self.screen.blit(txt, (x-10, y-10))
        
        # Selección
        if self.punto_seleccionado is not None and self.punto_seleccionado >= 0:
            x, y = self.posicion_punto(self.punto_seleccionado)
            pygame.draw.circle(self.screen, VERDE, (x, y), 25, 4)

    def dibujar_bar(self):
        """Dibuja la barra en el medio del tablero."""
        w = 70
        bar_gap = 80
        bar_x = 50 + 6*w + bar_gap//2
        
        # Fondo del bar
        pygame.draw.rect(self.screen, (70, 40, 15), (bar_x - 35, 50, 70, 620), border_radius=10)
        pygame.draw.line(self.screen, (200, 150, 50), (bar_x - 35, 360), (bar_x + 35, 360), 2)
        
        # Texto "BAR"
        txt_bar = self.font_big.render("BAR", True, (200, 150, 50))
        self.screen.blit(txt_bar, (bar_x - 25, 350))
        
        # Blancas en barra (parte inferior)
        bar_w = self.board.bar_count("white")
        if bar_w > 0:
            y_start = 550
            for i in range(min(bar_w, 5)):
                pygame.draw.circle(self.screen, BLANCO, (bar_x, y_start - i*35), 18)
                pygame.draw.circle(self.screen, GRIS, (bar_x, y_start - i*35), 18, 2)
            if bar_w > 5:
                txt = self.font_big.render(str(bar_w), True, ROJO)
                self.screen.blit(txt, (bar_x-10, 400))
        
        # Negras en barra (parte superior)
        bar_b = self.board.bar_count("black")
        if bar_b > 0:
            y_start = 170
            for i in range(min(bar_b, 5)):
                pygame.draw.circle(self.screen, NEGRO, (bar_x, y_start + i*35), 18)
                pygame.draw.circle(self.screen, GRIS, (bar_x, y_start + i*35), 18, 2)
            if bar_b > 5:
                txt = self.font_big.render(str(bar_b), True, ROJO)
                self.screen.blit(txt, (bar_x-10, 320))
        
        # Resaltar si está seleccionado
        if self.punto_seleccionado == -1:
            pygame.draw.rect(self.screen, VERDE, (bar_x - 35, 50, 70, 620), 4, border_radius=10)

    def dibujar_borne_off(self):
        """Dibuja fichas sacadas con zona clickeable."""
        x = 950
        
        # Zona de bear off para blancas (abajo)
        pygame.draw.rect(self.screen, (100, 80, 60), (x-30, 520, 60, 80), border_radius=8)
        pygame.draw.rect(self.screen, (200, 180, 140), (x-30, 520, 60, 80), 2, border_radius=8)
        
        borne_w = self.board.borne_off_count("white")
        pygame.draw.rect(self.screen, BLANCO, (x-20, 550, 40, 40), border_radius=5)
        txt = self.font_big.render(str(borne_w), True, NEGRO)
        txt_rect = txt.get_rect(center=(x, 570))
        self.screen.blit(txt, txt_rect)
        
        # Texto "OUT"
        txt_out = self.font.render("OUT", True, (200, 180, 140))
        self.screen.blit(txt_out, (x-18, 525))
        
        # Zona de bear off para negras (arriba)
        pygame.draw.rect(self.screen, (100, 80, 60), (x-30, 100, 60, 80), border_radius=8)
        pygame.draw.rect(self.screen, (200, 180, 140), (x-30, 100, 60, 80), 2, border_radius=8)
        
        borne_b = self.board.borne_off_count("black")
        pygame.draw.rect(self.screen, NEGRO, (x-20, 130, 40, 40), border_radius=5)
        txt = self.font_big.render(str(borne_b), True, BLANCO)
        txt_rect = txt.get_rect(center=(x, 150))
        self.screen.blit(txt, txt_rect)
        
        # Texto "OUT"
        txt_out = self.font.render("OUT", True, (200, 180, 140))
        self.screen.blit(txt_out, (x-18, 160))

    def dibujar_panel(self):
        """Dibuja panel lateral."""
        # Fondo
        pygame.draw.rect(self.screen, (70, 50, 30), (1000, 0, 200, ALTO))
        
        # Turno
        p = self.game.current_player
        emoji = "⚪" if p.color == "white" else "⚫"
        txt = self.font_big.render(f"{emoji} {p.name}", True, BLANCO)
        self.screen.blit(txt, (1020, 30))
        
        # Botón tirar
        self.btn_tirar = pygame.Rect(1020, 100, 150, 40)
        color_btn = VERDE if not self.dados_disponibles else GRIS
        pygame.draw.rect(self.screen, color_btn, self.btn_tirar, border_radius=5)
        txt = self.font.render("TIRAR DADOS", True, BLANCO)
        self.screen.blit(txt, (self.btn_tirar.x + 20, self.btn_tirar.y + 12))
        
        # Botón pasar
        self.btn_pasar = pygame.Rect(1020, 150, 150, 40)
        color_btn2 = ROJO if self.dados_disponibles else GRIS
        pygame.draw.rect(self.screen, color_btn2, self.btn_pasar, border_radius=5)
        txt = self.font.render("PASAR TURNO", True, BLANCO)
        self.screen.blit(txt, (self.btn_pasar.x + 18, self.btn_pasar.y + 12))
        
        # Dados disponibles
        if self.dados_disponibles:
            y = 220
            self.screen.blit(self.font.render("Dados disponibles:", True, VERDE), (1020, y))
            
            for i, d in enumerate(self.dados_disponibles):
                x = 1030 + (i % 2) * 60
                y_d = 250 + (i // 2) * 60
                pygame.draw.rect(self.screen, VERDE, (x, y_d, 40, 40), border_radius=5)
                txt = self.font_big.render(str(d), True, BLANCO)
                self.screen.blit(txt, (x+12, y_d+8))
            
            # Dados usados
            if len(self.dados_disponibles) < len(self.game.last_roll or []):
                y_us = 420
                self.screen.blit(self.font.render("Usados:", True, GRIS), (1020, y_us))
                
                usados = [d for d in (self.game.last_roll or []) if d not in self.dados_disponibles]
                for i, d in enumerate(usados):
                    x = 1030 + (i % 2) * 60
                    y_d = 450 + (i // 2) * 60
                    pygame.draw.rect(self.screen, GRIS, (x, y_d, 40, 40), border_radius=5)
                    txt = self.font.render(str(d), True, NEGRO)
                    self.screen.blit(txt, (x+12, y_d+10))
                    # Tachado
                    pygame.draw.line(self.screen, ROJO, (x, y_d), (x+40, y_d+40), 3)
        
        # Mensaje
        y_msg = 600
        palabras = self.mensaje.split()
        linea = ""
        y_actual = y_msg
        
        for palabra in palabras:
            test = linea + palabra + " "
            if self.font.size(test)[0] < 180:
                linea = test
            else:
                if linea:
                    txt = self.font.render(linea, True, self.color_mensaje)
                    self.screen.blit(txt, (1010, y_actual))
                    y_actual += 20
                linea = palabra + " "
        
        if linea:
            txt = self.font.render(linea, True, self.color_mensaje)
            self.screen.blit(txt, (1010, y_actual))

    def manejar_click(self, pos):
        """Maneja clicks."""
        # Botón tirar
        if self.btn_tirar.collidepoint(pos):
            if not self.dados_disponibles:
                valores = self.game.roll_dice()
                self.dados_disponibles = list(valores)
                
                moves = self.board.legal_moves(self.game.current_player, self.dados_disponibles)
                if not moves:
                    self.mensaje = "Sin movimientos. Turno terminado."
                    self.color_mensaje = ROJO
                    self.auto_terminar()
                else:
                    # Verificar si hay fichas en el bar
                    bar_count = self.board.bar_count(self.game.current_player.color)
                    if bar_count > 0:
                        self.mensaje = f"Dados: {valores}. ¡Sacá del BAR primero!"
                        self.color_mensaje = (255, 165, 0)  # Naranja
                    else:
                        self.mensaje = f"Dados: {valores}. Movete!"
                        self.color_mensaje = VERDE
            return
        
        # Botón pasar
        if self.btn_pasar.collidepoint(pos):
            if self.dados_disponibles:
                self.auto_terminar()
            return
        
        # Click en tablero
        if not self.dados_disponibles:
            return
        
        punto = self.punto_desde_click(pos)
        if punto is None:
            return
        
        # Verificar si hay fichas en el bar
        bar_count = self.board.bar_count(self.game.current_player.color)
        
        # Seleccionar
        if self.punto_seleccionado is None:
            # Si hay fichas en el bar, SOLO se puede seleccionar el bar
            if bar_count > 0:
                if punto == -1:
                    self.punto_seleccionado = -1
                    self.mensaje = "Bar seleccionado. Click donde quieras entrar"
                    self.color_mensaje = AZUL
                else:
                    self.mensaje = "¡Primero sacá del BAR!"
                    self.color_mensaje = ROJO
            else:
                # No hay fichas en el bar, movimiento normal
                if punto == -1:
                    self.mensaje = "El bar está vacío"
                    self.color_mensaje = ROJO
                else:
                    p = self.board.points[punto]
                    if p and p["color"] == self.game.current_player.color:
                        self.punto_seleccionado = punto
                        self.mensaje = f"Punto {punto} seleccionado"
                        self.color_mensaje = AZUL
        else:
            # Intentar mover
            moves = self.board.legal_moves(self.game.current_player, self.dados_disponibles)
            
            # Crear el movimiento en el formato correcto
            if self.punto_seleccionado == -1:
                # Movimiento desde el bar: formato ("reentry", destino)
                move = ("reentry", punto)
            else:
                # Si click en zona de bear off (-2) o doble click, intentar bear off
                bearoff_move = ("bearoff", self.punto_seleccionado)
                if bearoff_move in moves and (punto == -2 or punto == self.punto_seleccionado):
                    move = bearoff_move
                else:
                    # Movimiento normal: formato (origen, destino)
                    move = (self.punto_seleccionado, punto)
            
            if move in moves:
                try:
                    dado = self.calcular_dado_usado(move)
                    
                    if dado:
                        self.game.make_move(move)
                        self.dados_disponibles.remove(dado)
                        
                        # Mensaje según tipo de movimiento
                        if isinstance(move, tuple) and move[0] == "bearoff":
                            self.mensaje = f"✓ Sacaste ficha del punto {move[1]} (dado {dado})"
                        elif isinstance(move, tuple) and move[0] == "reentry":
                            self.mensaje = f"✓ BAR→{punto} (dado {dado})"
                        else:
                            self.mensaje = f"✓ {self.punto_seleccionado}→{punto} (dado {dado})"
                        
                        self.color_mensaje = VERDE
                        
                        if self.game.winner:
                            self.mensaje = f"¡{self.game.winner.name} GANÓ!"
                            self.color_mensaje = VERDE
                        
                        self.punto_seleccionado = None
                        self.verificar_auto_terminar()
                    else:
                        self.mensaje = "No se puede calcular el dado"
                        self.color_mensaje = ROJO
                        self.punto_seleccionado = None
                        
                except BackgammonError as e:
                    self.mensaje = f"Error: {str(e)[:40]}"
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
                    self.manejar_click(event.pos)
            
            self.dibujar_tablero()
            self.dibujar_fichas()
            self.dibujar_bar()
            self.dibujar_borne_off()
            self.dibujar_panel()
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()


def main():
    """Función principal."""
    # Pedir nombres por consola (más simple y funciona siempre)
    nombre1, nombre2 = pedir_nombres()
    
    # Crear e iniciar el juego
    juego = BackgammonSimple(nombre1, nombre2)
    juego.run()


if __name__ == "__main__":
    main()