class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        left = 0
        right = sum(nums[1:])
        if left == right:
            return 0
        for i in range(1, len(nums)):
            left += nums[i - 1]
            right -= nums[i]
            if left == right:
                return i

        return -1


print(Solution().findMiddleIndex(nums = [2,3,-1,8,4]))