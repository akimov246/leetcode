class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        negative = 0
        for row in grid:
            for i in range(len(row) - 1, -1, -1):
                if row[i] >= 0:
                    break
                negative += 1
        return negative


print(Solution().countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))