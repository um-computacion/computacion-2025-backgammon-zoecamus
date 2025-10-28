import pygame
import sys
from core.board import Board
from core.player import Player
from core.dice import Dice
from core.game import Game

MARRON = (139, 69, 19)
BEIGE = (245, 222, 179)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

ANCHO = 900
ALTO = 600
FPS = 60

# =============================
# FUNCIONES DE DIBUJO
# =============================

def dibujar_tablero(screen):
    """Dibuja las 24 puntas del tablero con márgenes y marco."""
    MARGEN = 50
    ancho_punta = (ANCHO - 2 * MARGEN) // 12
    alto_punta = (ALTO - 2 * MARGEN) // 2

    # Fondo del tablero 
    pygame.draw.rect(screen, (110, 60, 20), (MARGEN//2, MARGEN//2, ANCHO - MARGEN, ALTO - MARGEN), border_radius=10)

    for i in range(12):
        color = BEIGE if i % 2 == 0 else MARRON

        # Triángulos superiores
        puntos_superior = [
            (MARGEN + i * ancho_punta, MARGEN),
            (MARGEN + (i + 1) * ancho_punta, MARGEN),
            (MARGEN + i * ancho_punta + ancho_punta // 2, MARGEN + alto_punta)
        ]
        pygame.draw.polygon(screen, color, puntos_superior)

               # Triángulos inferiores
        puntos_inferior = [
            (MARGEN + i * ancho_punta, ALTO - MARGEN),
            (MARGEN + (i + 1) * ancho_punta, ALTO - MARGEN),
            (MARGEN + i * ancho_punta + ancho_punta // 2, ALTO - MARGEN - alto_punta)
        ]
        pygame.draw.polygon(screen, color, puntos_inferior)

def dibujar_fichas(screen, board):
    """Dibuja las fichas según el estado del tablero."""
    ancho_punta = ANCHO // 12
    radio = 15

    for i, punto in enumerate(board.points):  
        if not punto or not punto["color"]:
            continue

        color = BLANCO if punto["color"] == "white" else NEGRO
        cantidad = punto["count"]

        # Parte superior (puntos 0–11) o inferior (12–23)
        fila_superior = i < 12
        base_y = 40 if fila_superior else ALTO - 40

        for j in range(cantidad):
            x = i * ancho_punta + ancho_punta // 2
            y = base_y + (j * 2 * radio if not fila_superior else -j * 2 * radio)
            pygame.draw.circle(screen, color, (x, y), radio)

def dibujar_dados_fijos(screen, valores, fuente):
    """Dibuja los dados con valores fijos (no cambian hasta clic)."""
    dado_size = 60
    espacio = 20
    start_x = ANCHO // 2 - dado_size - espacio // 2
    y = ALTO // 2 - dado_size // 2

    for i, valor in enumerate(valores):
        x = start_x + i * (dado_size + espacio)
        pygame.draw.rect(screen, BLANCO, (x, y, dado_size, dado_size), border_radius=10)
        texto = fuente.render(str(valor), True, NEGRO)
        text_rect = texto.get_rect(center=(x + dado_size // 2, y + dado_size // 2))
        screen.blit(texto, text_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Backgammon - Pygame ")
    clock = pygame.time.Clock()

    board = Board()
    white = Player("Jugador 1", "white")
    black = Player("Jugador 2", "black")
    dice = Dice()
    game = Game(board, white, black, dice)

    fuente = pygame.font.SysFont("Arial", 24)
    valores_dados = [1, 1]  # valores iniciales
    boton_rect = pygame.Rect(ANCHO//2 - 80, ALTO - 80, 160, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #  Clic en el botón "Tirar dados"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_rect.collidepoint(event.pos):
                    valores_dados = dice.roll()  # nueva tirada

        # Fondo
        screen.fill(MARRON)
        dibujar_tablero(screen)
        dibujar_fichas(screen, board)
        dibujar_dados_fijos(screen, valores_dados, fuente)

        #  Mostrar turno actual
        jugador = game.current_player
        texto_turno = fuente.render(f"Turno: {jugador.name} ({jugador.color})", True, BLANCO)
        screen.blit(texto_turno, (20, 20))

        #  Botón
        pygame.draw.rect(screen, BEIGE, boton_rect, border_radius=8)
        texto_boton = fuente.render("Tirar dados", True, NEGRO)
        screen.blit(texto_boton, texto_boton.get_rect(center=boton_rect.center))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


def dibujar_dados(screen, dice, fuente):
    """Dos dados con sus valores."""
    valores = dice.roll()  # tirada
    dado_size = 60
    espacio = 20
    start_x = ANCHO // 2 - dado_size - espacio // 2
    y = ALTO // 2 - dado_size // 2

    for i, valor in enumerate(valores):
        x = start_x + i * (dado_size + espacio)
        pygame.draw.rect(screen, BLANCO, (x, y, dado_size, dado_size), border_radius=10)
        texto = fuente.render(str(valor), True, NEGRO)
        text_rect = texto.get_rect(center=(x + dado_size // 2, y + dado_size // 2))
        screen.blit(texto, text_rect)


if __name__ == "__main__":
    main()