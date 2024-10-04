class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        return sum(nums[i] * nums[i] for i in range(len(nums)) if len(nums) % (i + 1) == 0)

print(Solution().sumOfSquares(nums = [1,2,3,4]))