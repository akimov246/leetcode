class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        for num in set(nums):
            if nums.count(num) > n / 2:
                return num

print(Solution().majorityElement([3,2,3]))