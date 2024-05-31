class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        return next(iter(set(edges[0]).intersection(edges[1])))

print(Solution().findCenter(edges = [[1,2],[2,3],[4,2]]))