class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        result = 0

        for i in range(len(nums)):
            result += sum(nums[max(0, i - nums[i]): i + 1])

        return result

print(Solution().subarraySum(nums = [2,3,1]))