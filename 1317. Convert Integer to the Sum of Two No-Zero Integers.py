class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for i in range(1, n):
            if '0' not in str(i):
                if '0' not in str(n - i):
                    return [i, n - i]

print(Solution().getNoZeroIntegers(2))