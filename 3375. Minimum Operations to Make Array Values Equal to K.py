class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        nums = set(nums)
        nums.discard(k)
        if nums and min(nums) < k:
            return -1
        return len(nums)


print(Solution().minOperations(nums = [5,2,5,4,5], k = 2))