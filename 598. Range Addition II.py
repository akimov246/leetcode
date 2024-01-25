class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        if len(ops) == 0:
            return m * n
        for a, b in ops:
            m = min(a, m)
            n = min(b, n)
        return m * n


print(Solution().maxCount(40000, 40000, [[2,2], [3,3]]))