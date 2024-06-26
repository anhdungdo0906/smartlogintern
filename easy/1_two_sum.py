from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}  # Tạo dictionary lưu trữ phần tử + vị trí của phần tử

        for i, num in enumerate(nums):
            # Tính phần bù, lấy số cần tìm trừ
            comp = target - num
            if comp in dict:
                return [dict[comp], i]
            dict[num] = i

        # Nếu k có đáp án nào thỏa mãn
        return []
