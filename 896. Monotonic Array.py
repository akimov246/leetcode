class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        prev = nums[0]
        if nums[0] < nums[-1]:
            for i in range(1, len(nums)):
                if nums[i] < prev:
                    return False
                prev = nums[i]
        else:
            for i in range(1, len(nums)):
                if nums[i] > prev:
                    return False
                prev = nums[i]

        return True

print(Solution().isMonotonic(nums = [1,2,2,3]))