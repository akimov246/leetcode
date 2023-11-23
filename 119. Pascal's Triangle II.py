class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        return self.generate(rowIndex + 1)[-1]

    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        prev = triangle[0]
        for i in range(1, numRows + 1):
            row = [None] * i
            row[0] = 1
            row[-1] = 1
            if row.count(None):
                for j in range(1, len(row) - 1):
                    row[j] = prev[j] + prev[j - 1]
            prev = row
            triangle.append(row)
        return triangle


print(Solution().getRow(3))