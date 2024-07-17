class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        numbers = set(range(1, len(matrix) + 1))
        for row, column in zip(matrix, zip(*matrix)):
            if set(row) != numbers or set(column) != numbers:
                return False
        return True


print(Solution().checkValid(matrix = [[1,2,3],[3,1,2],[2,3,1]]))