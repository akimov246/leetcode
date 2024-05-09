class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        coordinates = set((x, x) for x in range(len(mat)))
        x = len(mat) - 1
        y = 0
        sum_ = 0
        while y != len(mat):
            coordinates.add((x, y))
            x -= 1
            y += 1
        for x, y in coordinates:
            sum_ += mat[x][y]
        return sum_

print(Solution().diagonalSum(mat = [[1,2,3],
                                    [4,5,6],
                                    [7,8,9]]))