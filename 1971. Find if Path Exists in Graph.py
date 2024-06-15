from itertools import chain
from collections import defaultdict

# Моё ублюдочное решение
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if n == 1 and destination == 0:
            return True

        paths = defaultdict(set)
        for from_, to_ in chain(edges, ((t, f) for f, t in edges)):
            paths[from_].add(to_)

        self.check = set(range(n))

        def helper(s):
            if dests := paths.get(s):
                self.check -= dests
                del paths[s]
                for d in dests:
                    helper(d)

        helper(source)

        return not (destination in self.check)




print(Solution().validPath(n = 10, edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]], source = 5, destination = 9))
#print(Solution().validPath(n = 50, source=48, destination=2, edges=[[18,46],[8,48],[13,30],[28,29],[2,16],[7,36],[12,19],[31,16],[11,46],[6,46],[19,27],[4,24],[10,37],[14,37],[39,31],[10,22],[23,2],[47,11],[40,7],[21,17],[9,3],[34,10],[48,1],[21,35],[43,48],[27,5],[36,11],[43,36],[31,48],[25,33],[46,19],[31,30],[16,45],[30,10],[35,47],[35,13],[37,48],[49,3],[7,26],[2,30],[0,27],[25,9],[28,27],[39,18],[32,6],[14,43],[9,27],[27,4],[6,0],[21,43]]))
