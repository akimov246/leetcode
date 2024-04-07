class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        matrix = []
        for i in range(m):
            matrix.append([])
            for _ in range(n):
                matrix[i].append(False)
        for r, c in indices:
            matrix[r] = [not bool(value) for value in matrix[r]]
            for i in range(len(matrix)):
                matrix[i][c] = not bool(matrix[i][c])
        ans = 0
        for row in matrix:
            ans += row.count(True)

        return ans


print(Solution().oddCells(m = 2, n = 3, indices = [[0,1],[1,1]]))