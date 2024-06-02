class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = ''
        while n >= k:
            res += str(n % k)
            n //= k
        res += str(n)
        print(res)
        return sum(int(n) for n in res)

print(Solution().sumBase(n = 42, k = 2))