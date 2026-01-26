"""
The following program uses multiple functions to check whether
a standard 9x9 sudoku grid is valid.  A valid sudoku grid has
the numbers 1-9 at most once in each row, column, and 3x3 block
within the 9x9 grid.    

The program first checks if the 9 columns and 9 rows are valid.
Then, the program checks the 9 3x3 blocks within the sudoku grid
for their validity.  If all the conditions for a correct sudoku grid
are met, then the sudoku_grid_correct function returns True;  else,
the function returns False.
"""

def row_correct(sudoku: list, row_no: int):
    numbers_list = []

    for cell in sudoku[row_no]:
        if cell > 0 and cell in numbers_list:
            return False
        numbers_list.append(cell)
    
    return True


def column_correct(sudoku: list, column_no: int):
    numbers_list = []
    for row in sudoku:
        cell = row[column_no]
        if cell > 0 and cell in numbers_list:
            return False
        numbers_list.append(cell)
    
    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers_list = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            cell = sudoku[i][j]
            if cell > 0 and cell in numbers_list:
                return False
            numbers_list.append(cell)
    
    return True


def sudoku_grid_correct(sudoku:list):
    for i in range(9):
        if not row_correct(sudoku, i) or not column_correct(sudoku, i):
            return False

    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
             if not block_correct(sudoku, row, column):
                return False
    
    return True


def main():
    sudoku_grid = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku_grid))


main()

