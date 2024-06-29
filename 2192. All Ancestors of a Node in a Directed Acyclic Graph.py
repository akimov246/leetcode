from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        answer = []
        to_from_map = defaultdict(list)
        for from_, to_ in edges:
            to_from_map[to_].append(from_)

        def get_ancestors(node: int, ancestors: set[int] = None):
            if ancestors is None:
                ancestors = set()
            if froms := to_from_map.get(node, None):
                for a in froms:
                    if a not in ancestors:
                        ancestors.add(a)
                        get_ancestors(a, ancestors)
            return ancestors

        for node in range(n):
            ancestors = sorted(list(get_ancestors(node)))
            answer.append(ancestors)

        return answer



#print(Solution().getAncestors(n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))