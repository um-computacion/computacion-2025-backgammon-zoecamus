from core.board import Board
from core.dice import Dice
from core.game import Game
from core.player import Player

def mostrar_encabezado():
    """Imprime el título del juego."""
    print("===================================")
    print("        .. BACKGAMMON ..           ")
    print("===================================")


def mostrar_menu():
    print("\nOpciones:")
    print("1. Tirar los dados")
    print("2. Salir")


def mostrar_tablero(board: Board):
    print("\nTablero actual:")
    print(board.render_pretty() if hasattr(board, "render_pretty") else board.render())

def main():
    mostrar_encabezado()

    # Crear jugadores y componentes del juego
    white = Player("Jugador 1", "white")
    black = Player("Jugador 2", "black")
    board = Board()
    dice = Dice()
    game = Game(board, white, black, dice)

    # Loop principal
    while not game.winner:
        mostrar_encabezado()
        print(f"Turno de: {game.current_player.name} ({game.current_player.color})\n")

        mostrar_menu()
        opcion = input("\nElegí una opción: ").strip()