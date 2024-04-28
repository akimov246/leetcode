class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        mins_in_row = set()
        maxs_in_col = set()
        for row in matrix:
            mins_in_row.add(min(row))
        for col in zip(*matrix):
            maxs_in_col.add(max(col))
        return list(mins_in_row.intersection(maxs_in_col))


print(Solution().luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]]))