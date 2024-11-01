class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = max(nums)
        nums.sort()
        base = [i for i in range(1, n + 1)] + [n]
        return base == nums

#print(Solution().isGood(nums = [2, 1, 3]))