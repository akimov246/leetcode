class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        result = -float('inf')
        i_values = [values[i] + i for i in range(len(values))]
        j_values = []
        cur_max_j = -float('inf')
        for j in range(len(values) - 1, -1, -1):
            cur_max_j = max(cur_max_j, values[j] - j)
            j_values.append(cur_max_j)
        j_values.reverse()

        i_value = -float('inf')
        for i in range(len(values) - 1):
            if i_values[i] > i_value:
                i_value = i_values[i]
                result = max(result, i_value + j_values[i + 1])

        return result


print(Solution().maxScoreSightseeingPair(values=[8,1,5,2,6]))