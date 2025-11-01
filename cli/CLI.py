from core.board import Board
from core.dice import Dice
from core.game import Game
from core.player import Player
from excepciones.excepciones import BackgammonError
import os


def mostrar_encabezado():
    """Imprime el título del juego."""
    print("===================================")
    print("        .. BACKGAMMON ..           ")
    print("===================================")


def mostrar_menu():
    """Imprime las opciones disponibles."""
    print("\nOpciones:")
    print("1. Tirar los dados")
    print("2. Realizar movimiento")
    print("3. Salir del juego")


def mostrar_tablero(board: Board):
    """Muestra el estado actual del tablero."""
    print("\nTablero actual:")
    print(board.render_pretty() if hasattr(board, "render_pretty") else board.render())


def main():
    """Función principal del juego por consola."""
    mostrar_encabezado()

    # Crear jugadores y componentes
    white = Player("Jugador 1", "white")
    black = Player("Jugador 2", "black")
    board = Board()
    dice = Dice()
    game = Game(board, white, black, dice)

    # Detectar si estamos en CI para tests
    en_test = os.environ.get("CI", "").lower() == "true"
    
    dados_disponibles = []

    while not game.winner:
        print(f"\nTurno de: {game.current_player.name} ({game.current_player.color})")
        
        # Mostrar dados disponibles si los hay
        if dados_disponibles:
            print(f" Dados disponibles: {dados_disponibles}")
        
        mostrar_menu()
        opcion = input("\nElegí una opción: ").strip()

        # Opción 1: Tirar dados
        if opcion == "1":
            if dados_disponibles:
                print("  Ya tiraste los dados. Usá la opción 2 para mover o 3 para pasar turno.")
                continue
            
            if not en_test:
                input("\nPresioná ENTER para tirar los dados...")
            
            valores = game.roll_dice()
            dados_disponibles = list(valores)
            print(f"\n Tirada de dados: {valores}")
            mostrar_tablero(board)
            
            # Verificar si hay movimientos legales
            moves = board.legal_moves(game.current_player, dados_disponibles)
            if not moves:
                print("\n Sin movimientos legales. Turno terminado automáticamente.")
                game.end_turn()
                dados_disponibles = []
                if not en_test and not game.winner:
                    input("\nPresioná ENTER para continuar...")

        # Opción 2: Realizar movimiento
        elif opcion == "2":
            if not dados_disponibles:
                print("  Primero tenés que tirar los dados (opción 1).")
                continue
            
            mostrar_tablero(board)
            
            # Mostrar movimientos legales
            moves = board.legal_moves(game.current_player, dados_disponibles)
            if not moves:
                print("\n Sin movimientos legales. Pasando turno...")
                game.end_turn()
                dados_disponibles = []
                continue
            
            print(f"\ Movimientos legales disponibles: {len(moves)}")
            
            move_input = input("\nIngresá tu movimiento (ej. '12 10' o 'bar 3' o 'bearoff 5'): ").strip().split()

            # Permitir ingresar en dos pasos
            if len(move_input) == 1:
                segundo = input("Destino: ").strip()
                move_input.append(segundo)

            if len(move_input) != 2:
                print(" Formato inválido. Ingresá origen y destino.")
                continue

            try:
                # Parsear movimiento
                src_str, dst_str = move_input
                
                # Determinar tipo de movimiento
                if src_str.lower() == "bar":
                    # Reingreso desde barra
                    dst = int(dst_str)
                    move = ("reentry", dst)
                elif src_str.lower() == "bearoff":
                    # Sacar ficha
                    src = int(dst_str)
                    move = ("bearoff", src)
                else:
                    # Movimiento normal
                    src = int(src_str)
                    dst = int(dst_str)
                    move = (src, dst)
                
                # Verificar si es legal
                if move not in moves:
                    print(f" Movimiento ilegal. Elegí uno de los {len(moves)} movimientos disponibles.")
                    continue
                
                # Aplicar movimiento
                board.apply_move(game.current_player, move)
                
                # Calcular qué dado se usó (considerando dirección)
                dado_usado = None
                if isinstance(move, tuple) and len(move) == 2:
                    if isinstance(move[0], int) and isinstance(move[1], int):
                        # Movimiento normal: la distancia real es abs()
                        distancia = abs(move[1] - move[0])
                        # Buscar el dado que coincida con esta distancia
                        if distancia in dados_disponibles:
                            dado_usado = distancia
                    elif move[0] == "reentry":
                        # Reingreso desde barra
                        dst = move[1]
                        if game.current_player.color == "white":
                            dado_usado = 24 - dst
                        else:
                            dado_usado = dst + 1
                    elif move[0] == "bearoff":
                        # Bear off
                        src = move[1]
                        if game.current_player.color == "white":
                            dado_exacto = src + 1
                        else:
                            dado_exacto = 24 - src
                        # Buscar dado exacto o mayor
                        if dado_exacto in dados_disponibles:
                            dado_usado = dado_exacto
                        else:
                            for d in sorted(dados_disponibles, reverse=True):
                                if d >= dado_exacto:
                                    dado_usado = d
                                    break
                
                # Quitar el dado usado
                if dado_usado and dado_usado in dados_disponibles:
                    dados_disponibles.remove(dado_usado)
                    print(f"\n✓ Movimiento exitoso. Usado dado: {dado_usado}")
                    print(f"   Dados restantes: {dados_disponibles}")
                else:
                    print("\n✓ Movimiento exitoso.")
                    print(f"  ADVERTENCIA: No se pudo calcular el dado usado correctamente")
                
                mostrar_tablero(board)
                
                # Verificar ganador
                if game.winner:
                    print(f"\n ¡El jugador {game.winner.name} ha ganado la partida!")
                    break
                
                # Verificar si quedan dados
                if not dados_disponibles:
                    print("\n✓ Todos los dados usados. Turno terminado.")
                    game.end_turn()
                    if not en_test and not game.winner:
                        input("\nPresioná ENTER para continuar...")
                else:
                    # Ver si hay movimientos legales con los dados restantes
                    moves = board.legal_moves(game.current_player, dados_disponibles)
                    if not moves:
                        print(f"\n✓ Sin más movimientos con dados {dados_disponibles}. Turno terminado.")
                        game.end_turn()
                        dados_disponibles = []
                        if not en_test and not game.winner:
                            input("\nPresioná ENTER para continuar...")

            except ValueError:
                print(" Ingresá números válidos (0-23).")
            except BackgammonError as e:
                print(f" Error: {e}")

        # Opción 3: Salir o pasar turno
        elif opcion == "3":
            if dados_disponibles:
                print("\n  Pasando turno...")
                game.end_turn()
                dados_disponibles = []
            else:
                print("\n Saliendo del juego... ¡Gracias por jugar!")
                break

        # Opción inválida
        else:
            print("Opción inválida. Intentá nuevamente.")

    if game.winner:
        print(f"\n ¡El jugador {game.winner.name} ha ganado la partida!")


if __name__ == "__main__":
    main()