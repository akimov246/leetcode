class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = 1
        ans = 0
        while left < len(nums):
            if right >= len(nums):
                left += 1
                right = left + 1
                continue
            if abs(nums[left] - nums[right]) == k:
                ans += 1
            right += 1
        return ans



print(Solution().countKDifference([1,2,2,1], 1))