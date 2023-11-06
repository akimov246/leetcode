class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums and i != nums.index(complement):
                return [i, nums.index(complement)]




nums = [2,7,11,15]
target = 9

print(Solution().twoSum(nums, target))