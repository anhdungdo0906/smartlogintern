class Solution:
    def myPow(self, x: float, n: int) -> float:
        # code này tle O(n)
        # abs_n = abs(n)
        # result = 1
        # for i in range(abs_n):
        #     result = result * x
        #
        # if n == 0:
        #     return 1
        # elif n < 0:
        #     return 1 / result
        # else:
        #     return result

        # https://en.wikipedia.org/wiki/Exponentiation_by_squaring
        # O(log(n))
        def exp(x, n):
            if n < 0:
                return exp(1 / x, -n)
            elif n == 0:
                return 1
            elif n % 2 == 0:
                return exp(x * x, n // 2)
            else:
                return x * exp(x * x, (n - 1) // 2)

        return exp(x, n)