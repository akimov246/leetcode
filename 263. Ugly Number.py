class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        while n not in [2, 3, 5]:
            if not n % 2:
                n //= 2
            elif not n % 3:
                n //= 3
            elif not n % 5:
                n //= 5
            else:
                return False
        return True

print(Solution().isUgly(14))