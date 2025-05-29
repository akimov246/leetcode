import math


class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        max_diagonal = 0
        max_area = 0

        for rectangle in dimensions:
            length = rectangle[0]
            width = rectangle[1]
            diagonal = math.sqrt(length ** 2 + width ** 2)
            if diagonal > max_diagonal:
                area = length * width
                max_area = area
                max_diagonal = diagonal
            elif diagonal == max_diagonal:
                area = length * width
                max_area = max(max_area, area)

        return max_area

print(Solution().areaOfMaxDiagonal(dimensions = [[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]]))