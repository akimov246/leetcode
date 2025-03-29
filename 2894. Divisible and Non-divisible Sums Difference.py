class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for x in range(1, n + 1):
            if x % m:
                num1 += x
            else:
                num2 += x
        return num1 - num2

print(Solution().differenceOfSums(n = 10, m = 3))