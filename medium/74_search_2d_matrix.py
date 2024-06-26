'''
Đầu vào:
- matrix: Một ma trận m x n (danh sách các danh sách) chứa các số nguyên, với hai tính chất sau:
Mỗi hàng được sắp xếp theo thứ tự không giảm (non-decreasing order).
- Số nguyên đầu tiên của mỗi hàng lớn hơn số nguyên cuối cùng của hàng trước đó.
- target: Một số nguyên cần kiểm tra xem nó có tồn tại trong ma trận hay không.
Đầu ra:
-Trả về True nếu target tồn tại trong ma trận, ngược lại trả về False.
'''


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1

        # Dùng Binary search
        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // n][mid % n]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
