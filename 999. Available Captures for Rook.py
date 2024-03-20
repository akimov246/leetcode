from dataclasses import dataclass

@dataclass(frozen=True)
class Figure:
    x: int
    y: int

class Rook(Figure):
    '''Ладья'''

class Bishop(Figure):
    '''Слон'''

class Pawn(Figure):
    '''Пешка'''

class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        captures = 0
        rook = None
        bishops = set()
        pawns = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                match board[i][j]:
                    case 'B':
                        bishops.add(Bishop(j, i))
                    case 'R':
                        rook = Rook(j, i)
                    case 'p':
                        pawns.add(Pawn(j, i))

        # up
        for pawn in pawns:
            if pawn.y < rook.y and pawn.x == rook.x:
                if not any(rook.y > bishop.y > pawn.y for bishop in bishops):
                    captures += 1
                    pawns.remove(pawn)
                    break

        # right
        for pawn in pawns:
            if pawn.x > rook.x and pawn.y == rook.y:
                if not any(rook.x < bishop.x < pawn.x for bishop in bishops):
                    captures += 1
                    pawns.remove(pawn)
                    break

        # down
        for pawn in pawns:
            if pawn.y > rook.y and pawn.x == rook.x:
                if not any(rook.y < bishop.y < pawn.y for bishop in bishops):
                    captures += 1
                    pawns.remove(pawn)
                    break

        # left
        for pawn in pawns:
            if pawn.x < rook.x and pawn.y == rook.y:
                if not any(rook.x > bishop.x > pawn.x for bishop in bishops):
                    captures += 1
                    pawns.remove(pawn)
                    break

        return captures

print(Solution().numRookCaptures(board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))