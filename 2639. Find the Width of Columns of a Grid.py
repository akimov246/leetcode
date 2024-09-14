class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        ans = []
        for col in zip(*grid):
            ans.append(len(str(max(col, key=lambda value: len(str(value))))))
        return ans

print(Solution().findColumnWidth(grid = [[1],[22],[333]]))