from math import factorial
from functools import cache

class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        dominoes = [frozenset(chip) for chip in dominoes]
        pairs = 0
        count = dict()
        for chip in dominoes:
            count[chip] = count.get(chip, 0) + 1

        @cache
        def combination(value):
            return factorial(value) // (factorial(value - 2) * factorial(2))

        for chip in count:
            if count[chip] > 1:
                pairs += combination(count[chip])
        return pairs

print(Solution().numEquivDominoPairs(dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]))