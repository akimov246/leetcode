class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        position = sorted(position, key=position.count, reverse=True)
        even_target = 0
        odd_target = 0
        count = {}
        for p in position:
            if not odd_target and p % 2:
                odd_target = p
            elif not even_target and p % 2 == 0:
                even_target = p
            count[p] = count.get(p, 0) + 1

        def get_cost(target):
            cost = 0
            for pos in count:
                if pos != target:
                    if (pos + target) % 2:
                        cost += count[pos]
            return cost

        return min(get_cost(even_target), get_cost(odd_target))


print(Solution().minCostToMoveChips(position = [11]))