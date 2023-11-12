import math

class VertexGraph:

    def __init__(self, name, score, state):
        self.value = name
        self.score = score
        self.state = state

    def __str__(self):
        return f"{self.value, self.score, self.state}"

class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.n = self._is_valid_n(n)
        self.edges = edges

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

    def get_vertex_with_min_score(self, vertices: list[VertexGraph]):
        minimal = math.inf
        for v in vertices:
            if v.score <= math.inf:
                minimal = v
        return minimal

    def my_sort(self, x: VertexGraph):
        if x.state != False:
            return x.score
        return -math.inf

    def get_genaral_state(self, vertices: list[VertexGraph]):
        return False in [v.state for v in vertices]

    def shortestPath2(self, node1: int, node2: int) -> int:
        vertices = [VertexGraph(i, math.inf, False) for i in range(self.n)]
        vertices[node1].score = 0
        print(*vertices)
        #w = sorted(vertices, key=lambda x: x.score)[0]
        while self.get_genaral_state(vertices):
            w = sorted(vertices, key=self.my_sort)[0]
            #vertices.sort(key=self.my_sort)
            #w = vertices[0]
            print(w)
            possibles = [edge for edge in self.edges if edge[0] == w.value]
            for edge in possibles:
                verext = edge[1]
                length = edge[2]
                if w.score + length < vertices[verext].score:
                    vertices[verext].score = w.score + length
            sorted(vertices, key=self.my_sort)[0].state = True

        return -1 if vertices[node2].score == math.inf else vertices[node2].score


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
                try:
                    if unvisited.get(w) != math.inf and unvisited.get(w) + length_path < unvisited.get(edge[1]):
                        unvisited.update({edge[1]: unvisited.get(w) + length_path})
                except:
                    if unvisited.get(w) != math.inf and unvisited.get(w) + length_path < visited.get(node):
                        unvisited.update({node: unvisited.get(w) + length_path})
            visited.update({w: unvisited.get(w)})
            unvisited.pop(w)
        return -1 if visited.get(node2) == math.inf else visited.get(node2)




# Your Graph object will be instantiated and called as such:
n = 4
edges = [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]

obj = Graph(n, edges)
obj.addEdge([1, 3, 4])
param_2 = obj.shortestPath2(0, 3)
print(param_2)