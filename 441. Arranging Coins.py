class Solution:
    def arrangeCoins(self, n: int) -> int:
        counter = 0
        while n > counter:
            counter += 1
            n -= counter
        return counter


print(Solution().arrangeCoins(8))