class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0, 1]
        nums.extend([None] * (n - 1))
        for i in range(2, len(nums)):
            if i % 2:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
            else:
                nums[i] = nums[i // 2]
        return max(nums)


print(Solution().getMaximumGenerated(7))