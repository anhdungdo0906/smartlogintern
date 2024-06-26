from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Kiểm tra xem mảng có rỗng không
        if not nums:
            return []

        permutations = [[]]

        for num in nums:
            new_permutations = []
            for permutation in permutations:
                for i in range(len(permutation) + 1):
                    new_permutation = permutation[:i] + [num] + permutation[i:]
                    # [:i]: danh sách các ptu từ đầu đến vị trí i-1
                    # [i:]: danh sách các ptu từ vị trí i đến cuối của permutation
                    new_permutations.append(new_permutation)
            # Cập nhật danh sách permuations
            permutations = new_permutations

        return permutations

sol = Solution()
nums1 = [1, 2, 3]
print(sol.permute(nums1))


