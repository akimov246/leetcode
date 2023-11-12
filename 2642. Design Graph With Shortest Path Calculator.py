import math

class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.n = self._is_valid_n(n)
        self.edges = edges
        print(self.edges)
        print()


    def _is_valid_n(self, n):
        if n > 0:
            return n
        raise ValueError

    def _dict_key_with_min_value(self, d: dict[int, int|float]):
        minimal = math.inf
        for key in d.keys():
            if d.get(key) <= minimal:
                minimal = key
        return minimal

    def addEdge(self, edge: list[int]) -> None:
        self.edges.append(edge)
        return None

    def shortestPath(self, node1: int, node2: int) -> int:
        unvisited = dict.fromkeys(range(self.n), math.inf)
        unvisited.update({node1: 0})
        visited = {}
        while unvisited:
            w = self._dict_key_with_min_value(unvisited)
            possible_nodes = [node for node in self.edges if node[0] == w]
            for edge in possible_nodes:
                node = edge[1]
                length_path = edge[2]
                if unvisited.get(w) != math.inf and unvisited.get(w) + length_path < unvisited.get(node):
                    unvisited.update({node: unvisited.get(w) + length_path})
            visited.update({w: unvisited.get(w)})
            unvisited.pop(w)
        return visited.get(node2)




# Your Graph object will be instantiated and called as such:
n = 4
edges = [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]

obj = Graph(n, edges)
#obj.addEdge([1, 3, 4])
param_2 = obj.shortestPath(0, 2)
print(param_2)