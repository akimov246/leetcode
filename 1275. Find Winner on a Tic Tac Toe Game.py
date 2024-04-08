class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        grid = []
        for i in range(3):
            grid.append([])
            for j in range(3):
                grid[i].append('')
        for i, move in enumerate(moves):
            grid[move[0]][move[1]] = '0' if i % 2 else 'X'
        for row in grid:
            if len(set(row)) == 1 and row[0] != '':
                return 'A' if row[0] == 'X' else 'B'
        for col in zip(*grid):
            if len(set(col)) == 1 and col[0] != '':
                return 'A' if col[0] == 'X' else 'B'
        if grid[1][1] != '' and (len(set((grid[0][0], grid[1][1], grid[2][2]))) == 1 or len(set((grid[0][2], grid[1][1], grid[2][0]))) == 1):
            return 'A' if grid[1][1] == 'X' else 'B'

        return 'Pending' if 9 - len(moves) else 'Draw'


print(Solution().tictactoe( moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]))