class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        end = 0
        total = 0
        for t in timeSeries:
            if end > t:
                total -= end - t
            end = t + duration
            total += duration
        return total



print(Solution().findPoisonedDuration([1, 4], 2))