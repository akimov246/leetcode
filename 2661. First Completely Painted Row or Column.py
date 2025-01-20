class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:

        coords_of_values = {mat[i][j]: (i, j) for i in range(len(mat))
                                              for j in range(len(mat[0]))}

        nope = {
            'row': set(),
            'col': set()
        }

        can_be_decorated = len(mat) + len(mat[0])

        i = len(arr) - 1

        while can_be_decorated - len(nope['row']) - len(nope['col']):
            row, col = coords_of_values[arr[i]]
            nope['row'].add(row)
            nope['col'].add(col)
            i -= 1

        return i + 1

print(Solution().firstCompleteIndex(arr = [1,3,4,2], mat = [[1,4],[2,3]]))