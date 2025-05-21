class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        zero_rows = set()
        zero_cols = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0


def printMatrix(matrix):
    for row in matrix:
        print(row)
    print()

matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
printMatrix(matrix)
Solution().setZeroes(matrix)
printMatrix(matrix)
