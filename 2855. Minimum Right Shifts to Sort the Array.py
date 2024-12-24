class Solution:
    def minimumRightShifts(self, nums: list[int]) -> int:
        target = sorted(nums)

        for shift in range(len(nums) - 1):
            if nums == target:
                return shift
            nums = [nums[-1]] + nums[:-1]

        return -1

print(Solution().minimumRightShifts(nums = [3,4,5,1,2]))