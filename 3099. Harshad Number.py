class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_ = sum(int(n) for n in str(x))
        return -1 if x % sum_ else sum_

print(Solution().sumOfTheDigitsOfHarshadNumber(18))