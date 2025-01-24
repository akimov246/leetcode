class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        cache = {}
        safe_nodes = []

        def helper(node, visited):
            if node in cache:
                return cache[node]
            if node in visited:
                return False
            possible_paths = graph[node]
            if not possible_paths:
                return True

            # result = any(helper(path, visited.union({node})) for path in possible_paths)
            # cache.update({node: result})
            # return result
            result = None
            for path in possible_paths:
                result = helper(path, visited.union({node}))
                if not result:
                    break

            cache.update({node: result})
            return result

        for i in range(len(graph)):
            if helper(i, set()):
                safe_nodes.append(i)

        return safe_nodes


print(Solution().eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]]))