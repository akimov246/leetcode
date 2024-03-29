class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return sum(nums[i:i + 3])
        return 0

print(Solution().largestPerimeter(nums = [1,2,1,10]))