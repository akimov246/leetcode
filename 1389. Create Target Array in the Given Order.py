class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target = []
        for i, n in zip(index, nums):
            target.insert(i, n)
        return target

print(Solution().createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]))