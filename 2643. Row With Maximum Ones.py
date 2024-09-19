class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        row_idx = -1
        num_of_ones = -1

        for i in range(len(mat)):
            current = mat[i].count(1)
            if current > num_of_ones:
                num_of_ones = current
                row_idx = i

        return [row_idx, num_of_ones]

print(Solution().rowAndMaximumOnes(mat = [[0,1],[1,0]]))