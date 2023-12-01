# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    dict = {0: False,
            1: False,
            2: False,
            3: False,
            4: True,
            5: True,
            }
    return dict.get(version)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        middle = (left + right) >> 1
        while left < right:
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
            middle = (left + right) >> 1
        return middle


print(Solution().firstBadVersion(5))

# f f f t t
# 1 2 3 4 5