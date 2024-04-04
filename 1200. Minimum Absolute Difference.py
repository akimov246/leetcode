from collections import defaultdict

class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        diff_pair = defaultdict(list)
        arr.sort()
        for i in range(len(arr) - 1):
            a, b = arr[i], arr[i + 1]
            diff = b - a
            diff_pair[diff].append([a, b])

        return diff_pair[min(diff_pair)]

print(Solution().minimumAbsDifference([40,11,26,27,-20, 1, 2]))