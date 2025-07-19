class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return sum(bool(n % 3) for n in nums)

print(Solution().minimumOperations(nums = [1,2,3,4]))