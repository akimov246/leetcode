class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        return (nums.pop() - 1) * (nums.pop() - 1)

print(Solution().maxProduct(nums = [3,4,5,2]))