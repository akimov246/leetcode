class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) >= 3:
            peak_idx = arr.index(max(set(arr)))
            if peak_idx == 0 or peak_idx == len(arr) - 1:
                return False
            for i in range(peak_idx):
                if arr[i] >= arr[i + 1]:
                    return False
            for i in range(peak_idx, len(arr) - 1):
                if arr[i] <= arr[i + 1]:
                    return False
            return True
        else:
            return False

print(Solution().validMountainArray(arr = [3,5,5]))