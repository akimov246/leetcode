class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        for _ in range(k):
            nums[nums.index(min(nums))] *= multiplier

        return nums


print(Solution().getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2))