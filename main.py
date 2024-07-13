class Board:
    """
    A class to represent a Sudoku board and provide methods for solving it.

    Attributes:
        board (list): A 2D list representing the Sudoku board.

    Methods:
        __str__(): Returns a string representation of the board.
        find_empty_cell(): Finds the next empty cell (with value 0) on the board.
        valid_in_row(row, num): Checks if a number is valid in the specified row.
        valid_in_col(col, num): Checks if a number is valid in the specified column.
        valid_in_square(row, col, num): Checks if a number is valid in the 3x3 square.
        is_valid(empty, num): Checks if a number is valid in the specified cell.
        solver(): Solves the Sudoku puzzle using backtracking.
    """

    def __init__(self, board):
        """
        Initializes the Board with the given 2D list.

        Args:
            board (list): A 2D list representing the Sudoku board.
        """
        self.board = board

    def __str__(self):
        """
        Returns a string representation of the board.

        Returns:
            str: The Sudoku board as a string with rows separated by newlines.
        """
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str
    
    def find_empty_cell(self):
        """
        Finds the next empty cell (with value 0) on the board.

        Returns:
            tuple: A tuple (row, col) indicating the position of the empty cell.
            None: If there are no empty cells.
        """
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        """
        Checks if a number is valid in the specified row.

        Args:
            row (int): The row index.
            num (int): The number to check.

        Returns:
            bool: True if the number is not in the row, False otherwise.
        """
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        """
        Checks if a number is valid in the specified column.

        Args:
            col (int): The column index.
            num (int): The number to check.

        Returns:
            bool: True if the number is not in the column, False otherwise.
        """
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        """
        Checks if a number is valid in the 3x3 square.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            num (int): The number to check.

        Returns:
            bool: True if the number is not in the 3x3 square, False otherwise.
        """
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True
        
    def is_valid(self, empty, num):
        """
        Checks if a number is valid in the specified cell.

        Args:
            empty (tuple): A tuple (row, col) indicating the position of the cell.
            num (int): The number to check.

        Returns:
            bool: True if the number is valid in the cell, False otherwise.
        """
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        
        return all([valid_in_row, valid_in_col, valid_in_square])
    
    def solver(self):
        """
        Solves the Sudoku puzzle using backtracking.

        Returns:
            bool: True if the puzzle is solved, False if it is unsolvable.
        """
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                self.board[row][col] = 0
        return False
    

def solve_sudoku(board):
    """
    Solves the given Sudoku puzzle.

    Args:
        board (list): A 2D list representing the Sudoku board.

    Returns:
        Board: The solved Sudoku board.
    """
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard

