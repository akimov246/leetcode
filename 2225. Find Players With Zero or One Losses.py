from collections import defaultdict

class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        winners = set()
        losers = defaultdict(int)
        for winner, loser in matches:
            winners.add(winner)
            losers[loser] += 1
        ans1 = list(winners.difference(losers.keys()))
        ans2 = [player for player in losers.keys() if losers[player] == 1]
        return [sorted(ans1), sorted(ans2)]

print(Solution().findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))