class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices.sort()
        if sum(prices[:2]) <= money:
            return money - sum(prices[:2])
        return money

print(Solution().buyChoco(prices = [1,2,2], money = 3))