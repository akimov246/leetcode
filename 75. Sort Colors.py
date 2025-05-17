class Solution:
    def sortColors(self, nums: list[int]) -> None:
        i = 1
        while i < len(nums):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                i = max(i - 1, 1)
            else:
                i += 1


Solution().sortColors(nums = [2,0,2,1,1,0])