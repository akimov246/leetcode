from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel = [0] + travel
        types_of_garbage = set("".join(garbage))
        result_time = 0

        for tog in types_of_garbage:
            truck_time = 0
            last_index = None
            for i in range(-1, -len(garbage) - 1, -1):
                if tog in garbage[i]:
                    last_index = i
                    break
            tmp_garbage = garbage[:len(garbage) + last_index + 1]
            for i in range(len(tmp_garbage)):
                truck_time += travel[i]
                if tog in garbage[i]:
                    amount_of_this_type_of_garbage = garbage[i].count(tog)
                    truck_time += amount_of_this_type_of_garbage

            result_time += truck_time

        return result_time


garbage = ["G", "P", "GP", "GG"]
travel = [2, 4, 3]
print(Solution().garbageCollection(garbage, travel))