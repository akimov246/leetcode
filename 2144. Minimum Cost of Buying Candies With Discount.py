class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        total = 0
        cost.sort()

        for i in range(len(cost), -1, -3):
            current_candies = cost[i - 3:i] if i - 3 > -1 else cost[:i]
            if len(current_candies) == 3:
                total += sum(current_candies[1:])
            else:
                total += sum(current_candies)
        return total


print(Solution().minimumCost(cost = [3,3,3,1]))