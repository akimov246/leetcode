# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    g = 6
    if num == g:
        return 0
    if num < g:
        return -1
    if num > g:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        # if n == 1:
        #     return 1
        left = 1
        right = n
        middle = (left + right) // 2
        while left < right:
            if guess(middle) == 0:
                return middle
            elif guess(middle) < 0:
                left = middle + 1
            elif guess(middle) > 0:
                right = middle
            middle = (left + right) // 2
        return middle

print(Solution().guessNumber(1488))
# 1, 2
# !