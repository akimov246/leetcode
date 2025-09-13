class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        col = {letter: i for i, letter in enumerate('abcdefgh', start=1)}

        def square_is_black(coord):
            if (col[coord[0]] % 2 and not int(coord[1]) % 2) or (not col[coord[0]] % 2 and int(coord[1]) % 2):
                return True
            return False

        return square_is_black(coordinate1) == square_is_black(coordinate2)

print(Solution().checkTwoChessboards(coordinate1 = "a1", coordinate2 = "c3"))