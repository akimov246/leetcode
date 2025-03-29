class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        result = -float('inf')
        for x in set(nums):
            for y in set(nums):
                if abs(x - y) <= min(x, y):
                    result = max(result, x ^ y)
        return result

print(Solution().maximumStrongPairXor(nums = [1,2,3,4,5]))