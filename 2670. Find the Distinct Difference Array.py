class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        diff = []
        for i in range(1, len(nums) + 1):
            diff.append(len(set(nums[:i])) - len(set(nums[i:])))
        return diff

print(Solution().distinctDifferenceArray(nums = [1,2,3,4,5]))