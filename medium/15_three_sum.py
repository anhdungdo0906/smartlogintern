'''
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array
        n = len(nums)
        result = []

        for i in range(n - 2):
            # Skip duplicates for the first element of the triplet
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
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for the second element of the triplet
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third element of the triplet
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result

    # sorting: O(nlog(n))
    # iterating: O(n)
    # two pointers (L and R): O(n)
    # duplicate handling: O(n)
