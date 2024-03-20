class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        for _ in range(k):
            i = nums.index(min(set(nums)))
            nums[i] = -nums[i]
        return sum(nums)


print(Solution().largestSumAfterKNegations(nums = [4,2,3], k = 1))