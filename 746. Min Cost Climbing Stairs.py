from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        @cache
        def helper(index: int):
            if index >= len(cost):
                return 0

            stair1 = cost[index] + helper(index + 1)
            stair2 = cost[index] + helper(index + 2)

            return min(stair1, stair2)

        return min(helper(0), helper(1))

#print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
#print(Solution().minCostClimbingStairs([10,15,20]))