class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        result = 0
        for column in zip(*grid):
            column = list(column)
            for i in range(1, len(column)):
                if column[i] <= column[i - 1]:
                    diff = column[i - 1] - column[i]
                    column[i] = column[i - 1] + 1
                    result += diff + 1

        return result


print(Solution().minimumOperations(grid = [[3,2],[1,3],[3,4],[0,1]]))