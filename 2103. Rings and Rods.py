from collections import defaultdict

class Solution:
    def countPoints(self, rings: str) -> int:
        rod_color_map = defaultdict(set)
        for i in range(2, len(rings) + 1, 2):
            pair = rings[i - 2:i]
            rod = pair[1]
            color = pair[0]
            rod_color_map[rod].add(color)
        result = 0
        for colors in rod_color_map.values():
            if len(colors) == 3:
                result += 1
        return result

print(Solution().countPoints(rings = "B9R9G0R4G6R8R2R9G9"))