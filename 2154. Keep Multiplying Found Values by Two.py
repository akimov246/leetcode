class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        while original in set(nums):
            original *= 2
        return original

print(Solution().findFinalValue(nums = [5,3,6,1,12], original = 3))