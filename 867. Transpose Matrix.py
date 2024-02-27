class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return [list(row) for row in list(zip(*matrix))]

print(Solution().transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]))