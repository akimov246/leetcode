class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        i = 0
        n = len(arr)
        while i < n - 1:
            if arr[i] == 0:
                arr[i + 1:] = arr[i:n - 1]
                i += 1
            i += 1



print(Solution().duplicateZeros(arr = [1,0,2,3,0,4,5,0]))

