class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                z = grid[i][j]
                tmp = bool(z) * 2
                # Top
                if i - 1 < 0:
                    tmp += z
                else:
                    top = grid[i - 1][j]
                    if z > top:
                        tmp += z - top
                # Right
                if j + 1 >= len(grid[i]):
                    tmp += z
                else:
                    right = grid[i][j + 1]
                    if z > right:
                        tmp += z - right
                # Down
                if i + 1 >= len(grid):
                    tmp += z
                else:
                    down = grid[i + 1][j]
                    if z > down:
                        tmp += z - down
                # Left
                if j - 1 < 0:
                    tmp += z
                else:
                    left = grid[i][j - 1]
                    if z > left:
                        tmp += z - left
                area += tmp

        return area


print(Solution().surfaceArea(grid = [[2,2,2],[2,1,2],[2,2,2]]))
