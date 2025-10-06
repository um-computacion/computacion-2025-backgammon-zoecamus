from core.board import Board

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