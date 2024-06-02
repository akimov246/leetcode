class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        ans = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                ans = min(ans, abs(i - start))
        return ans


print(Solution().getMinDistance(nums = [1,2,3,4,5], target = 5, start = 3))