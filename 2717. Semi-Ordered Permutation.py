class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        permutations = 0
        while True:
            if nums[0] == 1 and nums[-1] == len(nums):
                return permutations
            for i in range(2, len(nums) + 1):
                if (nums[i - 2:i][-1] == 1) or (nums[i - 2:i][0] == len(nums)):
                    nums[i - 2], nums[i - 1] = nums[i - 1], nums[i - 2]
                    permutations += 1
                    break

print(Solution().semiOrderedPermutation(nums = [2,1,4,3]))