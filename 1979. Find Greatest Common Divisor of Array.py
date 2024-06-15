class Solution:
    def findGCD(self, nums: list[int]) -> int:

        def binaty_alg(m: int, n: int) -> int:
            if n and m == 0:
                return n
            if m and n == 0:
                return m
            if m == n:
                return m
            if n and m == 1:
                return 1
            if m and n == 1:
                return 1
            if m % 2 == 0 and n % 2 == 0:
                return 2 * binaty_alg(m // 2, n // 2)
            if m % 2 == 0 and n % 2:
                return binaty_alg(m // 2, n)
            if m % 2 and n % 2 == 0:
                return binaty_alg(m, n // 2)
            if n > m and m % 2 and n % 2:
                return binaty_alg(m, (n - m) // 2)
            if m > n and m % 2 and n % 2:
                return binaty_alg((m - n) // 2, n)

        return binaty_alg(min(nums), max(nums))

print(Solution().findGCD(nums = [1337, 1488]))