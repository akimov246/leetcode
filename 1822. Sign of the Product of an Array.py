import operator
from functools import reduce

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        def signFunc(x):
            if x > 0:
                return 1
            if x < 0:
                return -1
            else:
                return 0

        product = reduce(operator.mul, nums)
        return signFunc(product)

print(Solution().arraySign(nums = [-1,-2,-3,-4,3,2,1]))