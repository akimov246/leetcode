class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        if target not in nums:
            return []
        nums.sort()
        indexes = []
        for i in range(len(nums)):
            if nums[i] == target:
                while i < len(nums) and nums[i] == target:
                    indexes.append(i)
                    i += 1
                return indexes

print(Solution().targetIndices(nums = [1,2,5,2,3], target = 2))