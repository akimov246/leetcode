class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        max_sum = 0
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_sum += nums[i]
            else:
                max_sum = max(max_sum, cur_sum)
                cur_sum = nums[i]
        max_sum = max(max_sum, cur_sum)
        return max_sum


print(Solution().maxAscendingSum(nums = [10,20,30,5,10,50]))