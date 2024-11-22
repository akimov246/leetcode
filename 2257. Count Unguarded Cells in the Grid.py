class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for x, y in guards:
            grid[x][y] = 'G'
        for x, y in walls:
            grid[x][y] = 'W'

        result = m * n - len(guards) - len(walls)

        for guard_x, guard_y in guards:
            for x, y in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                i = guard_x
                j = guard_y
                while True:
                    i += x
                    j += y
                    if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] in ['G', 'W']:
                        break
                    if not grid[i][j]:
                        grid[i][j] = 1
                        result -= 1

        return result


print(Solution().countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]))