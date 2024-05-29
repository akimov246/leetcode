import operator

from itertools import accumulate

class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        return list(accumulate(encoded, operator.xor, initial=first))

print(Solution().decode(encoded = [1,2,3], first = 1))