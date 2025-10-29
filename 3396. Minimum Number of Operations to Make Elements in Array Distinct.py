class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        result = 0
        while len(nums) != len(set(nums)):
            nums = nums[3:]
            result += 1

        return result


print(Solution().minimumOperations(nums = [1,2,3,4,2,3,3,5,7]))