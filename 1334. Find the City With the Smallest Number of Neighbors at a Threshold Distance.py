from collections import defaultdict

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        self.edges = edges
        self.neighbours = self.__neighbours()
        print(self.neighbours)

        def helper(city, distance = 0, visited = None, reached = None):
            if visited is None:
                visited = set()
            if reached is None:
                reached = set()
            for neighbour, dist in self.neighbours[city].items():
                print(neighbour, dist)

        helper(1)

    def __neighbours(self):
        result = defaultdict(dict)
        for from_, to_, dist in self.edges:
            result[from_].update({to_:dist})
            result[to_].update({from_:dist})
        return dict(result)




print(Solution().findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))
