class Solution:
    def sortedSquares(self, nums: list[int]) ->list[int]:
        nums = [n ** 2 for n in nums]
        return sorted(nums)

print(Solution().sortedSquares(nums = [-4,-1,0,3,10]))