class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        from_min = sorted(prices)
        from_max = from_min[::-1]
        for min_num in from_min:
            for max_num in from_max:
                if max_num == min_num:
                    return 0
                if prices.index(min_num) < prices.index(max_num):
                    return max_num - min_num if max_num - min_num > 0 else 0

print(Solution().maxProfit([7,6,4,3,1]))