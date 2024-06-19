class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = 0
        index = 3
        step = 3
        while index < len(s) + step:
            if s[index - step:index].startswith('X'):
                index += step
                moves += 1
            elif 'X' in s[index - step:index]:
                index += 1
            else:
                index += step
        return moves


print(Solution().minimumMoves(s = "0X0X"))