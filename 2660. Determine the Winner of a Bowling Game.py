class Solution:
    def isWinner(self, player1: list[int], player2: list[int]) -> int:

        def score(player):
            result = 0
            x2_turn = 0
            for s in player:
                if x2_turn:
                    result += s * 2
                    x2_turn -= 1
                else:
                    result += s
                if s == 10:
                    x2_turn = 2
            return result

        result1 = score(player1)
        result2 = score(player2)
        if result1 == result2:
            return 0
        return 1 if result1 > result2 else 2

print(Solution().isWinner(player1 = [5,10,3,2], player2 = [6,5,7,3]))