class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        ans = [None, None]
        values = set()

        for row in grid:
            for value in row:
                if value in values:
                    ans[0] = value
                else:
                    values.add(value)

        ans[1] = (set(range(1, len(grid) ** 2 + 1)) - values).pop()
        return ans

print(Solution().findMissingAndRepeatedValues(grid = [[1,3],[2,2]]))