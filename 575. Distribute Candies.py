class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n = len(candyType)
        return len(tuple(set(candyType))[:n // 2])

print(Solution().distributeCandies([6,6,6,6]))