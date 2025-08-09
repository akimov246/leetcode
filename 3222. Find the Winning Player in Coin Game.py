class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        winner = None

        turn = 1
        while True:
            if x >= 1 and y >= 4:
                if turn % 2:
                    winner = 'Alice'
                else:
                    winner = 'Bob'
            else:
                break
            x -= 1
            y -= 4
            turn += 1

        return winner if winner else 'Bob'



print(Solution().winningPlayer(x = 4, y = 11))