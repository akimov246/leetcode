class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        patterns = {}
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [int(not e) for e in matrix[i]]
            patterns[tuple(matrix[i])] = patterns.get(tuple(matrix[i]), 0) + 1
        return max(patterns.values())

print(Solution().maxEqualRowsAfterFlips(matrix = [[0,0,0],[0,0,1],[1,1,0]]))