# Sudoku Solver

## Description

This project is a Sudoku Solver implemented in Python. It uses Object-Oriented Programming (OOP) concepts to create a `Board` class, which represents the Sudoku board and includes methods to solve the puzzle. The solver uses a backtracking algorithm to find the solution.


## Function Definition

### `Board` Class

- **`__init__(self, board)`**: Initializes the board with a 2D list representing the Sudoku grid.
- **`__str__(self)`**: Returns a string representation of the board.
- **`find_empty_cell(self)`**: Finds the next empty cell (with value 0) on the board.
- **`valid_in_row(self, row, num)`**: Checks if a number is valid in the specified row.
- **`valid_in_col(self, col, num)`**: Checks if a number is valid in the specified column.
- **`valid_in_square(self, row, col, num)`**: Checks if a number is valid in the 3x3 square.
- **`is_valid(self, empty, num)`**: Checks if a number is valid in the specified cell.
- **`solver(self)`**: Solves the Sudoku puzzle using backtracking.

### `solve_sudoku(board)`

- **Args**:
  - `board (list)`: A 2D list representing the Sudoku board.
- **Returns**:
  - `Board`: The solved Sudoku board.

## Examples

### Example 1: Solvable Puzzle

```python
puzzle = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5]
]
solve_sudoku(puzzle

Output

Puzzle to solve:
* * 2 * * 8 * * *
* * * * * 3 7 6 2
4 3 * * * * 8 * *
* 5 * * 3 * * 9 *
* 4 * * * * * 2 6
* * * 4 6 7 * * *
* 8 6 7 * 4 * * *
* * * 5 1 9 * * 8
1 7 * * * 6 * * 5

Solved puzzle:
9 6 2 1 7 8 3 5 4
8 1 5 9 4 3 7 6 2
4 3 7 6 5 2 8 1 9
6 5 8 2 3 1 4 9 7
7 4 3 8 9 5 1 2 6
2 9 1 4 6 7 5 8 3
5 8 6 7 2 4 9 3 1
3 2 4 5 1 9 6 7 8
1 7 9 3 8 6 2 4 5
```

### Example 2: Unsolvable Puzzle

```
unsolvable_puzzle = [
    [1, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [0, 7, 0, 0, 0, 6, 0, 0, 1]
]
solve_sudoku(unsolvable_puzzle)

Output
Puzzle to solve:
1 * 2 * * 8 * * *
* * * * * 3 7 6 2
4 3 * * * * 8 * *
* 5 * * 3 * * 9 *
* 4 * * * * * 2 6
* * * 4 6 7 * * *
* 8 6 7 * 4 * * *
* * * 5 1 9 * * 8
* 7 * * * 6 * * 1

The provided puzzle is unsolvable.
```
