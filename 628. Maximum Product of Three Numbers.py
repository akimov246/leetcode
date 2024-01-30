class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        left = nums[0] * nums[1] * nums[-1]
        right = nums[-1] * nums[-2] * nums[-3]
        if right > left:
            return right
        else:
            return left

print(Solution().maximumProduct([-100,-98,-1,2,3,4]))