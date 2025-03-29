class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        result = float('inf')
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        result = min(result, nums[i] + nums[j] + nums[k])
        return result if result != float('inf') else -1

print(Solution().minimumSum(nums = [8,6,1,5,3]))