from collections.abc import Sequence
# Мое решение
class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        ans = [0 for _ in range(len(arr))]
        sorted_arr = sorted(set(arr))
        cache = dict()
        for i, value in enumerate(arr):
            if cache.get(value, 0):
                rank = cache[value]
            else:
                #rank = sorted_arr.index(value) + 1
                rank = self.binary_search_index(sorted_arr, value) + 1
                cache[value] = rank
            ans[i] = rank
        return ans

    def binary_search_index(self, arr: Sequence[int], value: int):
        left = 0
        right = len(arr) - 1

        while left <= right:
            middle = (right + left) // 2
            if arr[middle] == value:
                return middle
            if arr[middle] > value:
                right = middle - 1
            else:
                left = middle + 1

# Решение с leetcode (да, 2 строчки, нахуй)
class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        rank = {ele: i + 1 for i, ele in enumerate(sorted(set(arr)))}
        #return list(map(rank.get, arr))
        return [rank.get(element) for element in arr]

#f = open('text.txt', 'r')
#arr = [int(line) for line in f.read().split(',')]
#print(arr)

print(Solution().arrayRankTransform(arr = [37,12,28,9,100,56,80,5,12]))
#print(Solution().binary_search_index([5, 9, 12, 28, 37, 56, 80, 100], 100))