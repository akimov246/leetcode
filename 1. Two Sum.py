class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sum = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]




nums = [2,7,11,15]
target = 9

print(Solution().twoSum(nums, target))