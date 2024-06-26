from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize the matrix with zeros
        matrix = [[0] * n for _ in range(n)]

        # Initialize boundaries
        top, bottom = 0, n - 1
        left, right = 0, n - 1

        # Start with the number 1
        num = 1

        # Làm đầy ma trận cho đến khi đạt được n^2 phần tử
        while num <= n * n:
            # Làm đầy hàng đầu tiên, từ trái -> phải
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            # Dịch chuyển biên của top xuống đưới 1 đơn vị
            top += 1

            # Làm đầy cột phía bên phải, từ trên xuống dưới
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1  # Dịch chuyển biên của boundary sang trái 1 đơn vị

            # Làm đầy hàng dưới, từ phai sang trái
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1  # Dịch chuyển biên của bottom lên trên 1 đơn vị

            # Làm đầy cột trái, từ dưới -> trên
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1  # Dịch chuyển biên trái sang phải 1 đơn vị

        return matrix


solution = Solution()
print(solution.generateMatrix(3))