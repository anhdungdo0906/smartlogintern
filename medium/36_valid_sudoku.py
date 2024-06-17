'''
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    - Each row must contain the digits 1-9 without repetition.
    - Each column must contain the digits 1-9 without repetition.
    - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    Note:
    - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    - Only the filled cells need to be validated according to the mentioned rules.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def is_valid_row(board, row):
            seen = set()
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] in seen:
                        return False

                    seen.add(board[row][col])
            return True

        def is_valid_col(board, col):
            seen = set() # keep track of the digits encountered in the current column.
            for row in range(9):
                if board[row][col] != '.': # check if current cell is not empty
                    if board[row][col] in seen:
                        return False

                    seen.add(board[row][col])
            return True

        def is_valid_3x3(board, start_row, start_col):
            seen = set()
            for row in range(start_row, start_row + 3): # specify the starting row index
                for col in range(start_col, start_col + 3):  # specify the starting column index
                    if board[row][col] != '.':
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])
            return True

        # Check each row
        for row in range(9):
            if not is_valid_row(board, row):
                return False

        # Check each column
        for col in range(9):
            if not is_valid_col(board, col):
                return False

        # Kiểm tra từng hộp 3x3
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                if not is_valid_3x3(board, start_row, start_col):
                    return False


