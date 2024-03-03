from math import ceil

class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:

        max_ = max(nums)
        min_ = min(nums)

        if k == 0:
            return max_ - min_

        target = (max_ + min_) // 2
        k_range = set(range(-k, k + 1))

        for i in range(len(nums)):
            while (diff := target - nums[i]) not in k_range:
                if diff > k:
                    target = nums[i] + k
                else:
                    target = nums[i] - k

            nums[i] += diff

        return max(nums) - min(nums)

print(Solution().smallestRangeI(nums = [9,9,2,8,7], k = 4))