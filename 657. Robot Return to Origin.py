class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for move in moves:
            match move:
                case 'U':
                    y += 1
                case 'D':
                    y -= 1
                case 'R':
                    x += 1
                case 'L':
                    x -= 1
        return True if x == 0 and y == 0 else False

print(Solution().judgeCircle(moves = "UD"))