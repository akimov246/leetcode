class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        answer = []

        for i in range(len(prices)):
            price = prices[i]
            for j in range(i + 1, len(prices)):
                if prices[j] <= price:
                    price -= prices[j]
                    break
            answer.append(price)

        return answer

print(Solution().finalPrices(prices = [4,7,1,9,4,8,8,9,4]))
