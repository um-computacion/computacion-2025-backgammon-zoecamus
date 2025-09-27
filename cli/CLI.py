from core.player import Player
from core.dice import Dice
from core.board import Board
from core.game import Game

def main():
    print("=== ¡¡¡ Bienvenido a Backgammon !!! ===")
    white = Player("Jugador 1", "white")
    black = Player("Jugador 2", "black")
    board = Board()
    dice = Dice()
    game = Game(board, white, black, dice)


    while not game.winner:
        print("\n-----------------------------------")
        print(f"Turno de: {game.current_player.name} ({game.current_player.color})")

        print("Opciones:")
        print("1. Tirar los dados")
        print("2. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            valores = game.roll_dice()
            print(f"Tirada de dados: {valores}")
            game.end_turn()

        elif opcion == "2":
            print("Saliendo del juego...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")
