class Board:

    def __init__(self, n):
        self.n = n

    def first_queen_place(self, x, y):
        c = 0
        board = [[0] * self.n for _ in range(self.n)]

        def put_queen(x, y):
            board[x][y] = 1

        def horizontal(x):
            return not bool(sum(board[x]))

        def vertical(y):
            return not bool(sum((row[y] for row in board)))

        def diagonal1(x, y):
            while y > 0 and x > 0:
                x -= 1
                y -= 1
            while x < self.n and y < self.n:
                if board[x][y] == 1:
                    return False
                x += 1
                y += 1
            return True

        def diagonal2(x, y):
            while y != self.n - 1 and x != 0:
                y += 1
                x -= 1
            #print(x, y)
            while x < self.n and y < self.n:
                if board[x][y] == 1:
                    return False
                y -= 1
                x += 1
            return True

        put_queen(x, y)
        c += 1
        for i in range(self.n):
            for j in range(self.n):
                if horizontal(i) and vertical(j) and diagonal1(j, i) and diagonal2(j, i):
                    put_queen(i, j)
                    c += 1
        return 1 if c == self.n else 0

    def count(self):
        result = 0
        for i in range(self.n):
            for j in range(self.n):
                result += self.first_queen_place(i, j)
        return result


if __name__ == '__main__':
    b = Board(8)
    print(b.count())



#0 0 0 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 0