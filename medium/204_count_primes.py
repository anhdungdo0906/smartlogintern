class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        # Khởi tạo mảng để tìm số nguyên tố
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        # Use Sieve of Eratosthenes to mark non-prime numbers
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of i as non-prime starting from i*i
                for j in range(i * i, n, i):
                    is_prime[j] = False

        # Count primes
        return sum(is_prime)
