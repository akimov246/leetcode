class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        for i in range(len(grid)):
            if grid[i][i] == 0:
                return False
            grid[i][i] = None
        for i, j in zip(range(len(grid)), range(len(grid) - 1, -1, -1)):
            if grid[i][j] == 0:
                return False
            grid[i][j] = None
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] is not None and grid[i][j] != 0:
                    return False
        return True



print(Solution().checkXMatrix(grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]))