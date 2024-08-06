class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        max_local = []
        for _ in range(len(grid) - 2):
            max_local.append([None] * (len(grid) - 2))

        for i in range(len(max_local)):
            for j in range(len(max_local[i])):
                max_ = 0
                for a in range(i, i + 3):
                    for b in range(j, j + 3):
                        max_ = max(max_, grid[a][b])
                max_local[i][j] = max_
        return max_local

print(Solution().largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))