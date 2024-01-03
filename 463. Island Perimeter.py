class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        ans = 0
        row = len(grid[0])
        col = len(grid)
        for i in range(col):
            for j in range(row):
                if grid[i][j] == 1:
                    shore = 0
                    if j == 0 or grid[i][j - 1] == 0:
                        shore += 1
                    if i == 0 or grid[i - 1][j] == 0:
                        shore += 1
                    if j == row - 1 or grid[i][j + 1] == 0:
                        shore += 1
                    if i == col - 1 or grid[i + 1][j] == 0:
                        shore += 1
                    ans += shore
        return ans

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(Solution().islandPerimeter(grid))