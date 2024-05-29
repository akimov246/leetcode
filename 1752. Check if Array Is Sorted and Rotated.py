class Solution:
    def check(self, nums: list[int]) -> bool:
        return str(sorted(nums))[1:-1] in str(nums * 2)[1:-1]

print(Solution().check(nums = [6,10,6]))