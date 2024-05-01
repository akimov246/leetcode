class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        result = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    result.append(prices[i] - prices[j])
                    break
            else:
                result.append(prices[i])
        return result

print(Solution().finalPrices(prices = [8,4,6,2,3]))