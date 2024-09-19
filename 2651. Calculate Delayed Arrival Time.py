class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24

print(Solution().findDelayedArrivalTime(arrivalTime = 13, delayedTime = 11))