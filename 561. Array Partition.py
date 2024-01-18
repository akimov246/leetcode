class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        return sum(num for i, num in enumerate(sorted(nums)) if i % 2 == 0)

print(Solution().arrayPairSum([1,4,3,2]))