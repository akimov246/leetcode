class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums = set(nums)
        diapason = {num for num in range(0, len(nums) + 1)}
        return diapason.difference(nums).pop()

print(Solution().missingNumber([0,1]))