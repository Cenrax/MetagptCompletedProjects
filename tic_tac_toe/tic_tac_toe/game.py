from typing import List, Union, Tuple
from board import Board
from player import Player
from ai import AI
from utils import clear_screen

class Game:
    def __init__(self, player1: Player, player2: Union[Player, AI]):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.board = Board()

    def start(self) -> None:
        while not self.is_game_over():
            clear_screen()
            self.print_board()
            row, col = self.get_move()
            if not self.make_move(row, col):
                print("Invalid move. Please try again.")
                continue
            if self.is_game_over():
                clear_screen()
                self.print_board()
                winner = self.get_winner()
                if winner:
                    print(f"Player {winner.get_name()} wins!")
                else:
                    print("It's a tie!")
            else:
                self.switch_player()

    def reset(self) -> None:
        self.board.reset()
        self.current_player = self.player1

    def get_current_player(self) -> Player:
        return self.current_player

    def make_move(self, row: int, col: int) -> bool:
        if self.board.get_cell(row, col) is None:
            self.board.set_cell(row, col, self.current_player)
            return True
        return False

    def is_game_over(self) -> bool:
        return self.board.is_full() or self.board.is_winner(self.current_player)

    def get_winner(self) -> Union[Player, None]:
        if self.board.is_winner(self.player1):
            return self.player1
        if self.board.is_winner(self.player2):
            return self.player2
        return None

    def get_board(self) -> List[List[Union[Player, None]]]:
        return self.board.get_board()

    def print_board(self) -> None:
        board = self.board.get_board()
        for row in board:
            print(" | ".join([cell.get_symbol() if cell else " " for cell in row]))
            print("-" * 9)

    def get_move(self) -> Tuple[int, int]:
        while True:
            try:
                row = int(input("Enter the row number (0-2): "))
                col = int(input("Enter the column number (0-2): "))
                if row < 0 or row > 2 or col < 0 or col > 2:
                    raise ValueError
                return row, col
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 2.")

