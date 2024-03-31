class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        max_ = max(arr1)

        def my_sort(value: int):
            if value in arr2:
                return arr2.index(value)
            return value + max_

        return sorted(arr1, key=my_sort)

print(Solution().relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))