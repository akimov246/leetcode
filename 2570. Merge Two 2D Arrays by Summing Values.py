from itertools import zip_longest

class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        result = {}
        for n1, n2 in zip_longest(nums1, nums2):
            if n1:
                id = n1[0]
                val = n1[1]
                result[id] = result.get(id, 0) + val
            if n2:
                id = n2[0]
                val = n2[1]
                result[id] = result.get(id, 0) + val
        result = sorted([list(item) for item in list(result.items())], key=lambda item: item[0])
        return result

print(Solution().mergeArrays(nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]))