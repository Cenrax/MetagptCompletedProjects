## ai.py

from typing import List, Tuple
from random import choice
from game import Game
from player import Player

class AI:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def get_next_move(self, game: Game) -> Tuple[int, int]:
        board = game.get_board()
        empty_cells = board.get_empty_cells()
        return choice(empty_cells)
