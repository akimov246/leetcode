import math


class Solution:
    def countTriples(self, n: int) -> int:
        result = 0
        # squares = [x ** 2 for x in range(1, n + 1)]
        # for a in squares:
        #     for b in squares:
                # c = a + b
                # if c in squares:
                #     result += 1
        for a in range(1, n):
            for b in range(a + 1, n):
                s = math.sqrt(a * a + b * b)
                if int(s) == s and s <= n:
                    result += 2
        return result

print(Solution().countTriples(5))