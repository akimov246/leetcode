class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        if area == 1:
            return [1, 1]
        possible_ways = set()
        for w in range(1, area // 2 + 1):
            l = area / w
            if l.is_integer():
                if int(l) >= w:
                    possible_ways.add((int(l), w))
        return list(sorted(possible_ways)[0])


print(Solution().constructRectangle(37))