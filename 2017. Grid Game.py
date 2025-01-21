class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:

        result = float('inf')

        upper_value = sum(grid[0])
        lower_value = 0

        for i in range(len(grid[0])):
            upper_value -= grid[0][i]
            r = max(upper_value, lower_value)
            result = min(result, r)
            lower_value += grid[1][i]

        return result

print(Solution().gridGame(grid = [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]))