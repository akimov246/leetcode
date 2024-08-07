class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        x = 2
        while True:
            if x % n == 0:
                return x
            x += 2

print(Solution().smallestEvenMultiple(5))