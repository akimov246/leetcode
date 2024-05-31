class Solution:
    def minOperations(self, nums: list[int]) -> int:
        operations = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                operations += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
        return operations

print(Solution().minOperations(nums = [1,5,2,4,1]))