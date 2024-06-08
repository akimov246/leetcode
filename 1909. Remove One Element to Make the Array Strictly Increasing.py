class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            tmp = nums[:i] + nums[i + 1:]
            if len(tmp) == len(set(tmp)) and tmp == sorted(tmp):
                return True
        return False

print(Solution().canBeIncreasing(nums = [1, 1, 1]))
