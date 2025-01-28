class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        visited_cells = set()

        def explore(r, c, ocean=None):
            if not grid[r][c] or (r, c) in visited_cells:
                return 0
            if ocean is None:
                ocean = []
            ocean.append(grid[r][c])
            visited_cells.add((r, c))

            right = [r, c + 1] if c + 1 < len(grid[0]) else None
            left = [r, c - 1] if c - 1 >= 0 else None
            up = [r - 1, c] if r - 1 >= 0 else None
            down = [r + 1, c] if r + 1 < len(grid) else None

            for coords in [right, left, up, down]:
                if coords:
                    r = coords[0]
                    c = coords[1]
                    explore(r, c, ocean)

            return sum(ocean)

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result = max(result, explore(i, j))

        return result


print(Solution().findMaxFish(grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))