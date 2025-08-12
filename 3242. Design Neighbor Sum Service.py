class MyList(list):
    def __getitem__(self, index):
        if index < 0:
            raise IndexError

        value = super().__getitem__(index)

        if isinstance(value, list):
            return self.__class__(value)
        return value

class NeighborSum:

    def __init__(self, grid: list[list[int]]):
        self.grid = MyList(grid)
        self.grid = MyList(grid)
        self.n = len(self.grid)
        self.last_element_value = self.grid[self.n - 1][self.n - 1]

    def adjacentSum(self, value: int) -> int:
        i, j = self.find_coords(value)
        result = 0
        # top
        try:
            result += self.grid[i - 1][j]
        except IndexError:
            pass
        # bottom
        try:
            result += self.grid[i + 1][j]
        except IndexError:
            pass
        # left:
        try:
            result += self.grid[i][j - 1]
        except IndexError:
            pass
        # right
        try:
            result += self.grid[i][j + 1]
        except IndexError:
            pass

        return result

    def diagonalSum(self, value: int) -> int:
        i, j = self.find_coords(value)
        result = 0
        # top-left
        try:
            result += self.grid[i - 1][j - 1]
        except IndexError:
            pass
        # top-right
        try:
            result += self.grid[i - 1][j + 1]
        except IndexError:
            pass
        # bottom-left
        try:
            result += self.grid[i + 1][j - 1]
        except IndexError:
            pass
        # bottom-right
        try:
            result += self.grid[i + 1][j + 1]
        except IndexError:
            pass

        return result

    def find_coords(self, value):
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == value:
                    return i, j

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum([[3,6,0],[8,5,1],[2,4,7]])
# param_1 = obj.adjacentSum(2)
# param_2 = obj.adjacentSum(4)
# param_3 = obj.diagonalSum(4)
# param_4 = obj.diagonalSum(8)