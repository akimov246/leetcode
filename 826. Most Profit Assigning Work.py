from functools import cache

class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        total_profit = 0
        dificulty_profit_map = {}
        for d, p in zip(difficulty, profit):
            dificulty_profit_map[d] = max(dificulty_profit_map.get(d, 0), p)
        dificulty_profit_map_list = sorted(dificulty_profit_map.items(), key=lambda item: item[1], reverse=True)

        @cache
        def search(w: int) -> int:
            for d, p in dificulty_profit_map_list:
                if d <= w:
                    return p
            return 0

        for w in worker:
            total_profit += search(w)

        return total_profit

#print(Solution().maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]))
# print(Solution().maxProfitAssignment([66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63],
#                                      [66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77],
#                                      [61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]))