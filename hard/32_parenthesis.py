'''
    Cho một chuỗi chỉ chứa ngoặc đóng và mở.
    Trả về ĐỘ DÀI của chuỗi ngoặc con dài nhất hợp lệ
'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0 # Đếm số ngoặc trái
        right = 0 # Đếm số ngoặc phải
        max_length = 0 # Độ dài lớn nhất của ngoặc hợp lệ

        # cho biến đếm
        # gặp ngoặc trái thì tăng biến left, ngoặc phải thì tăng biến right
        # nếu có đủ left và right thì thêm vào max

        # tính max = left * 2

        # nếu gặp ngoặc k hợp lệ -> reset cả left và right về 0, vẫn giữ nguyên max

        # Duyệt từ trái sang phải
        # -> đảm bảo k có nhiều ngoặc phải hơn trái
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            # Tìm được chuỗi ngoặc hợp lệ
            if left == right:
                max_length = max(max_length, left*2)
            # Trương hợp chuỗi ngoặc k hợp lệ
            elif right > left:
                left = 0
                right =0

        left = 0
        right = 0

        # Duyệt từ phải sang trái
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_length = max(max_length, left*2)
            elif right < left:
                left = 0
                right =0

        return max_length


    # Time complexity: O(N)
