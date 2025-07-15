class Solution:
    def satisfiesConditions(self, grid: list[list[int]]) -> bool:
        if len(grid) == 1:
            for j in range(len(grid[0]) - 1):
                cell = grid[0][j]
                next_cell = grid[0][j + 1]
                if cell == next_cell:
                    return False

        for i in range(len(grid) - 1):
            row = grid[i]
            row_below = grid[i + 1]
            if row != row_below:
                return False
            for j in range(len(grid[i]) - 1):
                cell = grid[i][j]
                next_cell = grid[i][j + 1]
                if cell == next_cell:
                    return False
        return True

print(Solution().satisfiesConditions(grid = [[1,0,2],[1,0,2]]))