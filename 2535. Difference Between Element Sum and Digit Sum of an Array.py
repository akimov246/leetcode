class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            for n in str(num):
                digit_sum += int(n)
        return abs(element_sum - digit_sum)

print(Solution().differenceOfSum(nums = [1,15,6,3]))