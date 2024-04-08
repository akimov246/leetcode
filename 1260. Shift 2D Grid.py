class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        grid = [grid[i][j] for i in range(m)
                           for j in range(n)]
        def right_cycled_shift(grid, k):
            for _ in range(k):
                grid = [grid[-1]] + grid[:-1]
            return grid
        grid = right_cycled_shift(grid, k)
        res = []
        grid_iterator = iter(grid)
        for i in range(m):
            res.append([])
            for j in range(n):
                res[i].append(next(grid_iterator))
        return res

print(Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 2))