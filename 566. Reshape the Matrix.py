class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        len_row = len(mat[0])
        len_col = len(mat)
        if len_row * len_col != r * c:
            return mat
        values = (mat[i][j] for i in range(len_col) for j in range(len_row))
        result = [[None] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                result[i][j] = next(values)
        return result

print(Solution().matrixReshape([[1,2]], 1, 1))