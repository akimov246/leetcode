class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk_bottles = numBottles
        empty_bottles = numBottles
        while empty_bottles >= numExchange:
            empty_bottles -= numExchange
            drunk_bottles += 1
            empty_bottles += 1
        return drunk_bottles


print(Solution().numWaterBottles(numBottles = 9, numExchange = 3))