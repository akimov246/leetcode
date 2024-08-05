class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        nums = set(nums)
        if 0 in nums:
            return len(nums) - 1
        return len(nums)

print(Solution().minimumOperations(nums = [1,5,0,3,5]))