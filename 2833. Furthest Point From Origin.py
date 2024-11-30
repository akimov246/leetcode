class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counter = {}
        for move in moves:
            counter[move] = counter.get(move, 0) + 1
        _ = counter.pop('_') if counter.get('_', False) else 0
        max_ = counter.pop(max(counter.items(), key=lambda item: item[1])[0]) if counter else 0
        min_ = counter.popitem()[1] if counter else 0
        return max_ + _ - min_


print(Solution().furthestDistanceFromOrigin(moves = "L_RL__R"))