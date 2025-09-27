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