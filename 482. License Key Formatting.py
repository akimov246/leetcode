class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = ""
        key = s.replace('-', '')[::-1]
        for i in range(0, len(key), k):
            ans += key[i:i + k] + "-"
        return ans[:len(ans) - 1][::-1].upper()

print(Solution().licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4))