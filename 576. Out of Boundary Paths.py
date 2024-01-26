from functools import cache

class Solution:
    def __init__(self):
        self.MOD = 10 ** 9 + 7
        self.moves = 0
        self.mem = dict()

    # Мое решение. Работает, но очень медленно при большом значении maxMove
    # def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    #     if maxMove:
    #         print(self.moves)
    #         maxMove -= 1
    #         borders = self.countBorders(m, n, startRow, startColumn)
    #         if borders:
    #             self.moves += borders
    #         if startRow - 1 >= 0:
    #             self.findPaths(m, n, maxMove, startRow - 1, startColumn)
    #         if startRow + 1 <= m - 1:
    #             self.findPaths(m, n, maxMove, startRow + 1, startColumn)
    #         if startColumn - 1 >= 0:
    #             self.findPaths(m, n, maxMove, startRow, startColumn - 1)
    #         if startColumn + 1 <= n - 1:
    #             self.findPaths(m, n, maxMove, startRow, startColumn + 1)
    #     return self.moves % self.MOD

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return self.helper(m, n, maxMove, startRow, startColumn) % self.MOD

    @cache
    def helper(self, m, n, maxMove, x, y):
        if x == m or y == n or x < 0 or y < 0:
            return 1
        if maxMove == 0:
            return 0

        return self.helper(m, n, maxMove - 1, x - 1, y) + \
               self.helper(m, n, maxMove - 1, x + 1, y) + \
               self.helper(m, n, maxMove - 1, x, y - 1) + \
               self.helper(m, n, maxMove - 1, x, y + 1)


    @cache
    def countBorders(self, m, n, x, y):
        borders = 0
        if x == 0:
            borders += 1
        if y == 0:
            borders += 1
        if x == m - 1:
            borders += 1
        if y == n - 1:
            borders += 1
        return borders




print(Solution().findPaths(m = 8, n = 7, maxMove = 16, startRow = 1, startColumn = 5))