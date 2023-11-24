class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        my_coins = 0
        piles.sort()
        while piles:
            piles.pop()
            my_coins += piles.pop()
            piles.pop(0)
        return my_coins



piles = [9,5,6,8,10,1,4,10,7]
print(Solution().maxCoins(piles))