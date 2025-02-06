class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                return False
        return True

print(Solution().isArraySpecial([2, 1, 4]))