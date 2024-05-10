class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        l = 0
        r = m
        for _ in range(m, len(arr) + 1):
            pattern = arr[l:r] * k
            in_l = 0
            in_r = len(pattern)
            for _ in range(in_r, len(arr) + 1):
                if arr[in_l:in_r] == pattern:
                    return True
                in_l += 1
                in_r += 1
            l += 1
            r += 1
        return False

print(Solution().containsPattern(arr = [99,9], m = 1, k = 3))