from functools import cache

class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n in [1, 2]:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

print(Solution().tribonacci(500))