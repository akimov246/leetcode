class Solution:
    def minElement(self, nums: list[int]) -> int:
        minimum = float('inf')

        for n in nums:
            sum_of_digits = sum(int(digit) for digit in str(n))
            minimum = min(minimum, sum_of_digits)

        return minimum


print(Solution().minElement(nums = [10,12,13,14]))