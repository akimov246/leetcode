class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                result += len(set(nums[i:j])) ** 2
        return result

print(Solution().sumCounts(nums = [1,2,1]))