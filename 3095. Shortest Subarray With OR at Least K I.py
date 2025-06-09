class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        gap = 1
        while gap < len(nums) + 1:
            for i in range(gap, len(nums) + 1):
                current = nums[i - gap:i]
                result = 0
                for j in range(len(current)):
                    result |= current[j]
                    if result >= k:
                        return gap
            gap += 1
        return -1

print(Solution().minimumSubarrayLength(nums = [2,1,8], k = 10))