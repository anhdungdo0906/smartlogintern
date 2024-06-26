from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sắp xếp từ bé đến lớn
        nums.sort()

        # Khởi tạo giá trị tổng gần nhất với giá trị vô cùng
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            # Khởi tạo 2 con trỏ
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Nếu giá tri sum gần với giá trị target -> cập nhật giá trị closest sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1  # Dịch chuyển con trỏ trái sang phải
                elif current_sum > target:
                    right -= 1  # Dịch chuyển con trỏ phải sang trái
                else:
                    return current_sum  # Nếu current_sum == target, ta tìm được giá trị sum gần nhất

        return closest_sum

solution = Solution()
print(solution.threeSumClosest([-1, 2, 1, -4], 1))  # 2
print(solution.threeSumClosest([0, 0, 0], 1))  # 0
