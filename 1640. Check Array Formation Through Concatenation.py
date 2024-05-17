class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        index = 0
        length = 1
        while index + length <= len(arr):
            if arr[index:index + length] not in pieces:
                length += 1
            else:
                index += length
                length = 1
            if index == len(arr):
                return True
        return False

print(Solution().canFormArray(arr = [37,69,3,74,46], pieces = [[37,69,3,74,46]]))