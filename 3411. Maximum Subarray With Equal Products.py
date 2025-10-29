import math


class Solution:
    def maxLength(self, nums: list[int]) -> int:
        length = len(nums)

        while length:
            for i in range(len(nums) - length + 1):
                tmp_nums = nums[i: i + length]
                if math.prod(tmp_nums) == math.gcd(*tmp_nums) * math.lcm(*tmp_nums):
                    return length
            length -= 1
        return length


print(Solution().maxLength(nums = [1,2,1,2,1,1,1]))