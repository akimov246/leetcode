#Решение не мое. Я слишком тупой, чтобы такое решить, кроме как полным перебором за миллион лет

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        cache = {} # (n, target) -> count

        def count(n, target):
            if n == 0:
                return 1 if target == 0 else 0
            if (n, target) in cache:
                return cache[(n, target)]

            res = 0
            for value in range(1, k + 1):
                res = (res + count(n - 1, target - value)) % MOD
            cache[(n, target)] = res
            return res

        return count(n, target)

print(Solution().numRollsToTarget(100, 100, 500))
