import pygame
import sys
from core.board import Board
from core.player import Player
from core.dice import Dice
from core.game import Game

# Colores RGB
MARRON = (139, 69, 19)
BEIGE = (245, 222, 179)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (200, 0, 0)
AZUL = (0, 0, 200)

# Tamaño de la ventana
ANCHO = 900
ALTO = 600
FPS = 60

def dibujar_tablero(screen):
    """Dibuja las 24 puntas del tablero de backgammon."""
    ancho_punta = ANCHO // 12
    alto_punta = ALTO // 2

    for i in range(12):
        color = BEIGE if i % 2 == 0 else MARRON
        # Triángulos superiores
        puntos = [(i * ancho_punta, 0),
                  ((i + 1) * ancho_punta, 0),
                  (i * ancho_punta + ancho_punta // 2, alto_punta - 10)]
        pygame.draw.polygon(screen, color, puntos)

        # Triángulos inferiores
        puntos = [(i * ancho_punta, ALTO),
                  ((i + 1) * ancho_punta, ALTO),
                  (i * ancho_punta + ancho_punta // 2, ALTO - alto_punta + 10)]
        pygame.draw.polygon(screen, color, puntos)

def main():
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Backgammon - Pygame 🎲")
    clock = pygame.time.Clock()

    # Crear componentes del juego
    board = Board()
    white = Player("Jugador 1", "white")
    black = Player("Jugador 2", "black")
    dice = Dice()
    game = Game(board, white, black, dice)

    fuente = pygame.font.SysFont("Arial", 24)

    # Loop principal
    running = True
    while running:
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
