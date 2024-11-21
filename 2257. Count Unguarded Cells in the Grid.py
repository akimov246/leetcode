class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        self.grid = [[0] * n for _ in range(n)]
        self.grid[2][3] = 1
        self.print_grid()

    def print_grid(self):
        for row in self.grid:
            print(row)

print(Solution().countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]))