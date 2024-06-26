'''
    Cho một dãy số CHƯA SẮP XẾP
    Trả về SỐ NGUYÊN DƯƠNG nhỏ nhất KHÔNG xuất hiện trong dãy số trên
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Chiều dài của mảng
        n = len(nums)

        # Phần tử nhỏ nhất là 1
        # Ta chỉ quan tâm tới phần tử nguyên dương nhỏ nhất ko xuất hiện
        # -> Chỉ cần duyệt từ 1 -> n, do số nguyên dương bé nhất
        # kiểu gì cũng nằm trong khoảng 1 -> n+1

        # 1. Lọc phần tử không liên quan
        # Bao gồm phần tử nhỏ hơn 0 và phần tử lớn hơn n
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n+1
                # Thay thế, vì các phần tử nằm ngoài khoảng này không liên quan đến yc bài toàn

        # 2. Đánh dấu sự xuất hiện của các phần tử
        for i in range(n):
            # Lấy giá trị tuyệt đối để đảm bảo làm việc với giá trị dương
            num = abs(nums[i])

            if num <= n:
                # Đánh dấu 1 số đã xuất hiện bằng cách chuyển giá trị tại vị trí tương úng thành số âm
                nums[num - 1] = -abs(nums[num - 1])

        # 3. Tìm kiếm phần tử dương nhỏ nhất bị thiếu
        for i in range(n):
            if nums[i] > 0:
                return i + 1
            # Trường hợp nums[i] là số dương -> i+1 chưa xuất hiện trong mảng
            # Trả về i+1 là số nguyên dương nhỏ nhất bị thiếu

        # Nếu không có giá trị dương nào trong mảng -> mọi sô từ 1 tới n đã xuất hiện
        # Số nguyên dương nhỏ nhất là n+1

        return n+1
