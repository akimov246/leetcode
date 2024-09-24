from itertools import chain

class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:

        def helper(arr):
            prefixes = set()
            for value in chain(set(arr)):
                value = str(value)
                for i in range(len(value), 0, -1):
                    if value[:i] not in prefixes:
                        prefixes.add(value[:i])
                    else:
                        break
            return prefixes

        prefixes1 = helper(arr1)
        prefixes2 = helper(arr2)
        prefixes = prefixes1 & prefixes2
        return len(max(prefixes, key=len)) if prefixes else 0


print(Solution().longestCommonPrefix(arr1 = [1, 10, 100], arr2 = [1000]))