class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        dict1 = dict(items1)
        dict2 = dict(items2)
        ret = []
        for value in set(dict1) | set(dict2):
            ret.append([value, dict1.get(value, 0) + dict2.get(value, 0)])

        return sorted(ret)

print(Solution().mergeSimilarItems(items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]))