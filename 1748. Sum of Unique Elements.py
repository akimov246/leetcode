class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:

        def is_unique(value):
            count = 0
            for n in nums:
                if n == value:
                    count += 1
                if count > 1:
                    return False
            return True

        sum_ = 0
        for n in set(nums):
            if is_unique(n):
                sum_ += n
        return sum_

print(Solution().sumOfUnique(nums = [1,2,3,2]))