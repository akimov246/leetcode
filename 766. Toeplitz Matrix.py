class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:

        row_len = len(matrix[0])
        col_len = len(matrix)

        start_positions = set()
        start_positions.update((0, c) for c in range(row_len))
        start_positions.update((r, 0) for r in range(col_len))

        for r, c in start_positions:
            mem = matrix[r][c]
            r += 1
            c += 1
            while c < row_len and r < col_len:
                if mem != matrix[r][c]:
                    return False
                r += 1
                c += 1
        return True


print(Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
