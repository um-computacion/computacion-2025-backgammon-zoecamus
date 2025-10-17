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



def dibujar_fichas(screen, board):
    """Dibuja las fichas según el estado del tablero."""
    ancho_punta = ANCHO // 12
    alto_punta = ALTO // 2
    radio = 15

    # Puntos de la barra
    for i, punto in enumerate(board.points): 
            if not punto:
                continue


            color = BLANCO if punto["color"] == "white" else NEGRO
            cantidad = punto["count"]


       # Determinar si está arriba (0-11) o abajo (12-23)
            fila_superior = i < 12
            base_y = 40 if fila_superior else ALTO - 40


            for j in range(cantidad):
                x = i * ancho_punta + ancho_punta // 2
                y = base_y + (j * 2 * radio if not fila_superior else -j * 2 * radio)
                pygame.draw.circle(screen, color, (x, y), radio)


def main():
   pygame.init()
   screen = pygame.display.set_mode((ANCHO, ALTO))
   pygame.display.set_caption("Backgammon - Pygame 🎲")
   clock = pygame.time.Clock()


   # Componentes del juego
   board = Board()
   white = Player("Jugador 1", "white")
   black = Player("Jugador 2", "black")
   dice = Dice()
   game = Game(board, white, black, dice)


   fuente = pygame.font.SysFont("Arial", 24)


   running = True
   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False




