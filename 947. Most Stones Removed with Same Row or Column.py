from collections import defaultdict
from copy import deepcopy

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        stones = sorted(stones, key=lambda coords: (coords[0], coords[1]))
        # removed_stones = 0
        #
        # def helper(current, stones):
        #     for i in range(len(stones)):
        #         if current[0] == stones[i][0] or current[1] == stones[i][1]:
        #             return 1 + helper(stones[i], stones[:i] + stones[i + 1:])
        #     else:
        #         #return 0
        #         for i in range(len(stones)):
        #             current = stones[i]
        #             if current[0] == stones[i][0] or current[1] == stones[i][1]:
        #                 return helper(stones[i], stones[:i] + stones[i + 1:])
        #         else:
        #             return 0
        #
        # for i in range(len(stones)):
        #     removed_stones = max(removed_stones, helper(stones[i], stones[:i] + stones[i + 1:]))
        # return removed_stones

        neightbours = defaultdict(list)
        for i in range(len(stones)):
            for j in range(len(stones)):
                if (stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]) and i != j:
                    neightbours[tuple(stones[i])].append(tuple(stones[j]))

        neightbours = dict(neightbours)
        print(neightbours)

        visited = set()
        current = tuple(stones[0])
        while True:
            visited.add(current)
            for neighbour in neightbours[current]:
                if neighbour not in visited:
                    if current[0] == neighbour[0] or current[1] == neighbour[1]:
                        current = neighbour
                        break
            else:
                print(len(visited))
                break




print(Solution().removeStones(stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))