class Solution:
    def fillCups(self, amount: list[int]) -> int:
        seconds = 0
        amount.sort()
        while amount[-1]:
            seconds += 1
            amount[-1] -= 1
            amount[1] -= 1
            amount.sort()
        return seconds

print(Solution().fillCups(amount = [5, 4, 4]))