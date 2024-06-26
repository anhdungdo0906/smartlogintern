'''
    Leo thang bộ mất n bước để lên đỉnh
    Mỗi lần có thể leo 1/2 bước. Có bao nhiêu cách leo lên đỉnh?
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        # Đứng yên là 1 cách
        if n == 0:
            return 1
        # Có duy nhất 1 cách là đi 1 bước lên
        elif n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1  # Đứng yên là 1 cách
        dp[1] = 1  # Có duy nhất 1 cách là đi 1 bước lên

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
