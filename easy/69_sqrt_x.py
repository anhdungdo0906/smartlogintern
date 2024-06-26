class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 2
        right = x // 2 # chia lấy phần nguyên

        while left <= right:
            mid = (left + right) // 2
            num = mid*mid

            if num == x:
                return mid
            elif num < x:
                left = mid+1
            else:
                right = mid-1

        return right
