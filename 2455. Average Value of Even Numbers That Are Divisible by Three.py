class Solution:
    def averageValue(self, nums: list[int]) -> int:
        sum_ = 0
        length = 0
        for n in nums:
            if n % 2 == 0 and n % 3 == 0:
                sum_ += n
                length += 1
        return sum_ // length if length else 0

print(Solution().averageValue(nums = [1,3,6,10,12,15]))