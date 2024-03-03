class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        xy = sum(bool(grid[i][j]) for i in range(len(grid))
                                  for j in range(len(grid[i])))
        xz = sum(max(v) for v in grid)
        yz = sum(max(v) for v in zip(*grid))
        return xy + xz + yz

print(Solution().projectionArea(grid = [[1,2],[3,4]]))