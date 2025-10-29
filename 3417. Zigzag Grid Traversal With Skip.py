class Solution:
    def zigzagTraversal(self, grid: list[list[int]]) -> list[int]:
        result = []
        for i in range(len(grid)):
            if i % 2:
                start = len(grid[i]) - 2 if len(grid[i]) % 2 else len(grid[i]) - 1
                stop = -1
                step = -2
            else:
                start = 0
                stop = len(grid[i])
                step = 2
            for j in range(start, stop, step):
                result.append(grid[i][j])

        return result



print(Solution().zigzagTraversal(grid = [[1,2,3],[4,5,6],[7,8,9]]))