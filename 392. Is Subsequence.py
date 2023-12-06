class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        ans = ""
        i_s = 0
        i_t = 0
        while i_t < len(t) and i_s < len(s):
            if s[i_s] == t[i_t]:
                ans += s[i_s]
                i_s += 1
            i_t += 1
        return ans == s

print(Solution().isSubsequence("", "ahbgdc"))