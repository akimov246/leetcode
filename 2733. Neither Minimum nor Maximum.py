class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return -1
        nums.sort()
        return nums[1]

print(Solution().findNonMinOrMax(nums = [3,2,1,4]))