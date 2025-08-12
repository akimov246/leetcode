class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        single_digit_sum = 0
        double_digit_sum = 0
        for n in nums:
            if n < 10:
                single_digit_sum += n
            else:
                double_digit_sum += n

        return single_digit_sum != double_digit_sum

print(Solution().canAliceWin(nums = [1,2,3,4,10]))