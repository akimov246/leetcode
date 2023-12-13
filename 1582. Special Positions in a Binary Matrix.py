import numpy

class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        ans = 0
        mat = numpy.array(mat, dtype="i1")

        for i in range(len(mat)):
            if (mat[i] == 1).sum() == 1:
                for j in range(len(mat[i])):
                    if mat[i, j] == 1:
                        if (mat[:,j] == 1).sum() == 1:
                            ans += 1
                            break
        return ans

# Решение с Leetcode
class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:

        def get_column_sum(column):
            return sum(row[column] for row in mat)

        special = 0
        for row in mat:
            if sum(row) == 1:
                column = row.index(1)
                special += get_column_sum(column) == 1

        return special



print(Solution().numSpecial([[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]]))