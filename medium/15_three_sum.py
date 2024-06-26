'''
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sắp xếp mảng từ bé -> lớn
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            # Loại bỏ phần tử trùng lặp đầu tiên
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                # total == 0
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # Loại bỏ phần tử trùng lặp thứ 2
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Loại bỏ phần tử trùng lặp thứ 3
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result

    # sorting: O(nlog(n))
    # iterating: O(n)
    # two pointers (L and R): O(n)
    # duplicate handling: O(n)
