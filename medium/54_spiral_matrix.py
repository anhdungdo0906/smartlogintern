from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rows_length = len(matrix)
        cols_length = len(matrix[0])
        length = rows_length * cols_length

        rows_start = 0
        rows_end = rows_length - 1
        rows_index = 0

        cols_start = 0
        cols_end = cols_length - 1
        cols_index = 0

        result = []

        for i in range(length):
            current_number = matrix[rows_index][cols_index]
            result.append(current_number)

            # from left to right
            if rows_index == rows_start and cols_index < cols_end:
                cols_index += 1
                continue

            # from top to bottom
            if cols_index == cols_end and (rows_index == rows_start or rows_index < rows_end):
                rows_index += 1
                continue

            # from right to left
            if rows_index == rows_end and (cols_index == cols_end or cols_index > cols_start):
                # if we are at right bottom point for the second time, move cols start index
                if cols_index == cols_end and rows_index == rows_end and cols_end < cols_length - 1 and rows_end < rows_length - 1:
                    cols_start += 1

                cols_index -= 1
                continue

            # if we are at left bottom point, move rows start point and go up
            if rows_index == rows_end and cols_index == cols_start:
                rows_start += 1
                rows_index -= 1
                continue

            # from bottom to up
            if cols_index == cols_start and rows_index >= rows_start:
                rows_index -= 1

                # if we done one full circle, move cols and rows endpoints
                if rows_index == rows_start:
                    cols_end -= 1
                    rows_end -= 1
                continue

        return result


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sol = Solution()
print(sol.spiralOrder(matrix1))