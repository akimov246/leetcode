from functools import reduce
import operator

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = reduce(operator.mul, (int(num) for num in str(n)), 1)
        sum_ = sum((int(num) for num in str(n)))
        return product - sum_

print(Solution().subtractProductAndSum(234))