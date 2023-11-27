class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev == nums[i]:
                return True
            prev = nums[i]
        return False