class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = max(prices)
        while profit:
            for i in range(len(prices)):
                if prices[i] - profit in prices:
                    if prices.index(prices[i] - profit) < i:
                        # print("За что продали - профит = за что купили")
                        # print(f"{prices[i]} - {profit} = {prices[i] - profit}")
                        return profit
            profit -= 1
        return profit

print(Solution().maxProfit([2,1,2,0,1]))
# За что продали - за что купили = профит
# За что продали - профит = за что купили
# Профит - за что продали = -за что купили