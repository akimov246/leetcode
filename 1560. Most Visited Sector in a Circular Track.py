class Solution:
    def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
        sectors = {}
        current = rounds[0]
        for end in rounds[1:]:
            while True:
                sectors[current] = sectors.get(current, 0) + 1
                current = (current % n) + 1
                if current == end:
                    break
        sectors[rounds[-1]] = sectors.get(rounds[-1], 0) + 1
        max_ = max(sectors.values())
        return sorted([sector for sector in sectors if sectors[sector] == max_])

print(Solution().mostVisited(n = 7, rounds = [1,3,5,7]))