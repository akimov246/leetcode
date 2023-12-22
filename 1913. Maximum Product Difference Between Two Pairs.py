class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        nums = sorted(nums)
        return nums[-1] * nums[-2] - nums[0] * nums[1]

nums = [5,6,2,7,4]
print(Solution().maxProductDifference(nums))