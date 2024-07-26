class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:

        reach = set()
        visited = set()
        def helper(city, distance = 0):
            #print(distance)
            neighbors = []
            for f, t, d in edges:
                if city == f:
                    neighbors.append((t, d))
                elif city == t:
                    neighbors.append((f, d))
            #print(neighbors)
            for neighbor, d in neighbors:
                if neighbor not in visited and distance + d <= distanceThreshold:
                    reach.add(neighbor)
                    helper(neighbor, distance + d)
                    visited.add(city)


        result = {}
        for city in range(n):
            helper(city)
            if city in reach:
                reach.remove(city)
            result[city] = reach
            reach = set()
            visited = set()

        return sorted(result.items(), key=lambda item:(len(item[1]), -item[0]))[0][0]


print(Solution().findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2))
