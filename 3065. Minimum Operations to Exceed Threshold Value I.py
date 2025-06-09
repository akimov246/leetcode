class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        counter = 0
        for n in nums:
            if n < k:
                counter += 1
        return counter

print(Solution().minOperations(nums = [2,11,10,1,3], k = 10))