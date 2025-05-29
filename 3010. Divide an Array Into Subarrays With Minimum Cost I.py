class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        return nums.pop(0) + nums.pop(nums.index(min(nums))) + nums.pop(nums.index(min(nums)))

print(Solution().minimumCost(nums = [1,5,1,6]))