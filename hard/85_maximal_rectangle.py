from typing import List

# xem lại
# https://www.youtube.com/watch?v=X0X6G-eWgQ8
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Nếu ma trận rỗng/ dòng đầu tiên rỗng -> trả về 0
        if not matrix or not matrix[0]:
            return 0

        # Số hàng và số cột của ma trận
        rows = len(matrix)
        cols = len(matrix[0])

        # Biến lưu trữ hình chữ nhất lớn nhất tìm đc
        max_area = 0

        # Là một dãy các số 0 tương ứng với số cột
        # Dùng để lưu trữ chiều cao của cột
        height = [0] * cols

        for i in range(rows):
            for j in range(cols):
                # Nếu bằng 1, tăng độ dài của cột
                if matrix[i][j] == '1':
                    height[j] += 1
                # Nếu bằng 0, reset chiều cao của cột về 0
                else:
                    height[j] = 0

            # Tính toán hình chữ nhật lớn nhát với height hiện tại
            # Cập nhật max_area nếu nhu có diện tích lớn hơn
            max_area = max(max_area, self.largestRectangleArea(height))

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        # Nếu list chiều cao rỗng, trả về 0
        if not heights:
            return 0

        # Thêm 0 vào cuối danh sách
        # Đảm bảo tất cả các thanh có trong stack được xử lý sau khi vòng lặp kết thúc
        # Chiều cao của thanh nhỏ hơn bất kỳ thanh nào có trong danh sách, pop các thanh còn lại và tính toán diện tích
        heights.append(0)

        # Khởi tạo list, nhưng dùng như một stack sau này
        stack = []

        max_area = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                # Lấy chiều cao của thanh cuối cùng trong stack
                h = heights[stack.pop()]

                # chiều rộng là i nếu stack rỗng
                if not stack:
                    w = i
                    # Nếu stack không rỗng, chiều rộng là khoảng cách giữa chỉ số hiện tại
                    # và chỉ số của thanh ở đỉnh stack mới
                else:
                    w = i - stack[-1] - 1

                # Cập nhật diện tích lớn nhất của hình chữ nhật
                max_area = max(max_area, h * w)
            stack.append(i)

        return max_area
