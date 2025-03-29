class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        champion = None
        max_score = 0
        for team in range(len(grid)):
            score = grid[team].count(1)
            if score > max_score:
                max_score = score
                champion = team
        return champion


print(Solution().findChampion(grid = [[0,0,1],[1,0,1],[0,0,0]]))