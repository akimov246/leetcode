import itertools
import operator

from functools import reduce

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        total = 0
        length = 1
        while length != len(nums) + 1:
            subsets = itertools.combinations(nums, length)
            for subset in subsets:
                total += reduce(operator.xor, subset, 0)
            length += 1

        return total


print(Solution().subsetXORSum(nums = [5,1,6]))