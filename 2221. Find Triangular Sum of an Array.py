class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        while len(nums) != 1:
            for i in range(1, len(nums)):
                nums[i - 1] = (nums[i - 1] + nums[i]) % 10
            nums.pop()

        return nums[0]

print(Solution().triangularSum(nums = [1,2,3,4,5]))