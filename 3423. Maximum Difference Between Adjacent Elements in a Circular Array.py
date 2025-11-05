class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        nums.append(nums[0])
        max_diff = 0
        for i in range(1, len(nums)):
            max_diff = max(max_diff, abs(nums[i] - nums[i - 1]))

        return max_diff


print(Solution().maxAdjacentDistance(nums = [1,2,4]))