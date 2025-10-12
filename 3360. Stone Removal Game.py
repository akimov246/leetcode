class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn = 10

        alice_is_winner = False

        while n >= turn:
            n -= turn
            turn -= 1
            alice_is_winner = not alice_is_winner

        return alice_is_winner


print(Solution().canAliceWin(1))