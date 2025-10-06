from core.board import Board
from core.dice import Dice
from core.game import Game
from core.player import Player
from excepciones.excepciones import BackgammonError

def mostrar_encabezado():
    """Imprime el título del juego."""
    print("===================================")
    print("        .. BACKGAMMON ..           ")
    print("===================================")


def mostrar_menu():
    print("\nOpciones:")
    print("1. Tirar los dados")
    print("2. Realizar movimiento")
    print("3. Salir del juego")


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

        # Opción 1: Tirar los dados
        if opcion == "1":
            input("\nPresioná ENTER para tirar los dados...")
            valores = game.roll_dice()
            print(f"\n🎲 Tirada de dados: {valores}")
            mostrar_tablero(board)

        # Opción 2: Realizar movimiento
        elif opcion == "2":
            try:
                mostrar_tablero(board)
                src = int(input("\nDesde punto (0-23): "))
                dst = int(input("Hasta punto (0-23): "))
                board.apply_move(game.current_player, (src, dst))
                print(" Movimiento realizado correctamente.")
                mostrar_tablero(board)

            except ValueError:
                print(" Ingresá números válidos.")
            except BackgammonError as e:
                print(f" Error: {e}")

        # Opción 3: Salir
        elif opcion == "3":
            print("\nSaliendo del juego... ¡Gracias por jugar!")
            break