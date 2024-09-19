class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        return sum(range(max(nums), max(nums) + k))

print(Solution().maximizeSum(nums = [5,5,5], k = 2))