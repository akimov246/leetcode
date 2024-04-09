class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        def my_sort(value: int) -> int:
            return bin(value).count('1')

        return sorted(arr, key=lambda value: (my_sort(value), value))

print(Solution().sortByBits(arr = [0,1,2,3,4,5,6,7,8]))