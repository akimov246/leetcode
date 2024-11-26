class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        if n == 1:
            return 0

        all_teams = set(range(n))
        winners = set()
        losers = set()

        for edge in edges:
            winners.add(edge[0])
            losers.add(edge[1])

        winners = winners.difference(losers)
        idle_teams = all_teams.difference(winners.union(losers))

        return winners.pop() if len(winners) == 1 and not idle_teams else -1


print(Solution().findChampion(n = 3, edges=[[0,1]]))