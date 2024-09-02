class Solution:
    def captureForts(self, forts: list[int]) -> int:
        result = 0
        left = 0
        right = 1
        while right < len(forts):
            if forts[left] == forts[right] and forts[left] != 0:
                left = right
                right = left + 1
            elif forts[left] != -forts[right] and forts[left] != 0:
                right += 1
            else:
                result = max(result, right - left - 1)
                left = right
                right = left + 1
        return result

print(Solution().captureForts(forts = [0,-1,-1,0,-1]))