'''
    Cho một mảng các số nguyên ĐẴ SẮP XÊP theo thứ tự TĂNG DẦN
    Tìm điểm BẮT ĐẦU và KẾT THÚC của giá trị TARGET cho trước
'''

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Sử dụng cách tiếp cận Binary Search
        def searchFirst(nums, target):
            left = 0
            right = len(nums) - 1

            # Chỉ số sô nguyên đầu tiên cần tìm
            # K tìm được số nguyên nào thì trả về -1
            first_pos = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first_pos = mid # Tìm được vị trí đầu tiên -> update

                    #
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_pos

        def searchLast(nums, target):
            left = 0
            right = len(nums) - 1
            last_pos = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last_pos = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_pos

        first_position = searchFirst(nums, target)
        last_position = searchLast(nums, target)

        if first_position != -1:
            return [first_position, last_position]
        else:
            return [-1, -1]


solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 8))  # Output: [3, 4]