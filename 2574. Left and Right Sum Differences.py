class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        total = sum(nums)
        left_sum = [0]
        right_sum = [total - nums[0]]
        answer = []
        for i in range(1, len(nums)):
            answer.append(abs(left_sum[i - 1] - right_sum[i - 1]))
            left_sum.append(left_sum[-1] + nums[i - 1])
            right_sum.append(right_sum[-1] - nums[i])
        answer.append(left_sum[-1])
        return answer




print(Solution().leftRightDifference(nums = [10,4,8,3]))