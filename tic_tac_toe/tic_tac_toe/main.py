from game import Game
from player import Player
from ai import AI
from utils import clear_screen

def main():
    player1 = Player("Player 1", "X")
    player2 = AI("O")
    game = Game(player1, player2)
    game.start()

if __name__ == "__main__":
    main()
