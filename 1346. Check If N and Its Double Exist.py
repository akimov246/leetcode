class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
                    return True
        return False

print(Solution().checkIfExist(arr = [10,2,5,3]))