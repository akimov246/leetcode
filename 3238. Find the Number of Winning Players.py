from collections import defaultdict

class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        players_picks = defaultdict(dict)
        for player, color in pick:
            players_picks[player][color] = players_picks[player].get(color, 0) + 1

        winners = 0

        for player, picks in players_picks.items():
            if any(pick > player for pick in picks.values()):
                winners += 1

        return winners

print(Solution().winningPlayerCount(n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]))