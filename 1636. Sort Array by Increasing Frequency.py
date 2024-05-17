class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        count = {}
        for value in set(nums):
            count[value] = nums.count(value)

        return sorted(nums, key=lambda value: (count[value], -value))

print(Solution().frequencySort(nums = [2,3,1,3,2]))