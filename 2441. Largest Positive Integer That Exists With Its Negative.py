class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for n in nums:
            if n > 0 and -n in nums:
                return n
        return -1

print(Solution().findMaxK(nums = [-1,2,-3,3]))