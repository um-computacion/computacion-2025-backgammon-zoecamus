import pygame
import sys
from core.board import Board
from core.player import Player
from core.dice import Dice
from core.game import Game

# Colores
MARRON = (139, 69, 19)
BEIGE = (245, 222, 179)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Tamaño de la ventana
ANCHO = 900
ALTO = 600
FPS = 60

def dibujar_tablero(screen):
    """Dibuja las 24 puntas del tablero."""
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

