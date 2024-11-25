from copy import deepcopy

# Решение - полная хуйня, но работает. Если убрать ограничение в количестве moves, она будет работать 1488 лет
class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        goal = [[1, 2, 3], [4, 5, 0]]
        if board == goal:
            return 0

        def helper(current, combinations = None, moves = 0):
            if current == goal:
                return moves

            if combinations and (current in combinations) or moves > 20:
                return float('inf')

            paths = {'up', 'right', 'down', 'left'}
            row = 0 if 0 in current[0] else 1
            col = current[row].index(0)

            if row == 0:
                paths.remove('up')
            else:
                paths.remove('down')
            if col == 0:
                paths.remove('left')
            elif col == 2:
                paths.remove('right')

            if not combinations:
                combinations = [current]
            else:
                combinations = deepcopy(combinations)
                combinations.append(current)

            up_current = None
            right_current = None
            down_current = None
            left_current = None
            if 'up' in paths:
                up_current = deepcopy(current)
                up_current[row][col], up_current[row - 1][col] = up_current[row - 1][col], up_current[row][col]
                if up_current in combinations:
                    up_current = None
            if 'right' in paths:
                right_current = deepcopy(current)
                right_current[row][col], right_current[row][col + 1] = right_current[row][col + 1], right_current[row][col]
                if right_current in combinations:
                    right_current = None
            if 'down' in paths:
                down_current = deepcopy(current)
                down_current[row][col], down_current[row + 1][col] = down_current[row + 1][col], down_current[row][col]
                if down_current in combinations:
                    down_current = None
            if 'left' in paths:
                left_current = deepcopy(current)
                left_current[row][col], left_current[row][col - 1] = left_current[row][col - 1], left_current[row][col]
                if left_current in combinations:
                    left_current = None

            return min(helper(up_current, combinations, moves + 1) if up_current else float('inf'),
                       helper(right_current, combinations, moves + 1) if right_current else float('inf'),
                       helper(down_current, combinations, moves + 1) if down_current else float('inf'),
                       helper(left_current, combinations, moves + 1) if left_current else float('inf'),
                       )


        result = helper(board)
        return result if result != float('inf') else -1

print(Solution().slidingPuzzle(board = [[5,3,2],[0,4,1]]))
