class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        sum_of_longest_prefix = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                break
            sum_of_longest_prefix += nums[i]

        while True:
            if sum_of_longest_prefix not in nums:
                return sum_of_longest_prefix
            sum_of_longest_prefix += 1

print(Solution().missingInteger(nums = [29,30,31,32,33,34,35,36,37]))