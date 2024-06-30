class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        current = nums[:k]
        current_min = min(current)
        for i in range(k, len(nums)):
            if nums[i] > current_min:
                current.remove(current_min)
                current.append(nums[i])
                current_min = min(current)
        return current

print(Solution().maxSubsequence(nums = [-1,-2,3,4], k = 3))