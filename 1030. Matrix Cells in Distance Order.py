class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        matrix = [[i, j] for i in range(rows)
                         for j in range(cols)]

        def cell_sort(cell):
            return abs(cell[0] - rCenter) + abs(cell[1] - cCenter)

        return sorted(matrix, key=cell_sort)



print(Solution().allCellsDistOrder(rows = 2, cols = 2, rCenter = 0, cCenter = 1))