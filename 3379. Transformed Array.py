class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        return [nums[(i + nums[i]) % (len(nums))] for i in range(len(nums))]


print(Solution().constructTransformedArray(nums = [3,-2,1,1]))