import numpy

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        prices = numpy.array(prices, "i4")
        if len(prices) == 1:
            return 0
        #profits = (max(prices[i + 1:]) - prices[i] for i in range(len(prices) - 1))
        profits = (numpy.max(prices[i + 1:]) - prices[i] for i in range(len(prices) - 1))
        profit = max(profits)
        return profit if profit > 0 else 0

# Решение с Leetcode
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0 #Buy
        right = 1 #Sell
        profit = 0
        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                profit = max(current_profit, profit)
            else:
                left = right
            right += 1
        return profit




print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
# За что продали - за что купили = профит
# За что продали - профит = за что купили
# Профит - за что продали = -за что купили