from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: # Kiểm tra xem mảng rỗng hay không
            return 0

        # Theo dõi vị trí phần tử duy nhất cuối cùng
        i = 0

        for j in range(1, len(nums)):
            # Nếu phần tử tại j khác i thì tăng i và cập nhật phần tử
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        # Trả về số lượng phần tử duy nhất
        return i + 1

solution = Solution()
nums1 = [1, 1, 2]
k1 = solution.removeDuplicates(nums1)
print(k1,",",nums1[:k1])