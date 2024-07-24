class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        result = set(nums[-1])
        for i in range(len(nums) - 1):
            result &= set(nums[i])
        return sorted(result)


nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
print(Solution().intersection(nums))