from typing import List



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Kiểm tra hàng đầu tiên có chứa phần tử 0 nào không
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Kiểm tra cột đầu tiên có chứa phần tử 0 nào không
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Dùng cột đầu tiên và hàng đầu tiên để chứa phần tử 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set matrix cells to zero based on markers in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Với trường
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

solution = Solution()
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.setZeroes(matrix1)
print(matrix1)  # Output: [[1,0,1],[0,0,0],[1,0,1]]