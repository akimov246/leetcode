class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        for i in range(k, len(str(num)) + 1):
            if int(str(num)[i - k: i]) and num % int(str(num)[i - k: i]) == 0:
                ans += 1
        return ans

print(Solution().divisorSubstrings(num = 240, k = 2))