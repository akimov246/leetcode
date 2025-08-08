from collections import deque

class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        average = float('inf')
        nums = deque(sorted(nums))

        while nums:
            average = min(average, (nums.popleft() + nums.pop()) / 2)

        return average


print(Solution().minimumAverage(nums = [7,8,3,4,15,13,4,1]))