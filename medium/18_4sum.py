'''
    Cho một mảng nums gồm n số nguyên, trả về một mảng bốn phần tử duy nhất sao cho:
    0 <= a, b, c, d < n
    a, b, c và d là các chỉ số khác nhau.
    nums[a] + nums[b] + nums[c] + nums[d] == target
    Có thể trả về theo bất kỳ thứ tự nào.
'''


from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sắp xếp mảng từ nhỏ đến lớn
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            # Bỏ qua những phần tử trùng lập cho số đầu tiên
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Bỏ qua những phần tử trùng lập cho số thứ 2
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j+1
                right = n-1
                while left < right:
                    # Tổng bằng tống 4 chỉ số
                    # i,j, left, right lần lượt là số thứ nhất đến số thứ 4.
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    # Kiểm tra xem bốn phần tử cộng vào có bằng target k
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Bỏ qua những phần tử trùng lập cho số thứ 3
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        # Bỏ qua những phần tử trùng lặp cho số cuối
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result

solution = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 2
print(solution.fourSum(nums, target))