class Solution:
    def canMakeSquare(self, grid: list[list[str]]) -> bool:
        for i in range(len(grid) - 1):
            for j in range(1, len(grid[0])):
                black_counter = 0
                white_counter = 0
                if grid[i][j - 1] == 'B':
                    black_counter += 1
                else:
                    white_counter += 1
                if grid[i][j] == 'B':
                    black_counter += 1
                else:
                    white_counter += 1
                if grid[i + 1][j - 1] == 'B':
                    black_counter += 1
                else:
                    white_counter += 1
                if grid[i + 1][j] == 'B':
                    black_counter += 1
                else:
                    white_counter += 1
                if black_counter in (0, 1) or white_counter in (0, 1):
                    return True
        return False


print(Solution().canMakeSquare(grid = [["B","W","B"],["B","W","W"],["B","W","B"]]))