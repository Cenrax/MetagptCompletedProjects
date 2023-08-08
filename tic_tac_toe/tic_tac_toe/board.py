class Board:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]

    def get_cell(self, row: int, col: int):
        return self.board[row][col]

    def set_cell(self, row: int, col: int, player):
        self.board[row][col] = player

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True

    def is_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        # Check columns
        for col in range(3):
            if all(row[col] == player for row in self.board):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i] == player for i in range(3)):
            return True

        return False

    def get_empty_cells(self):
        empty_cells = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] is None:
                    empty_cells.append((row, col))
        return empty_cells
