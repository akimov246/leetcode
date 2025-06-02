class Solution:
    def triangleType(self, nums: list[int]) -> str:
        a = nums[0]
        b = nums[1]
        c = nums[2]

        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return 'none'
        if len(set(nums)) == 1:
            return 'equilateral'
        if len(set(nums)) == 2:
            return 'isosceles'
        if len(set(nums)) == 3:
            return 'scalene'

print(Solution().triangleType(nums = [3,4,5]))