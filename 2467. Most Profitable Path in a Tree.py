from collections import defaultdict

# Вроде как работает, но не проходит TimeLimit
class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        node_neighbour = defaultdict(list)

        for edge in edges:
            node_neighbour[edge[0]].append(edge[1])
            node_neighbour[edge[1]].append(edge[0])
        print(node_neighbour)
        leaves = {node for node in node_neighbour if node != 0 and len(node_neighbour[node]) == 1}
        print(leaves)

        def bob(node=bob, path=None, paths=None):
            if paths is None:
                paths = []
            if path is None:
                path = []

            path.append(node)
            if node == 0:
                paths.append(path)
            for next_node in node_neighbour[node]:
                if next_node not in path:
                    bob(next_node, path.copy(), paths)

            return paths

        bobs_paths = bob()
        print(bobs_paths)

        def alice(node, step, cash, bobs_path, visited=None, current_amount=amount.copy(), results=None):
            if visited is None:
                visited = set()
            if results is None:
                results = []

            if step < len(bobs_path) and node == bobs_path[step]:
                cash += current_amount[node] // 2
            else:
                cash += current_amount[node]
            if step < len(bobs_path):
                current_amount[bobs_path[step]] = 0
            current_amount[node] = 0
            visited.add(node)

            if node in leaves:
                results.append(cash)
                return

            for next_node in node_neighbour[node]:
                if next_node not in visited:
                    alice(next_node, step + 1, cash, bobs_path, visited.copy(), current_amount.copy(), results)

            return max(results) if results else -float('inf')

        #print(alice(0, 0, 0, bobs_paths[0]))
        result = -float('inf')
        for bobs_path in bobs_paths:
            result = max(result, alice(0, 0, 0, bobs_path))

        return result


#print(Solution().mostProfitablePath(edges = [[0,1]], bob = 1, amount = [-7280,2350]))